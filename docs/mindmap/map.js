/* The mind map view. Lazily built the first time #/map is opened, so the rest of
   the application costs nothing when nobody looks at it. */

let uid=0, ROOT=null, laid=[], links=[], maxDepth=0, mapReady=false;
let tx=90, ty=0, sc=1, sel=null, MODE='schema';

function N(name,kind,opt){return Object.assign({id:++uid,name,kind,open:false,kids:null,parent:null},opt||{})}

function fromCurated(c,mod){
  /* the feature map writes `conf`/`src`; the older hand-authored trees write
     `confidence`/`source`. Reading only one of each silently dropped half the
     evidence labels and every source path on the feature map. */
  return N(c.name,c.kind||'capability',{mod:c.mod||mod,detail:c.detail||'',
    conf:c.conf||c.confidence||'derived',
    src:c.src||c.source||'Hand-authored module analysis',
    key:c.key,rid:c.rid,oos:!!c.oos,
    statement:c.statement,parts:c.parts,objects:c.objects,shots:c.shots,
    curatedKids:c.children||[]});
}

/* What a single column is, said in a sentence a reader can use: the label the
   user sees, who owns the field, whether it is required, and what its catalogued
   type code means. A field node used to say "a text field on Contract". */
const FLAG_FIRM=1,FLAG_REQ=2,FLAG_RO=4,FLAG_INV_REQ=8,FLAG_FUNC=16,FLAG_NOPG=32;
function fieldProse(obj,col,ftype,fam,label,flags,code,def,role,pg){
  const s=[];
  /* the vendor's own definition leads: it is the only source that says what the
     field is FOR rather than what it is called */
  if(def) s.push(def);
  if(label) s.push(`Shown to users as \u201c${label}\u201d.`);
  if(role&&D.roleNote&&D.roleNote[role]) s.push(`In the schema it is ${D.roleNote[role]}.`);
  s.push(fam==='fk'
    ?`A typed foreign key on ${obj}, declared as ${ftype} \u2014 the type names the record it points at.`
    :fam==='dropdown'
    ?`A coded value on ${obj}, bound to a master list an administrator controls rather than a developer.`
    :fam==='soft'
    ?`A soft reference on ${obj}: it names another record without a typed key behind it, so the join has to be made explicit in a rebuild.`
    :`A ${String(ftype).toLowerCase()} column on ${obj}.`);
  if(code&&D.typeLegend&&D.typeLegend[code]) s.push(`Catalogued as ${code}: ${D.typeLegend[code]}`);
  if(flags&FLAG_FIRM) s.push('Firm scope \u2014 this tenant defined it, the platform did not ship it. Firm fields are physical Firm_-prefixed columns, so adding one is a schema change.');
  else if(code) s.push('Global scope \u2014 shipped by the platform for every tenant.');
  /* the two captures disagree on 213 fields estate-wide, so which one marks a
     field required is itself the finding \u2014 never flatten them into "required" */
  if(flags&(FLAG_REQ|FLAG_INV_REQ)) s.push(
    ((flags&FLAG_REQ)&&(flags&FLAG_INV_REQ))
      ? 'Both the Data Fields catalogue and the field inventory mark it required.'
      : 'Marked required by '+((flags&FLAG_REQ)?'the Data Fields catalogue, but NOT by the field inventory':'the field inventory, but NOT by the Data Fields catalogue')
        +'. The two captures disagree on 213 fields estate-wide; this is one of them, so a rebuild reading only one capture gets this field wrong.');
  if(flags&(FLAG_REQ|FLAG_INV_REQ)) s.push('Required-ness has no layout-level layer: the asterisk a user sees is this flag, rendered at paint time.');
  if(flags&FLAG_RO) s.push('Read-only in the catalogue \u2014 written by the engine, not by a user.');
  if(flags&FLAG_FUNC) s.push('A functional field: it carries business meaning rather than plumbing.');
  if(pg){const bit=pg.split(':');
    s.push('Lands in the replication target as '+bit[0]+(bit[1]?', typed '+bit[1]:'')+'.');}
  else if(flags&FLAG_NOPG) s.push('Not extracted to PostgreSQL \u2014 the replication loader creates no column for it, so anything reading the replica rather than the product will not see this field.');
  if(ftype==='Currency'||ftype==='Percentage') s.push('Stored as TEXT in the physical database, like 6,882 of the 7,069 exported columns; a rebuild has to impose its own BigDecimal typing.');
  return s.join(' ');
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
    if(cur) k.push(N('Analysis \u00b7 '+cur.name,'walkthrough',{mod:m.id,curatedKids:cur.children||[],
      conf:cur.confidence||'derived',src:cur.source||'Hand-authored module analysis',
      detail:(cur.detail||'')+' This is a hand-written analysis branch inside the schema map, kept distinct from the feature map: it organises this module by how it works internally, and carries the rules and constraints the schema alone cannot show.'}));
    if(m.dep&&m.dep.length) k.push(N('Depends on '+m.dep.length+' other module'+(m.dep.length>1?'s':''),'link-group',
      {mod:m.id,deps:m.dep,conf:'derived',src:'docs/mindmap/edges.json',
       detail:'Modules this one holds foreign keys into. Following these is how you find the blast radius of a schema change.'}));
    m.objects.forEach(name=>{const o=objOf(name);if(!o)return;
      /* the description comes from the Data Fields catalogue, not from a
         template: the node has to say what the record IS */
      k.push(N(name,'entity',{mod:m.id,obj:name,conf:'observed',
        src:(o.ds&&o.ds.length?o.ds.join(', '):'_lucernex_objects_summary.txt'),
        detail:o.d||`A record type in the ${m.title.toLowerCase()} area, holding ${fmt(o.n)} fields.`}));});
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
    k=n.fields.map(f=>{
      const fn=f[0],ft=f[1],fam=f[2],label=f[3]||'',flags=f[4]||0,code=f[5]||'';
      const def=f[6]||'',role=f[7]||'',pg=f[8]||'';
      return N(fn,'field',{mod:n.mod,obj:n.obj,ftype:ft,fam,label,flags,code,def,role,pg,conf:'observed',
        src:def?'docs/data-model/pg/bbw-field-inventory.csv'
               :(code?'docs/data-fields/all-fields.csv':'_lucernex_objects_summary.txt'),
        detail:fieldProse(n.obj,fn,ft,fam,label,flags,code,def,role,pg)});});
  }
  else if(n.kind==='field'){
    k=[N(n.ftype,'type',{mod:n.mod,obj:n.obj,ftype:n.ftype,fam:n.fam,col:n.name,code:n.code,conf:'observed',
      src:'Declared field type',
      detail:((n.code&&D.typeLegend&&D.typeLegend[n.code])?D.typeLegend[n.code]+' ':'')
       +(D.typeNote[n.ftype]||(n.fam==='fk'
        ?'A foreign key. Lx names the type after the table it points at, so the relationship is declared rather than implied.'
        :n.fam==='dropdown'?'A value chosen from a master code table an administrator controls.'
        :n.fam==='soft'?'A soft reference \u2014 it names another record without a typed key behind it.'
        :'A declared field type.'))})];
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
        detail:'A master list of allowed values. Lx keeps 207 platform-fixed Firm Drop Downs whose values you may edit but whose catalogue you may not extend, plus tenant-authored Client Drop Downs which support cascading lists and carry an audit trail.'})];
    }
  }
  n.kids=k;k.forEach(c=>c.parent=n);return k;
}

