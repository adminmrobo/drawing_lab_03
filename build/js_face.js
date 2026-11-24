/* ===================== 얼굴 그리기 도구 (SVG) ===================== */
var FC={ink:'#2a2230',skin:'#F8E3D3',guide:'#e0337f',guide2:'#9aa5b1',iris:'#4a3b5c',hot:'#e8731a'};
function pth(s,d,a){a=a||{};return el('path',{d:d,fill:a.fill||'none',stroke:a.stroke||FC.ink,'stroke-width':a.w||2.2,'stroke-linecap':'round','stroke-linejoin':'round','stroke-dasharray':a.dash||null,opacity:a.op==null?null:a.op},s);}
function hline(s,x1,x2,y,lab,col,right){el('line',{x1:x1,y1:y,x2:x2,y2:y,stroke:col||FC.guide,'stroke-width':1.6,'stroke-dasharray':'6 4'},s);if(lab)ktxt(s,right?x2+6:x1-6,y+4,lab,{size:12.5,fill:col||FC.guide,anchor:right?'start':'end',weight:'bold'});}
function P2(x,y){return x.toFixed(1)+','+y.toFixed(1);}
/* 앞에서 본 얼굴. o.sex 'f'|'m', o.H 머리 높이, 비율 값은 모두 예시 기준값 */
function faceGeo(o){var sex=o.sex||'f',cx=o.cx||260,top=o.top||40,G={sex:sex,cx:cx,top:top};
  if(sex==='f'){var H=o.H||340,R=H/2;G.H=H;G.R=R;G.cy=top+R;G.chin=top+H;G.xw=R*(o.shave==null?0.86:o.shave);G.half=G.xw;}
  else{var r=o.r||(o.H||340)/3.1,a=(o.attach==null?0.1:o.attach)*r,rect=1.3*r,tip=(o.tip==null?0.7:o.tip)*r;G.r=r;G.cy=top+r;G.y1=G.cy+a;G.jaw=G.y1+rect;G.chin=G.jaw+tip;G.H=G.chin-top;G.xw=0.97*r;G.half=G.xw;G.cut=o.cut==null?0.45:o.cut;}
  var sh=(o.shift||0)*G.H;G.eyelid=top+G.H*(o.eyelid==null?0.5:o.eyelid)+sh;
  G.nose=G.chin-G.H*(o.nose==null?(sex==='f'?0.25:0.27):o.nose)+sh;
  G.mouth=G.nose+(G.chin-G.nose)*(o.mouth==null?(sex==='f'?0.5:1/3):o.mouth);
  G.hair=top+G.H*(o.hair==null?(sex==='f'?1/6:0.17):o.hair);
  return G;}
function contourD(G,o){var cx=G.cx,top=G.top;
  if(G.sex==='f'){var R=G.R,cy=G.cy,xw=G.xw,cb=o.cheek==null?0.55:o.cheek;
    return 'M'+P2(cx,top)+' C'+P2(cx-R*0.56,top)+' '+P2(cx-xw,cy-R*0.62)+' '+P2(cx-xw,cy-R*0.05)+' C'+P2(cx-xw,cy+R*cb)+' '+P2(cx-R*0.36,G.chin-R*0.1)+' '+P2(cx,G.chin)+' C'+P2(cx+R*0.36,G.chin-R*0.1)+' '+P2(cx+xw,cy+R*cb)+' '+P2(cx+xw,cy-R*0.05)+' C'+P2(cx+xw,cy-R*0.62)+' '+P2(cx+R*0.56,top)+' '+P2(cx,top)+'Z';}
  var r=G.r,yA2=G.cy-Math.sqrt(Math.max(0,r*r-G.xw*G.xw)),jx=0.9*r,fw=0.32*r*G.cut,tipY=G.chin;
  var jy=G.jaw;var cornerIn=0.06*r;
  return 'M'+P2(cx,top)+' A'+r+','+r+' 0 0 0 '+P2(cx-G.xw,yA2)+' L'+P2(cx-G.xw,G.y1)+' L'+P2(cx-jx,jy-cornerIn)+' Q'+P2(cx-jx+2,jy)+' '+P2(cx-jx+cornerIn*1.2,jy+cornerIn)+' L'+P2(cx-fw,tipY)+(fw>0?' L'+P2(cx+fw,tipY):'')+' L'+P2(cx+jx-cornerIn*1.2,jy+cornerIn)+' Q'+P2(cx+jx-2,jy)+' '+P2(cx+jx,jy-cornerIn)+' L'+P2(cx+G.xw,G.y1)+' L'+P2(cx+G.xw,yA2)+' A'+r+','+r+' 0 0 0 '+P2(cx,top)+'Z';}
function eyeF(s,x,y,w,h,side,o){/* x: 눈 가운데, y: 위 눈꺼풀 높이 */
  var sex=o.sex,tilt=o.tilt||0,lid=o.lid||0,inX=x-side*w/2,outX=x+side*w/2;var g=el('g',{},s);
  var inY=y+h*0.22,outY=y+h*0.12-tilt*h*0.3;
  if(sex==='f'){el('ellipse',{cx:x,cy:y+h*0.56,rx:w*0.34,ry:h*0.44,fill:FC.iris},g);el('ellipse',{cx:x,cy:y+h*0.62,rx:w*0.16,ry:h*0.24,fill:'#1d1622'},g);el('circle',{cx:x-side*w*0.12,cy:y+h*0.38,r:w*0.08,fill:'#fff'},g);
    pth(g,'M'+P2(inX+side*w*0.08,y+h*0.95)+' Q'+P2(x,y+h*1.05)+' '+P2(outX-side*w*0.1,y+h*0.9),{w:1.6});}
  else{el('circle',{cx:x+side*w*0.02,cy:y+h*0.5,r:h*0.42,fill:FC.iris},g);el('circle',{cx:x+side*w*0.02,cy:y+h*0.52,r:h*0.2,fill:'#1d1622'},g);
    pth(g,'M'+P2(inX,inY+h*0.1)+' Q'+P2(x,y+h*1.15)+' '+P2(outX,outY+h*0.35),{w:1.3});}
  if(lid>0){var ly=y+lid*h;el('path',{d:'M'+P2(inX-side*2,y-h*0.5)+' L'+P2(outX+side*3,y-h*0.5)+' L'+P2(outX+side*3,outY+lid*h*0.9)+' Q'+P2(x,ly)+' '+P2(inX-side*2,inY+lid*h*0.6)+'Z',fill:FC.skin},g);
    pth(g,'M'+P2(inX,inY)+' Q'+P2(x,y-h*0.12)+' '+P2(outX,outY),{w:1,op:.45});inY+=lid*h*0.6;outY+=lid*h*0.9;y=ly-h*0.12;}
  pth(g,'M'+P2(inX,inY)+' Q'+P2(x,y-h*0.12)+' '+P2(outX,outY),{w:sex==='f'?4.2:3});
  if(sex==='f')pth(g,'M'+P2(outX,outY)+' l'+P2(side*w*0.12,-h*0.08),{w:2.6});
  return g;}
