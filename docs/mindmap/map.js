/* The mind map view. Lazily built the first time #/map is opened, so the rest of
   the application costs nothing when nobody looks at it. */

let uid=0, ROOT=null, laid=[], links=[], maxDepth=0, mapReady=false;
let tx=90, ty=0, sc=1, sel=null, MODE='schema';

function N(name,kind,opt){return Object.assign({id:++uid,name,kind,open:false,kids:null,parent:null},opt||{})}

function fromCurated(c,mod){
  return N(c.name,c.kind||'capability',{mod:c.mod||mod,detail:c.detail||'',
    conf:c.confidence||'derived',src:c.source||'Hand-authored module analysis',
    key:c.key,oos:!!c.oos,
    curatedKids:c.children||[]});
}

function childrenOf(n){
  if(n.kids) return n.kids;
  let k=[];
  if(n.curatedKids){
    k=n.curatedKids.map(c=>fromCurated(c,n.mod));
    n.kids=k;k.forEach(c=>c.parent=n);return k;
  }
  if(n.kind==='product'){
    k=D.modules.map(m=>N(m.title,'module',{mod:m.id,detail:m.what,conf:'derived',
      src:'docs/mindmap/modules.json',
      meta:[['Record types',fmt(m.oc)],['Fields',fmt(m.fc)],['Keys in',fmt(m.ei)],['Keys out',fmt(m.eo)],
            ['In scope',m.scope?'yes':'no \u2014 cost and budget excluded by decision']]}));
  }
  else if(n.kind==='module'){
    const m=modOf(n.mod);
    (NOTES[m.id]||[]).forEach(([t,c,d])=>k.push(N(t,'finding',{mod:m.id,detail:d,conf:c,src:'Live capture, 2026-09-10'})));
    const cur=D.curated&&D.curated[m.id];
    if(cur) k.push(N(cur.name,'walkthrough',{mod:m.id,curatedKids:cur.children||[],
      conf:cur.confidence||'derived',src:cur.source||'Hand-authored module analysis',
      detail:(cur.detail||'')+' This branch is written by hand: it organises the module by what it DOES, and carries the rules and constraints the schema alone cannot show.'}));
    if(m.dep&&m.dep.length) k.push(N('Depends on '+m.dep.length+' other module'+(m.dep.length>1?'s':''),'link-group',
      {mod:m.id,deps:m.dep,conf:'derived',src:'docs/mindmap/edges.json',
       detail:'Modules this one holds foreign keys into. Following these is how you find the blast radius of a schema change.'}));
    m.objects.forEach(name=>{const o=objOf(name);if(!o)return;
      k.push(N(name,'entity',{mod:m.id,obj:name,conf:'observed',src:'_lucernex_objects_summary.txt',
        detail:`A record type in the ${m.title.toLowerCase()} area, holding ${fmt(o.n)} fields.`}));});
  }
  else if(n.kind==='link-group'){
    k=n.deps.map(id=>{const m=modOf(id);
      return N(m?m.title:id,'module',{mod:id,detail:m?m.what:'',conf:'derived',src:'docs/mindmap/edges.json'})});
  }
  else if(n.kind==='entity'){
    const o=objOf(n.obj);
    k=o.g.map(([g,fields])=>N(g,'group',{mod:n.mod,obj:n.obj,fields,conf:'derived',
      src:'Grouped from the entity field list',detail:D.groupBlurb[g]||'',meta:[['Fields',fmt(fields.length)]]}));
  }
  else if(n.kind==='group'){
    k=n.fields.map(([fn,ft,fam])=>N(fn,'field',{mod:n.mod,obj:n.obj,ftype:ft,fam,conf:'observed',
      src:'_lucernex_objects_summary.txt',detail:`A ${ft.toLowerCase()} field on ${n.obj}.`}));
  }
  else if(n.kind==='field'){
    k=[N(n.ftype,'type',{mod:n.mod,obj:n.obj,ftype:n.ftype,fam:n.fam,col:n.name,conf:'observed',
      src:'Declared field type',
      detail:D.typeNote[n.ftype]||(n.fam==='fk'
        ?'A foreign key. Lucernex names the type after the table it points at, so the relationship is declared rather than implied.'
        :n.fam==='dropdown'?'A value chosen from a master code table an administrator controls.'
        :n.fam==='soft'?'A soft reference \u2014 it names another record without a typed key behind it.'
        :'A declared field type.')})];
  }
  else if(n.kind==='type'){
    if(n.fam==='fk'){
      const e=(edgesFrom[n.obj]||[]).find(x=>x[1]===n.col);
      if(e&&e[3]&&objOf(e[3])){const t=objOf(e[3]);
        k=[N(e[3],'entity',{mod:t.m,obj:e[3],conf:'observed',src:'docs/mindmap/edges.json',
          detail:'The record this key points at. Opening it continues the map \u2014 the graph is cyclic, so you can keep going indefinitely.',
          meta:[['Reached via',n.obj+'.'+n.col],['Declared type',n.ftype],['Resolution',e[5]]]})];}
      else if(e) k=[N(e[2],'unresolved',{conf:'inferred',src:'docs/mindmap/edges.json',
        detail:'This key declares a type that resolves to no named object. Generic handles like "Entity ID" behave this way \u2014 they point at whichever table the row belongs to.'})];
    } else if(n.fam==='dropdown'){
      const m=/\(([^)]+)\)/.exec(n.ftype);
      k=[N(m?m[1]:'Code table','code-table',{conf:'derived',src:'docs/admin/007-firm-and-client-drop-downs.md',
        detail:'A master list of allowed values. Lucernex keeps 207 platform-fixed Firm Drop Downs whose values you may edit but whose catalogue you may not extend, plus tenant-authored Client Drop Downs which support cascading lists and carry an audit trail.'})];
    }
  }
  n.kids=k;k.forEach(c=>c.parent=n);return k;
}