function depthOf(n){let d=0,p=n;while(p.parent){d++;p=p.parent}return d}
function mightHaveKids(n){
  if(n.curatedKids) return n.curatedKids.length>0;
  if(n.kind==='unresolved'||n.kind==='code-table'||n.kind==='finding'
     ||n.kind==='rule'||n.kind==='fact'||n.kind==='question') return false;
  if(n.kind==='type') return n.fam==='fk'||n.fam==='dropdown';
  return true;
}

const ROW=30,COLW=250,BOXH=24;
/* Feature-map labels are names (<=24 chars), so depth-2+ boxes size to fit the
   full name: 24 + 24*6.9 = 190 < 230, nothing clips. Schema-map field names
   can still run long, so the cap stays. */
function measure(n){const name=typeof n==='string'?n:n.name;const d=typeof n==='string'?3:(n._d||0);
  return Math.min(d<=1?320:230, 24+name.length*6.9)}
function labelCap(n){return (n._d||0)<=1?44:32}

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
    if(n.kind==='group')cls+=' rule';
    /* an open question is not a finding: drawn like an unresolved node so a
       reader can see at a glance how much of a feature is still unknown */
    if(n.kind==='question')cls+=' oos';
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

/* A rule's own statement, in the panel. The complaint that started this was
   "you see the name of the rule, but nothing else" \u2014 so a rule node renders the
   statement, the labelled parts a rule engine would consume, what it constrains,
   and the document that states it. */