function brow(s,x,y,w,side,sex,raise){raise=raise||0;var g=pth(s,'M'+P2(x-side*w*0.5,y+2+raise*4)+' Q'+P2(x,y-(sex==='f'?4:3))+' '+P2(x+side*w*0.55,y+2-raise*10),{w:sex==='f'?1.6:2.8});return g;}
function faceFront(s,o){o=o||{};var G=faceGeo(o),cx=G.cx,sex=G.sex,g=el('g',{},s);
  var ew=o.ew||(sex==='f'?0.44*G.R:0.5*G.r),eh=ew*(o.eyeRatio||(sex==='f'?0.92:0.48)),gap=(o.gap==null?(sex==='f'?1.1:1):o.gap)*ew;
  G.ew=ew;G.eh=eh;G.gapPx=gap;
  if(o.neck){var nw=o.neckW||(sex==='f'?ew*1.05:ew*1.25);el('rect',{x:cx-nw,y:G.chin-G.H*0.12,width:2*nw,height:G.H*0.32,fill:FC.skin},g);pth(g,'M'+P2(cx-nw,G.chin-G.H*0.1)+' L'+P2(cx-nw,G.chin+G.H*0.2)+' M'+P2(cx+nw,G.chin-G.H*0.1)+' L'+P2(cx+nw,G.chin+G.H*0.2));}
  if(o.hairCol){var hb=o.hairCol;el('path',{d:'M'+P2(cx-G.half*1.12,G.eyelid+G.H*0.28)+' Q'+P2(cx-G.half*1.25,G.top-G.H*0.06)+' '+P2(cx,G.top-G.H*0.06)+' Q'+P2(cx+G.half*1.25,G.top-G.H*0.06)+' '+P2(cx+G.half*1.12,G.eyelid+G.H*0.28)+'Z',fill:hb,stroke:FC.ink,'stroke-width':2},g);}
  // 귀
  var eT=o.earTop!=null?o.earTop:(sex==='f'?G.eyelid+eh*0.5:G.eyelid),eB=o.earBot!=null?o.earBot:(sex==='f'?G.nose-G.H*0.015:G.nose-G.H*0.02);
  [-1,1].forEach(function(d){var ex=cx+d*(G.half*(sex==='f'?0.9:0.93));pth(g,'M'+P2(ex,eT)+' C'+P2(ex+d*G.H*0.11,eT-6)+' '+P2(ex+d*G.H*0.115,eB)+' '+P2(ex,eB),{fill:FC.skin,w:2});});
  el('path',{d:contourD(G,o),fill:FC.skin,stroke:FC.ink,'stroke-width':2.6,'stroke-linejoin':'round'},g);
  G.earTop=eT;G.earBot=eB;
  if(o.hairCol){var hd='M'+P2(cx-G.half*1.05,G.eyelid-eh*0.2)+' Q'+P2(cx-G.half*1.1,G.top-G.H*0.04)+' '+P2(cx,G.top-G.H*0.05)+' Q'+P2(cx+G.half*1.1,G.top-G.H*0.04)+' '+P2(cx+G.half*1.05,G.eyelid-eh*0.2);
    var n=9;for(var i=0;i<=n;i++){var x=cx+G.half*(1.0-2*i/n);var tip=i%2===1;var y=tip?G.eyelid-eh*(0.45+0.1*((i*7)%3)):G.hair+G.H*(0.05+0.02*Math.abs(i-n/2)/n*4);if(i===0||i===n)y=G.eyelid-eh*0.2;hd+=' L'+P2(x,y);}
    el('path',{d:hd+'Z',fill:o.hairCol,stroke:FC.ink,'stroke-width':2,'stroke-linejoin':'round'},g);}
  // 눈·눈썹
  var exs=[cx-gap/2-ew/2,cx+gap/2+ew/2];G.eyes=exs;
  exs.forEach(function(x,i){var d=i?1:-1;eyeF(g,x,G.eyelid,ew,eh,d,{sex:sex,tilt:o.tilt,lid:o.lid});
    var by=o.browY!=null?o.browY:(sex==='f'?G.eyelid-eh*0.8:G.eyelid-eh*1.0);brow(g,x+d*ew*0.04,by,ew*1.05,d,sex,o.brow);G.browY=by;});
  // 코
  if(sex==='f'){pth(g,'M'+P2(cx-1,G.nose-G.H*0.03)+' Q'+P2(cx-5,G.nose-G.H*0.012)+' '+P2(cx-1,G.nose),{w:1.6});}
  else{pth(g,'M'+P2(cx+3,G.eyelid+eh*0.6)+' L'+P2(cx+5,G.nose-G.H*0.03),{w:1.5,op:.8});pth(g,'M'+P2(cx-7,G.nose-G.H*0.015)+' Q'+P2(cx-3,G.nose+2)+' '+P2(cx+4,G.nose),{w:1.8});}
  // 입
  var mw=sex==='f'?G.R*0.17:G.r*0.3;pth(g,'M'+P2(cx-mw,G.mouth)+' Q'+P2(cx,G.mouth+(o.smile==null?4:o.smile))+' '+P2(cx+mw,G.mouth),{w:sex==='f'?2:2.2});
  if(o.glasses){var gl=o.glasses,rh=eh*(gl.rim||1.3),rw=ew*1.25;exs.forEach(function(x){var y0=G.eyelid+eh*0.5-rh/2+(gl.drop||0)*eh;
      if(gl.under)pth(g,'M'+P2(x-rw/2,y0+rh*0.25)+' L'+P2(x-rw/2,y0+rh)+' L'+P2(x+rw/2,y0+rh)+' L'+P2(x+rw/2,y0+rh*0.25),{stroke:C.blue,w:3});
      else el('rect',{x:x-rw/2,y:y0,width:rw,height:rh,rx:4,fill:'none',stroke:C.blue,'stroke-width':3},g);});
    pth(g,'M'+P2(exs[0]+rw/2,G.eyelid+eh*0.3)+' Q'+P2(cx,G.eyelid+eh*0.1)+' '+P2(exs[1]-rw/2,G.eyelid+eh*0.3),{stroke:C.blue,w:2.5});}
  if(o.guide){var gx1=cx-G.half-40,gx2=cx+G.half+26;var L=o.guide===true?['hair','eyelid','nose','mouth']:o.guide;
    var lab={hair:'머리선',eyelid:'위 눈꺼풀',nose:'코 밑',mouth:'입',brow:'눈썹'};L.forEach(function(k){var y=k==='brow'?G.browY:G[k];hline(s,gx1+30,gx2,y,lab[k],k==='mouth'||k==='hair'?FC.guide2:FC.guide,true);});
    el('line',{x1:gx1+20,y1:G.top,x2:gx1+20,y2:G.chin,stroke:FC.guide2,'stroke-width':1.5},s);el('line',{x1:gx1+14,y1:G.top,x2:gx1+26,y2:G.top,stroke:FC.guide2,'stroke-width':1.5},s);el('line',{x1:gx1+14,y1:G.chin,x2:gx1+26,y2:G.chin,stroke:FC.guide2,'stroke-width':1.5},s);}
  G.g=g;return G;}
/* 옆얼굴(왼쪽을 본다) */
function sideGeo(o){var sex=o.sex||'f',cx=o.cx||270,cy=o.cy||190,r=o.r||120;var G={sex:sex,cx:cx,cy:cy,r:r,top:cy-r};
  G.chin=sex==='f'?cy+0.8*r:cy+0.95*r;G.H=G.chin-G.top;G.front=cx-r;G.W=2*r;
  G.eyelid=G.top+G.H*0.5;G.brow=G.eyelid-G.H*(sex==='f'?0.045:0.035);
  if(sex==='m'){var a=G.H*0.17,b=(G.H-a)/3;G.hair=G.top+a;G.brow=G.hair+b;var mid=o.mid==null?1:o.mid;var rest=G.chin-G.brow;G.nose=G.brow+rest*mid/(1+mid);G.eyelid=G.top+G.H*0.5;}
  else{var midf=o.mid==null?1:o.mid;var rest2=G.chin-G.brow;G.nose=G.brow+rest2*0.55*midf/(0.55*midf+0.45);G.hair=G.top+G.H/6;}
  G.mouth=G.nose+(G.chin-G.nose)*(sex==='f'?0.45:1/3);return G;}
function faceSide(s,o){o=o||{};var G=sideGeo(o),cx=G.cx,cy=G.cy,r=G.r,sex=G.sex,F=G.front,root=el('g',{},s);
  var ng=el('g',{},root),g=el('g',{},root);var rot=o.chinUp||0;if(rot)g.setAttribute('transform','rotate('+rot+' '+(cx+0.05*r)+' '+(cy+0.55*r)+')');
  // 목 기하
  var na=rad(o.neckAngle==null?5:o.neckAngle),nw=(o.neckW||(sex==='f'?0.25:0.5))*G.W,ncx=cx+0.05*r,fx0=ncx-nw/2,bx0=ncx+nw/2;
  var jc=sex==='f'?[cx-0.12*r,cy+0.6*r]:[cx+0.02*r,cy+0.72*r],chinX=sex==='f'?F+0.12*r:F+0.05*r,cp=[chinX+0.08*r,G.chin];
  var tt=clamp((fx0-cp[0])/(jc[0]-cp[0]),0,1),yT=cp[1]+tt*(jc[1]-cp[1]);var N=[bx0+0.04*r,cy+0.62*r];var nb=G.chin+0.95*r,dx=Math.tan(na)*(nb-yT);
  var curve=o.curve!==false;
  el('path',{d:'M'+P2(fx0,cy+0.3*r)+' L'+P2(fx0,yT)+' L'+P2(fx0+dx,nb)+' L'+P2(bx0+dx,nb)+' L'+P2(bx0,N[1])+' L'+P2(bx0,cy+0.3*r)+'Z',fill:FC.skin},ng);
  // 머리
  var bk=1+(o.back||0)*0.22,backX=cx+r*bk;var lip=o.lip==null?(sex==='f'?0.15:0.6):o.lip,nk=o.noseK||1;
  var up='M'+P2(N[0],N[1])+' C'+P2(N[0]+0.25*r,N[1]-0.04*r)+' '+P2(backX,cy+0.35*r)+' '+P2(backX,cy-0.05*r)+' C'+P2(backX,cy-0.62*r)+' '+P2(cx+0.38*r,cy-r)+' '+P2(cx,cy-r)+' C'+P2(cx-0.6*r,cy-r)+' '+P2(F,cy-0.66*r)+' '+P2(F+0.02*r,cy-0.3*r)+' L'+P2(F+0.01*r,G.brow-0.05*r)+' Q'+P2(F+0.06*r,G.brow)+' '+P2(F+0.04*r,G.eyelid+0.06*r);
  if(sex==='f')up+=' L'+P2(F+0.0*r,G.nose-0.1*r)+' L'+P2(F-0.1*r*nk,G.nose-0.025*r)+' L'+P2(F-0.01*r,G.nose+0.03*r)+' L'+P2(F-0.01*r-lip*0.06*r,G.mouth-0.05*r)+' L'+P2(F+0.02*r,G.mouth-0.01*r)+' L'+P2(F-0.02*r-lip*0.08*r,G.mouth+0.02*r)+' L'+P2(F+0.03*r,G.mouth+0.08*r);
  else up+=' L'+P2(F-0.2*r*nk,G.nose-0.02*r)+' L'+P2(F+0.0*r,G.nose+0.03*r)+' L'+P2(F-0.04*r-lip*0.06*r,G.mouth-0.04*r)+' L'+P2(F+0.03*r,G.mouth)+' L'+P2(F-0.01*r-lip*0.07*r,G.mouth+0.05*r)+' Q'+P2(F-0.04*r-lip*0.04*r,G.mouth+0.12*r)+' '+P2(F+0.02*r,G.mouth+0.15*r);
  up+=' L'+P2(chinX-0.03*r,G.chin-0.07*r)+' Q'+P2(chinX-0.02*r,G.chin+0.01*r)+' '+P2(cp[0],cp[1])+' L'+P2(fx0,yT);
  el('path',{d:up+' L'+P2(jc[0],jc[1])+' L'+P2(N[0],N[1])+'Z',fill:FC.skin},g);
  // 목 선(머리와 잇는 곳)
  var fr=curve?'M'+P2(fx0-0.1*r,yT-0.01*r)+' Q'+P2(fx0,yT)+' '+P2(fx0+dx*0.12,yT+0.13*r)+' L'+P2(fx0+dx,nb):'M'+P2(fx0,yT)+' L'+P2(fx0+dx,nb);
  var bkL=curve?'M'+P2(N[0]+0.1*r,N[1]-0.12*r)+' Q'+P2(bx0,N[1])+' '+P2(bx0+dx*0.12,N[1]+0.16*r)+' L'+P2(bx0+dx,nb):'M'+P2(N[0],N[1])+' L'+P2(bx0,N[1])+' L'+P2(bx0+dx,nb);
  pth(ng,fr,{w:2.2});pth(ng,bkL,{w:2.2});
  pth(g,up,{w:2.6});
  if(sex==='m')pth(g,'M'+P2(jc[0],jc[1])+' L'+P2(jc[0]+0.08*r,jc[1]-0.18*r),{w:1.4,op:.7});
  // 귀
  var ex=F+(o.earX==null?(sex==='f'?0.55:0.66):o.earX)*G.W,eT=sex==='f'?G.eyelid+G.H*0.02:G.brow,eB=sex==='f'?G.nose+G.H*0.03:G.nose+G.H*0.01;G.earX=ex;G.earT=eT;G.earB=eB;
  if(o.scm)pth(ng,'M'+P2(ex+0.08*r,eB)+' L'+P2(fx0+dx*0.9+0.05*r,nb-6),{stroke:FC.guide,w:5,op:.7});
  pth(g,'M'+P2(ex-0.04*r,eT+0.02*r)+' C'+P2(ex+0.02*r,eT-0.06*r)+' '+P2(ex+0.14*r,eT-0.02*r)+' '+P2(ex+0.12*r,(eT+eB)/2)+' C'+P2(ex+0.1*r,eB)+' '+P2(ex+0.02*r,eB+0.02*r)+' '+P2(ex-0.04*r,eB-0.02*r),{fill:FC.skin,w:2});
  pth(g,'M'+P2(ex+0.01*r,eT+0.06*r)+' Q'+P2(ex+0.08*r,eT+0.04*r)+' '+P2(ex+0.07*r,(eT+eB)/2),{w:1.3});
  // 눈(기울인 삼각김밥)
  var er=rad(o.eyeRot==null?(sex==='f'?10:20):o.eyeRot),ew=sex==='f'?0.1*r:0.13*r,eh=sex==='f'?0.15*r:0.09*r,e0=[F+0.08*r,G.eyelid];
  var tri=[[0,0],[ew,-eh*0.08],[ew*0.45,eh]].map(function(p){var c=Math.cos(er),s_=Math.sin(er);return [e0[0]+p[0]*c+p[1]*s_, e0[1]-p[0]*s_*0.35+p[1]*c];});
  el('path',{d:'M'+P2(tri[0][0],tri[0][1])+' Q'+P2((tri[0][0]+tri[1][0])/2,tri[0][1]-3)+' '+P2(tri[1][0],tri[1][1])+' Q'+P2(tri[1][0]-1,tri[2][1]-eh*0.3)+' '+P2(tri[2][0],tri[2][1])+' Q'+P2(tri[0][0]+1,tri[2][1]-eh*0.4)+' '+P2(tri[0][0],tri[0][1])+'Z',fill:FC.iris,stroke:FC.ink,'stroke-width':1.6},g);
  pth(g,'M'+P2(tri[0][0]-1,tri[0][1])+' L'+P2(tri[1][0]+3,tri[1][1]-1),{w:sex==='f'?3.6:2.6});
  pth(g,'M'+P2(F+0.06*r,G.brow-0.02*r)+' Q'+P2(F+0.13*r,G.brow-0.05*r)+' '+P2(F+0.2*r+(sex==='m'?0.06*r:0),G.brow-0.01*r),{w:sex==='f'?1.6:2.8});
  G.eyeTri=tri;G.g=root;G.nape=N;G.backX=backX;
  if(o.guide){var x1=F-0.42*r,x2=cx+r*1.25;var lab={hair:'머리선',brow:'눈썹',eyelid:'위 눈꺼풀',nose:'코 밑',mouth:'입'};(o.guide===true?['eyelid','nose']:o.guide).forEach(function(k){hline(s,x1,x2,G[k],lab[k],k==='brow'||k==='hair'?FC.guide2:FC.guide,true);});}
  return G;}