function depthOf(n){let d=0,p=n;while(p.parent){d++;p=p.parent}return d}
function mightHaveKids(n){
  if(n.curatedKids) return n.curatedKids.length>0;
  if(n.kind==='unresolved'||n.kind==='code-table'||n.kind==='finding'
     ||n.kind==='rule'||n.kind==='fact') return false;
  if(n.kind==='type') return n.fam==='fk'||n.fam==='dropdown';
  return true;
}

const ROW=30,COLW=250,BOXH=24;
function measure(n){const name=typeof n==='string'?n:n.name;const d=typeof n==='string'?3:(n._d||0);
  return Math.min(d<=1?320:210, 24+name.length*6.9)}
function labelCap(n){return (n._d||0)<=1?44:28}

function layout(){
  laid=[];links=[];maxDepth=0;let y=0;
  (function walk(n,depth){
    maxDepth=Math.max(maxDepth,depth);
    const kids=n.open?childrenOf(n):[];
    if(kids.length){const ys=[];kids.forEach(c=>ys.push(walk(c,depth+1)));
      n._y=(ys[0]+ys[ys.length-1])/2;kids.forEach(c=>links.push([n,c]));}
    else{n._y=y;y+=ROW}
    n._x=depth*COLW;n._d=depth;laid.push(n);return n._y;
  })(ROOT,0);
}

const NS='http://www.w3.org/2000/svg';
function applyCam(){document.getElementById('cam').setAttribute('transform',`translate(${tx},${ty}) scale(${sc})`);
  document.getElementById('hz').textContent=Math.round(sc*100)+'%'}

function drawMap(){
  layout();
  const gL=document.getElementById('links'),gN=document.getElementById('nodes');
  gL.textContent='';gN.textContent='';
  links.forEach(([a,b])=>{
    const p=document.createElementNS(NS,'path');
    const x1=a._x+measure(a)+16,y1=a._y,x2=b._x-4,y2=b._y,mx=(x1+x2)/2;
    p.setAttribute('d',`M${x1},${y1} C${mx},${y1} ${mx},${y2} ${x2},${y2}`);
    p.setAttribute('class','link');gL.appendChild(p);
  });
  laid.forEach(n=>{
    const w=measure(n),g=document.createElementNS(NS,'g');
    let cls='node'+(sel===n?' sel':'');
    if(n.kind==='module'){const mm=modOf(n.mod);if(mm&&!mm.scope)cls+=' oos'}
    if(n.oos)cls+=' oos';
    if(n.kind==='rule')cls+=' rule';
    if(n.kind==='walkthrough'||n.kind==='area')cls+=' walkthrough';
    g.setAttribute('class',cls);
    g.setAttribute('transform',`translate(${n._x},${n._y-BOXH/2})`);
    const r=document.createElementNS(NS,'rect');
    r.setAttribute('class','bx');r.setAttribute('width',w+16);r.setAttribute('height',BOXH);g.appendChild(r);
    const hue=document.createElementNS(NS,'rect');
    hue.setAttribute('class','hue');hue.setAttribute('width',3);hue.setAttribute('height',BOXH-8);
    hue.setAttribute('x',0);hue.setAttribute('y',4);
    hue.setAttribute('fill',n.mod?hueOf[n.mod]:'var(--accent)');g.appendChild(hue);
    const t=document.createElementNS(NS,'text');
    t.setAttribute('x',10);t.setAttribute('y',BOXH/2);
    if(n.kind==='field'||n.kind==='entity'||n.kind==='type')t.setAttribute('class','n');
    const LC=labelCap(n);
    t.textContent=n.name.length>LC?n.name.slice(0,LC-1)+'\u2026':n.name;
    g.appendChild(t);
    const could=n.open?((n.kids||[]).length):mightHaveKids(n);
    if(could){
      const c=document.createElementNS(NS,'circle');
      c.setAttribute('class','toggle');c.setAttribute('cx',w+16);c.setAttribute('cy',BOXH/2);c.setAttribute('r',7);
      g.appendChild(c);
      const s=document.createElementNS(NS,'text');
      s.setAttribute('class','tsign');s.setAttribute('x',w+16);s.setAttribute('y',BOXH/2+.5);
      s.textContent=n.open?'\u2212':'+';g.appendChild(s);
    }
    g.addEventListener('click',ev=>{ev.stopPropagation();if(dragMoved)return;toggleNode(n)});
    gN.appendChild(g);
  });
  document.getElementById('hn').textContent=fmt(laid.length);
  document.getElementById('hd').textContent=maxDepth;
  applyCam();
}