function rulePanel(rid){
  const r=(RULES.rules||[]).find(x=>x.id===rid);
  if(!r) return '';
  const out=[];
  if(r.statement) out.push(`<p class="lead">${esc(r.statement)}</p>`);
  if(r.parts&&r.parts.length)
    out.push(`<dl class="kv" style="font-size:12px">${r.parts.map(([a,b])=>
      `<dt>${esc(a)}</dt><dd>${esc(b)}</dd>`).join('')}</dl>`);
  else if(r.text) out.push(`<p>${esc(r.text)}</p>`);
  if(r.quote) out.push(`<p style="border-left:2px solid var(--line);padding-left:9px;color:var(--ink2)">
    &ldquo;${esc(r.quote)}&rdquo;</p>`);
  if(r.objects&&r.objects.length)
    out.push(`<p style="font-size:12px">Constrains ${r.objects.map(o=>
      objOf(o)?`<a href="#/e/${encodeURIComponent(o)}">${esc(o)}</a>`:esc(o)).join(', ')}.</p>`);
  if(r.fields&&r.fields.length)
    out.push(`<p style="font-size:11.5px;color:var(--muted)">Columns named: ${r.fields.map(esc).join(', ')}</p>`);
  if(r.related&&r.related.length)
    out.push(`<p style="font-size:12px">Cites ${r.related.map(i=>
      `<a href="#/r/${esc(i)}">${esc(i)}</a>`).join(', ')}.</p>`);
  if(r.confNote) out.push(`<p style="font-size:11.5px;color:var(--muted)">Confidence: ${esc(r.confNote)}</p>`);
  return out.join('');
}

/* An entity's caveats, rendered as callouts rather than buried in a sentence. */
function noteBlocks(notes){
  if(!notes||!notes.length) return '';
  return notes.map(([t,c,d])=>`<div class="find"><h5>${esc(t)} ${ctag(c)}</h5><p>${esc(d)}</p></div>`).join('');
}

function selectNode(n){
  sel=n;
  const el=document.getElementById('mapdet');
  const trail=[];let p=n;while(p){trail.unshift(p.name);p=p.parent}
  const kv=[];
  if(n.meta)n.meta.forEach(x=>kv.push(x));
  let extra='';
  if(n.kind==='entity'){const o=objOf(n.obj);
    kv.push(['Fields',fmt(o.n)]);kv.push(['Postgres table',o.t||'none']);
    if(o.tc>1)kv.push(['Physical tables',fmt(o.tc)]);
    if(o.cat)kv.push(['Catalogued fields',`${fmt(o.cat[0])} (${fmt(o.cat[1])} global, ${fmt(o.cat[2])} firm)`]);
    if(o.inv)kv.push(['Fields with a definition',`${fmt(o.inv[1])} of ${fmt(o.inv[0])}`]);
    if(o.pgt&&o.pgt.length)kv.push(['Physical tables',o.pgt.join(', ')]);
    if(o.pgdb)kv.push(['Replication database',o.pgdb]);
    kv.push(['Referenced by',fmt((edgesTo[n.obj]||[]).length)+' keys']);
    kv.push(['Points at',fmt((edgesFrom[n.obj]||[]).filter(e=>e[3]).length)+' records']);
    const rs=(RULES.byEntity||{})[n.obj]||[];
    if(rs.length)kv.push(['Rules that name it',fmt(rs.length)]);
    extra=noteBlocks(o.notes);
    if(rs.length) extra+=`<p style="font-size:12px">Governed by ${rs.slice(0,10).map(i=>
      `<a href="#/r/${esc(i)}">${esc(i)}</a>`).join(', ')}${rs.length>10?` and ${rs.length-10} more`:''}.</p>`;
  }
  if(n.kind==='field'){
    if(n.label)kv.push(['Label',n.label]);
    kv.push(['Declared type',n.ftype]);kv.push(['On record',n.obj]);
    if(n.code)kv.push(['Catalogue type',n.code]);
    kv.push(['Scope',(n.flags&FLAG_FIRM)?'Firm \u2014 defined by this tenant':(n.code?'Global \u2014 shipped by the platform':'not catalogued')]);
    if(n.flags&(FLAG_REQ|FLAG_INV_REQ))kv.push(['Required',
      ((n.flags&FLAG_REQ)&&(n.flags&FLAG_INV_REQ))?'yes \u2014 in both captures'
      :((n.flags&FLAG_REQ)?'catalogue only \u2014 the inventory does not'
                          :'inventory only \u2014 the catalogue does not')]);
    if(n.flags&FLAG_RO)kv.push(['Read-only','yes']);
    if(n.role&&D.roleNote&&D.roleNote[n.role])kv.push(['Key role',n.role]);
    if(n.pg)kv.push(['Physical column',n.pg.replace(':',' \u00b7 ')]);
    else if(n.flags&FLAG_NOPG)kv.push(['Physical column','not extracted to the replica']);
  }
  if(n.kind==='module'){const m=modOf(n.mod);
    if(m&&m.lead)extra=`<p>${esc(m.lead)}</p>`;}
  if(n.shots&&n.shots.length)
    extra+=`<p style="font-size:11.5px;color:var(--muted)">Screen captures: ${n.shots.slice(0,8).map(s=>esc(s.split('/').pop())).join(', ')}${n.shots.length>8?` +${n.shots.length-8} more`:''}</p>`;
  if(n.src)kv.push(['Source',n.src]);
  /* Every node also exists as a markdown document in the static mirror. Shown as
     a path rather than a link: this page is published standalone, where a
     relative link into the mirror would 404. */
  const fslug=s=>String(s).replace(/[^A-Za-z0-9_.-]/g,'_');
  if(n.kind==='entity')kv.push(['Markdown','md/entities/'+fslug(n.obj)+'.md']);
  else if(n.kind==='module')kv.push(['Markdown','md/modules/'+fslug(n.mod)+'.md']);
  let deep='';
  if(n.kind==='entity') deep=`<p><a class="btn" href="#/e/${encodeURIComponent(n.obj)}">Open the full record page &rarr;</a></p>`;
  if(n.kind==='field') deep=`<p><a class="btn" href="#/f/${encodeURIComponent(n.obj)}/${encodeURIComponent(n.name)}">Open the full field page &rarr;</a></p>`;
  if(n.kind==='module') deep=`<p><a class="btn" href="#/m/${encodeURIComponent(n.mod)}">Open the full module page &rarr;</a></p>`;
  /* feature-map rule nodes carry their ID in `rid`: the visible label is a short
     name, so the ID is not in the node text to regex out */
  const rid=n.rid||((/\b([A-Z]{2,4}-R-\d{2,4})\b/).exec(n.name)||[])[1];
  if(rid){ extra=rulePanel(rid)+extra;
    kv.push(['Markdown','md/rules/'+fslug(rid)+'.md']);
    deep=`<p><a class="btn" href="#/r/${rid}">Open rule ${rid} &rarr;</a></p>`; }
  /* a rule's own statement replaces the run-on detail string; everything else
     keeps its prose */
  const body=(rid&&extra)?'':(n.detail?`<p>${esc(n.detail)}</p>`:'');
  el.innerHTML=`<h4>${esc(n.name)}</h4>
    <p style="font-size:11px;color:var(--muted)">${trail.map(esc).join(' \u203A ')}</p>
    ${n.conf?ctag(n.conf):''}<span class="tag">Level ${depthOf(n)}</span>
    ${rid?`<span class="tag">${esc(rid)}</span>`:''}
    ${body}${extra}
    ${kv.length?`<dl class="kv" style="font-size:12px">${kv.map(([a,b])=>`<dt>${esc(a)}</dt><dd>${esc(b)}</dd>`).join('')}</dl>`:''}
    ${deep}`;
  el.classList.add('on');
}