/* 앞에서 본 목·어깨 */
function bustFront(s,o){var sex=o.sex||'f',cx=o.cx||260,top=o.top||30,H=o.H||170;var G=faceGeo({sex:sex,cx:cx,top:top,H:H});var hw=G.half*2;
  var F=faceFront(s,{sex:sex,cx:cx,top:top,H:H});var eyeIn=F.gapPx/2,pupil=F.gapPx/2+F.ew/2;
  var nw=(o.neckW==null?(sex==='f'?1:1):o.neckW)*(sex==='f'?eyeIn:pupil);var triW=(o.triW||(sex==='f'?1.15:2.1))*hw,triH=(o.triH||(sex==='f'?0.2:0.33))*G.H;
  var nTop=G.chin-G.H*0.12,nBot=G.chin+(o.neckL||(sex==='f'?0.24:0.16))*G.H,ty=nBot+triH;
  var g=el('g',{},s);s.insertBefore(g,F.g);
  el('path',{d:'M'+P2(cx-nw,nTop)+' L'+P2(cx-nw,nBot)+' Q'+P2(cx-nw-6,nBot+triH*0.5)+' '+P2(cx-triW/2,ty)+' Q'+P2(cx-triW/2-12,ty+8)+' '+P2(cx-triW/2-10,ty+G.H*0.45)+' L'+P2(cx+triW/2+10,ty+G.H*0.45)+' Q'+P2(cx+triW/2+12,ty+8)+' '+P2(cx+triW/2,ty)+' Q'+P2(cx+nw+6,nBot+triH*0.5)+' '+P2(cx+nw,nBot)+' L'+P2(cx+nw,nTop)+'Z',fill:FC.skin},g);
  pth(g,'M'+P2(cx-nw,nTop)+' L'+P2(cx-nw,nBot)+' Q'+P2(cx-nw-6,nBot+triH*0.5)+' '+P2(cx-triW/2,ty)+' Q'+P2(cx-triW/2-12,ty+8)+' '+P2(cx-triW/2-10,ty+G.H*0.45)+' M'+P2(cx+nw,nTop)+' L'+P2(cx+nw,nBot)+' Q'+P2(cx+nw+6,nBot+triH*0.5)+' '+P2(cx+triW/2,ty)+' Q'+P2(cx+triW/2+12,ty+8)+' '+P2(cx+triW/2+10,ty+G.H*0.45),{w:2.2});
  pth(g,'M'+P2(cx-triW*0.32,ty-triH*0.05)+' Q'+P2(cx-triW*0.15,ty-triH*0.25)+' '+P2(cx-6,ty-triH*0.1)+' M'+P2(cx+triW*0.32,ty-triH*0.05)+' Q'+P2(cx+triW*0.15,ty-triH*0.25)+' '+P2(cx+6,ty-triH*0.1),{w:1.4,op:.8});
  if(o.tri)el('path',{d:'M'+P2(cx-triW/2,ty)+' L'+P2(cx,nBot)+' L'+P2(cx+triW/2,ty)+'Z',fill:'rgba(224,51,127,.12)',stroke:FC.guide,'stroke-width':1.6},s);
  if(o.chest){var chH=(sex==='f'?1:1.5)*G.H,chW=G.H*1.08;el('ellipse',{cx:cx,cy:ty-triH*0.3+chH/2,rx:chW/2,ry:chH/2,fill:'none',stroke:FC.guide,'stroke-width':1.6,'stroke-dasharray':'6 4'},s);}
  return {G:G,F:F,nw:nw,triW:triW,triH:triH,hw:hw,eyeIn:eyeIn,pupil:pupil,ty:ty,nBot:nBot};}
function pick(h,sel){return ctl(h).querySelector(sel);}
function rv(h,name){var e=pick(h,'[name='+name+']');return e?(e.type==='checkbox'?e.checked:+e.value):null;}
function allIn(h,f){ctl(h).querySelectorAll('input,select').forEach(function(i){i.addEventListener(i.tagName==='SELECT'||i.type==='checkbox'?'change':'input',f);});}
function bg(s,W,H){el('rect',{x:0,y:0,width:W,height:H,fill:'#fbfcfd'},s);}
function seg2(h,cb){var bs=ctl(h).querySelectorAll('button[data-v]');bs.forEach(function(b){b.addEventListener('click',function(){bs.forEach(function(x){x.classList.remove('on');});b.classList.add('on');cb(b.dataset.v);});});}
function verdict(ok,txt){return '<span style="color:'+(ok?C.green:C.red)+';font-weight:700">'+(ok?'✔ ':'⚠ ')+txt+'</span>';}

/* ===================== 1부 정면 얼굴(모아) ===================== */
P.p1_lines=function(h){var W=520,H=440;
  function draw(){var e=rv(h,'eye')/100,n=rv(h,'nose')/100;var s=svgOf(h,W,H);bg(s,W,H);
    el('circle',{cx:250,cy:220,r:180,fill:'none',stroke:'#d0d6de','stroke-width':1.5},s);el('line',{x1:250,y1:40,x2:250,y2:400,stroke:'#d0d6de','stroke-dasharray':'4 4'},s);
    var G=faceFront(s,{sex:'f',cx:250,top:40,H:360,eyelid:e,nose:n,guide:true,hairCol:rv(h,'hair')?'#D8C09A':null});
    var top=40,HH=360;[[0.5,'1/2'],[0.75,'1/4']].forEach(function(q){var y=top+HH*q[0];el('line',{x1:28,y1:y,x2:52,y2:y,stroke:C.teal,'stroke-width':3},s);ktxt(s,24,y+4,q[1],{size:12,fill:C.teal,anchor:'end',weight:'bold'});});
    var e24=e*24,n24=n*24;out(h).innerHTML='머리 높이 24로 보면 위 눈꺼풀은 위에서 <b>'+f2(e24,1)+'</b>, 코 밑은 턱에서 <b>'+f2(n24,1)+'</b>입니다. '+
      verdict(Math.abs(e-0.5)<0.021,Math.abs(e-0.5)<0.021?'눈꺼풀이 한가운데(12)':'눈꺼풀이 '+(e<0.5?'위로':'아래로')+' 치우침 — 이마가 '+(e<0.5?'좁아':'넓어')+' 보입니다')+' · '+
      verdict(Math.abs(n-0.25)<0.021,Math.abs(n-0.25)<0.021?'코 밑이 턱에서 1/4(6)':'코 밑이 1/4에서 벗어남 — 얼굴 아래쪽이 '+(n>0.25?'짧아':'길어')+' 보입니다');}
  allIn(h,draw);draw();};
P.p1_shave=function(h){var W=520,H=420;
  function draw(){var cb=rv(h,'cheek')/100,k=rv(h,'shave')/100;var s=svgOf(h,W,H);bg(s,W,H);
    el('circle',{cx:260,cy:210,r:170,fill:'rgba(224,51,127,.10)',stroke:'#d0d6de','stroke-width':1.5},s);
    var G=faceFront(s,{sex:'f',cx:260,top:40,H:340,cheek:cb,shave:k});
    var bulge=G.cy+G.R*(0.42+cb*0.6);hline(s,60,470,G.mouth,'입 높이',FC.guide2,true);el('circle',{cx:260-G.xw-2,cy:bulge,r:7,fill:FC.hot,stroke:'#fff','stroke-width':2},s);el('circle',{cx:260+G.xw+2,cy:bulge,r:7,fill:FC.hot,stroke:'#fff','stroke-width':2},s);
    var rel=(bulge-G.mouth)/G.H;var lab=rel>0.03?'둥글고 앳된 인상':rel<-0.05?'갸름하고 성숙한 인상':'중간 — 기본 얼굴';
    out(h).innerHTML='볼이 가장 불룩한 곳(주황 점)이 입 높이보다 <b>'+(rel>=0?'아래로 ':'위로 ')+f2(Math.abs(rel)*100,1)+'%</b> → <b>'+lab+'</b>. 원 양옆을 깎은 두께(분홍): 눈~코 높이에서 <b>'+f2((1-k)*100,0)+'%</b>. '+(k>0.9?verdict(false,'덜 깎아 얼굴이 넓적해 보입니다'):k<0.78?verdict(false,'너무 깎아 볼이 꺼져 보입니다'):verdict(true,'깎은 두께가 알맞습니다'))+' <span class="hint">같은 20대 성인이어도 볼 위치만으로 인상이 달라집니다.</span>';}
  allIn(h,draw);draw();};