function toggleNode(n){
  if(mightHaveKids(n)){n.open=!n.open;if(n.open)childrenOf(n)}
  selectNode(n);drawMap();
}

function selectNode(n){
  sel=n;
  const el=document.getElementById('mapdet');
  const trail=[];let p=n;while(p){trail.unshift(p.name);p=p.parent}
  const kv=[];
  if(n.meta)n.meta.forEach(x=>kv.push(x));
  if(n.kind==='entity'){const o=objOf(n.obj);
    kv.push(['Fields',fmt(o.n)]);kv.push(['Postgres table',o.t||'none']);
    kv.push(['Referenced by',fmt((edgesTo[n.obj]||[]).length)+' keys']);}
  if(n.kind==='field'){kv.push(['Declared type',n.ftype]);kv.push(['On record',n.obj]);}
  if(n.src)kv.push(['Source',n.src]);
  let deep='';
  if(n.kind==='entity') deep=`<p><a class="btn" href="#/e/${encodeURIComponent(n.obj)}">Open the full record page &rarr;</a></p>`;
  if(n.kind==='field') deep=`<p><a class="btn" href="#/f/${encodeURIComponent(n.obj)}/${encodeURIComponent(n.name)}">Open the full field page &rarr;</a></p>`;
  if(n.kind==='module') deep=`<p><a class="btn" href="#/m/${encodeURIComponent(n.mod)}">Open the full module page &rarr;</a></p>`;
  if(!deep&&n.mod&&(n.kind==='area'||n.kind==='capability'))
    deep=`<p><a class="btn" href="#/m/${encodeURIComponent(n.mod)}">Open the module documentation &rarr;</a></p>`;
  const rid=/\b([A-Z]{2,4}-R-\d{2,4})\b/.exec(n.name);
  if(rid) deep=`<p><a class="btn" href="#/r/${rid[1]}">Open rule ${rid[1]} &rarr;</a></p>`;
  el.innerHTML=`<h4>${esc(n.name)}</h4>
    <p style="font-size:11px;color:var(--muted)">${trail.map(esc).join(' \u203A ')}</p>
    ${n.conf?ctag(n.conf):''}<span class="tag">Level ${depthOf(n)}</span>
    ${n.detail?`<p>${esc(n.detail)}</p>`:''}
    ${kv.length?`<dl class="kv" style="font-size:12px">${kv.map(([a,b])=>`<dt>${esc(a)}</dt><dd>${esc(b)}</dd>`).join('')}</dl>`:''}
    ${deep}`;
  el.classList.add('on');
}