/* pointer: capture only after real movement, or clicks never reach a node */
let dragging=false,dragMoved=false,dsx=0,dsy=0,ddx=0,ddy=0,dpid=null;
function initMapEvents(){
  /* mode switches rebuild the tree but NOT these listeners: #stage is one static
     element, and wiring it twice doubles every pan and zoom step */
  if(initMapEvents.done)return;initMapEvents.done=true;
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
  document.getElementById('mreset').onclick=resetMap;
  /* the view toggle lives on the map itself, so switching is one click and
     always visible - no hunting through the sidebar */
  const go=d=>{location.hash=d};
  const bf=document.getElementById('mfeat'),bs=document.getElementById('mschema');
  if(bf)bf.onclick=()=>go('/map?set=feature');
  if(bs)bs.onclick=()=>go('/map');
}

function syncMapMode(){
  const bf=document.getElementById('mfeat'),bs=document.getElementById('mschema');
  if(bf)bf.classList.toggle('on',MODE==='feature');
  if(bs)bs.classList.toggle('on',MODE!=='feature');
  const mm=document.getElementById('mmode');
  if(mm)mm.textContent=MODE==='feature'?'feature':'schema';
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
      /* every feature and its capabilities visible on arrival - the map opens
         readable, not as one root box demanding a click per branch */
      ROOT.open=true;childrenOf(ROOT).forEach(a=>{a.open=true;childrenOf(a)});
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
  syncMapMode();
}

/* the feature map's natural resting state: root + areas open, capabilities
   showing. Reset returns to it in either mode. */
function resetMap(){
  ROOT.kids=null;ROOT.open=true;childrenOf(ROOT);sel=null;
  if(MODE==='feature')childrenOf(ROOT).forEach(a=>{a.open=true;childrenOf(a)});
  document.getElementById('mapdet').classList.remove('on');drawMap();fitMap();
}