P.p1_eyes=function(h){var W=520,H=400,tilt=0;seg2(h,function(v){tilt=+v;draw();});
  function draw(){var gap=rv(h,'gap')/100;var s=svgOf(h,W,H);bg(s,W,H);var G=faceFront(s,{sex:'f',cx:260,top:30,H:340,gap:gap,tilt:tilt,hairCol:'#D8C09A'});
    var y=G.eyelid-4,ew=G.ew,eh=G.eh;var xs=[G.cx-G.half,G.eyes[0]-ew/2,G.eyes[0]+ew/2,G.eyes[1]-ew/2,G.eyes[1]+ew/2,G.cx+G.half];
    for(var i=0;i<5;i++){el('rect',{x:xs[i],y:y,width:Math.max(0,xs[i+1]-xs[i]),height:eh+8,fill:i%2?'none':'rgba(224,51,127,.12)',stroke:FC.guide,'stroke-width':1.4},s);}
    var side=(G.half*2-2*ew-G.gapPx)/2;out(h).innerHTML='눈 너비를 1로 보면 눈 사이 <b>'+f2(gap,2)+'</b>, 눈~윤곽 <b>'+f2(side/ew,2)+'</b> (합계 '+f2(2+gap+2*side/ew,2)+'). '+
      (gap<0.95?verdict(false,'눈 사이가 좁아 가운데로 몰린 눈처럼 보입니다'):gap>1.45?verdict(false,'눈 사이가 너무 넓어 얼굴 바깥으로 밀려 보입니다'):verdict(true,'눈 하나보다 조금 넓게 — 알맞습니다'))+' · 모양: <b>'+(tilt>0?'올라간 눈(바깥 위 삼각형을 작게 자름)':tilt<0?'처진 눈(안쪽 위 삼각형을 작게 자름)':'기본 눈')+'</b>';}
  onIn(pick(h,'[name=gap]'),draw);draw();};
P.p1_parts=function(h){var W=520,H=440;
  function draw(){var sh=rv(h,'shift')/1000,m=rv(h,'mouth')/100;var s=svgOf(h,W,H);bg(s,W,H);
    var G=faceFront(s,{sex:'f',cx:260,top:40,H:340,shift:sh,mouth:m,hairCol:'#D8C09A',guide:['eyelid','nose','mouth']});
    var midR=(G.nose-G.eyelid)/G.H,low=(G.chin-G.nose)/G.H;out(h).innerHTML='부위 전체를 <b>'+f2(sh*100,1)+'%</b> 내림 · 입은 코 밑~턱의 <b>'+f2(m*100,0)+'%</b> 지점. 눈꺼풀~코 밑 <b>'+f2(midR*100,1)+'%</b> / 코 밑~턱 <b>'+f2(low*100,1)+'%</b>. '+
      (sh<0.008?'기준 그대로 — 그대로도 되지만 가운데가 조금 길어 보일 수 있습니다.':sh<=0.026?verdict(true,'조금 내려 얼굴이 짜여 보입니다'):verdict(false,'너무 내려 턱이 짧고 이마가 넓어 보입니다'))+' · '+(Math.abs(m-0.5)<=0.08?verdict(true,'입은 코와 턱 사이 가운데쯤'):verdict(false,m<0.5?'입이 코에 붙었습니다':'입이 턱에 붙었습니다'));}
  allIn(h,draw);draw();};
/* ===================== 2부 정면 남성(박사) ===================== */
P.p2_shogi=function(h){var W=520,H=470;
  function draw(){var at=rv(h,'attach')/100,tip=rv(h,'tip')/100,cut=rv(h,'cut')/100;var s=svgOf(h,W,H);bg(s,W,H);var r=105;
    el('circle',{cx:260,cy:30+r,r:r,fill:'none',stroke:'#c7ced8','stroke-width':1.5,'stroke-dasharray':'4 4'},s);
    var G=faceFront(s,{sex:'m',cx:260,top:30,r:r,attach:at,tip:tip,cut:cut});
    var ratio=G.H/(2*G.xw);var bad=tip>1.0,shortF=ratio<1.45;
    out(h).innerHTML='얼굴 길이 ÷ 폭 = '+f2(G.H,0)+' ÷ '+f2(2*G.xw,0)+' = <b>'+f2(ratio,2)+'</b> · 장기말을 원 중심에서 <b>'+f2(at,2)+'r</b> 아래에 붙임 · 턱 끝 자르기 <b>'+f2(cut*100,0)+'%</b>. '+
      (bad?verdict(false,'장기말이 길고 턱이 뾰족해 균형이 나쁩니다'):shortF?verdict(false,'얼굴이 짧아 남성다운 긴 얼굴이 안 나옵니다'):verdict(true,'자연스럽게 긴 얼굴'))+(cut>=0.5&&!bad?' · 턱 끝을 넓게 잘라 각진 남성 턱입니다.':'');}
  allIn(h,draw);draw();};
P.p2_thirds=function(h){var W=520,H=470;
  function draw(){var b=rv(h,'brow')/100,n=rv(h,'nose')/100;var s=svgOf(h,W,H);bg(s,W,H);var r=110,top=30;var G0=faceGeo({sex:'m',cx:250,top:top,r:r});var HH=G0.H,hair=top+HH*0.17;
    var by=top+HH*b,ny=top+HH*n;var G=faceFront(s,{sex:'m',cx:250,top:top,r:r,browY:by-4,nose:(G0.chin-ny)/HH,hairCol:'#3a3a44'});
    [[hair,'머리선'],[by,'눈썹'],[ny,'코 밑'],[G.chin,'턱']].forEach(function(q){hline(s,120,420,q[0],q[1],FC.guide,true);});
    var a=by-hair,bb=ny-by,c=G.chin-ny,mx=Math.max(a,bb,c),mn=Math.min(a,bb,c);var t=HH/26;
    out(h).innerHTML='머리 높이 26으로 보면: 머리선~눈썹 <b>'+f2(a/t,1)+'</b> · 눈썹~코 밑 <b>'+f2(bb/t,1)+'</b> · 코 밑~턱 <b>'+f2(c/t,1)+'</b>. '+((mx-mn)/t<=0.8?verdict(true,'세 간격이 같습니다 — 짜인 얼굴'):bb>c?verdict(false,'가운데가 길어 얼굴이 늘어져 보입니다'):verdict(false,'간격이 고르지 않습니다'));}
  allIn(h,draw);draw();};
P.p2_compare=function(h){var W=560,H=440,mode='both';seg2(h,function(v){mode=v;draw();});
  function draw(){var s=svgOf(h,W,H);bg(s,W,H);var HH=360,top=40;
    if(mode!=='m'){var F=faceFront(s,{sex:'f',cx:mode==='both'?150:280,top:top,H:HH,guide:mode==='f'?true:null});}
    if(mode!=='f'){var M=faceFront(s,{sex:'m',cx:mode==='both'?410:280,top:top,H:HH,guide:mode==='m'?true:null});}
    if(mode==='both'){var Fg=faceGeo({sex:'f',cx:150,top:top,H:HH}),Mg=faceGeo({sex:'m',cx:410,top:top,H:HH});[['eyelid','위 눈꺼풀'],['nose','코 밑'],['mouth','입']].forEach(function(k,i){el('line',{x1:40,y1:Fg[k[0]],x2:270,y2:Fg[k[0]],stroke:FC.guide,'stroke-dasharray':'5 4'},s);el('line',{x1:290,y1:Mg[k[0]],x2:530,y2:Mg[k[0]],stroke:C.blue,'stroke-dasharray':'5 4'},s);ktxt(s,280,(Fg[k[0]]+Mg[k[0]])/2+4,k[1],{size:11.5,anchor:'middle',fill:C.ink});});}
    var Fg2=faceGeo({sex:'f',top:0,H:24}),Mg2=faceGeo({sex:'m',top:0,H:24});
    out(h).innerHTML='머리 높이 24 기준 · 여: 코 밑 턱에서 <b>'+f2(24-Fg2.nose,1)+'</b>, 입 턱에서 <b>'+f2(24-Fg2.mouth,1)+'</b>, 눈 세로:가로 <b>1:1</b>, 눈 사이 <b>눈 1개보다 조금 넓게</b> · 남: 코 밑 <b>'+f2(24-Mg2.nose,1)+'</b>(조금 높게), 입 <b>'+f2(24-Mg2.mouth,1)+'</b>(코 쪽 1/3), 눈 <b>1:2</b>, 눈 사이 <b>눈 1개</b>. 위 눈꺼풀은 둘 다 <b>12(1/2)</b>.';}
  draw();};
P.p2_neck=function(h){var W=540,H=460,sex='m';seg2(h,function(v){sex=v;draw();});
  function draw(){var nk=rv(h,'neck')/100,tw=rv(h,'tri')/100;var s=svgOf(h,W,H);bg(s,W,H);var B=bustFront(s,{sex:sex,cx:270,top:30,H:180,neckW:nk,triW:tw,tri:true,chest:rv(h,'chest')});
    var okN=Math.abs(nk-1)<=0.15,okT=sex==='m'?tw>=2&&tw<=2.4:tw>=1.05&&tw<=1.3;
    out(h).innerHTML=(sex==='m'?'남성':'여성')+' · 목 너비 = '+(sex==='m'?'검은 눈동자 사이':'눈과 눈 사이')+' × <b>'+f2(nk,2)+'</b> · 어깨 삼각형 너비 = 머리 너비 × <b>'+f2(tw,2)+'</b>. '+verdict(okN,okN?'목 굵기 알맞음':nk<1?'목이 가늘어 머리가 떠 보입니다':'목이 굵어 둔해 보입니다')+' · '+verdict(okT,okT?'어깨 너비 알맞음':(sex==='m'?'남성 어깨는 머리 너비의 2배 남짓':'여성 어깨는 머리보다 조금 넓게'));}
  allIn(h,draw);draw();};