/* pointer: capture only after real movement, or clicks never reach a node */
let dragging=false,dragMoved=false,dsx=0,dsy=0,ddx=0,ddy=0,dpid=null;
function initMapEvents(){
  const stage=document.getElementById('stage');
  stage.addEventListener('pointerdown',e=>{
    if(e.button!==0)return;
    dragging=true;dragMoved=false;dpid=e.pointerId;
    ddx=e.clientX;ddy=e.clientY;dsx=e.clientX-tx;dsy=e.clientY-ty;});
  stage.addEventListener('pointermove',e=>{
    if(!dragging)return;
    if(!dragMoved){ if(Math.abs(e.clientX-ddx)<4&&Math.abs(e.clientY-ddy)<4)return;
      dragMoved=true;stage.classList.add('drag');try{stage.setPointerCapture(dpid)}catch(err){} }
    tx=e.clientX-dsx;ty=e.clientY-dsy;applyCam();});
  const end=()=>{ if(!dragging)return; dragging=false;stage.classList.remove('drag');
    if(dragMoved&&dpid!==null){try{stage.releasePointerCapture(dpid)}catch(err){}}
    dpid=null;setTimeout(()=>{dragMoved=false},0);};
  stage.addEventListener('pointerup',end);
  stage.addEventListener('pointercancel',end);
  stage.addEventListener('wheel',e=>{
    e.preventDefault();
    const r=stage.getBoundingClientRect(),mx=e.clientX-r.left,my=e.clientY-r.top;
    const k=Math.exp(-e.deltaY*0.0016),ns=Math.min(2.6,Math.max(0.06,sc*k));
    tx=mx-(mx-tx)*(ns/sc);ty=my-(my-ty)*(ns/sc);sc=ns;applyCam();},{passive:false});

  document.querySelectorAll('#maptools [data-d]').forEach(b=>b.onclick=()=>{
    const d=+b.dataset.d, base=sel||ROOT;
    (function w(n,depth){n.open=depth<d;
      if(n.open)childrenOf(n).forEach(c=>w(c,depth+1));
      else if(n.kids)n.kids.forEach(c=>c.open=false)})(base,0);
    let p=base.parent;while(p){p.open=true;p=p.parent}
    drawMap();fitMap();});
  document.getElementById('mfit').onclick=fitMap;
  document.getElementById('mreset').onclick=()=>{
    ROOT.kids=null;ROOT.open=true;childrenOf(ROOT);sel=null;
    document.getElementById('mapdet').classList.remove('on');drawMap();fitMap();};
}

function fitMap(){
  if(!laid.length)return;
  const stage=document.getElementById('stage');
  const xs=laid.map(n=>n._x),ys=laid.map(n=>n._y);
  const minX=Math.min(...xs),maxX=Math.max(...xs),minY=Math.min(...ys),maxY=Math.max(...ys);
  const w=maxX+320-minX,h=maxY-minY+120,r=stage.getBoundingClientRect();
  const whole=Math.min(r.width/w,r.height/h)*.92;
  /* a tidy tree with hundreds of leaves is taller than any screen; squeezing it to
     fit produces an unreadable smear, so stay legible and centre on the selection */
  if(whole<0.45){ sc=0.8; const f=(sel&&sel._x!==undefined)?sel:laid[0];
    tx=Math.min(180,r.width*0.25)-f._x*sc; ty=r.height/2-f._y*sc; }
  else { sc=Math.min(2.4,whole); tx=40-minX*sc; ty=r.height/2-((minY+maxY)/2)*sc; }
  applyCam();
}

function ensureMap(){
  const h=location.hash;
  const setM=/[?&]set=([^&]+)/.exec(h);
  const want=(setM&&decodeURIComponent(setM[1])==='feature')?'feature':'schema';
  /* switching datasets rebuilds the tree; each mode keeps its own interactions */
  if(mapReady&&want!==MODE){
    mapReady=false;sel=null;ROOT=null;
    const det=document.getElementById('mapdet');
    det.classList.remove('on');det.innerHTML='';
  }
  if(!mapReady){
    MODE=want;
    if(MODE==='feature'){
      ROOT=N(FM.meta.name,'product',{detail:FM.meta.detail,conf:FM.meta.conf,
        src:FM.meta.src,curatedKids:FM.root.children});
      ROOT.open=true;childrenOf(ROOT);
    } else {
      ROOT=N(D.meta.product,'product',{
        detail:`${D.meta.vendor}'s integrated workplace management system, as configured for the ${D.meta.tenant} tenant. Everything below was read out of the running application on ${D.meta.captured}.`,
        conf:'observed',src:'Live application, build '+D.meta.build});
      ROOT.open=true;childrenOf(ROOT);
    }
    initMapEvents();mapReady=true;drawMap();fitMap();
  }
  if(MODE==='feature'){
    const f=/[?&]f=([^&]+)/.exec(h);
    if(f){
      const id=decodeURIComponent(f[1]);
      const node=childrenOf(ROOT).find(c=>c.key===id);
      if(node){ node.open=true;childrenOf(node);selectNode(node);drawMap();fitMap(); }
    }
  } else {
    const m=/[?&]m=([^&]+)/.exec(h);
    if(m){
      const id=decodeURIComponent(m[1]);
      const node=childrenOf(ROOT).find(c=>c.mod===id);
      if(node){ node.open=true;
        const wt=childrenOf(node).find(c=>c.kind==='walkthrough');
        if(wt){wt.open=true;childrenOf(wt);selectNode(wt);} else selectNode(node);
        drawMap();fitMap(); }
    }
  }
}