/* ===================== 3부 옆얼굴(시아·박사) ===================== */
P.p3_frame=function(h){var W=540,H=440,sex='f';seg2(h,function(v){sex=v;pick(h,'[name=rot]').value=0;draw();});
  function draw(){var rot=rv(h,'rot');var s=svgOf(h,W,H);bg(s,W,H);var cx=290,cy=190,r=125;
    if(sex==='f'){el('circle',{cx:cx,cy:cy,r:r,fill:'none',stroke:'#c7ced8','stroke-dasharray':'4 4'},s);pth(s,'M'+P2(cx-r,cy)+' L'+P2(cx-r,cy+0.8*r)+' L'+P2(cx-0.1*r,cy+0.62*r),{stroke:FC.guide,w:2.4,op:.7});}
    else{el('rect',{x:cx-r*1.02,y:cy-r,width:r*2.08,height:r*1.85,fill:'none',stroke:'#c7ced8','stroke-dasharray':'4 4'},s);pth(s,'M'+P2(cx-r,cy+0.05*r)+' L'+P2(cx-r*0.95,cy+0.95*r)+' L'+P2(cx+0.02*r,cy+0.74*r)+' L'+P2(cx+0.08*r,cy+0.05*r),{stroke:C.blue,w:2.2,op:.7});el('ellipse',{cx:cx+0.05*r,cy:cy-0.12*r,rx:r*1.02,ry:r*0.86,fill:'none',stroke:'#c7ced8','stroke-dasharray':'4 4'},s);}
    var G=faceSide(s,{sex:sex,cx:cx,cy:cy,r:r,eyeRot:rot,guide:['eyelid']});
    var t=G.eyeTri;el('line',{x1:t[0][0],y1:t[0][1]-30,x2:t[0][0],y2:t[0][1]+40,stroke:FC.guide2,'stroke-dasharray':'4 3'},s);
    var want=sex==='f'?10:20;out(h).innerHTML=(sex==='f'?'여성: 원 + L자, 코끝을 뾰족하게':'남성: 가로로 조금 긴 상자 + 기울어진 컵(턱) + 눕힌 달걀(머리)')+' · 옆 눈은 기울어진 삼각김밥, 눈썹 뿌리에서 <b>'+rot+'°</b> 안쪽으로. '+verdict(Math.abs(rot-want)<=4,Math.abs(rot-want)<=4?'기준('+want+'° 안팎)에 맞음':rot<want?'덜 기울여 눈이 얼굴 앞면에 붙어 납작해 보입니다':'너무 기울여 눈이 얼굴 안으로 꺼져 보입니다');}
  onIn(pick(h,'[name=rot]'),draw);draw();};
P.p3_ear=function(h){var W=540,H=440,sex='f';seg2(h,function(v){sex=v;draw();});
  function draw(){var ex=rv(h,'ear')/100;var s=svgOf(h,W,H);bg(s,W,H);var cx=290,cy=190,r=125;var G=faceSide(s,{sex:sex,cx:cx,cy:cy,r:r,earX:ex});
    el('line',{x1:G.front,y1:G.top-12,x2:G.front+G.W,y2:G.top-12,stroke:FC.guide2,'stroke-width':1.5},s);el('line',{x1:cx,y1:G.top-20,x2:cx,y2:G.chin,stroke:FC.guide2,'stroke-dasharray':'4 4'},s);ktxt(s,cx,G.top-24,'1/2',{size:12,anchor:'middle',fill:FC.guide2});
    el('line',{x1:G.earX,y1:G.top-20,x2:G.earX,y2:G.chin,stroke:FC.guide,'stroke-width':2},s);
    var d20=ex*20;var ok=sex==='f'?ex>=0.52&&ex<=0.6:ex>=0.62&&ex<=0.72;
    out(h).innerHTML='이마~뒤통수를 20으로 보면 귀 앞쪽은 이마에서 <b>'+f2(d20,1)+'</b> ('+f2(ex*100,0)+'%). '+verdict(ok,ok?(sex==='f'?'1/2보다 조금 뒤 — 여성 기준':'1/2보다 꽤 뒤 — 실제 사람에 가까운 남성 기준'):ex<0.5?'귀가 1/2보다 앞 — 얼굴이 납작하고 뒤통수가 커 보입니다':'귀가 너무 뒤 — 얼굴이 길쭉해 보입니다');}
  onIn(pick(h,'[name=ear]'),draw);draw();};
P.p3_nose=function(h){var W=540,H=440,sex='m';seg2(h,function(v){sex=v;draw();});
  function draw(){var mid=rv(h,'mid')/100,lip=rv(h,'lip')/100;var s=svgOf(h,W,H);bg(s,W,H);var G=faceSide(s,{sex:sex,cx:300,cy:185,r:120,mid:mid,lip:lip,guide:sex==='m'?['hair','brow','nose']:['brow','nose']});
    hline(s,G.front-50,G.front+G.W*1.1,G.chin,'턱',FC.guide2,true);
    var a=G.nose-G.brow,b=G.chin-G.nose;var monkey=a>b*1.15,lipBad=sex==='f'?lip>0.45:false;
    out(h).innerHTML='눈썹~코 밑 : 코 밑~턱 = <b>'+f2(a/b,2)+'</b> : 1 · 입술 기복 <b>'+f2(lip*100,0)+'%</b>. '+(monkey?verdict(false,'가운데가 길어 늘어진 얼굴(원숭이 얼굴)로 보입니다'):verdict(true,'간격이 고릅니다'))+' · '+(sex==='f'?(lipBad?verdict(false,'애니풍 여성 옆얼굴에서 입술 기복이 크면 입 주변이 튀어나와 보입니다 — 생략하거나 턱을 조금 내밀어 작게'):verdict(true,'입술 기복을 작게 줄인 애니풍 표현')):(lip<0.3?verdict(false,'남성은 입술 기복이 있어야 반실사에 가까워집니다'):verdict(true,'남성다운 입술 기복')));}
  allIn(h,draw);draw();};
P.p3_neck=function(h){var W=540,H=460,sex='f';seg2(h,function(v){sex=v;draw();});
  function draw(){var ang=rv(h,'ang'),nw=rv(h,'nw')/100,cur=rv(h,'curve');var s=svgOf(h,W,H);bg(s,W,H);var G=faceSide(s,{sex:sex,cx:290,cy:160,r:110,neckAngle:ang,neckW:nw,curve:cur,scm:true});
    el('circle',{cx:G.cx,cy:G.cy,r:5,fill:FC.guide},s);var ok1=ang>=3&&ang<=8,want=sex==='f'?0.25:0.5,ok2=Math.abs(nw-want)<=0.05;
    out(h).innerHTML='목 기울기 <b>'+ang+'°</b> · 목 너비 = 머리 너비 × <b>'+f2(nw,2)+'</b> · 분홍 띠는 귀 뒤에서 쇄골 가운데로 내려가는 목 근육(흉쇄유돌근). '+verdict(ok1,ok1?'5° 안팎으로 기울임':ang<3?'꼿꼿이 세워 차렷한 인형 같습니다':'너무 숙여 거북목처럼 보입니다')+' · '+verdict(ok2,ok2?(sex==='f'?'머리 너비의 1/4':'머리 너비의 1/2'):'목 굵기가 기준('+(sex==='f'?'1/4':'1/2')+')과 다릅니다')+' · '+(cur?verdict(true,'머리와 목을 곡선으로 이음'):verdict(false,'곡선 없이 이어 인형처럼 딱딱합니다'));}
  allIn(h,draw);draw();};
/* ===================== 4부 변형과 점검(하루) ===================== */
P.p4_jito=function(h){var W=520,H=380;
  function draw(){var lid=rv(h,'lid')/100,br=rv(h,'brow')/100;var s=svgOf(h,W,H);bg(s,W,H);faceFront(s,{sex:'f',cx:260,top:30,H:320,lid:lid,brow:br,hairCol:'#E9909A',smile:lid>0.3?1:4});
    var lab=lid<0.15?'기본 눈':br>0.5?'반쯤 감은 눈 + 올린 눈썹 → 대담하고 자신만만한 인상':'반쯤 감은 눈 → 나른하거나 시큰둥한 인상';out(h).innerHTML='위 눈꺼풀을 <b>'+f2(lid*100,0)+'%</b> 내리고 눈썹을 <b>'+f2(br*100,0)+'%</b> 올림 → <b>'+lab+'</b>. 원래 눈꺼풀 자리에는 연한 선이 남습니다(눈의 크기는 그대로라는 표시).';}
  allIn(h,draw);draw();};
P.p4_glasses=function(h){var W=520,H=380;
  function draw(){var rim=rv(h,'rim')/100,un=rv(h,'under'),sx=rv(h,'drop')/100;var s=svgOf(h,W,H);bg(s,W,H);var G=faceFront(s,{sex:'f',cx:260,top:30,H:320,hairCol:'#E9909A',glasses:{rim:rim,under:un,drop:sx}});
    var rh=G.eh*rim,top=G.eyelid+G.eh*0.5-rh/2+sx*G.eh,eyeT=G.eyelid,eyeB=G.eyelid+G.eh;var lines=un?[top+rh]:[top,top+rh];var cover=0;lines.forEach(function(y){if(y>eyeT+G.eh*0.15&&y<eyeB-G.eh*0.1)cover+=1;});
    var irisT=G.eyelid-G.eh*0.2,irisB=G.eyelid+G.eh*1.2;var hit=lines.filter(function(y){return y>irisT&&y<irisB;}).length;
    out(h).innerHTML='림(렌즈 테) 높이 = 눈 높이 × <b>'+f2(rim,2)+'</b>'+(un?' · 위 테 없는 언더림':' · 테 전체')+' · 눈을 가로지르거나 바짝 붙은 테 <b>'+hit+'</b>줄. '+(hit?verdict(false,'테가 눈에 걸려 눈이 가려 보입니다 — 림을 키우거나 언더림으로'):verdict(true,'테가 눈을 피해 눈매가 다 보입니다'))+' <span class="hint">애니풍 여성 얼굴은 눈이 크고 귀가 낮아 테가 눈에 걸리기 쉽습니다.</span>';}
  allIn(h,draw);draw();};
P.p4_pose=function(h){var W=540,H=460;
  function draw(){var tilt=rv(h,'tilt'),turn=rv(h,'turn');var s=svgOf(h,W,H);bg(s,W,H);var cx=270;var g=el('g',{transform:'rotate('+(-tilt*0.5)+' '+cx+' 330)'},s);
    var sw=170-turn*1.6,ty=270;el('path',{d:'M'+P2(cx-sw,ty+tilt*2.2)+' Q'+P2(cx,ty-30)+' '+P2(cx+sw,ty-tilt*2.2)+' L'+P2(cx+sw-10,460)+' L'+P2(cx-sw+10,460)+'Z',fill:'#e9e4f4',stroke:FC.ink,'stroke-width':2.4},g);
    pth(g,'M'+P2(cx+turn*1.2,ty-8)+' L'+P2(cx+turn*2.2,460),{stroke:FC.guide,dash:'6 4',w:2});
    el('ellipse',{cx:cx-sw+12,cy:ty+tilt*2.2+28,rx:26,ry:36,fill:'none',stroke:'rgba(224,51,127,.6)','stroke-width':1.8},g);el('ellipse',{cx:cx+sw-12,cy:ty-tilt*2.2+28,rx:26,ry:36,fill:'none',stroke:'rgba(224,51,127,.6)','stroke-width':1.8},g);
    el('rect',{x:cx-22,y:200,width:44,height:70,fill:FC.skin,stroke:FC.ink,'stroke-width':2},s);faceFront(s,{sex:'m',cx:cx,top:20,H:220,hairCol:'#3a3a44'});
    var stiff=Math.max(0,100-tilt*6-turn*2.5);out(h).innerHTML='어깨 기울기 <b>'+tilt+'°</b> · 몸 비틀기 <b>'+turn+'</b> → 딱딱함 지수 <b>'+f2(stiff,0)+'</b> (예시 계산: 100 − 기울기×6 − 비틀기×2.5). '+(stiff>70?verdict(false,'얼굴도 몸도 정면이라 증명사진처럼 굳어 보입니다'):stiff<25?verdict(false,'너무 비틀어 얼굴과 몸이 따로 놉니다'):verdict(true,'얼굴은 정면, 목 아래는 살짝 비스듬히 — 자연스럽습니다'));}
  allIn(h,draw);draw();};
P.p4_check=function(h){var W=540,H=440;
  function draw(){var bk=rv(h,'back')/100,cu=rv(h,'chin');var s=svgOf(h,W,H);bg(s,W,H);var G=faceSide(s,{sex:'m',cx:290,cy:180,r:118,back:bk,chinUp:cu});
    el('circle',{cx:G.cx+0.02*G.r,cy:G.cy-0.08*G.r,r:G.r*1.02,fill:'none',stroke:FC.guide,'stroke-width':1.6,'stroke-dasharray':'6 4'},s);
    var bulge=bk>0.25,jut=cu>-3&&cu<6;out(h).innerHTML='뒤통수 부풂 <b>'+f2(bk*100,0)+'%</b> · 턱 각도 <b>'+cu+'°</b>('+(cu<0?'당김':cu>0?'듦':'정면')+'). '+(bulge?verdict(false,'뒤통수가 머리 크기 원(점선) 밖으로 나와 머리가 무겁고 둔해 보입니다'):verdict(true,'뒤통수가 원 안에 있습니다'))+' · '+(jut?'목을 가늘게 줄인 그림에서는 이 각도에서 턱이 앞으로 튀어나와 보이기 쉽습니다 — 턱을 당기거나(−8° 이하) 크게 들어(10° 이상) 보세요.':verdict(true,'턱 방향을 바꿔 튀어나온 느낌을 줄였습니다'));}
  allIn(h,draw);draw();};
/* ===================== 5부 AI와 얼굴 ===================== */
var FQ={sex:[['','— 성별 —'],['f','woman'],['m','man']],shape:[['','— 윤곽 —'],['round','soft rounded jaw, cheeks fullest at mouth level'],['oval','slim oval face, cheeks fullest above mouth level'],['angular','defined angular jaw, square chin tip']],
 eyes:[['','— 눈 —'],['big','large round eyes (height ≈ width), eyes spaced slightly more than one eye width apart'],['almond','narrow almond eyes (height ≈ half the width), eyes spaced one eye width apart']],
 parts:[['','— 부위 높이 —'],['std','upper eyelids at half the head height, nose bottom one quarter above the chin'],['low','facial features placed slightly lower than standard'],['long','features placed high (long midface)']],
 view:[['','— 각도 —'],['front','front view, body turned slightly'],['three','three-quarter view'],['side','side profile facing left, neck tilted forward about five degrees']],
 age:[['','— 나이·금지 —'],['adult','an adult in their late twenties with adult proportions; not childlike, no school uniform']]};
function faceForm(host,onchange){var form=document.createElement('div');form.style.cssText='display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:8px 14px;width:100%';host.appendChild(form);
  var lab={sex:'성별 신호',shape:'윤곽',eyes:'눈 모양·간격',parts:'부위 높이',view:'각도',age:'나이·금지'};
  Object.keys(FQ).forEach(function(k){var l=document.createElement('label');l.innerHTML=lab[k]+' <select name="'+k+'">'+FQ[k].map(function(o){return '<option value="'+o[0]+'">'+o[1]+'</option>';}).join('')+'</select>';form.appendChild(l);});
  form.querySelectorAll('select').forEach(function(x){x.addEventListener('change',onchange);});
  return function(){var o={};Object.keys(FQ).forEach(function(k){o[k]=form.querySelector('[name='+k+']').value;});return o;};}
function facePrompt(o){var t=[],sc=0,miss=[],warn=[];var nm={sex:'성별',shape:'윤곽',eyes:'눈',parts:'부위 높이',view:'각도',age:'나이·금지'};
  Object.keys(FQ).forEach(function(k){if(o[k]){sc++;var v=FQ[k].filter(function(x){return x[0]===o[k];})[0][1];t.push(v);}else miss.push(nm[k]);});
  if(o.sex==='m'&&o.eyes==='big')warn.push('남성인데 크고 둥근 눈 — 앳되거나 여성처럼 보이기 쉽습니다');
  if(o.sex==='f'&&o.shape==='angular')warn.push('각진 턱 — 의도한 것이 아니면 여성 얼굴이 굳어 보입니다');
  if(o.parts==='long')warn.push('가운데 얼굴이 길어 늘어져 보입니다');
  if(o.shape==='round'&&o.eyes==='big'&&o.parts==='low'&&o.age!=='adult')warn.push('둥근 볼 + 큰 눈 + 낮은 부위 → 나이가 어려 보이는 쪽으로 쏠립니다. 성인 나이를 적으세요');
  var text='Portrait of '+(o.sex==='m'?'a man':o.sex==='f'?'a woman':'a person')+'.\n'+t.slice(o.sex?1:0).map(function(x){return '- '+x;}).join('\n')+'\nNo text, no logos, not resembling any famous character.';
  return {text:text,score:sc,miss:miss,warn:warn};}
P.p5_prompt=function(h){h.innerHTML='';var get=faceForm(h,draw);var pb=document.createElement('div');pb.className='promptbox';pb.innerHTML='<b>조립된 얼굴 문장</b><pre aria-live="polite"></pre><button type="button" class="btn">복사하기</button>';h.appendChild(pb);
  pb.querySelector('button').addEventListener('click',function(){var t=pb.querySelector('pre').textContent;var b=this;if(navigator.clipboard)navigator.clipboard.writeText(t).then(function(){b.textContent='복사했습니다';},function(){b.textContent='직접 선택해 복사하세요';});});
  function draw(){var r=facePrompt(get());pb.querySelector('pre').textContent=r.text;out(h).innerHTML='점검표 <b>'+r.score+' / 6</b>'+(r.miss.length?' · 빠진 것: '+r.miss.join(', '):' · 다 찼습니다')+(r.warn.length?'<br>'+r.warn.map(function(w){return verdict(false,w);}).join('<br>'):'');}
  draw();};
P.p5_turn=function(h){var W=620,H=300;
  function draw(){var ang=rv(h,'ang'),keep=rv(h,'keep');var s=svgOf(h,W,H);bg(s,W,H);var HH=180,top=50,base=top+HH*0.5;
    faceFront(s,{sex:'f',cx:100,top:top,H:HH,hairCol:'#1E1B22'});
    var t=ang/90,cx2=290,drift=keep?0:t*0.08;var g=el('g',{},s);faceFront(g,{sex:'f',cx:cx2,top:top,H:HH,eyelid:0.5-drift,hairCol:'#1E1B22',gap:1.1*(1-t*0.5)});
    g.setAttribute('transform','translate('+(cx2)+',0) scale('+(1-t*0.35)+',1) translate('+(-cx2)+',0)');
    var r=HH/1.8;faceSide(s,{sex:'f',cx:480,cy:top+r,r:r});
    hline(s,10,600,base,'',FC.guide);ktxt(s,600,base-8,'1/2 선',{size:12,anchor:'end',fill:FC.guide,weight:'bold'});
    ktxt(s,100,H-12,'정면',{size:12.5,anchor:'middle'});ktxt(s,290,H-12,ang+'° 돌림',{size:12.5,anchor:'middle'});ktxt(s,480,H-12,'옆',{size:12.5,anchor:'middle'});
    var e=base-drift*HH;out(h).innerHTML='돌린 각도 <b>'+ang+'°</b> · 가운데 얼굴의 위 눈꺼풀 높이 <b>'+f2((e-top)/HH*24,1)+'</b> / 24. '+(keep||ang===0?verdict(true,'정면·비스듬히·옆 모두 위 눈꺼풀이 1/2 선 위에 있습니다 — 같은 사람으로 보입니다'):verdict(false,'돌릴수록 눈이 위로 떠 정면과 다른 사람처럼 보입니다 — 각도마다 1/2 선을 먼저 긋기'));}
  allIn(h,draw);draw();};
P.p5_mask=function(h){var W=300,H=450;var cv=canvasOf(h,W,H,340),ctx=cv.getContext('2d');var K=W/512;
  function draw(){var mw=rv(h,'mw'),mh=rv(h,'mh'),my=rv(h,'my');ctx.fillStyle='#fbfcfd';ctx.fillRect(0,0,W,H);
    ctx.fillStyle='#F8E3D3';ctx.strokeStyle='#2a2230';ctx.lineWidth=2;ctx.beginPath();ctx.ellipse(256*K,190*K,95*K,120*K,0,0,7);ctx.fill();ctx.stroke();ctx.fillStyle='#1E1B22';ctx.beginPath();ctx.ellipse(256*K,150*K,110*K,90*K,0,Math.PI,0);ctx.fill();
    ctx.fillRect(146*K,150*K,20*K,180*K);ctx.fillRect(346*K,150*K,20*K,180*K);ctx.fillStyle='#4a3b5c';[[220,200],[292,200]].forEach(function(p){ctx.beginPath();ctx.ellipse(p[0]*K,p[1]*K,14*K,17*K,0,0,7);ctx.fill();});
    ctx.strokeStyle='#2a2230';ctx.beginPath();ctx.moveTo(240*K,262*K);ctx.quadraticCurveTo(256*K,270*K,272*K,262*K);ctx.stroke();ctx.fillStyle='#34363F';ctx.fillRect(150*K,330*K,212*K,440*K);ctx.fillStyle='#F8E3D3';ctx.fillRect(236*K,300*K,40*K,40*K);
    var mx=256-mw/2;ctx.fillStyle='rgba(232,115,26,.28)';ctx.fillRect(mx*K,my*K,mw*K,mh*K);ctx.strokeStyle='#e8731a';ctx.setLineDash([6,4]);ctx.strokeRect(mx*K,my*K,mw*K,mh*K);ctx.setLineDash([]);
    var ratio=mw*mh/393216*100;var hair=my<150,neck=my+mh>320,small=mw<130||mh<60||my>185||my+mh<215;
    out(h).innerHTML='가림 영역 '+mw+' × '+mh+' = '+(mw*mh).toLocaleString()+' ÷ 393,216(512×768) = <b>'+f2(ratio,1)+'%</b>'+(hair?' · '+verdict(false,'머리카락까지 가려 머리 모양이 바뀝니다'):'')+(neck?' · '+verdict(false,'목·옷깃까지 가려 목이 달라집니다'):'')+(small?' · '+verdict(false,'눈 하나나 입이 영역 밖이라 고친 곳과 안 고친 곳이 따로 놉니다'):'')+(!hair&&!neck&&!small?' · '+verdict(true,'눈·코·입만 다시 그립니다'):'');}
  allIn(h,draw);draw();};
var STYF={anime:[1,0.15,'애니풍','눈 세로:가로 1:1, 코는 빛 받는 점 하나, 입술 기복 생략'],semireal:[0.75,0.4,'반실사','눈 1:1.5, 코는 콧날 선과 그림자, 입술 기복 조금'],photo:[0.5,0.8,'실사풍','눈 1:2, 코는 면과 그림자, 입술 기복 그대로']};
P.p5_style=function(h){var W=560,H=340,sty='anime';seg2(h,function(v){sty=v;draw();});
  function draw(){var p=STYF[sty];var s=svgOf(h,W,H);bg(s,W,H);faceFront(s,{sex:'f',cx:150,top:30,H:280,eyeRatio:0.92*p[0]+0.0,ew:0.44*140*(0.8+0.2*p[0]),hairCol:'#D8C09A'});faceSide(s,{sex:'f',cx:430,cy:150,r:105,lip:p[1]});
    out(h).innerHTML='<b>'+p[2]+'</b>: '+p[3]+'. 위 눈꺼풀 1/2, 코 밑 1/4 같은 <b>높이 기준은 화풍이 바뀌어도 그대로</b>이고, 바뀌는 것은 눈 모양과 코·입술 표현의 양입니다.';}
  draw();};
/* ===================== 6부 진단 ===================== */
var CHECK6=['① 큰 틀(원·장기말·옆 상자)','② 높이 기준선(1/2·1/4·세 간격)','③ 눈 상자·간격','④ 코·입·귀 위치','⑤ 목·어깨 잇기'];
var FAIL6=[2,1,0,0,0,4,2,3];var FAILWHY6=['눈 사이가 눈 하나보다 좁습니다.','부위가 위로 몰려 가운데 얼굴이 깁니다.','장기말을 너무 길게 그려 턱이 뾰족합니다.','뒤통수가 머리 크기 원 밖으로 부풀었습니다.','턱이 앞으로 튀어나와 보이는 각도입니다.','머리와 목을 직선으로 이어 인형처럼 딱딱합니다.','안경 테가 눈동자를 가로지릅니다.','애니풍 옆얼굴에 입술 기복을 크게 넣었습니다.'];
P.p6_check=function(h){var c=ctl(h),sel=c.querySelector('select');h.innerHTML='';var list=document.createElement('div');list.style.cssText='display:flex;flex-direction:column;gap:6px';h.appendChild(list);var done=0;
  function build(){list.innerHTML='';done=0;CHECK6.forEach(function(t,i){var b=document.createElement('button');b.type='button';b.className='btn';b.style.textAlign='left';b.textContent=t;b.addEventListener('click',function(){press(i,b);});list.appendChild(b);});out(h).innerHTML='점검표를 <b>위에서부터</b> 눌러 보세요.';}
  function press(i,b){var f=+sel.value,at=FAIL6[f];if(i!==done){out(h).innerHTML='순서대로! 먼저 <b>'+CHECK6[done]+'</b>을 보세요. 큰 틀에서 작은 부위 순서입니다.';return;}
    if(i<at){b.style.borderColor=C.green;b.style.background='#ecf7ef';b.textContent=CHECK6[i]+' — 통과';done++;out(h).innerHTML=CHECK6[i]+' 통과. 다음 항목으로.';}
    else{b.style.borderColor=C.red;b.style.background='#fdeceb';b.textContent=CHECK6[i]+' — 여기서 걸림';done=99;out(h).innerHTML='<b>'+CHECK6[i]+'</b>에서 처음 걸렸습니다: '+FAILWHY6[f]+' 아래 실패 카드 f'+(f+1)+'에서 고치는 조각을 보세요.';}}
  sel.addEventListener('change',build);build();};

/* ===================== 실전 연습장 ===================== */
function practice(){var root=document.getElementById('practice');if(!root)return;var tabs=root.querySelectorAll('.tabs button'),scenes=root.querySelectorAll('.scene');
  function show(id){tabs.forEach(function(b){b.classList.toggle('on',b.dataset.t===id);});scenes.forEach(function(s){s.classList.toggle('on',s.id===id);});if(history.replaceState)history.replaceState(null,'','#'+id);}
  tabs.forEach(function(b){b.addEventListener('click',function(){show(b.dataset.t);});});var hsh=(location.hash||'').slice(1);show([].some.call(scenes,function(s){return s.id===hsh;})?hsh:'bench');
  bench();swap();workshop();desk();}
function wire(S,f){S.querySelectorAll('.ctrl input,.ctrl select').forEach(function(i){i.addEventListener(i.tagName==='SELECT'||i.type==='checkbox'?'change':'input',f);});}
function bench(){var S=document.getElementById('bench');if(!S)return;var q=function(n){return S.querySelector('[name='+n+']');};var touched=false;
  function upd(e){if(e)touched=true;var sex=q('sex').value,eye=+q('eye').value/100,nose=+q('nose').value/100,gap=+q('gap').value/100,mouth=+q('mouth').value/100;
    var tN=sex==='f'?0.25:0.27,tM=sex==='f'?0.5:1/3,tG=sex==='f'?1.1:1;
    var okE=Math.abs(eye-0.5)<=0.02,okN=Math.abs(nose-tN)<=0.02,okG=Math.abs(gap-tG)<=0.1,okM=Math.abs(mouth-tM)<=0.06;
    board(S.querySelector('.board'),[['위 눈꺼풀',f2(eye*24,1)+' / 24',okE],['코 밑(턱에서)',f2(nose*24,1)+' / 24',okN],['눈 사이',f2(gap,2)+' 눈',okG],['입 위치',f2(mouth*100,0)+'%',okM]]);
    var s=el('svg',{viewBox:'0 0 430 330',role:'img','aria-label':'비율 작업대 얼굴'});var g1=S.querySelector('.g1');g1.innerHTML='';g1.appendChild(s);el('rect',{x:0,y:0,width:430,height:330,fill:'#fbfcfd'},s);
    faceFront(s,{sex:sex,cx:175,top:20,H:290,eyelid:eye,nose:nose,gap:gap,mouth:mouth,guide:['eyelid','nose','mouth'],hairCol:sex==='f'?'#1E1B22':'#3a3a44'});
    var s2=el('svg',{viewBox:'0 0 360 200',role:'img','aria-label':'기준과의 차이 막대'});var g2=S.querySelector('.g2');g2.innerHTML='';g2.appendChild(s2);
    [['눈꺼풀',Math.abs(eye-0.5)/0.1],['코 밑',Math.abs(nose-tN)/0.1],['눈 사이',Math.abs(gap-tG)/0.6],['입',Math.abs(mouth-tM)/0.3]].forEach(function(b,i){var v=clamp(b[1],0,1);el('rect',{x:90,y:20+i*42,width:Math.max(4,240*v),height:24,rx:5,fill:v<0.25?C.green:C.orange},s2);ktxt(s2,84,37+i*42,b[0],{size:12.5,anchor:'end',fill:C.ink});});
    ktxt(s2,90,192,'막대가 짧을수록 기준에 가깝습니다',{size:11.5});
    var M=[sex==='f'&&okE&&okN,sex==='m'&&okE&&okN&&okM,okG&&(sex==='f'?gap>=1:true)&&okE];if(touched)missions(S.querySelector('.missions'),M,true);
    say(S.querySelector('.talk'),[['doctor','e10','박사',(sex==='f'?'여성 기준':'남성 기준')+': 위 눈꺼풀 12, 코 밑 턱에서 '+f2(tN*24,1)+', 입은 코 밑~턱의 '+(sex==='f'?'가운데':'코 쪽 1/3')+'.'],['haru','e10','조수','지금 눈꺼풀 '+f2(eye*24,1)+', 코 밑 '+f2(nose*24,1)+'이에요. '+(okE&&okN?'두 기준선이 다 맞았어요!':'기준선부터 맞춰 봐요.')],['fruitfly','e09','초파리',okG?'눈 사이도 좋아.':'눈 사이가 '+(gap<tG?'좁아 몰린 눈처럼':'넓어 밀린 눈처럼')+' 보여.']]);}
  wire(S,upd);upd();}
var SWAP_T={fs:['여성 정면',{shape:'circle',eye:'1',ear:'low',neck:'thin'}],ms:['남성 정면',{shape:'shogi',eye:'2',ear:'high',neck:'thick'}],fp:['여성 옆얼굴',{shape:'circle',eye:'1',ear:'mid',neck:'thin'}],mp:['남성 옆얼굴',{shape:'shogi',eye:'2',ear:'back',neck:'thick'}]};
function swap(){var S=document.getElementById('swap');if(!S)return;var q=function(n){return S.querySelector('[name='+n+']');};var touched=false,hit={};
  function upd(e){if(e)touched=true;var tk=q('target').value,T=SWAP_T[tk][1];var o={shape:q('shape').value,eye:q('eye').value,ear:q('ear').value,neck:q('neck').value};
    var front=tk==='fs'||tk==='ms';var earOk=front?(T.ear===o.ear):(T.ear===o.ear);var ok={shape:o.shape===T.shape,eye:o.eye===T.eye,ear:earOk,neck:o.neck===T.neck};var n=Object.keys(ok).filter(function(k){return ok[k];}).length;
    if(n===4&&touched)hit[tk]=1;
    board(S.querySelector('.board'),[['윤곽',o.shape==='circle'?'원에서 깎기':'원 + 장기말',ok.shape],['눈 세로:가로',o.eye==='1'?'1:1':'1:2',ok.eye],['귀',{low:'눈 가운데~코',high:'눈꺼풀~코끝',mid:'1/2보다 조금 뒤',back:'1/2보다 꽤 뒤'}[o.ear],ok.ear],['목',o.neck==='thin'?'가늘게':'굵게',ok.neck]]);
    var sex=o.shape==='circle'?'f':'m';var s=el('svg',{viewBox:'0 0 360 330',role:'img','aria-label':'남녀 바꾸기 결과'});var g1=S.querySelector('.g1');g1.innerHTML='';g1.appendChild(s);el('rect',{x:0,y:0,width:360,height:330,fill:'#fbfcfd'},s);
    if(front){var Gf=faceGeo({sex:sex,cx:180,top:20,H:280});faceFront(s,{sex:sex,cx:180,top:20,H:280,eyeRatio:o.eye==='1'?0.92:0.48,neck:true,neckW:o.neck==='thin'?24:38,earTop:o.ear==='low'?Gf.eyelid+18:Gf.eyelid,earBot:o.ear==='low'?Gf.nose-4:Gf.nose-8});}
    else faceSide(s,{sex:sex,cx:200,cy:140,r:100,earX:{low:0.55,mid:0.55,high:0.66,back:0.68}[o.ear],neckW:o.neck==='thin'?0.25:0.5});
    var s2=el('svg',{viewBox:'0 0 360 200',role:'img','aria-label':'목표 네 가지'});var g2=S.querySelector('.g2');g2.innerHTML='';g2.appendChild(s2);
    Object.keys(SWAP_T).forEach(function(k,i){el('rect',{x:16+i*86,y:40,width:78,height:90,rx:8,fill:hit[k]?'#e8f6ec':'#f2f4f7',stroke:hit[k]?C.green:'#d5dbe2'},s2);ktxt(s2,55+i*86,90,SWAP_T[k][0]+(hit[k]?' ✓':''),{size:11.5,anchor:'middle',fill:C.ink});});
    var M=[!!hit.ms,!!hit.fp,Object.keys(hit).length===4];if(touched)missions(S.querySelector('.missions'),M,true);
    say(S.querySelector('.talk'),[['doctor','e10','박사','목표: '+SWAP_T[tk][0]+'. 맞은 항목 '+n+' / 4.'],['sia','e10','시아',ok.ear?'귀 위치가 맞았어요.':front?'정면에서는 남성 귀가 더 높아요(눈꺼풀~코끝).':'옆얼굴에서는 남성 귀가 더 뒤예요.'],['jupanbot','e16','주판봇',n===4?'완성! 남녀 신호 네 개가 다 맞았습니다!':'눈만 바꿔서는 안 되는군요…']]);}
  wire(S,upd);upd();}
function workshop(){var S=document.getElementById('workshop');if(!S)return;var touched=false;var get=faceForm(S.querySelector('.ow'),function(){touched=true;upd();});var job=S.querySelector('[name=job]');job.addEventListener('change',function(){touched=true;upd();});
  function upd(){var o=get();var r=facePrompt(o);S.querySelector('.g1 pre').textContent=r.text;var need={sheet:['parts','eyes'],turn:['view','parts'],goods:['age','shape']}[job.value];var jobOk=need.every(function(k){return o[k];});
    board(S.querySelector('.board'),[['점검표',r.score+' / 6',r.score===6],['요청 상황 맞춤',jobOk?'맞음':'부족',jobOk],['충돌 경고',r.warn.length+'개',r.warn.length===0],['나이 표기',o.age?'성인 명시':'없음',!!o.age]]);
    var s=el('svg',{viewBox:'0 0 360 200',role:'img','aria-label':'점검표 막대'});var g2=S.querySelector('.g2');g2.innerHTML='';g2.appendChild(s);['성별','윤곽','눈','부위 높이','각도','나이'].forEach(function(t,i){var ok=[o.sex,o.shape,o.eyes,o.parts,o.view,o.age][i];el('rect',{x:76,y:14+i*30,width:ok?260:40,height:20,rx:4,fill:ok?C.teal:'#e3e8ee'},s);ktxt(s,70,29+i*30,t,{size:12.5,anchor:'end',fill:C.ink});});
    var M=[r.score===6&&r.warn.length===0,o.sex==='m'&&o.shape==='angular'&&o.eyes==='almond'&&o.view==='side',o.sex==='f'&&o.shape==='round'&&o.eyes==='big'&&o.age==='adult'];if(touched)missions(S.querySelector('.missions'),M,true);
    say(S.querySelector('.talk'),[['doctor','e10','박사','요청 상황: '+job.options[job.selectedIndex].text+'. '+(jobOk?'필요한 조각이 들어 있다.':'이 상황에 꼭 필요한 조각이 빠졌다.')],['haru','e10','조수','점검표 '+r.score+' / 6'+(r.miss.length?', 빠진 것: '+r.miss.join(', '):'!')],['fruitfly','e09','초파리',r.warn.length?r.warn[0]:'충돌 없음. 문장이 서로 맞아.']]);}
  var cp=S.querySelector('.copy');if(cp)cp.addEventListener('click',function(){var t=S.querySelector('.g1 pre').textContent;if(navigator.clipboard)navigator.clipboard.writeText(t).then(function(){cp.textContent='복사했습니다';},function(){cp.textContent='직접 선택해 복사하세요';});});upd();}
var DESK_CA=['눈 사이 좁음','부위가 위로 몰림','장기말이 김','뒤통수 부풂','턱이 튀어나온 각도','목을 직선으로 이음','안경 테가 눈을 가림','입술 기복 과다'];
var DESK_SYM=['두 눈이 가운데로 몰려 사시처럼 보인다','이마는 좁고 눈~코 사이가 길어 얼굴이 늘어져 보인다','남성 얼굴의 턱이 뾰족하고 얼굴이 지나치게 길다','옆얼굴의 머리가 뒤로 크게 부풀어 둔해 보인다','목이 가는 옆얼굴인데 턱이 앞으로 튀어나와 보인다','옆얼굴에서 머리와 목이 꺾인 직선으로 붙어 인형 같다','안경을 씌웠더니 테 선이 눈동자 한가운데를 지난다','애니풍 여성 옆얼굴의 입 주변이 앞으로 불룩하다'];
function desk(){var S=document.getElementById('desk');if(!S)return;var CA=DESK_CA,SYM=DESK_SYM;
  var cur=0,streak=0,seen={},wrong=0,right=0,touched=false;var r=rng(Date.now()%9999+1);
  function next(){cur=Math.floor(r()*8);S.querySelector('.sym').textContent='증상: '+SYM[cur];var o=S.querySelector('.deskopts');o.innerHTML='';
    var opts=[cur];while(opts.length<4){var k=Math.floor(r()*8);if(opts.indexOf(k)<0)opts.push(k);}opts.sort(function(){return r()-.5;});
    opts.forEach(function(k){var b=document.createElement('button');b.type='button';b.textContent=CA[k];b.addEventListener('click',function(){touched=true;if(k===cur){streak++;right++;seen[cur]=1;b.classList.add('ok');setTimeout(next,500);}else{streak=0;wrong++;b.classList.add('no');}upd();});o.appendChild(b);});}
  function upd(){var n=Object.keys(seen).length;board(S.querySelector('.board'),[['연속 정답',streak,streak>=3],['맞힌 종류',n+' / 8',n===8],['맞힘',right,right>0],['틀림',wrong,wrong===0]]);
    var M=[streak>=3,n===8,right>=5&&wrong===0];if(touched)missions(S.querySelector('.missions'),M,true);
    var s=el('svg',{viewBox:'0 0 360 200',role:'img','aria-label':'맞힌 실패 종류'});var g=S.querySelector('.g2');g.innerHTML='';g.appendChild(s);CA.forEach(function(t,i){el('rect',{x:16+(i%4)*86,y:20+Math.floor(i/4)*90,width:78,height:70,rx:8,fill:seen[i]?'#e8f6ec':'#f2f4f7',stroke:seen[i]?C.green:'#d5dbe2'},s);ktxt(s,55+(i%4)*86,60+Math.floor(i/4)*90,'f'+(i+1)+(seen[i]?' ✓':''),{size:14,anchor:'middle',fill:C.ink});});
    say(S.querySelector('.talk'),[['doctor','e10','박사','순서: 큰 틀 → 높이 기준선 → 눈 상자 → 코·입·귀 → 목·어깨.'],['haru','e10','조수','연속 '+streak+'개, 맞힌 종류 '+n+' / 8이에요.'],['x2','e09','평가단 X2',wrong?'틀린 건 6부 실패 카드에서 다시 보세요.':'아직 틀린 게 없어요!']]);}
  next();upd();}
/* 프롬프트 복사 버튼(직접 만들기 실습) */
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.promptbox .copy');if(!b||b.closest('#workshop'))return;var pre=b.parentNode.querySelector('pre');if(!pre)return;var t=pre.textContent;
  if(navigator.clipboard)navigator.clipboard.writeText(t).then(function(){b.textContent='복사했습니다';},function(){b.textContent='직접 선택해 복사하세요';});else b.textContent='직접 선택해 복사하세요';});
