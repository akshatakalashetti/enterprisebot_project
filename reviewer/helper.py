import requests
from bs4 import BeautifulSoup


url_red_64 =        "https://www.amazon.in/New-Apple-iPhone-12-64GB/product-reviews/B08L5TGWD1/ref=cm_cr_arp_d_viewopt_rvwer?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=1&formatType=current_format"
url_purple_256 =    "https://www.amazon.in/New-Apple-iPhone-12-256GB/product-reviews/B0932RLX4G/ref=cm_cr_arp_d_viewopt_rvwer?ie=UTF8&reviewerType=avp_only_reviews&formatType=current_format&pageNumber=1"
url_white_256 =     "https://www.amazon.in/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_viewopt_fmt?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=1&formatType=current_format"
url_green_256 =     "https://www.amazon.in/New-Apple-iPhone-12-256GB/product-reviews/B08L5VJM1K/ref=cm_cr_arp_d_viewopt_fmt?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=1&formatType=current_format"

#response = requests.get(url_red_64)
#print(response)
#html_red = response.text

html_red= """ 


<!doctype html><html lang="en-in" class="a-no-js" data-19ax5a9jf="dingo"><!-- sp:feature:head-start -->
<head><script>var aPageStart = (new Date()).getTime();</script><meta charset="utf-8"/>
<!-- sp:end-feature:head-start -->
<!-- sp:feature:csm:head-open-part1 -->

<script type='text/javascript'>var ue_t0=ue_t0||+new Date();</script>
<!-- sp:end-feature:csm:head-open-part1 -->
<!-- sp:feature:cs-optimization -->
<meta http-equiv='x-dns-prefetch-control' content='on'>
<link rel="dns-prefetch" href="https://images-eu.ssl-images-amazon.com">
<link rel="dns-prefetch" href="https://m.media-amazon.com">
<link rel="dns-prefetch" href="https://completion.amazon.com">
<!-- sp:end-feature:cs-optimization -->
<!-- sp:feature:csm:head-open-part2 -->
<script type='text/javascript'>
window.ue_ihb = (window.ue_ihb || window.ueinit || 0) + 1;
if (window.ue_ihb === 1) {

var ue_csm = window,
    ue_hob = +new Date();
(function(d){var e=d.ue=d.ue||{},f=Date.now||function(){return+new Date};e.d=function(b){return f()-(b?0:d.ue_t0)};e.stub=function(b,a){if(!b[a]){var c=[];b[a]=function(){c.push([c.slice.call(arguments),e.d(),d.ue_id])};b[a].replay=function(b){for(var a;a=c.shift();)b(a[0],a[1],a[2])};b[a].isStub=1}};e.exec=function(b,a){return function(){try{return b.apply(this,arguments)}catch(c){ueLogError(c,{attribution:a||"undefined",logLevel:"WARN"})}}}})(ue_csm);


    var ue_err_chan = 'jserr-rw';
(function(d,e){function h(f,b){if(!(a.ec>a.mxe)&&f){a.ter.push(f);b=b||{};var c=f.logLevel||b.logLevel;c&&c!==k&&c!==m&&c!==n&&c!==p||a.ec++;c&&c!=k||a.ecf++;b.pageURL=""+(e.location?e.location.href:"");b.logLevel=c;b.attribution=f.attribution||b.attribution;a.erl.push({ex:f,info:b})}}function l(a,b,c,e,g){d.ueLogError({m:a,f:b,l:c,c:""+e,err:g,fromOnError:1,args:arguments},g?{attribution:g.attribution,logLevel:g.logLevel}:void 0);return!1}var k="FATAL",m="ERROR",n="WARN",p="DOWNGRADED",a={ec:0,ecf:0,
pec:0,ts:0,erl:[],ter:[],buffer:[],mxe:50,startTimer:function(){a.ts++;setInterval(function(){d.ue&&a.pec<a.ec&&d.uex("at");a.pec=a.ec},1E4)}};l.skipTrace=1;h.skipTrace=1;h.isStub=1;d.ueLogError=h;d.ue_err=a;e.onerror=l})(ue_csm,window);


var ue_id = 'RZ67A764XT8VEYCF2P53',
    ue_url = '/rd/uedata',
    ue_navtiming = 1,
    ue_mid = 'A21TJRUUN4KGV',
    ue_sid = '257-4714000-6327435',
    ue_sn = 'www.amazon.in',
    ue_furl = 'fls-eu.amazon.in',
    ue_surl = 'https://unagi-eu.amazon.com/1/events/com.amazon.csm.nexusclient.prod',
    ue_int = 0,
    ue_fcsn = 1,
    ue_urt = 3,
    ue_rpl_ns = 'cel-rpl',
    ue_ddq = 1,
    ue_fpf = '//fls-eu.amazon.in/1/batch/1/OP/A21TJRUUN4KGV:257-4714000-6327435:RZ67A764XT8VEYCF2P53$uedata=s:',
    ue_sbuimp = 1,
    ue_ibft = 0,
    ue_sswmts = 0,
    ue_jsmtf = 0,
    ue_fnt = 0,
    ue_lpsi = 6000,
    ue_no_counters = 0,

    ue_swi = 1;
var ue_viz=function(){(function(b,e,a){function k(c){if(b.ue.viz.length<p&&!l){var a=c.type;c=c.originalEvent;/^focus./.test(a)&&c&&(c.toElement||c.fromElement||c.relatedTarget)||(a=e[m]||("blur"==a||"focusout"==a?"hidden":"visible"),b.ue.viz.push(a+":"+(+new Date-b.ue.t0)),"visible"==a&&(b.ue.isl&&q("at"),l=1))}}for(var l=0,q=b.uex,f,g,m,n=["","webkit","o","ms","moz"],d=0,p=20,h=0;h<n.length&&!d;h++)if(a=n[h],f=(a?a+"H":"h")+"idden",d="boolean"==typeof e[f])g=a+"visibilitychange",m=(a?a+"V":"v")+
"isibilityState";k({});d&&e.addEventListener(g,k,0);b.ue&&d&&(b.ue.pageViz={event:g,propHid:f})})(ue_csm,ue_csm.document,ue_csm.window)};

(function(d,h,N){function H(a){return a&&a.replace&&a.replace(/^\s+|\s+$/g,"")}function u(a){return"undefined"===typeof a}function B(a,b){for(var c in b)b[v](c)&&(a[c]=b[c])}function I(a){try{var b=N.cookie.match(RegExp("(^| )"+a+"=([^;]+)"));if(b)return b[2].trim()}catch(c){}}function O(k,b,c){var q=(x||{}).type;if("device"!==c||2!==q&&1!==q)k&&(d.ue_id=a.id=a.rid=k,w&&(w=w.replace(/((.*?:){2})(\w+)/,function(a,b){return b+k})),D&&(e("id",D,k),D=0)),b&&(w&&(w=w.replace(/(.*?:)(\w|-)+/,function(a,
c){return c+b})),d.ue_sid=b),c&&a.tag("page-source:"+c),d.ue_fpf=w}function P(){var a={};return function(b){b&&(a[b]=1);b=[];for(var c in a)a[v](c)&&b.push(c);return b}}function y(d,b,c,q){q=q||+new E;var f,m;if(b||u(c)){if(d)for(m in f=b?e("t",b)||e("t",b,{}):a.t,f[d]=q,c)c[v](m)&&e(m,b,c[m]);return q}}function e(d,b,c){var e=b&&b!=a.id?a.sc[b]:a;e||(e=a.sc[b]={});"id"===d&&c&&(Q=1);return e[d]=c||e[d]}function R(d,b,c,e,f){c="on"+c;var m=b[c];"function"===typeof m?d&&(a.h[d]=m):m=function(){};b[c]=
function(a){f?(e(a),m(a)):(m(a),e(a))};b[c]&&(b[c].isUeh=1)}function S(k,b,c,q){function p(b,c){var d=[b],g=0,f={},m,h;c?(d.push("m=1"),f[c]=1):f=a.sc;for(h in f)if(f[v](h)){var q=e("wb",h),p=e("t",h)||{},n=e("t0",h)||a.t0,l;if(c||2==q){q=q?g++:"";d.push("sc"+q+"="+h);for(l in p)u(p[l])||null===p[l]||d.push(l+q+"="+(p[l]-n));d.push("t"+q+"="+p[k]);if(e("ctb",h)||e("wb",h))m=1}}!J&&m&&d.push("ctb=1");return d.join("&")}function m(b,c,g,e,f){if(b){var k=d.ue_err;d.ue_url&&!e&&!f&&b&&0<b.length&&(e=
new Image,a.iel.push(e),e.src=b,a.count&&a.count("postbackImageSize",b.length));w?(f=h.encodeURIComponent)&&b&&(e=new Image,b=""+d.ue_fpf+f(b)+":"+(+new E-d.ue_t0),a.iel.push(e),e.src=b):a.log&&(a.log(b,"uedata",{n:1}),a.ielf.push(b));k&&!k.ts&&k.startTimer();a.b&&(k=a.b,a.b="",m(k,c,g,1))}}function A(b){var c=x?x.type:F,d=2==c||a.isBFonMshop,c=c&&!d,e=a.bfini;Q||(e&&1<e&&(b+="&bfform=1",c||(a.isBFT=e-1)),d&&(b+="&bfnt=1",a.isBFT=a.isBFT||1),a.ssw&&a.isBFT&&(a.isBFonMshop&&(a.isNRBF=0),u(a.isNRBF)&&
(d=a.ssw(a.oid),d.e||u(d.val)||(a.isNRBF=1<d.val?0:1)),u(a.isNRBF)||(b+="&nrbf="+a.isNRBF)),a.isBFT&&!a.isNRBF&&(b+="&bft="+a.isBFT));return b}if(!a.paused&&(b||u(c))){for(var l in c)c[v](l)&&e(l,b,c[l]);a.isBFonMshop||y("pc",b,c);l="ld"===k&&b&&e("wb",b);var s=e("id",b)||a.id;l||s===a.oid||(D=b,ba(s,(e("t",b)||{}).tc||+e("t0",b),+e("t0",b)));var s=e("id",b)||a.id,t=e("id2",b),g=a.url+"?"+k+"&v="+a.v+"&id="+s,J=e("ctb",b)||e("wb",b),z;J&&(g+="&ctb="+J);t&&(g+="&id2="+t);1<d.ueinit&&(g+="&ic="+d.ueinit);
if(!("ld"!=k&&"ul"!=k||b&&b!=s)){if("ld"==k){try{h[K]&&h[K].isUeh&&(h[K]=null)}catch(I){}if(h.chrome)for(t=0;t<L.length;t++)T(G,L[t]);(t=N.ue_backdetect)&&t.ue_back&&t.ue_back.value++;d._uess&&(z=d._uess());a.isl=1}a._bf&&(g+="&bf="+a._bf());d.ue_navtiming&&f&&(e("ctb",s,"1"),a.isBFonMshop||y("tc",F,F,M));!C||a.isBFonMshop||U||(f&&B(a.t,{na_:f.navigationStart,ul_:f.unloadEventStart,_ul:f.unloadEventEnd,rd_:f.redirectStart,_rd:f.redirectEnd,fe_:f.fetchStart,lk_:f.domainLookupStart,_lk:f.domainLookupEnd,
co_:f.connectStart,_co:f.connectEnd,sc_:f.secureConnectionStart,rq_:f.requestStart,rs_:f.responseStart,_rs:f.responseEnd,dl_:f.domLoading,di_:f.domInteractive,de_:f.domContentLoadedEventStart,_de:f.domContentLoadedEventEnd,_dc:f.domComplete,ld_:f.loadEventStart,_ld:f.loadEventEnd,ntd:("function"!==typeof C.now||u(M)?0:new E(M+C.now())-new E)+a.t0}),x&&B(a.t,{ty:x.type+a.t0,rc:x.redirectCount+a.t0}),U=1);a.isBFonMshop||B(a.t,{hob:d.ue_hob,hoe:d.ue_hoe});a.ifr&&(g+="&ifr=1")}y(k,b,c,q);var r,n;l||b&&
b!==s||ca(b);(c=d.ue_mbl)&&c.cnt&&!l&&(g+=c.cnt());l?e("wb",b,2):"ld"==k&&(a.lid=H(s));for(r in a.sc)if(1==e("wb",r))break;if(l){if(a.s)return;g=p(g,null)}else c=p(g,null),c!=g&&(c=A(c),a.b=c),z&&(g+=z),g=p(g,b||a.id);g=A(g);if(a.b||l)for(r in a.sc)2==e("wb",r)&&delete a.sc[r];z=0;a._rt&&(g+="&rt="+a._rt());c=h.csa;if(!l&&c)for(n in r=e("t",b)||{},c=c("PageTiming"),r)r[v](n)&&c("mark",da[n]||n,r[n]);l||(a.s=0,(n=d.ue_err)&&0<n.ec&&n.pec<n.ec&&(n.pec=n.ec,g+="&ec="+n.ec+"&ecf="+n.ecf),z=e("ctb",b),
"ld"!==k||b||a.markers?a.markers&&a.isl&&!l&&b&&B(a.markers,e("t",b)):(a.markers={},B(a.markers,e("t",b))),e("t",b,{}));a.tag&&a.tag().length&&(g+="&csmtags="+a.tag().join("|"),a.tag=P());n=a.viz||[];(r=n.length)&&(g+="&viz="+n.splice(0,r).join("|"));u(d.ue_pty)||(g+="&pty="+d.ue_pty+"&spty="+d.ue_spty+"&pti="+d.ue_pti);a.tabid&&(g+="&tid="+a.tabid);a.aftb&&(g+="&aftb=1");!a._ui||b&&b!=s||(g+=a._ui());a.a=g;m(g,k,z,l,b&&"string"===typeof b&&-1!==b.indexOf("csa:"))}}function ca(a){var b=h.ue_csm_markers||
{},c;for(c in b)b[v](c)&&y(c,a,F,b[c])}function A(a,b,c){c=c||h;if(c[V])c[V](a,b,!1);else if(c[W])c[W]("on"+a,b)}function T(a,b,c){c=c||h;if(c[X])c[X](a,b,!1);else if(c[Y])c[Y]("on"+a,b)}function Z(){function a(){d.onUl()}function b(a){return function(){c[a]||(c[a]=1,S(a))}}var c={},e,f;d.onLd=b("ld");d.onLdEnd=b("ld");d.onUl=b("ul");e={stop:b("os")};h.chrome?(A(G,a),L.push(a)):e[G]=d.onUl;for(f in e)e[v](f)&&R(0,h,f,e[f]);d.ue_viz&&ue_viz();A("load",d.onLd);y("ue")}function ba(e,b,c){var f=d.ue_mbl,
p=h.csa,m=p&&p("SPA"),p=p&&p("PageTiming");f&&f.ajax&&f.ajax(b,c);m&&p&&(m("newPage",{requestId:e,transitionType:"soft"}),p("mark","transitionStart",b));a.tag("ajax-transition")}d.ueinit=(d.ueinit||0)+1;var a=d.ue=d.ue||{};a.t0=h.aPageStart||d.ue_t0;a.id=d.ue_id;a.url=d.ue_url;a.rid=d.ue_id;a.a="";a.b="";a.h={};a.s=1;a.t={};a.sc={};a.iel=[];a.ielf=[];a.viz=[];a.v="0.247493.0";a.paused=!1;var v="hasOwnProperty",G="beforeunload",K="on"+G,V="addEventListener",X="removeEventListener",W="attachEvent",
Y="detachEvent",da={cf:"criticalFeature",af:"aboveTheFold",fn:"functional",fp:"firstPaint",fcp:"firstContentfulPaint",bb:"bodyBegin",be:"bodyEnd",ld:"loaded"},E=h.Date,C=h.performance||h.webkitPerformance,f=(C||{}).timing,x=(C||{}).navigation,M=(f||{}).navigationStart,w=d.ue_fpf,Q=0,U=0,L=[],D=0,F;a.oid=H(a.id);a.lid=H(a.id);a._t0=a.t0;a.tag=P();a.ifr=h.top!==h.self||h.frameElement?1:0;a.markers=null;a.attach=A;a.detach=T;if("000-0000000-8675309"===d.ue_sid){var $=I("cdn-rid"),aa=I("session-id");
$&&aa&&O($,aa,"cdn")}d.uei=Z;d.ueh=R;d.ues=e;d.uet=y;d.uex=S;a.reset=O;a.pause=function(d){a.paused=d};Z()})(ue_csm,ue_csm.window,ue_csm.document);


ue.stub(ue,"event");ue.stub(ue,"onSushiUnload");ue.stub(ue,"onSushiFlush");

ue.stub(ue,"log");ue.stub(ue,"onunload");ue.stub(ue,"onflush");
(function(b){var a=b.ue,g=1===b.ue_no_counters;a.cv={};a.cv.scopes={};a.cv.buffer=[];a.count=function(b,f,c){var e={},d=a.cv,h=c&&0===c.c;e.counter=b;e.value=f;e.t=a.d();c&&c.scope&&(d=a.cv.scopes[c.scope]=a.cv.scopes[c.scope]||{},e.scope=c.scope);if(void 0===f)return d[b];d[b]=f;d=0;c&&c.bf&&(d=1);g||(ue_csm.ue_sclog||!a.clog||0!==d||h?a.log&&a.log(e,"csmcount",{c:1,bf:d}):a.clog(e,"csmcount",{bf:d}));a.cv.buffer.push({c:b,v:f})};a.count("baselineCounter2",1);a&&a.event&&(a.event({requestId:b.ue_id||
"rid",server:b.ue_sn||"sn",obfuscatedMarketplaceId:b.ue_mid||"mid"},"csm","csm.CSMBaselineEvent.4"),a.count("nexusBaselineCounter",1,{bf:1}))})(ue_csm);



var ue_hoe = +new Date();
}
window.ueinit = window.ue_ihb;
</script>

<!-- 1i5uqmtlyn3cujr -->
<script>window.ue && ue.count && ue.count('CSMLibrarySize', 9812)</script>
<!-- sp:end-feature:csm:head-open-part2 -->
<!-- sp:feature:aui-assets -->
<link rel="stylesheet" href="https://m.media-amazon.com/images/I/11EIQ5IGqaL._RC|01ZTHTZObnL.css,410yLeQZHKL.css,31OSFXVtM5L.css,013z33uKh2L.css,017DsKjNQJL.css,0131vqwP5UL.css,41EWOOlBJ9L.css,11TIuySqr6L.css,01ElnPiDxWL.css,11fJbvhE5HL.css,01Dm5eKVxwL.css,01IdKcBuAdL.css,01y-XAlI+2L.css,21P6CS3L9LL.css,01oDR3IULNL.css,41Axm2+z87L.css,01XPHJk60-L.css,01S0vRENeAL.css,21IbH+SoKSL.css,11MrAKjcAKL.css,21fecG8pUzL.css,11a5wZbuKrL.css,01CFUgsA-YL.css,31pHA2U5D9L.css,11qour3ND0L.css,116t+WD27UL.css,11gKCCKQV+L.css,11061HxnEvL.css,11oHt2HYxnL.css,01j2JE3j7aL.css,11JQtnL-6eL.css,21KA2rMsZML.css,11jtXRmppwL.css,0114z6bAEoL.css,21uwtfqr5aL.css,11QyqG8yiqL.css,11K24eOJg4L.css,11F2+OBzLyL.css,01890+Vwk8L.css,01g+cOYAZgL.css,01cbS3UK11L.css,21F85am0yFL.css,01giMEP+djL.css_.css?AUIClients/AmazonUI&VGEEt8I0#not-trident.388250-T1.432724-T1.577951-T1.577971-T1.577969-T1.632675-T1.577970-T1" />
<script>
(function(d,f,R,H){function x(a){A&&A.tag&&A.tag(k(":","aui",a))}function n(a,b){A&&A.count&&A.count("aui:"+a,0===b?0:b||(A.count("aui:"+a)||0)+1)}function t(a){try{return a.test(navigator.userAgent)}catch(b){return!1}}function u(a){return"function"===typeof a}function B(a,b,c){a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent&&a.attachEvent("on"+b,c)}function k(a,b,c,d){b=b&&c?b+a+c:b||c;return d?k(a,b,d):b}function I(a,b,c){try{Object.defineProperty(a,b,{value:c,writable:!1})}catch(y){a[b]=
c}return c}function ta(a,b,c){var d=c=a.length,g=function(){d--||(S.push(b),T||(setTimeout(da,0),T=!0))};for(g();c--;)ea[a[c]]?g():(C[a[c]]=C[a[c]]||[]).push(g)}function ua(a,b,c,d,g){var e=f.createElement(a?"script":"link");B(e,"error",d);g&&B(e,"load",g);a?(e.type="text/javascript",e.async=!0,c&&/AUIClients|images[/]I/.test(b)&&e.setAttribute("crossorigin","anonymous"),e.src=b):(e.rel="stylesheet",e.href=b);f.getElementsByTagName("head")[0].appendChild(e)}function fa(a,b){return function(c,y){function g(){ua(b,
c,e,function(b){U?n("resource_unload"):e?(e=!1,n("resource_retry"),g()):(n("resource_error"),a.log("Asset failed to load: "+c));b&&b.stopPropagation?b.stopPropagation():d.event&&(d.event.cancelBubble=!0)},y)}if(ha[c])return!1;ha[c]=!0;n("resource_count");var e=!0;return!g()}}function va(a,b,c){for(var d={name:a,guard:function(c){return b.guardFatal(a,c)},guardTime:function(a){return b.guardTime(a)},logError:function(c,e,d){b.logError(c,e,d,a)}},g=[],e=0;e<c.length;e++)J.hasOwnProperty(c[e])&&(g[e]=
V.hasOwnProperty(c[e])?V[c[e]](J[c[e]],d):J[c[e]]);return g}function D(a,b,c,y,g){return function(e,f){function n(){var a=null;y?a=f:u(f)&&(m.start=w(),a=f.apply(d,va(e,l,h)),m.end=w());if(b){J[e]=a;a=e;for(ea[a]=!0;(C[a]||[]).length;)C[a].shift()();delete C[a]}m.done=!0}var l=g||this;u(e)&&(f=e,e=H);b&&(e=e?e.replace(ia,""):"__NONAME__",W.hasOwnProperty(e)&&l.error(k(", reregistered by ",k(" by ",e+" already registered",W[e]),l.attribution),e),W[e]=l.attribution);for(var h=[],r=0;r<a.length;r++)h[r]=
a[r].replace(ia,"");var m=E[e||"anon"+ ++wa]={depend:h,registered:w(),namespace:l.namespace};e&&xa.hasOwnProperty(e);c?n():ta(h,l.guardFatal(e,n),e);return{decorate:function(a){V[e]=l.guardFatal(e,a)}}}}function ja(a){return function(){var b=Array.prototype.slice.call(arguments);return{execute:D(b,!1,a,!1,this),register:D(b,!0,a,!1,this)}}}function X(a,b){return function(c,d){d||(d=c,c=H);var g=this.attribution;return function(){z.push(b||{attribution:g,name:c,logLevel:a});var e=d.apply(this,arguments);
z.pop();return e}}}function K(a,b){this.load={js:fa(this,!0),css:fa(this)};I(this,"namespace",b);I(this,"attribution",a)}function ka(){f.body?v.trigger("a-bodyBegin"):setTimeout(ka,20)}function F(a,b){a.className=Y(a,b)+" "+b}function Y(a,b){return(" "+a.className+" ").split(" "+b+" ").join(" ").replace(/^ | $/g,"")}function la(a){try{return a()}catch(b){return!1}}function L(){if(M){var a={w:d.innerWidth||h.clientWidth,h:d.innerHeight||h.clientHeight};5<Math.abs(a.w-Z.w)||50<a.h-Z.h?(Z=a,N=4,(a=m.mobile||
m.tablet?450<a.w&&a.w>a.h:1250<=a.w)?F(h,"a-ws"):h.className=Y(h,"a-ws")):0<N&&(N--,ma=setTimeout(L,16))}}function ya(a){(M=a===H?!M:!!a)&&L()}function za(){return M}"use strict";var O=R.now=R.now||function(){return+new R},w=function(a){return a&&a.now?a.now.bind(a):O}(d.performance),P=w(),xa={},p=d.AmazonUIPageJS||d.P;if(p&&p.when&&p.register){P=[];for(var q=f.currentScript;q;q=q.parentElement)q.id&&P.push(q.id);return p.log("A copy of P has already been loaded on this page.","FATAL",P.join(" "))}var A=
d.ue;x();x("aui_build_date:3.23.1-2023-04-19");var S=[],Aa=[],T=!1;var da=function(){for(var a=setTimeout(da,0),b=O();Aa.length||S.length;)if(S.shift()(),50<O()-b)return;clearTimeout(a);T=!1};var ea={},C={},ha={},U=!1;B(d,"beforeunload",function(){U=!0;setTimeout(function(){U=!1},1E4)});var ia=/^prv:/,W={},J={},V={},E={},wa=0,aa=String.fromCharCode(92),z=[],na=!0,oa=d.onerror;d.onerror=function(a,b,c,y,g){g&&"object"===typeof g||(g=Error(a,b,c),g.columnNumber=y,g.stack=b||c||y?k(aa,g.message,"at "+
k(":",b,c,y)):H);var e=z.pop()||{};g.attribution=k(":",g.attribution||e.attribution,e.name);g.logLevel=e.logLevel;g.attribution&&console&&console.log&&console.log([g.logLevel||"ERROR",a,"thrown by",g.attribution].join(" "));z=[];oa&&(e=[].slice.call(arguments),e[4]=g,oa.apply(d,e))};K.prototype={logError:function(a,b,c,y){b={message:b,logLevel:c||"ERROR",attribution:k(":",this.attribution,y)};if(d.ueLogError)return d.ueLogError(a||b,a?b:null),!0;console&&console.error&&(console.log(b),console.error(a));
return!1},error:function(a,b,c,d){a=Error(k(":",d,a,c));a.attribution=k(":",this.attribution,b);throw a;},guardError:X(),guardFatal:X("FATAL"),guardCurrent:function(a){var b=z[z.length-1];return b?X(b.logLevel,b).call(this,a):a},guardTime:function(a){var b=z[z.length-1],c=b&&b.name;return c&&c in E?function(){var b=w(),d=a.apply(this,arguments);E[c].async=(E[c].async||0)+w()-b;return d}:a},log:function(a,b,c){return this.logError(null,a,b,c)},declare:D([],!0,!0,!0),register:D([],!0),execute:D([]),
AUI_BUILD_DATE:"3.23.1-2023-04-19",when:ja(),now:ja(!0),trigger:function(a,b,c){var f=O();this.declare(a,{data:b,pageElapsedTime:f-(d.aPageStart||NaN),triggerTime:f});c&&c.instrument&&G.when("prv:a-logTrigger").execute(function(b){b(a)})},handleTriggers:function(){this.log("handleTriggers deprecated")},attributeErrors:function(a){return new K(a)},_namespace:function(a,b){return new K(a,b)},setPriority:function(a){na?na=!1:this.log("setPriority only accept the first call.")}};var v=I(d,"AmazonUIPageJS",
new K);var G=v._namespace("PageJS","AmazonUI");G.declare("prv:p-debug",E);v.declare("p-recorder-events",[]);v.declare("p-recorder-stop",function(){});I(d,"P",v);ka();if(f.addEventListener){var pa;f.addEventListener("DOMContentLoaded",pa=function(){v.trigger("a-domready");f.removeEventListener("DOMContentLoaded",pa,!1)},!1)}var h=f.documentElement,ba=function(){var a=["O","ms","Moz","Webkit"],b=f.createElement("div");return{testGradients:function(){return!0},test:function(c){var d=c.charAt(0).toUpperCase()+
c.substr(1);c=(a.join(d+" ")+d+" "+c).split(" ");for(d=c.length;d--;)if(""===b.style[c[d]])return!0;return!1},testTransform3d:function(){return!0}}}();p=h.className;var qa=/(^| )a-mobile( |$)/.test(p),ra=/(^| )a-tablet( |$)/.test(p),m={audio:function(){return!!f.createElement("audio").canPlayType},video:function(){return!!f.createElement("video").canPlayType},canvas:function(){return!!f.createElement("canvas").getContext},svg:function(){return!!f.createElementNS&&!!f.createElementNS("http://www.w3.org/2000/svg",
"svg").createSVGRect},offline:function(){return navigator.hasOwnProperty&&navigator.hasOwnProperty("onLine")&&navigator.onLine},dragDrop:function(){return"draggable"in f.createElement("span")},geolocation:function(){return!!navigator.geolocation},history:function(){return!(!d.history||!d.history.pushState)},webworker:function(){return!!d.Worker},autofocus:function(){return"autofocus"in f.createElement("input")},inputPlaceholder:function(){return"placeholder"in f.createElement("input")},textareaPlaceholder:function(){return"placeholder"in
f.createElement("textarea")},localStorage:function(){return"localStorage"in d&&null!==d.localStorage},orientation:function(){return"orientation"in d},touch:function(){return"ontouchend"in f},gradients:function(){return ba.testGradients()},hires:function(){var a=d.devicePixelRatio&&1.5<=d.devicePixelRatio||d.matchMedia&&d.matchMedia("(min-resolution:144dpi)").matches;n("hiRes"+(qa?"Mobile":ra?"Tablet":"Desktop"),a?1:0);return a},transform3d:function(){return ba.testTransform3d()},touchScrolling:function(){return t(/Windowshop|android|OS ([5-9]|[1-9][0-9]+)(_[0-9]{1,2})+ like Mac OS X|SOFTWARE=([5-9]|[1-9][0-9]+)(.[0-9]{1,2})+.*DEVICE=iPhone|Chrome|Silk|Firefox|Trident.+?; Touch/i)},
ios:function(){return t(/OS [1-9][0-9]*(_[0-9]*)+ like Mac OS X/i)&&!t(/trident|Edge/i)},android:function(){return t(/android.([1-9]|[L-Z])/i)&&!t(/trident|Edge/i)},mobile:function(){return qa},tablet:function(){return ra},rtl:function(){return"rtl"===h.dir}};for(q in m)m.hasOwnProperty(q)&&(m[q]=la(m[q]));for(var ca="textShadow textStroke boxShadow borderRadius borderImage opacity transform transition".split(" "),Q=0;Q<ca.length;Q++)m[ca[Q]]=la(function(){return ba.test(ca[Q])});var M=!0,ma=0,Z=
{w:0,h:0},N=4;L();B(d,"resize",function(){clearTimeout(ma);N=4;L()});var sa={getItem:function(a){try{return d.localStorage.getItem(a)}catch(b){}},setItem:function(a,b){try{return d.localStorage.setItem(a,b)}catch(c){}}};h.className=Y(h,"a-no-js");F(h,"a-js");!t(/OS [1-8](_[0-9]*)+ like Mac OS X/i)||d.navigator.standalone||t(/safari/i)||F(h,"a-ember");p=[];for(q in m)m.hasOwnProperty(q)&&m[q]&&p.push("a-"+q.replace(/([A-Z])/g,function(a){return"-"+a.toLowerCase()}));F(h,p.join(" "));h.setAttribute("data-aui-build-date",
"3.23.1-2023-04-19");v.register("p-detect",function(){return{capabilities:m,localStorage:m.localStorage&&sa,toggleResponsiveGrid:ya,responsiveGridEnabled:za}});t(/UCBrowser/i)||m.localStorage&&F(h,sa.getItem("a-font-class"));v.declare("a-event-revised-handling",!1);v.execute("RetailPageServiceWorker",function(){function a(a,b){l.controller&&a?(a={feature:"retail_service_worker_messaging",command:a},b&&(a.data=b),l.controller.postMessage(a)):a&&n("sw:sw_message_no_ctrl",1)}function b(a){var b=a.data;
if(b&&"retail_service_worker_messaging"===b.feature&&b.command&&b.data){var c=b.data;a=d.ue;var e=d.ueLogError;switch(b.command){case "log_counter":a&&u(a.count)&&c.name&&a.count(c.name,0===c.value?0:c.value||1);break;case "log_tag":a&&u(a.tag)&&c.tag&&(a.tag(c.tag),b=d.uex,a.isl&&u(b)&&b("at"));break;case "log_error":e&&u(e)&&c.message&&e({message:c.message,logLevel:c.level||"ERROR",attribution:c.attribution||"RetailServiceWorker"});break;case "log_weblab_trigger":if(!c.weblab||!c.treatment)break;
a&&u(a.trigger)?a.trigger(c.weblab,c.treatment):(n("sw:wt:miss"),n("sw:wt:miss:"+c.weblab+":"+c.treatment));break;default:n("sw:unsupported_message_command",1)}}}function c(a,b){return"sw:"+(b||"")+":"+a+":"}function h(a,b,c){v.logError(a,"[AUI SW] Failed to "+c+" service worker: ","ERROR","RetailPageServiceWorker");n(b+"failure")}function g(){p.forEach(function(a){x(a)})}function e(a){return a.capabilities.isAmazonApp&&a.capabilities.android}function m(a,b,d){if(b)if(b.mshop&&e(a))a=c(d,"mshop_and"),
b=b.mshop.action,p.push(a+"supported"),b(a,d);else if(b.browser){a=t(/Chrome/i)&&!t(/Edge/i)&&!t(/OPR/i)&&!a.capabilities.isAmazonApp&&!t(new RegExp(aa+"bwv"+aa+"b"));var g=b.browser;b=c(d,"browser");a?(a=g.action,p.push(b+"supported"),a(b,d)):p.push(b+"unsupported")}}function q(a,b,d){a&&p.push(c("register",d)+"unsupported");b&&p.push(c("unregister",d)+"unsupported");g()}try{var l=navigator.serviceWorker}catch(Ba){x("sw:nav_err")}(function(){if(l){var c=function(){a("page_loaded",{rid:d.ue_id,mid:d.ue_mid,
pty:d.ue_pty,sid:d.ue_sid,spty:d.ue_spty,furl:d.ue_furl})};B(l,"message",b);a("client_messaging_ready");v.when("load").execute(c);B(l,"controllerchange",function(){a("client_messaging_ready");"complete"===f.readyState&&c()})}})();var p=[],r=function(a,b){var c=d.uex,e=d.uet;a=k(":","aui","sw",a);"ld"===b&&u(c)?c("ld",a,{wb:1}):u(e)&&e(b,a,{wb:1})},z=function(a,b,c){function e(a){b&&u(b.failure)&&b.failure(a)}function g(){m=setTimeout(function(){x(k(":","sw:"+h,f.TIMED_OUT));e({ok:!1,statusCode:f.TIMED_OUT,
done:!1});r(h,"ld")},c||4E3)}var f={NO_CONTROLLER:"no_ctrl",TIMED_OUT:"timed_out",UNSUPPORTED_BROWSER:"unsupported_browser",UNEXPECTED_RESPONSE:"unexpected_response"},h=k(":",a.feature,a.command),m,p=!0;if("MessageChannel"in d&&l&&"controller"in l)if(l.controller){var q=new MessageChannel;q.port1.onmessage=function(c){(c=c.data)&&c.feature===a.feature&&c.command===a.command?(p&&(r(h,"cf"),p=!1),r(h,"af"),clearTimeout(m),c.done||g(),c.ok?b&&u(b.success)&&b.success(c):e(c),c.done&&r(h,"ld")):n(k(":",
"sw:"+h,f.UNEXPECTED_RESPONSE),1)};g();r(h,"bb");l.controller.postMessage(a,[q.port2])}else x(k(":","sw:"+a.feature,f.NO_CONTROLLER)),e({ok:!1,statusCode:f.NO_CONTROLLER,done:!0});else x(k(":","sw:"+a.feature,f.UNSUPPORTED_BROWSER)),e({ok:!1,statusCode:f.UNSUPPORTED_BROWSER,done:!0})};(function(){l?(r("ctrl_changed","bb"),l.addEventListener("controllerchange",function(){x("sw:ctrl_changed");r("ctrl_changed","ld")})):n(k(":","sw:ctrl_changed","sw_unsupp"),1)})();(function(){var a=function(){r(b,"ld");
var a=d.uex;z({feature:"page_proxy",command:"request_feature_tags"},{success:function(b){b=b.data;Array.isArray(b)&&b.forEach(function(a){"string"===typeof a?x(k(":","sw:ppft",a)):n(k(":","sw:ppft","invalid_tag"),1)});n(k(":","sw:ppft","success"),1);A&&A.isl&&u(a)&&a("at")},failure:function(a){n(k(":","sw:ppft","error:"+(a.statusCode||"ppft_error")),1)}})};if("requestIdleCallback"in d){var b=k(":","ppft","callback_ricb");d.requestIdleCallback(a,{timeout:1E3})}else b=k(":","ppft","callback_timeout"),
setTimeout(a,0);r(b,"bb")})();var w={reg:{},unreg:{}};w.unreg.mshop={action:function(a,b){try{l.getRegistrations().then(function(c){c.forEach(function(c){c.unregister().then(function(){n(a+"success")}).catch(function(c){h(c,a,b)})})})}catch(Ca){x("sw:api_error")}}};w.reg.browser={action:function(a,b){l.register("/service-worker.js").then(function(){n(a+"success")}).catch(function(c){h(c,a,b)})}};(function(a){var b=a.reg,c=a.unreg;l&&l.getRegistrations?(G.when("A").execute(function(b){if((a.reg.mshop||
a.unreg.mshop)&&"function"===typeof e&&e(b)){var g=a.reg.mshop?"T1":"C",f=d.ue;f&&f.trigger?f.trigger("MSHOP_SW_CLIENT_446196",g):n("sw:mshop:wt:failed")}m(b,c,"unregister")}),B(d,"load",function(){G.when("A").execute(function(a){m(a,b,"register");g()})})):(q(b&&b.browser,c&&c.browser,"browser"),G.when("A").execute(function(a){"function"===typeof e&&e(a)&&q(b&&b.mshop,c&&c.mshop,"mshop_and")}))})(w)});v.declare("a-fix-event-off",!1);n("pagejs:pkgExecTime",w()-P)})(window,document,Date);
(function(b){function q(a,e,d){function g(a,b,c){var f=Array(e.length);~l&&(f[l]={});~m&&(f[m]=c);for(c=0;c<n.length;c++){var g=n[c],h=a[c];f[g]=h}for(c=0;c<p.length;c++)g=p[c],h=b[c],f[g]=h;a=d.apply(null,f);return~l?f[l]:a}"string"!==typeof a&&b.P.error("C001");-1===a.indexOf("@")&&-1<a.indexOf("/")&&(-1<a.indexOf("es3")||-1<a.indexOf("evergreen"))&&(a=a.substring(0,a.lastIndexOf("/")));if(!r[a]){r[a]=!0;d||(d=e,e=[]);a=a.split(":",2);var c=a[1]?a[0]:void 0,f=(a[1]||a[0]).replace(/@capability\//,
"@c/"),k=c?b.P._namespace(c):b.P,t=!f.lastIndexOf("@c/",0),u=!f.lastIndexOf("@m/",0),n=[];a=[];var p=[],v=[],m=-1,l=-1;for(c=0;c<e.length;c++){var h=e[c];"module"===h&&k.error("C002");"exports"===h?l=c:"require"===h?m=c:h.lastIndexOf("@p/",0)?h.lastIndexOf("@c/",0)&&h.lastIndexOf("@m/",0)?(n.push(c),a.push("mix:"+h)):(p.push(c),v.push(h)):(n.push(c),a.push(h.substr(3)))}k.when.apply(k,a).register("mix:"+f,function(){var a=[].slice.call(arguments);return t||u||~m||p.length?{capabilities:v,cardModuleFactory:function(b,
c){b=g(a,b,c);b.P=k;return b},require:~m?q:void 0}:g(a,[],function(){})});(t||u)&&k.when("mix:@amzn/mix.client-runtime","mix:"+f).execute(function(a,b){a.registerCapabilityModule(f,b)});k.when("mix:"+f).register("xcp:"+f,function(a){return a});var q=function(a,b,c){try{var e=-1<f.indexOf("/")?f.split("/")[0]:f,d=a[0],g=d.lastIndexOf("./",0)?d:e+"/"+d.substr(2),h=g.lastIndexOf("@p/",0)?"mix:"+g:g.substr(3);k.when(h).execute(function(a){try{b(a)}catch(x){c(x)}})}catch(w){c(w)}}}}"use strict";var r=
{};b.mix_d||((b.Promise?P:P.when("3p-promise")).register("@p/promise-is-ready",function(a){b.Promise=b.Promise||a}),(Array.prototype.includes?P:P.when("a-polyfill")).register("@p/polyfill-is-ready",function(){}),b.mix_d=function(a,b,d){P.when("@p/promise-is-ready","@p/polyfill-is-ready").execute("@p/mix-d-deps",function(){q(a,b,d)})},b.xcp_d=b.mix_d,P.when("mix:@amzn/mix.client-runtime").execute(function(a){P.declare("xcp:@xcp/runtime",a)}));b.mixTimeout||(b.mixTimeout=function(a,e,d){b.mixCardInitTimeouts||
(b.mixCardInitTimeouts={});b.mixCardInitTimeouts[e]&&clearTimeout(b.mixCardInitTimeouts[e]);b.mixCardInitTimeouts[e]=setTimeout(function(){P.log("Client-side initialization timeout","WARN",a)},d)});b.mix_csa_map=b.mix_csa_map||{};b.mix_csa_internal=b.mix_csa_internal||function(a,e,d){return b.mix_csa_map[e]=b.mix_csa_map[e]||b.csa(a,d)};b.mix_csa_internal_key=b.mix_csa_internal_key||function(a,b){for(var d="",e=0;e<b.length;e++){var c=b[e];void 0!==a[c]&&"object"!==typeof a[c]&&(d+=c+":"+a[c]+",")}if(!d)throw Error("bad mix-csa key gen.");
return d};b.mix_csa_event=b.mix_csa_event||function(a){try{var e=b.mix_csa_internal_key(a,["producerId"])}catch(d){return P.logError(d,"MIX C005","WARN",void 0),function(){}}try{return b.mix_csa_internal("Events",e,a)}catch(d){return P.logError(d,"MIX C004","WARN",e),function(){}}};b.mix_csa=b.mix_csa||function(a,e){try{e=e||"";var d=document.querySelectorAll(a);if(1<d.length)for(var g=0;g<d.length;g++){if(d[g].querySelector(e)){var c=d[g];break}}else 1===d.length&&(c=d[0]);if(!c)throw Error(" ");
return b.mix_csa_internal("Content",a,{element:c})}catch(f){return P.logError(f,"MIX C004","WARN",a),function(){}}}})(window);
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('sp.load.js').execute(function() {
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://m.media-amazon.com/images/I/61ZS63EQSsL.js?AUIClients/AmazonUIjQuery');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://m.media-amazon.com/images/I/11Y+5x+kkTL._RC|51Am7NcREVL.js,11yKORv-GTL.js,11GgN1+C7hL.js,01+z+uIeJ-L.js,01VRMV3FBdL.js,21SDJtBU-PL.js,012FVc3131L.js,11rRjDLdAVL.js,516j7qaWchL.js,11kWu3cNjYL.js,11wr1I7-WYL.js,11OREnu1epL.js,11Wm6BwZ+6L.js,21ssiLNIZvL.js,0190vxtlzcL.js,51+N26vFcBL.js,01JYHc2oIlL.js,31nfKXylf6L.js,01ezj5Rkz1L.js,11bEz2VIYrL.js,31o2NGTXThL.js,01rpauTep4L.js,01XC3MnuvfL.js_.js?AUIClients/AmazonUI&MFdCk5El#567364-T1.432724-T1.577970-T1');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://m.media-amazon.com/images/I/51EIwpasq4L.js?AUIClients/CardJsRuntimeBuzzCopyBuild');
});
</script>
<!-- sp:end-feature:aui-assets -->
<!-- sp:feature:nav-inline-css -->
<!-- NAVYAAN CSS -->

<style type="text/css">
.nav-sprite-v1 .nav-sprite, .nav-sprite-v1 .nav-icon {
  background-image: url(https://m.media-amazon.com/images/G/31/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405936311_.png);
  background-position: 0 1000px;
  background-repeat: repeat-x;
}
.nav-spinner {
  background-image: url(https://m.media-amazon.com/images/G/31/javascripts/lib/popover/images/snake._CB485935600_.gif);
  background-position: center center;
  background-repeat: no-repeat;
}
.nav-timeline-icon, .nav-access-image, .nav-timeline-prime-icon {
  background-image: url(https://m.media-amazon.com/images/G/31/gno/sprites/timeline_sprite_1x._CB439943932_.png);
  background-repeat: no-repeat;
}
</style>
<link rel="stylesheet" href="https://images-eu.ssl-images-amazon.com/images/I/41H4XraWzVL._RC|71a3cNe7BIL.css,41u7Uj+4jbL.css,11OsNOdrK6L.css,31yYV8flaYL.css,313Ydl5aIRL.css,21MKjoYL8wL.css,41yQj5y2obL.css,110Nj+wUGYL.css,31OvHRW+XiL.css,01R53xsjpjL.css,11iUHDm4--L.css,41yKpEQVJkL.css,01YWmXMYw8L.css_.css?AUIClients/NavDesktopUberAsset&tMisNZxb#desktop.in.427118-T3.310484-T1.472106-T1" />
<!-- sp:end-feature:nav-inline-css -->
<!-- sp:feature:host-assets -->
<!---->
<span id="cr-state-object" data-state='{"asin":"B08L5VRVTD","deviceType":"desktop","contextId":"","reviewCommentsAjaxUrl":"/hz/reviews-render/ajax/comment/get/","reviewCommentSubmissionAjaxUrl":"/hz/reviews-render/ajax/comment/submit/","approvedAuthorAjaxUrl":"/hz/reviews-render/ajax/approved-author/get/","reviewsAjaxUrl":"/hz/reviews-render/ajax/reviews/get/","medleyReviewsAjaxUrl":"","reviewerType":"avp_only_reviews","formatType":"current_format","filterByKeyword":"","filterByLanguage":"","filterByStar":"","filterByHeight":"","filterByWeight":"","filterByAge":"","showLanguageFilter":false,"showHeightFilter":false,"showAgeFilter":false,"languageOfPreference":"en_IN","isCardTreatmentEnabled":false,"lazyWidgetLoaderBufferPixels":"1000","lazyWidgetLoaderDelayBeforeTriggering":"5000","lazyWidgetLoaderUrl":"/hz/reviews-render/ajax/lazy-widgets/stream","lazyWidgetCsrfToken":"hIE0LjYCOg3QzMoNq%2FdVxDBinlzb30Wf4xQd5wBlgdj9AAAAAGRDx%2FcAAAAB","lazyWidgetDomainWhitelist":["amazon.com","amazon.ca","amazon.com.mx","amazon.com.br","amazon.cl","amazon.com.co","amazon.co.uk","amazon.de","amazon.it","amazon.sa","amazon.com.tr","amazon.es","amazon.fr","amazon.in","amazon.ae","amazon.nl","amazon.se","amazon.pl","amazon.eg","amazon.co.za","amazon.com.be","amazon.com.ng","amazon.co.jp","amazon.com.au","amazon.sg","amazon.cn"],"signinUrl":"https://www.amazon.in/ap/signin?openid.return_to\u003dhttps%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%3Fie%3DUTF8%26reviewerType%3Davp_only_reviews%26formatType%3Dcurrent_format\u0026openid.identity\u003dhttp%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select\u0026openid.assoc_handle\u003dinflex\u0026openid.mode\u003dcheckid_setup\u0026marketPlaceId\u003dA21TJRUUN4KGV\u0026language\u003den\u0026openid.claimed_id\u003dhttp%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select\u0026openid.ns\u003dhttp%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0","reftagTriggerUrl":"/hz/reviews-render/ajax/reftag-trigger","mobileImageGalleryUrl":"","productInfoUrl":"/hz/reviews-render/ajax/product-info/get/","disableScroll":false,"marketplaceId":"A21TJRUUN4KGV","locale":"en_IN"}'></span>
<link rel="stylesheet" href="https://images-eu.ssl-images-amazon.com/images/I/01STrEog8JL._RC|017IiNKULqL.css,01LKsGfpclL.css,41V7rn1NJUL.css,017IH9bX79L.css,11hlEWdpPvL.css,41y14qLm1eL.css_.css?AUIClients/DesktopRemoteARPMetaAsset&Ct5DXiVO#622182-T2.647640-T1.569585-T1.569718-T1.386124-T1" />
<script>
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-eu.ssl-images-amazon.com/images/I/41mZH03vbIL._RC|31p6M2WZFzL.js,11KGVmb0nxL.js,41uK3DtcmfL.js,41Ul1U+eUaL.js,31yCl0u2BnL.js,61pfqC7ku3L.js,41l6Ts6x3oL.js_.js?AUIClients/DesktopRemoteARPMetaAsset&b8hGKle5#622182-T2.647640-T1.386124-T1');
</script>
<meta name="description" content="Find helpful customer reviews and review ratings for Apple iPhone 12 (256GB) - White at Amazon.com.  Read honest and unbiased product reviews from our users." />
<meta name="keywords" content="Review, Reviews, Rating, Ratings, Consumer Review, Consumer Reviews, Product Review, Product Reviews, Customer Review, Customer Reviews, Review Rating, Review Ratings, Amazon.com" />
<meta name="robots" content="noindex, nofollow" />
<link rel="canonical" href="https://www.amazon.in/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD" />

<title>Amazon.in:Customer reviews: Apple iPhone 12 (256GB) - White</title>
<!--&&&Portal&Delimiter&&&--><!-- sp:end-feature:host-assets -->
<!-- sp:feature:csm:head-close -->
<script type='text/javascript'>
window.ue_ihe = (window.ue_ihe || 0) + 1;
if (window.ue_ihe === 1) {
(function(c){c&&1===c.ue_jsmtf&&"object"===typeof c.P&&"function"===typeof c.P.when&&c.P.when("mshop-interactions").execute(function(e){"object"===typeof e&&"function"===typeof e.addListener&&e.addListener(function(b){"object"===typeof b&&"ORIGIN"===b.dataSource&&"number"===typeof b.clickTime&&"object"===typeof b.events&&"number"===typeof b.events.pageVisible&&(c.ue_jsmtf_interaction={pv:b.events.pageVisible,ct:b.clickTime})})})})(ue_csm);
(function(c,e,b){function m(a){f||(f=d[a.type].id,"undefined"===typeof a.clientX?(h=a.pageX,k=a.pageY):(h=a.clientX,k=a.clientY),2!=f||l&&(l!=h||n!=k)?(r(),g.isl&&e.setTimeout(function(){p("at",g.id)},0)):(l=h,n=k,f=0))}function r(){for(var a in d)d.hasOwnProperty(a)&&g.detach(a,m,d[a].parent)}function s(){for(var a in d)d.hasOwnProperty(a)&&g.attach(a,m,d[a].parent)}function t(){var a="";!q&&f&&(q=1,a+="&ui="+f);return a}var g=c.ue,p=c.uex,q=0,f=0,l,n,h,k,d={click:{id:1,parent:b},mousemove:{id:2,
parent:b},scroll:{id:3,parent:e},keydown:{id:4,parent:b}};g&&p&&(s(),g._ui=t)})(ue_csm,window,document);


(function(s,l){function m(b,e,c){c=c||new Date(+new Date+t);c="expires="+c.toUTCString();n.cookie=b+"="+e+";"+c+";path=/"}function p(b){b+="=";for(var e=n.cookie.split(";"),c=0;c<e.length;c++){for(var a=e[c];" "==a.charAt(0);)a=a.substring(1);if(0===a.indexOf(b))return decodeURIComponent(a.substring(b.length,a.length))}return""}function q(b,e,c){if(!e)return b;-1<b.indexOf("{")&&(b="");for(var a=b.split("&"),f,d=!1,h=!1,g=0;g<a.length;g++)f=a[g].split(":"),f[0]==e?(!c||d?a.splice(g,1):(f[1]=c,a[g]=
f.join(":")),h=d=!0):2>f.length&&(a.splice(g,1),h=!0);h&&(b=a.join("&"));!d&&c&&(0<b.length&&(b+="&"),b+=e+":"+c);return b}var k=s.ue||{},t=3024E7,n=ue_csm.document||l.document,r=null,d;a:{try{d=l.localStorage;break a}catch(u){}d=void 0}k.count&&k.count("csm.cookieSize",document.cookie.length);k.cookie={get:p,set:m,updateCsmHit:function(b,e,c){try{var a;if(!(a=r)){var f;a:{try{if(d&&d.getItem){f=d.getItem("csm-hit");break a}}catch(k){}f=void 0}a=f||p("csm-hit")||"{}"}a=q(a,b,e);r=a=q(a,"t",+new Date);
try{d&&d.setItem&&d.setItem("csm-hit",a)}catch(h){}m("csm-hit",a,c)}catch(g){"function"==typeof l.ueLogError&&ueLogError(Error("Cookie manager: "+g.message),{logLevel:"WARN"})}}}})(ue_csm,window);


(function(l,e){function c(b){b="";var c=a.isBFT?"b":"s",d=""+a.oid,g=""+a.lid,h=d;d!=g&&20==g.length&&(c+="a",h+="-"+g);a.tabid&&(b=a.tabid+"+");b+=c+"-"+h;b!=f&&100>b.length&&(f=b,a.cookie?a.cookie.updateCsmHit(m,b+("|"+ +new Date)):e.cookie="csm-hit="+b+("|"+ +new Date)+n+"; path=/")}function p(){f=0}function d(b){!0===e[a.pageViz.propHid]?f=0:!1===e[a.pageViz.propHid]&&c({type:"visible"})}var n="; expires="+(new Date(+new Date+6048E5)).toGMTString(),m="tb",f,a=l.ue||{},k=a.pageViz&&a.pageViz.event&&
a.pageViz.propHid;a.attach&&(a.attach("click",c),a.attach("keyup",c),k||(a.attach("focus",c),a.attach("blur",p)),k&&(a.attach(a.pageViz.event,d,e),d({})));a.aftb=1})(ue_csm,ue_csm.document);


ue_csm.ue.stub(ue,"impression");


ue.stub(ue,"trigger");


if(window.ue&&uet) { uet('bb'); }

}
</script>
<script>window.ue && ue.count && ue.count('CSMLibrarySize', 3172)</script>
<!-- sp:end-feature:csm:head-close -->
<!-- sp:feature:head-close -->
<script>
window.P && P.register('bb');
if (typeof ues === 'function') {
  ues('t0', 'portal-bb', new Date());
  ues('ctb', 'portal-bb', 1);
}
</script>
</head><!-- sp:end-feature:head-close -->
<!-- sp:feature:start-body -->
<body class="a-aui_72554-c a-aui_accordion_a11y_role_354025-t1 a-aui_killswitch_csa_logger_372963-c a-aui_pci_risk_banner_210084-c a-aui_preload_261698-c a-aui_rel_noreferrer_noopener_309527-c a-aui_template_weblab_cache_333406-c a-aui_tnr_v2_180836-c"><div id="a-page"><script type="a-state" data-a-state="{&quot;key&quot;:&quot;a-wlab-states&quot;}">{"AUI_TNR_V2_180836":"C","AUI_ACCORDION_A11Y_ROLE_354025":"T1","AUI_PRELOAD_261698":"C","AUI_TEMPLATE_WEBLAB_CACHE_333406":"C","AUI_72554":"C","AUI_KILLSWITCH_CSA_LOGGER_372963":"C","AUI_REL_NOREFERRER_NOOPENER_309527":"C","AUI_PCI_RISK_BANNER_210084":"C"}</script><script>typeof uex === 'function' && uex('ld', 'portal-bb', {wb: 1})</script><!-- sp:end-feature:start-body -->
<!-- sp:feature:csm:body-open -->


<script>
!function(){function n(n,t){var r=i(n);return t&&(r=r("instance",t)),r}var r=[],c=0,i=function(t){return function(){var n=c++;return r.push([t,[].slice.call(arguments,0),n,{time:Date.now()}]),i(n)}};n._s=r,this.csa=n}();;
csa('Config', {"ContentInteractionsSummary.FlushInterval":5000});
if (window.csa) {
    csa("Config", {
        'Application': 'Retail:Prod:www.amazon.in',
        'Events.Namespace': 'csa',
        'ObfuscatedMarketplaceId': 'A21TJRUUN4KGV',
        'Events.SushiEndpoint': 'https://unagi.amazon.in/1/events/com.amazon.csm.csa.prod',
        'CacheDetection.RequestID': "RZ67A764XT8VEYCF2P53",
        'CacheDetection.Callback': window.ue && ue.reset,
        'LCP.elementDedup': 1
    });

    csa("Events")("setEntity", {
        page: {requestId: "RZ67A764XT8VEYCF2P53", meaningful: "interactive"},
        session: {id: "257-4714000-6327435"}
    });
}
!function(r){var i,e,o="splice",u=r.csa,f={},c={},a=r.csa._s,s=0,l=0,g=-1,h={},v={},d={},n=Object.keys,p=function(){};function t(n,t){return u(n,t)}function m(n,t){var r=c[n]||{};k(r,t),c[n]=r,l++,S(U,0)}function w(n,t,r){var i=!0;return t=D(t),r&&r.buffered&&(i=(d[n]||[]).every(function(n){return!1!==t(n)})),i?(h[n]||(h[n]=[]),h[n].push(t),function(){!function(n,t){var r=h[n];r&&r[o](r.indexOf(t),1)}(n,t)}):p}function b(n,t){if(t=D(t),n in v)return t(v[n]),p;return w(n,function(n){return t(n),!1})}function y(n,t){if(u("Errors")("logError",n),f.DEBUG)throw t||n}function E(){return Math.abs(4294967295*Math.random()|0).toString(36)}function D(n,t){return function(){try{return n.apply(this,arguments)}catch(n){y(n.message||n,n)}}}function S(n,t){return r.setTimeout(D(n),t)}function U(){for(var n=0;n<a.length;){var t=a[n],r=t[0]in c;if(!r&&!e)return void(s=t.length);r?(a[o](s=n,1),I(t)):n++}g=l}function I(n){var arguments,t=c[n[0]],r=(arguments=n[1])[0];if(!t||!t[r])return y("Undefined function: "+t+"/"+r);i=n[3],c[n[2]]=t[r].apply(t,arguments.slice(1))||{},i=0}function O(){e=1,U()}function k(t,r){n(r).forEach(function(n){t[n]=r[n]})}b("$beforeunload",O),m("Config",{instance:function(n){k(f,n)}}),u.plugin=D(function(n){n(t)}),t.config=f,t.register=m,t.on=w,t.once=b,t.blank=p,t.emit=function(n,t,r){for(var i=h[n]||[],e=0;e<i.length;)!1===i[e](t)?i[o](e,1):e++;v[n]=t||{},r&&r.buffered&&(d[n]||(d[n]=[]),100<=d[n].length&&d[n].shift(),d[n].push(t||{}))},t.UUID=function(){return[E(),E(),E(),E()].join("-")},t.time=function(n){var t=i?new Date(i.time):new Date;return"ISO"===n?t.toISOString():t.getTime()},t.error=y,t.warn=function(n,t){if(u("Errors")("logWarn",n),f.DEBUG)throw t||n},t.exec=D,t.timeout=S,t.interval=function(n,t){return r.setInterval(D(n),t)},(t.global=r).csa._s.push=function(n){n[0]in c&&(!a.length||e)?(I(n),a.length&&g!==l&&U()):a[o](s++,0,n)},U(),S(function(){S(O,f.SkipMissingPluginsTimeout||5e3)},1)}("undefined"!=typeof window?window:global);csa.plugin(function(o){var f="addEventListener",e="requestAnimationFrame",t=o.exec,r=o.global,u=o.on;o.raf=function(n){if(r[e])return r[e](t(n))},o.on=function(n,e,t,r){if(n&&"function"==typeof n[f]){var i=o.exec(t);return n[f](e,i,r),function(){n.removeEventListener(e,i,r)}}return"string"==typeof n?u(n,e,t,r):o.blank}});csa.plugin(function(o){var t,n,r={},e="localStorage",c="sessionStorage",a="local",i="session",u=o.exec;function s(e,t){var n;try{r[t]=!!(n=o.global[e]),n=n||{}}catch(e){r[t]=!(n={})}return n}function f(){t=t||s(e,a),n=n||s(c,i)}function l(e){return e&&e[i]?n:t}o.store=u(function(e,t,n){f();var o=l(n);return e?t?void(o[e]=t):o[e]:Object.keys(o)}),o.storageSupport=u(function(){return f(),r}),o.deleteStored=u(function(e,t){f();var n=l(t);if("function"==typeof e)for(var o in n)n.hasOwnProperty(o)&&e(o,n[o])&&delete n[o];else delete n[e]})});csa.plugin(function(n){n.types={ovl:function(n){var r=[];if(n)for(var i in n)n.hasOwnProperty(i)&&r.push(n[i]);return r}}});csa.plugin(function(i){function e(n){return function(e){i("Metrics",{producerId:"csa",dimensions:{message:e}})("recordMetric",n,1)}}function n(r){var o,t,l=i("Events",{producerId:r.producerId}),u=["name","type","csm","adb"],c={url:"pageURL",file:"f",line:"l",column:"c"};this.log=function(e){if(!function(e){if(!e)return!0;for(var n in e)return!1;return!0}(e)){var n=r.logOptions||{ent:{page:["pageType","subPageType","requestId"]}};l("log",function(n){return o=i.UUID(),t={messageId:o,schemaId:r.schemaId||"<ns>.Error.4",errorMessage:n.m||null,attribution:n.attribution||null,logLevel:"FATAL",url:null,file:null,line:null,column:null,stack:n.s||[],context:{},surfaceInfo:{}},n.logLevel&&(t.logLevel=""+n.logLevel),u.forEach(function(e){n[e]&&(t.context[e]=n[e])}),"INFO"===n.logLevel||Object.keys(c).forEach(function(e){"number"!=typeof n[c[e]]&&"string"!=typeof n[c[e]]||(t[e]=""+n[c[e]])}),t}(e),n)}}}i.register("Errors",{instance:function(e){return new n(e||{})},logError:e("jsError"),logWarn:e("jsWarn")})});csa.plugin(function(o){var r,e,n,t,a,i="function",u="willDisappear",f="$app.",p="$document.",c="focus",s="blur",d="active",l="resign",$=o.global,b=o.exec,m=o.config["Transport.AnonymizeRequests"]||!1,g=o("Events"),h=$.location,v=$.document||{},y=$.P||{},P=(($.performance||{}).navigation||{}).type,w=o.on,k=o.emit,E=v.hidden,T={};h&&v&&(w($,"beforeunload",D),w($,"pagehide",D),w(v,"visibilitychange",R(p,function(){return v.visibilityState||"unknown"})),w(v,c,R(p+c)),w(v,s,R(p+s)),y.when&&y.when("mash").execute(function(e){e&&(w(e,"appPause",R(f+"pause")),w(e,"appResume",R(f+"resume")),R(f+"deviceready")(),$.cordova&&$.cordova.platformId&&R(f+cordova.platformId)(),w(v,d,R(f+d)),w(v,l,R(f+l)))}),e=$.app||{},n=b(function(){k(f+"willDisappear"),D()}),a=typeof(t=e[u])==i,e[u]=b(function(){n(),a&&t()}),$.app||($.app=e),"complete"===v.readyState?A():w($,"load",A),E?S():x(),o.on("$app.blur",S),o.on("$app.focus",x),o.on("$document.blur",S),o.on("$document.focus",x),o.on("$document.hidden",S),o.on("$document.visible",x),o.register("SPA",{newPage:I}),I({transitionType:{0:"hard",1:"refresh",2:"back-button"}[P]||"unknown"}));function I(n,e){var t=!!r,a=(e=e||{}).keepPageAttributes;t&&(k("$beforePageTransition"),k("$pageTransition")),t&&!a&&g("removeEntity","page"),r=o.UUID(),a?T.id=r:T={schemaId:"<ns>.PageEntity.1",id:r,url:m?h.href.split("?")[0]:h.href,server:h.hostname,path:h.pathname,referrer:m?v.referrer.split("?")[0]:v.referrer,title:v.title},Object.keys(n||{}).forEach(function(e){T[e]=n[e]}),g("setEntity",{page:T}),k("$pageChange",T,{buffered:1}),t&&k("$afterPageTransition")}function A(){k("$load"),k("$ready"),k("$afterload")}function D(){k("$ready"),k("$beforeunload"),k("$unload"),k("$afterunload")}function S(){E||(k("$visible",!1,{buffered:1}),E=!0)}function x(){E&&(k("$visible",!0,{buffered:1}),E=!1)}function R(n,t){return b(function(){var e=typeof t==i?n+t():n;k(e)})}});csa.plugin(function(c){var e="Events",t="UNKNOWN",s="id",a="all",n="messageId",i="timestamp",u="producerId",o="application",r="obfuscatedMarketplaceId",f="entities",d="schemaId",l="version",p="attributes",v="<ns>",g="session",h=c.config,m=(c.global.location||{}).host,y=h[e+".Namespace"]||"csa_other",I=h.Application||"Other"+(m?":"+m:""),b=h["Transport.AnonymizeRequests"]||!1,O=c("Transport"),E={},U=function(e,t){Object.keys(e).forEach(t)};function A(n,i,o){U(i,function(e){var t=o===a||(o||{})[e];e in n||(n[e]={version:1,id:i[e][s]||c.UUID()}),N(n[e],i[e],t)})}function N(t,n,i){U(n,function(e){!function(e,t,n){return"string"!=typeof t&&e!==l?c.error("Attribute is not of type string: "+e):!0===n||1===n||(e===s||!!~(n||[]).indexOf(e))}(e,n[e],i)||(t[e]=n[e])})}function S(o,e,r){U(e,function(e){var t=o[e];if(t[d]){var n={},i={};n[s]=t[s],n[u]=t[u]||r,n[d]=t[d],n[l]=t[l]++,n[p]=i,k(n),N(i,t,1),w(i),O("log",n)}})}function k(e){e[i]=function(e){return"number"==typeof e&&(e=new Date(e).toISOString()),e||c.time("ISO")}(e[i]),e[n]=e[n]||c.UUID(),e[o]=I,e[r]=h.ObfuscatedMarketplaceId||t,e[d]=e[d].replace(v,y)}function w(e){delete e[l],delete e[d],delete e[u]}function D(o){var r={};this.log=function(e,t){var n={},i=(t||{}).ent;return e?"string"!=typeof e[d]?c.error("A valid schema id is required for the event"):(k(e),A(n,E,i),A(n,r,i),A(n,e[f]||{},i),U(n,function(e){w(n[e])}),e[u]=o[u],e[f]=n,void O("log",e,t)):c.error("The event cannot be undefined")},this.setEntity=function(e){b&&delete e[g],A(r,e,a),S(r,e,o[u])}}h["KillSwitch."+e]||c.register(e,{setEntity:function(e){b&&delete e[g],A(E,e,a),S(E,e,"csa")},removeEntity:function(e){delete E[e]},instance:function(e){return new D(e)}})});csa.plugin(function(s){var c,g="Transport",l="post",f="preflight",r="csa.cajun.",i="store",a="deleteStored",u="sendBeacon",t="__merge",e="messageId",n=".FlushInterval",o=0,d=s.config[g+".BufferSize"]||2e3,h=s.config[g+".RetryDelay"]||1500,p=s.config[g+".AnonymizeRequests"]||!1,v={},y=0,m=[],E=s.global,R=E.document,b=s.timeout,k=E.Object.keys,w=s.config[g+n]||5e3,I=w,O=s.config[g+n+".BackoffFactor"]||1,S=s.config[g+n+".BackoffLimit"]||3e4,B=0;function T(n){if(864e5<s.time()-+new Date(n.timestamp))return s.warn("Event is too old: "+n);y<d&&(n[e]in v||(v[n[e]]=n,y++),"function"==typeof n[t]&&n[t](v[n[e]]),!B&&o&&(B=b(q,function(){var n=I;return I=Math.min(n*O,S),n}())))}function q(){m.forEach(function(e){var o=[];k(v).forEach(function(n){var t=v[n];e.accepts(t)&&o.push(t)}),o.length&&(e.chunks?e.chunks(o).forEach(function(n){D(e,n)}):D(e,o))}),v={},B=0}function D(t,e){function o(){s[a](r+n)}var n=s.UUID();s[i](r+n,JSON.stringify(e)),[function(n,t,e){var o=E.navigator||{},r=E.cordova||{};if(p)return 0;if(!o[u]||!n[l])return 0;n[f]&&r&&"ios"===r.platformId&&!c&&((new Image).src=n[f]().url,c=1);var i=n[l](t);if(!i.type&&o[u](i.url,i.body))return e(),1},function(n,t,e){if(!n[l])return 0;var o=n[l](t),r=o.url,i=o.body,c=o.type,f=new XMLHttpRequest,a=0;function u(n,t,e){f.open("POST",n),f.withCredentials=!p,e&&f.setRequestHeader("Content-Type",e),f.send(t)}return f.onload=function(){f.status<299?e():s.config[g+".XHRRetries"]&&a<3&&b(function(){u(r,i,c)},++a*h)},u(r,i,c),1}].some(function(n){try{return n(t,e,o)}catch(n){}})}k&&(s.once("$afterload",function(){o=1,function(e){(s[i]()||[]).forEach(function(n){if(!n.indexOf(r))try{var t=s[i](n);s[a](n),JSON.parse(t).forEach(e)}catch(n){s.error(n)}})}(T),s.on(R,"visibilitychange",q,!1),q()}),s.once("$afterunload",function(){o=1,q()}),s.on("$afterPageTransition",function(){y=0,I=w}),s.register(g,{log:T,register:function(n){m.push(n)}}))});csa.plugin(function(n){var r=n.config["Events.SushiEndpoint"];n("Transport")("register",{accepts:function(n){return n.schemaId},post:function(n){var t=n.map(function(n){return{data:n}});return{url:r,body:JSON.stringify({events:t})}},preflight:function(){var n,t=/\/\/(.*?)\//.exec(r);return t&&t[1]&&(n="https://"+t[1]+"/ping"),{url:n}},chunks:function(n){for(var t=[];500<n.length;)t.push(n.splice(0,500));return t.push(n),t}})});csa.plugin(function(n){var t,a,o,r,e=n.config,i="PageViews",d=e[i+".ImpressionMinimumTime"]||1e3,s="hidden",c="innerHeight",g="innerWidth",l="renderedTo",f=l+"Viewed",m=l+"Meaningful",u=l+"Impressed",p=1,v=2,h=3,w=4,y=5,P="loaded",I=7,T=8,b=n.global,E=n.on,V=n("Events",{producerId:"csa"}),$=b.document,M={},S={},H=y;function K(e){if(!M[I]){var i;if(M[e]=n.time(),e!==h&&e!==P||(t=t||M[e]),t&&H===w)a=a||M[e],(i={})[m]=t-o,i[f]=a-o,R("PageView.4",i),r=r||n.timeout(j,d);if(e!==y&&e!==p&&e!==v||(clearTimeout(r),r=0),e!==p&&e!==v||R("PageRender.3",{transitionType:e===p?"hard":"soft"}),e===I)(i={})[m]=t-o,i[f]=a-o,i[u]=M[e]-o,R("PageImpressed.2",i)}}function R(e,i){S[e]||(i.schemaId="<ns>."+e,V("log",i,{ent:"all"}),S[e]=1)}function W(){0===b[c]&&0===b[g]?(H=T,n("Events")("setEntity",{page:{viewport:"hidden-iframe"}})):H=$[s]?y:w,K(H)}function j(){K(I),r=0}function k(){var e=o?v:p;M={},S={},a=t=0,o=n.time(),K(e),W()}function q(){var e=$.readyState;"interactive"===e&&K(h),"complete"===e&&K(P)}e["KillSwitch."+i]||($&&void 0!==$[s]?(k(),E($,"visibilitychange",W,!1),E($,"readystatechange",q,!1),E("$afterPageTransition",k),E("$timing:loaded",q),n.once("$load",q)):n.warn("Page visibility not supported"))});csa.plugin(function(c){var s=c.config["Interactions.ParentChainLength"]||35,e="click",r="touches",f="timeStamp",o="length",u="pageX",g="pageY",p="pageXOffset",h="pageYOffset",m=250,v=5,d=200,l=.5,t={capture:!0,passive:!0},X=c.global,Y=c.emit,n=c.on,x=X.Math.abs,a=(X.document||{}).documentElement||{},y={x:0,y:0,t:0,sX:0,sY:0},N={x:0,y:0,t:0,sX:0,sY:0};function b(t){if(t.id)return"//*[@id='"+t.id+"']";var e=function(t){var e,n=1;for(e=t.previousSibling;e;e=e.previousSibling)e.nodeName===t.nodeName&&(n+=1);return n}(t),n=t.nodeName;return 1!==e&&(n+="["+e+"]"),t.parentNode&&(n=b(t.parentNode)+"/"+n),n}function I(t,e,n){var a=c("Content",{target:n}),i={schemaId:"<ns>.ContentInteraction.1",interaction:t,interactionData:e,messageId:c.UUID()};if(n){var r=b(n);r&&(i.attribution=r);var o=function(t){for(var e=t,n=e.tagName,a=!1,i=t?t.href:null,r=0;r<s;r++){if(!e||!e.parentElement){a=!0;break}n=(e=e.parentElement).tagName+"/"+n,i=i||e.href}return a||(n=".../"+n),{pc:n,hr:i}}(n);o.pc&&(i.interactionData.parentChain=o.pc),o.hr&&(i.interactionData.href=o.hr)}a("log",i),Y("$content.interaction",i)}function i(t){I(e,{interactionX:""+t.pageX,interactionY:""+t.pageY},t.target)}function C(t){if(t&&t[r]&&1===t[r][o]){var e=t[r][0];N=y={e:t.target,x:e[u],y:e[g],t:t[f],sX:X[p],sY:X[h]}}}function D(t){if(t&&t[r]&&1===t[r][o]&&y&&N){var e=t[r][0],n=t[f],a=n-N.t,i={e:t.target,x:e[u],y:e[g],t:n,sX:X[p],sY:X[h]};N=i,d<=a&&(y=i)}}function E(t){if(t){var e=x(y.x-N.x),n=x(y.y-N.y),a=x(y.sX-N.sX),i=x(y.sY-N.sY),r=t[f]-y.t;if(m<1e3*e/r&&v<e||m<1e3*n/r&&v<n){var o=n<e;o&&a&&e*l<=a||!o&&i&&n*l<=i||I((o?"horizontal":"vertical")+"-swipe",{interactionX:""+y.x,interactionY:""+y.y,endX:""+N.x,endY:""+N.y},y.e)}}}n(a,e,i,t),n(a,"touchstart",C,t),n(a,"touchmove",D,t),n(a,"touchend",E,t)});csa.plugin(function(r){var a,o,t,e="MutationObserver",c="observe",n="disconnect",s="mutObs",f="_csa_flt",l="_csa_llt",b="_csa_mr",d="_csa_mi",m="lastChild",p="length",_={childList:!0,subtree:!0},g=10,h=4,u=r.global,i=u.document,v=i.body||i.documentElement,y=Date.now,O=[],k=[],w=[],L=0,B=0,I=0,M=1,Y=[],$=[],x=0,A=r.blank,C={buffered:1},D=0;function E(e){r.global.ue_csa_ss_tag||r.emit("$csmTag:"+e,0,C)}y&&u[e]?(E(s+"Yes"),L=0,o=new u[e](N),(t=new u[e](F))[c](v,{attributes:!0,subtree:!0,attributeFilter:["src"],attributeOldValue:!0}),A=r.on(u,"scroll",S,{passive:!0}),r.once("$ready",V),M&&T(),r.register("SpeedIndexBuffers",{getBuffers:function(e){e&&(V(),S(),e(L,Y,O,k,w),o&&o[n](),t&&t[n](),A())},registerListener:function(e){a=e},replayModuleIsLive:function(){r.raf(V)}})):E(s+"No");function F(e){O.push({t:y(),m:e})}function N(e){k.push({t:y(),m:e}),D||E(s+"Active"),D=I=1,a&&a()}function S(){I&&(w.push({t:y(),y:B}),B=u.pageYOffset,I=0)}function T(){for(var e=v,t=y(),n=[],s=[],u=0,i=0;e;)e[f]?++u:(e[f]=t,n.push(e),i=1),s[p]<h&&s.push(e),e[d]=x,e[l]=t,e=e[m];i&&(u<$[p]&&function(e){for(var t=e,n=$[p];t<n;t++){var s=$[t];if(s){if(s[b])break;if(s[d]<x){s[b]=1,o[c](s,_);break}}}}(u),$=s,Y.push({t:t,m:n}),++x,I=i,a&&a()),M&&(i?r.raf(T):r.timeout(T,g))}function V(){M&&(M=0,T(),o[c](v,_))}});

var ue_csa_ss_tag = false;
csa.plugin(function(b){var a=b.global,e=a.uet,f=a.uex,c=a.ue,d=a.Object,g={largestContentfulPaint:"lcp",speedIndex:"si",atfSpeedIndex:"atfsi",visuallyLoaded50:"vl50",visuallyLoaded90:"vl90",visuallyLoaded100:"vl100"},k="perfNo perfYes browserQuiteFn browserQuiteUd browserQuiteLd browserQuiteMut mutObsNo mutObsYes mutObsActive startVL endVL".split(" ");b&&e&&f&&d.keys&&c&&(d.keys(g).forEach(function(h){b.on("$timing:"+h,function(a){var b=g[h];if(c.isl){var d="csa:"+b;e(b,d,void 0,a);f("at",d)}else e(b,
void 0,void 0,a)})}),a.ue_csa_ss_tag||k.forEach(function(a){b.on("$csmTag:"+a,function(){c.tag&&c.tag(a);c.isl&&f("at","csa:"+a)},{buffered:1})}))});

</script>
<script>window.ue && ue.count && ue.count('CSMLibrarySize', 15800)</script>
<!-- sp:end-feature:csm:body-open -->
<!-- sp:feature:nav-inline-js -->
<!-- NAVYAAN JS -->

<script type="text/javascript">!function(n){function e(n,e){return{m:n,a:function(n){return[].slice.call(n)}(e)}}document.createElement("header");var r=function(n){function u(n,r,u){n[u]=function(){a._replay.push(r.concat(e(u,arguments)))}}var a={};return a._sourceName=n,a._replay=[],a.getNow=function(n,e){return e},a.when=function(){var n=[e("when",arguments)],r={};return u(r,n,"run"),u(r,n,"declare"),u(r,n,"publish"),u(r,n,"build"),r.depends=n,r.iff=function(){var r=n.concat([e("iff",arguments)]),a={};return u(a,r,"run"),u(a,r,"declare"),u(a,r,"publish"),u(a,r,"build"),a},r},u(a,[],"declare"),u(a,[],"build"),u(a,[],"publish"),u(a,[],"importEvent"),r._shims.push(a),a};r._shims=[],n.$Nav||(n.$Nav=r("rcx-nav")),n.$Nav.make||(n.$Nav.make=r)}(window)</script><script type="text/javascript">
$Nav.importEvent('navbarJS-beaconbelt');
$Nav.declare('img.sprite', {
  'png32': 'https://m.media-amazon.com/images/G/31/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405936311_.png',
  'png32-2x': 'https://m.media-amazon.com/images/G/31/gno/sprites/nav-sprite-global-2x-hm-dsk-reorg._CB405936311_.png'
});
$Nav.declare('img.timeline', {
  'timeline-icon-2x': 'https://m.media-amazon.com/images/G/31/gno/sprites/timeline_sprite_2x._CB443580981_.png'
});
window._navbarSpriteUrl = 'https://m.media-amazon.com/images/G/31/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405936311_.png';
$Nav.declare('img.pixel', 'https://m.media-amazon.com/images/G/31/x-locale/common/transparent-pixel._CB485934990_.gif');
</script>

<img src="https://m.media-amazon.com/images/G/31/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405936311_.png" style="display:none" alt=""/>
<script type="text/javascript">var nav_t_after_preload_sprite = + new Date();</script>
<script>
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('navCF').execute(function() {
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-eu.ssl-images-amazon.com/images/I/412HK5CgpXL._RC|71mLbqg5g8L.js,01F+A05ogQL.js,01phmzCOwJL.js,01eOvPdxG7L.js,71GecmAeHOL.js,41gNKoK0s7L.js,115pV8Rl02L.js,01+pnQJuQ0L.js,21rDHgaooIL.js,41rU9l+NGKL.js,51t-JTxfnwL.js,317BC63dC8L.js,11lEMI5MhIL.js,31c7Fn9h9gL.js,01LEzWzrPZL.js,01AqeWA7PKL.js_.js?AUIClients/NavDesktopUberAsset&pYZxqR4I#desktop.language-en.in.488400-T1.488413-T1.375680-T1.479940-T1.455533-T1.432287-T1.420134-T1.366740-T1.310484-T1.472106-T1');
});
</script>
<!-- sp:end-feature:nav-inline-js -->
<!-- sp:feature:nav-skeleton -->
<!-- sp:end-feature:nav-skeleton -->
<!-- sp:feature:navbar -->

<!--Pilu -->


  <!-- NAVYAAN -->











<!-- navmet initial definition -->



<script type='text/javascript'>
    if(window.navmet===undefined) {
      window.navmet=[];
      if (window.performance && window.performance.timing && window.ue_t0) {
        var t = window.performance.timing;
        var now = + new Date();
        window.navmet.basic = {
          'networkLatency': (t.responseStart - t.fetchStart),
          'navFirstPaint': (now - t.responseStart),
          'NavStart': (now - window.ue_t0)
        };
        window.navmet.push({key:"NavFirstPaintStart",end:+new Date(),begin:window.ue_t0});
      }
    }
    if (window.ue_t0) {
      window.navmet.push({key:"NavMainStart",end:+new Date(),begin:window.ue_t0});
    }
</script>




<script type='text/javascript'>window.navmet.tmp=+new Date();</script>
  <script type='text/javascript'>
    // Nav start should be logged at this place only if request is NOT progressively loaded.
    // For progressive loading case this metric is logged as part of skeleton.
    // Presence of skeleton signals that request is progressively loaded.
    if(!document.getElementById("navbar-skeleton")) {
      window.uet && uet('ns');
    }
    window._navbar = (function (o) {
      o.componentLoaded = o.loading = function(){};
      o.browsepromos = {};
      o.issPromos = [];
      return o;
    }(window._navbar || {}));
    window._navbar.declareOnLoad = function () { window.$Nav && $Nav.declare('page.load'); };
    if (window.addEventListener) {
      window.addEventListener("load", window._navbar.declareOnLoad, false);
    } else if (window.attachEvent) {
      window.attachEvent("onload", window._navbar.declareOnLoad);
    } else if (window.$Nav) {
      $Nav.when('page.domReady').run("OnloadFallbackSetup", function () {
        window._navbar.declareOnLoad();
      });
    }
    window.$Nav && $Nav.declare('logEvent.enabled',
      'false');

    window.$Nav && $Nav.declare('config.lightningDeals', {});
  </script>

    <style mark="aboveNavInjectionCSS" type="text/css">
      .nav-bluebeacon .nav-cobrand{background-image: url(https://images-eu.ssl-images-amazon.com/images/G/31/gno/images/irctc/IRCTC_Logo-dark-small.png);} div.navFooterLine{white-space:normal;} div.navFooterColHead{white-space:normal;} #nav-flyout-ewc .nav-flyout-buffer-left { display: none; } #nav-flyout-ewc .nav-flyout-buffer-right { display: none; } 
    </style>
    <script mark="aboveNavInjectionJS" type="text/javascript">
      try {
        window.$Nav && $Nav.when('$').run('defineIsArray', function(jQuery) { if(jQuery.isArray===undefined) { jQuery.isArray=function(param) { if(param.length===undefined) { return false; } return true; }; } }); window.$Nav && $Nav.when('$','$F','config','logEvent','panels','phoneHome','dataPanel','flyouts.renderPromo','flyouts.sloppyTrigger','flyouts.accessibility','util.mouseOut','util.onKey','debug.param').build('flyouts.buildSubPanels',function($,$F,config,logEvent,panels,phoneHome,dataPanel,renderPromo,createSloppyTrigger,a11yHandler,mouseOutUtility,onKey,debugParam){var flyoutDebug=debugParam('navFlyoutClick');return function(flyout,event){var linkKeys=[];$('.nav-item',flyout.elem()).each(function(){var $item=$(this);linkKeys.push({link:$item,panelKey:$item.attr('data-nav-panelkey')});});if(linkKeys.length===0){return;} var visible=false;var $parent=$('<div class=\'nav-subcats\'></div>').appendTo(flyout.elem());var panelGroup=flyout.getName()+'SubCats';var hideTimeout=null;var sloppyTrigger=createSloppyTrigger($parent);var showParent=function(){if(hideTimeout){clearTimeout(hideTimeout);hideTimeout=null;} if(visible){return;} var height=$('#nav-flyout-shopAll').height();$parent.css({'height': height});$parent.animate({width:'show'},{duration:200,complete:function(){$parent.css({overflow:'visible'});}});visible=true;};var hideParentNow=function(){$parent.stop().css({overflow:'hidden',display:'none',width:'auto',height:'auto'});panels.hideAll({group:panelGroup});visible=false;if(hideTimeout){clearTimeout(hideTimeout);hideTimeout=null;}};var hideParent=function(){if(!visible){return;} if(hideTimeout){clearTimeout(hideTimeout);hideTimeout=null;} hideTimeout=setTimeout(hideParentNow,10);};flyout.onHide(function(){sloppyTrigger.disable();hideParentNow();this.elem().hide();});var addPanel=function($link,panelKey){var panel=dataPanel({className:'nav-subcat',dataKey:panelKey,groups:[panelGroup],spinner:false,visible:false});if(!flyoutDebug){var mouseout=mouseOutUtility();mouseout.add(flyout.elem());mouseout.action(function(){panel.hide();});mouseout.enable();} var a11y=a11yHandler({link:$link,onEscape:function(){panel.hide();$link.focus();}});var logPanelInteraction=function(promoID,wlTriggers){var logNow=$F.once().on(function(){var panelEvent=$.extend({},event,{id:promoID});if(config.browsePromos&&!!config.browsePromos[promoID]){panelEvent.bp=1;} logEvent(panelEvent);phoneHome.trigger(wlTriggers);});if(panel.isVisible()&&panel.hasInteracted()){logNow();}else{panel.onInteract(logNow);}};panel.onData(function(data){renderPromo(data.promoID,panel.elem());logPanelInteraction(data.promoID,data.wlTriggers);});panel.onShow(function(){var columnCount=$('.nav-column',panel.elem()).length;panel.elem().addClass('nav-colcount-'+columnCount);showParent();var $subCatLinks=$('.nav-subcat-links > a',panel.elem());var length=$subCatLinks.length;if(length>0){var firstElementLeftPos=$subCatLinks.eq(0).offset().left;for(var i=1;i<length;i++){if(firstElementLeftPos===$subCatLinks.eq(i).offset().left){$subCatLinks.eq(i).addClass('nav_linestart');}} if($('span.nav-title.nav-item',panel.elem()).length===0){var catTitle=$.trim($link.html());catTitle=catTitle.replace(/ref=sa_menu_top/g,'ref=sa_menu');var $subPanelTitle=$('<span class=\'nav-title nav-item\'>'+ catTitle+'</span>');panel.elem().prepend($subPanelTitle);}} $link.addClass('nav-active');});panel.onHide(function(){$link.removeClass('nav-active');hideParent();a11y.disable();sloppyTrigger.disable();});panel.onShow(function(){a11y.elems($('a, area',panel.elem()));});sloppyTrigger.register($link,panel);if(flyoutDebug){$link.click(function(){if(panel.isVisible()){panel.hide();}else{panel.show();}});} var panelKeyHandler=onKey($link,function(){if(this.isEnter()||this.isSpace()){panel.show();}},'keydown',false);$link.focus(function(){panelKeyHandler.bind();}).blur(function(){panelKeyHandler.unbind();});panel.elem().appendTo($parent);};var hideParentAndResetTrigger=function(){hideParent();sloppyTrigger.disable();};for(var i=0;i<linkKeys.length;i++){var item=linkKeys[i];if(item.panelKey){addPanel(item.link,item.panelKey);}else{item.link.mouseover(hideParentAndResetTrigger);}}};});
      } catch ( err ) {
        if ( window.$Nav ) {
          window.$Nav.when('metrics', 'logUeError').run(function(metrics, log) {
            metrics.increment('NavJS:AboveNavInjection:error');
            log(err.toString(), {
              'attribution': 'rcx-nav',
              'logLevel': 'FATAL'
            });
          });
        }
      }
    </script>

  <noscript>
    <style type="text/css"><!--
      #navbar #nav-shop .nav-a:hover {
        color: #ff9900;
        text-decoration: underline;
      }
      #navbar #nav-search .nav-search-facade,
      #navbar #nav-tools .nav-icon,
      #navbar #nav-shop .nav-icon,
      #navbar #nav-subnav .nav-hasArrow .nav-arrow {
        display: none;
      }
      #navbar #nav-search .nav-search-submit,
      #navbar #nav-search .nav-search-scope {
        display: block;
      }
      #nav-search .nav-search-scope {
        padding: 0 5px;
      }
      #navbar #nav-search .nav-search-dropdown {
        position: relative;
        top: 5px;
        height: 23px;
        font-size: 14px;
        opacity: 1;
        filter: alpha(opacity = 100);
      }
    --></style>
 </noscript>
<script type='text/javascript'>window.navmet.push({key:'PreNav',end:+new Date(),begin:window.navmet.tmp});</script>

<a id='nav-top'></a>




<a id="skiplink" tabindex="0" class="skip-link">Skip to main content</a>

<script type='text/javascript'>window.navmet.tmp=+new Date();</script>
<!-- Navyaan Upnav -->
    <div id="nav-upnav" aria-hidden="true" >
      <!-- unw1 failed -->
      
    </div>
<script type='text/javascript'>window.navmet.push({key:'UpNav',end:+new Date(),begin:window.navmet.tmp});</script>


<script type='text/javascript'>window.navmet.main=+new Date();</script>



<header id="navbar-main" class = "nav-opt-sprite nav-flex nav-locale-in nav-lang-en nav-ssl nav-unrec nav-progressive-attribute">

   
  <div id='navbar' cel_widget_id='Navigation-desktop-navbar'
  role='navigation' class="nav-sprite-v1 celwidget nav-bluebeacon nav-a11y-t1 bold-focus-hover layout2 nav-flex layout3 layout3-alt nav-packard-glow hamburger nav-progressive-attribute">
    
    <div id='nav-belt'>
      <div class='nav-left'>
        <script type='text/javascript'>window.navmet.tmp=+new Date();</script>
  <div id="nav-logo" >
    <a href="/ref=nav_logo" id="nav-logo-sprites" class="nav-logo-link nav-progressive-attribute" aria-label="Amazon.in">
      <span class="nav-sprite nav-logo-base"></span>
      <span id="logo-ext" class="nav-sprite nav-logo-ext nav-progressive-content"></span>
      <span class="nav-logo-locale">.in</span>
    </a>
  </div>
<script type='text/javascript'>window.navmet.push({key:'Logo',end:+new Date(),begin:window.navmet.tmp});</script>
        
<div id="nav-global-location-slot">
    <span id="nav-global-location-data-modal-action" class="a-declarative nav-progressive-attribute" data-a-modal='{&quot;width&quot;:375, &quot;closeButton&quot;:&quot;false&quot;,&quot;popoverLabel&quot;:&quot;Choose your location&quot;, &quot;ajaxHeaders&quot;:{&quot;anti-csrftoken-a2z&quot;:&quot;gM82cr2fiJuFsMIJqCY2URb8BUYeNZujOryM7zUAAAAMAAAAAGRDx/dyYXcAAAAA;hB9R/xrmlYtSdzBL6kBhtmZvVc5iIBOMOcgoJzfhJoFZAAAAAGRDx/cAAAAB&quot;}, &quot;name&quot;:&quot;glow-modal&quot;, &quot;url&quot;:&quot;/portal-migration/hz/glow/get-rendered-address-selections?deviceType&#x3D;desktop&amp;pageType&#x3D;CustomerReviews&amp;storeContext&#x3D;NoStoreName&amp;actionSource&#x3D;desktop-modal&quot;, &quot;footer&quot;:null,&quot;header&quot;:&quot;Choose your location&quot;}' data-action="a-modal">
        <a id="nav-global-location-popover-link" class="nav-a nav-a-2 a-popover-trigger a-declarative nav-progressive-attribute" tabindex="0">
            <div class="nav-sprite nav-progressive-attribute" id="nav-packard-glow-loc-icon"></div>
            <div id="glow-ingress-block">
                <span class="nav-line-1 nav-progressive-content" id="glow-ingress-line1">
                   Hello
                </span>
                <span class="nav-line-2 nav-progressive-content" id="glow-ingress-line2">
                   Select your address
                </span>
            </div>
        </a>
        </span>
        <input data-addnewaddress="add-new" id="unifiedLocation1ClickAddress" name="dropdown-selection" type="hidden" value="add-new" class="nav-progressive-attribute" />
        <input data-addnewaddress="add-new" id="ubbShipTo" name="dropdown-selection-ubb" type="hidden" value="add-new" class="nav-progressive-attribute"/>
        <input id="glowValidationToken" name="glow-validation-token" type="hidden" value="gM82cr2fiJuFsMIJqCY2URb8BUYeNZujOryM7zUAAAAMAAAAAGRDx/dyYXcAAAAA;hB9R/xrmlYtSdzBL6kBhtmZvVc5iIBOMOcgoJzfhJoFZAAAAAGRDx/cAAAAB" class="nav-progressive-attribute"/>
</div>

<div id="nav-global-location-toaster-script-container" class="nav-progressive-content">
</div>

      </div>
          <div class='nav-fill'>
            <script type='text/javascript'>window.navmet.tmp=+new Date();</script>
<div id="nav-search">
  <div id="nav-bar-left"></div>
  <form
    id="nav-search-bar-form"
    accept-charset="utf-8"
    action="/s/ref=nb_sb_noss"
    class="nav-searchbar nav-progressive-attribute"
    method="GET"
    name="site-search"
    role="search"
  >

    <div class="nav-left">
      <div id="nav-search-dropdown-card">
        
  <div class="nav-search-scope nav-sprite">
    <div class="nav-search-facade" data-value="search-alias=aps">
      <span id="nav-search-label-id" class="nav-search-label nav-progressive-content">All</span>
      <i class="nav-icon"></i>
    </div>
    <label id="searchDropdownDescription" for="searchDropdownBox" class="nav-progressive-attribute" style="display:none">Select the department you want to search in</label>
    <select
      aria-describedby="searchDropdownDescription"
      class="nav-search-dropdown searchSelect nav-progressive-attrubute nav-progressive-search-dropdown"
      data-nav-digest="YaNDxYMsix1vZjM7upEvnpX/VWU="
      data-nav-selected="0"
      id="searchDropdownBox"
      name="url"
      style="display: block;"
      tabindex="0"
      title="Search in"
    >
        <option selected="selected" value="search-alias=aps">All Categories</option>
        <option value="search-alias=alexa-skills">Alexa Skills</option>
        <option value="search-alias=amazon-devices">Amazon Devices</option>
        <option value="search-alias=fashion">Amazon Fashion</option>
        <option value="search-alias=nowstore">Amazon Fresh</option>
        <option value="search-alias=amazon-pharmacy">Amazon Pharmacy</option>
        <option value="search-alias=appliances">Appliances</option>
        <option value="search-alias=mobile-apps">Apps & Games</option>
        <option value="search-alias=baby">Baby</option>
        <option value="search-alias=beauty">Beauty</option>
        <option value="search-alias=stripbooks">Books</option>
        <option value="search-alias=automotive">Car & Motorbike</option>
        <option value="search-alias=apparel">Clothing & Accessories</option>
        <option value="search-alias=collectibles">Collectibles</option>
        <option value="search-alias=computers">Computers & Accessories</option>
        <option value="search-alias=todays-deals">Deals</option>
        <option value="search-alias=electronics">Electronics</option>
        <option value="search-alias=furniture">Furniture</option>
        <option value="search-alias=lawngarden">Garden & Outdoors</option>
        <option value="search-alias=gift-cards">Gift Cards</option>
        <option value="search-alias=grocery">Grocery & Gourmet Foods</option>
        <option value="search-alias=hpc">Health & Personal Care</option>
        <option value="search-alias=kitchen">Home & Kitchen</option>
        <option value="search-alias=industrial">Industrial & Scientific</option>
        <option value="search-alias=jewelry">Jewellery</option>
        <option value="search-alias=digital-text">Kindle Store</option>
        <option value="search-alias=luggage">Luggage & Bags</option>
        <option value="search-alias=luxury-beauty">Luxury Beauty</option>
        <option value="search-alias=dvd">Movies & TV Shows</option>
        <option value="search-alias=popular">Music</option>
        <option value="search-alias=mi">Musical Instruments</option>
        <option value="search-alias=office-products">Office Products</option>
        <option value="search-alias=pets">Pet Supplies</option>
        <option value="search-alias=instant-video">Prime Video</option>
        <option value="search-alias=shoes">Shoes & Handbags</option>
        <option value="search-alias=software">Software</option>
        <option value="search-alias=sporting">Sports, Fitness & Outdoors</option>
        <option value="search-alias=specialty-aps-sns">Subscribe & Save</option>
        <option value="search-alias=home-improvement">Tools & Home Improvement</option>
        <option value="search-alias=toys">Toys & Games</option>
        <option value="search-alias=under-ten-dollars">Under ₹500</option>
        <option value="search-alias=videogames">Video Games</option>
        <option value="search-alias=watches">Watches</option>
    </select>
  </div>

      </div>
    </div>
    <div class="nav-fill">
      <div class="nav-search-field ">
        <label for="twotabsearchtextbox" style="display: none;">Search Amazon.in</label>
        <input
          type="text"
          id="twotabsearchtextbox"
          value=""
          name="field-keywords"
          autocomplete="off"
          placeholder="Search Amazon.in"
          class="nav-input nav-progressive-attribute"
          dir="auto"
          tabindex="0"
          aria-label="Search Amazon.in"
          spellcheck="false"
        >
      </div>
      <div id="nav-iss-attach"></div>
    </div>
    <div class="nav-right">
      <div class="nav-search-submit nav-sprite">
        <span id="nav-search-submit-text" class="nav-search-submit-text nav-sprite nav-progressive-attribute" aria-label="Go">
          <input id="nav-search-submit-button" type="submit" class="nav-input nav-progressive-attribute" value="Go" tabindex="0">
        </span>
      </div>
    </div>
  </form>
</div>
<script type='text/javascript'>window.navmet.push({key:'Search',end:+new Date(),begin:window.navmet.tmp});</script>
          </div>
      <div class='nav-right'>
          <script type='text/javascript'>window.navmet.tmp=+new Date();</script>
          <div id='nav-tools' class="layoutToolbarPadding">
              
              
              
              
  <a href="/customer-preferences/edit?ie=UTF8&preferencesReturnUrl=%2F&ref_=topnav_lang" id="icp-nav-flyout" class="nav-a nav-a-2 icp-link-style-2" aria-label="Choose a language for shopping.">
    <span class="icp-nav-link-inner">
      <span class="nav-line-1">
      </span>
      <span class="nav-line-2">
        <span class="icp-nav-flag icp-nav-flag-in icp-nav-flag-lop"></span>
          <div>EN</div>
        <span class="nav-icon nav-arrow"></span>
      </span>
    </span>
  </a>

              
  <a href="https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_viewopt_fmt%2F%3F_encoding%3DUTF8%26formatType%3Dcurrent_format%26ie%3DUTF8%26pageNumber%3D1%26reviewerType%3Davp_only_reviews%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&" class="nav-a nav-a-2   nav-progressive-attribute" data-nav-ref="nav_ya_signin"  data-nav-role="signin" data-ux-jq-mouseenter="true" id="nav-link-accountList" tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav-link-accountList" data-csa-c-content-id="nav_ya_signin">
  <div class="nav-line-1-container"><span id="nav-link-accountList-nav-line-1" class="nav-line-1 nav-progressive-content">Hello, sign in</span></div>
  <span class="nav-line-2 ">Account & Lists<span class="nav-icon nav-arrow"></span>
  </span>
</a>

              
<a href="/gp/css/order-history?ref_=nav_orders_first" class="nav-a nav-a-2   nav-progressive-attribute" id="nav-orders" tabindex="0">
  <span class="nav-line-1">Returns</span>
  <span class="nav-line-2">& Orders<span class="nav-icon nav-arrow"></span></span>
</a>

              
              
  <a href="https://www.amazon.in/gp/cart/view.html?ref_=nav_cart" aria-label="0 items in cart" class="nav-a nav-a-2 nav-progressive-attribute" id="nav-cart">
    <div id="nav-cart-count-container">
      <span id="nav-cart-count" aria-hidden="true" class="nav-cart-count nav-cart-0 nav-progressive-attribute nav-progressive-content">0</span>
      <span class="nav-cart-icon nav-sprite"></span>
    </div>
    <div id="nav-cart-text-container" class=" nav-progressive-attribute">
      <span aria-hidden="true" class="nav-line-1">
         
      </span>
      <span aria-hidden="true" class="nav-line-2">
        Cart
        <span class="nav-icon nav-arrow"></span>
      </span>
    </div>
  </a>

          </div>
          <script type='text/javascript'>window.navmet.push({key:'Tools',end:+new Date(),begin:window.navmet.tmp});</script>

      </div>
    </div>
    <div id='nav-main' class='nav-sprite'>
      <div class='nav-left'>
        <script type='text/javascript'>window.navmet.tmp=+new Date();</script>
  <a href="/gp/site-directory?ref_=nav_em_js_disabled" id="nav-hamburger-menu" role="button" aria-label="Open Menu" data-csa-c-type="widget" data-csa-c-slot-id="HamburgerMenuDesktop"
  data-csa-c-interaction-events="click" >
    <i class="hm-icon nav-sprite"></i>
    <span class="hm-icon-label">All</span>
  </a>
  
<script type="text/javascript">
  var hmenu = document.getElementById("nav-hamburger-menu");
  hmenu.setAttribute("href", "javascript: void(0)");
  window.navHamburgerMetricLogger = function() {
    if (window.ue && window.ue.count) {
      var metricName = "Nav:Hmenu:IconClickActionPending";
      window.ue.count(metricName, (ue.count(metricName) || 0) + 1);
    }
    window.$Nav && $Nav.declare("navHMenuIconClicked",!0);
    window.$Nav && $Nav.declare("navHMenuIconClickedNotReadyTimeStamp", Date.now());
  };
  hmenu.addEventListener("click", window.navHamburgerMetricLogger);
  window.$Nav && $Nav.declare('hamburgerMenuIconAvailableOnLoad', false);
</script>  
<script type='text/javascript'>window.navmet.push({key:'HamburgerMenuIcon',end:+new Date(),begin:window.navmet.tmp});</script>
      </div>
      <div class='nav-fill'>
        
 <div id="nav-shop">
 </div>
        <div id='nav-xshop-container'>
          <div id='nav-xshop' class="nav-progressive-content">
            <script type='text/javascript'>window.navmet.tmp=+new Date();</script>
<a href="/minitv?ref_=nav_avod_desktop_topnav" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_0" data-csa-c-content-id="nav_avod_desktop_topnav">Amazon miniTV</a>

<a href="/b/32702023031?node=32702023031&ld=AZINSOANavDesktop_T3&ref_=nav_cs_sell_T3" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_1" data-csa-c-content-id="nav_cs_sell_T3">Sell</a>

<a href="/gp/bestsellers/?ref_=nav_cs_bestsellers" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_2" data-csa-c-content-id="nav_cs_bestsellers">Best Sellers</a>

<a href="/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_3" data-csa-c-content-id="nav_cs_mobiles">Mobiles</a>

<a href="/deals?ref_=nav_cs_gb" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_4" data-csa-c-content-id="nav_cs_gb">Today's Deals</a>

<a href="/gp/help/customer/display.html?nodeId=200507590&ref_=nav_cs_help" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_5" data-csa-c-content-id="nav_cs_help">Customer Service</a>

<a href="/electronics/b/?ie=UTF8&node=976419031&ref_=nav_cs_electronics" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_6" data-csa-c-content-id="nav_cs_electronics"> Electronics </a>

<a href="/prime?ref_=nav_cs_primelink_nonmember" class="nav-a  " data-ux-jq-mouseenter="true" id="nav-link-amazonprime" tabindex="0"  data-csa-c-type="link" data-csa-c-slot-id="nav-link-amazonprime" data-csa-c-content-id="nav_cs_primelink_nonmember"><span>Prime</span><span class="nav-icon nav-arrow"></span></a>

<a href="/gp/new-releases/?ref_=nav_cs_newreleases" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_8" data-csa-c-content-id="nav_cs_newreleases">New Releases</a>

<a href="/Home-Kitchen/b/?ie=UTF8&node=976442031&ref_=nav_cs_home" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_9" data-csa-c-content-id="nav_cs_home">Home & Kitchen</a>

<a href="/gp/sva/dashboard?ref_=nav_cs_apay" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_10" data-csa-c-content-id="nav_cs_apay">Amazon Pay</a>

<a href="/gp/browse.html?node=6648217031&ref_=nav_cs_fashion" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_11" data-csa-c-content-id="nav_cs_fashion">Fashion</a>

<a href="/computers-and-accessories/b/?ie=UTF8&node=976392031&ref_=nav_cs_pc" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_12" data-csa-c-content-id="nav_cs_pc">Computers</a>

<a href="/beauty/b/?ie=UTF8&node=1355016031&ref_=nav_cs_beauty" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_13" data-csa-c-content-id="nav_cs_beauty">Beauty & Personal Care</a>

<a href="/Books/b/?ie=UTF8&node=976389031&ref_=nav_cs_books" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_14" data-csa-c-content-id="nav_cs_books">Books</a>

<a href="/amazon-coupons/b/?_encoding=UTF8&node=10465704031&ref_=nav_cs_coupons" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_15" data-csa-c-content-id="nav_cs_coupons">Coupons</a>

<a href="/Toys-Games/b/?ie=UTF8&node=1350380031&ref_=nav_cs_toys" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_16" data-csa-c-content-id="nav_cs_toys">Toys & Games</a>

<a href="/Gourmet-Specialty-Foods/b/?ie=UTF8&node=2454178031&ref_=nav_cs_grocery" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_17" data-csa-c-content-id="nav_cs_grocery">Grocery & Gourmet Foods</a>

<a href="/Sports/b/?ie=UTF8&node=1984443031&ref_=nav_cs_sports" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_18" data-csa-c-content-id="nav_cs_sports">Sports, Fitness & Outdoors</a>

<a href="/Car-Motorbike-Store/b/?ie=UTF8&node=4772060031&ref_=nav_cs_automotive" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_19" data-csa-c-content-id="nav_cs_automotive">Car & Motorbike</a>

<a href="/health-and-personal-care/b/?ie=UTF8&node=1350384031&ref_=nav_cs_hpc" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_20" data-csa-c-content-id="nav_cs_hpc">Health, Household & Personal Care</a>

<a href="/Home-Improvement/b/?ie=UTF8&node=4286640031&ref_=nav_cs_hi" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_21" data-csa-c-content-id="nav_cs_hi">Home Improvement</a>

<a href="/gift-card-store/b/?ie=UTF8&node=3704982031&ref_=nav_cs_gc" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_22" data-csa-c-content-id="nav_cs_gc">Gift Cards</a>

<a href="/Baby/b/?ie=UTF8&node=1571274031&ref_=nav_cs_baby" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_23" data-csa-c-content-id="nav_cs_baby">Baby</a>

<a href="/video-games/b/?ie=UTF8&node=976460031&ref_=nav_cs_video_games" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_24" data-csa-c-content-id="nav_cs_video_games">Video Games</a>

<a href="/gcx/-/gfhz/?ref_=nav_cs_giftfinder" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_25" data-csa-c-content-id="nav_cs_giftfinder">Gift Ideas	</a>

<a href="/Pet-Supplies/b/?ie=UTF8&node=2454181031&ref_=nav_cs_pets" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_26" data-csa-c-content-id="nav_cs_pets">Pet Supplies</a>

<a href="/Audible-Books-and-Originals/b/?ie=UTF8&node=17941593031&ref_=nav_cs_audible" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_27" data-csa-c-content-id="nav_cs_audible">Audible</a>

<a href="/auto-deliveries/landing?ref_=nav_cs_sns" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_28" data-csa-c-content-id="nav_cs_sns">Subscribe & Save</a>

<a href="/b/?node=6637738031&ref_=nav_cs_amazonbasics" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_29" data-csa-c-content-id="nav_cs_amazonbasics">AmazonBasics</a>

<a href="/Kindle-eBooks/b/?ie=UTF8&node=1634753031&ref_=nav_cs_kindle_books" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_30" data-csa-c-content-id="nav_cs_kindle_books">Kindle eBooks</a>
<script type='text/javascript'>window.navmet.push({key:'CrossShop',end:+new Date(),begin:window.navmet.tmp});</script>
          </div>
        </div>
      </div>
      <div class='nav-right'>
        <script type='text/javascript'>window.navmet.tmp=+new Date();</script><!-- Navyaan SWM -->
<div id="nav-swmslot">
  <div id="navSwmHoliday" style="height: 39px; width: 400px; overflow: hidden; position: relative; ">
    <a aria-label="New Launches from Mobile, Electronics &amp; more" href="/b/?_encoding=UTF8&node=56944732031&ref_=nav_swm_swm_gd&pf_rd_p=6e65e9fd-815c-440d-a9ca-7a65e47c0c17&pf_rd_s=nav-sitewide-msg&pf_rd_t=4201&pf_rd_i=navbar-4201&pf_rd_m=A21TJRUUN4KGV&pf_rd_r=RZ67A764XT8VEYCF2P53" class="nav-imageHref" >
  <img alt="New Launches from Mobile, Electronics &amp; more" src="https://m.media-amazon.com/images/G/31/Gateway_IN/testing/NewLaunches_400x39._CB593645585_.jpg">
</a>
      </div>
  
</div><script type='text/javascript'>window.navmet.push({key:'SWM',end:+new Date(),begin:window.navmet.tmp});</script>
      </div>
    </div>

    <div id='nav-subnav-toaster'></div>

    
    <div id="nav-progressive-subnav">
      
    </div>

    <div id='nav-flyout-ewc' class='nav-ewc-lazy-align nav-ewc-hide-head'><div class='nav-flyout-body ewc-beacon' tabindex='-1'><div class='nav-ewc-arrow'></div><div class='nav-ewc-content'></div></div></div><script type='text/javascript'>
(function() {
  var viewportWidth = function() {
    return window.innerWidth ||
      document.documentElement.clientWidth ||
      document.body.clientWidth;
  };

  if (typeof uet === 'function') {  uet('x1', 'ewc', {wb: 1}); }

  window.$Nav && $Nav.declare('config.ewc', (function() {
    var config = {"enablePersistent":true,"viewportWidthForPersistent":1400,"isEWCLogging":1,"isEWCStateExpanded":true,"EWCStateReason":"fixed","isSmallScreenEnabled":true,"isFreshCustomer":false,"errorContent":{"html":"<div class='nav-ewc-error'><span class='nav-title'>Oops!</span><p class='nav-paragraph'>There is a problem loading your cart right now</p><a href='/gp/cart/view.html?ref_=nav_err_ewc_timeout' class='nav-action-button'><span class='nav-action-inner'>Your Cart</span></a></div>"},"url":"/cart/ewc/compact?hostPageType=CustomerReviews&hostSubPageType=remoteProduct&hostPageRID=RZ67A764XT8VEYCF2P53&prerender=0","cartCount":0,"freshCartCount":0,"almCartCount":0,"primeWardrobeCartCount":0,"isCompactViewEnabled":true,"isCompactEWCRendered":true,"isWiderCompactEWCRendered":true,"EWCBrowserCacheKey":"EWC_Cache_257-4714000-6327435__INR_en_IN","isContentRepainted":false,"clearCache":false,"loadFromCacheWithDelay":0,"delayRenderingTillATF":false};
    var hasAui = window.P && window.P.AUI_BUILD_DATE;
    var isRTLEnabled = (document.dir === 'rtl');
    config.pinnable = config.pinnable && hasAui;
    config.isMigrationTreatment = true;

    config.flyout = (function() {
      var navbelt = document.getElementById('nav-belt');
      var navCart = document.getElementById('nav-cart');
      var ewcFlyout = document.getElementById('nav-flyout-ewc');
      var persistentClassOnBody = 'nav-ewc-persistent-hover nav-ewc-full-height-persistent-hover';
      var flyout = {};

      var getDocumentScrollTop = function() {
        return (document.documentElement && document.documentElement.scrollTop) || document.body.scrollTop;
      };

      var isWindow = function(obj) {
        return obj != null && obj === obj.window;
      };

      var getWindow = function(elem) {
        return isWindow(elem) ? elem : elem.nodeType === 9 && elem.defaultView;
      };

      var getOffset = function(elem) {
        if (elem.getClientRects && !elem.getClientRects().length) {
          return {top: 0};
        }

        var rect = elem.getBoundingClientRect
          ? elem.getBoundingClientRect()
          : {top: 0};

        if (rect.width || rect.height) {
          var doc = elem.ownerDocument;
          var win = getWindow(doc);
          return {
            top: rect.top + win.pageYOffset - doc.documentElement.clientTop
          };
        }
        return rect;
      };

      flyout.align = function() {
        var newTop = getOffset(navbelt).top - getDocumentScrollTop();
        ewcFlyout.style.top = (newTop > 0 ? newTop + 'px' : 0);
      };

      flyout.hide = function() {
        isRTLEnabled
          ? (ewcFlyout.style.left = '')
          : (ewcFlyout.style.right = '');
      };

      if(typeof config.isCompactEWCRendered === 'undefined') {
        if (
          (config.isSmallScreenEnabled && viewportWidth() < 1400) ||
          (config.isCompactViewEnabled && viewportWidth() >= 1400)
        ) {
          config.isCompactEWCRendered = true;
          config.isEWCStateExpanded = true;
          config.url = config.url.replace("/gp/navcart/sidebar", "/cart/ewc/compact");
        } else {
          config.isCompactEWCRendered = false;
        }
      }

      var viewportQualifyForPersistent = function () {
        return (config.isCompactEWCRendered)
          ? true
          : viewportWidth() >= 1400;
      }

      flyout.hasQualifiedViewportForPersistent = viewportQualifyForPersistent;

      var getEWCRightOffset = function() {
        if (!config.isCompactEWCRendered) {
          return 0;
        }

        var $navbelt = document.getElementById('nav-belt');
        if ($navbelt === undefined || $navbelt === null) {
          return 0;
        }

        var EWCCompactViewWidth = (config.isWiderCompactEWCRendered  && viewportWidth() >= 1280) ? 130 : 100;
        var scrollLeft = (window.pageXOffset !== undefined)
          ? window.pageXOffset
          : (document.documentElement || document.body.parentNode || document.body).scrollLeft;
        var scrollXAxis = Math.abs(scrollLeft);
        var windowWidth = document.documentElement.clientWidth;
        var navbeltWidth = $navbelt.offsetWidth;
        var isPartOfNavbarNotVisible = (navbeltWidth + EWCCompactViewWidth) > windowWidth;

        if (isPartOfNavbarNotVisible) {
          return 0 - (navbeltWidth - scrollXAxis - windowWidth + EWCCompactViewWidth);
        } else {
          return 0;
        }
      }

      flyout.getEWCRightOffsetCssProperty = function () {
        return getEWCRightOffset() + 'px';
      }

      if (config.isCompactEWCRendered) {
        persistentClassOnBody = 'nav-ewc-persistent-hover nav-ewc-compact-view';
        if (config.isWiderCompactEWCRendered) { persistentClassOnBody += ' nav-ewc-wider-compact-view'; }
      }

      flyout.show = function() {
        isRTLEnabled
          ? (ewcFlyout.style.left = flyout.getEWCRightOffsetCssProperty())
          : (ewcFlyout.style.right = flyout.getEWCRightOffsetCssProperty());
      };

      var isIOSDevice = function() {
        return (/iPad|iPhone|iPod/.test(navigator.platform) ||
                (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1)) &&
                !window.MSStream;
      }

      var checkForPersistent = function() {
        if (!hasAui) {
          return { result: false, reason: 'noAui' };
        }
        if (!config.enablePersistent) {
          return { result: false, reason: 'config' };
        }
        if (!viewportQualifyForPersistent()) {
          return { result: false, reason: 'viewport' };
        }
        if (isIOSDevice()) {
          return { result: false, reason: 'iOS' };
        }
        if (!config.cartCount > 0) {
          return { result: false, reason: 'emptycart' };
        }
        return { result: true };
      };

      flyout.ableToPersist = function() {
        return checkForPersistent().result;
      };
      var persistentClassRegExp = '(?:^|\\s)' + persistentClassOnBody + '(?!\\S)';
      flyout.applyPageLayoutForPersistent = function() {
        if (!document.documentElement.className.match( new RegExp(persistentClassRegExp) )) {
          document.documentElement.className += ' ' + persistentClassOnBody;
        }
      };

      flyout.unapplyPageLayoutForPersistent = function() {
        document.documentElement.className = document.documentElement.className.replace( new RegExp(persistentClassRegExp, 'g'), '');
      };

      flyout.persist = function() {
        flyout.applyPageLayoutForPersistent();
        flyout.show();
        if (config.isCompactEWCRendered) {
          flyout.align();
        }
      };

      flyout.unpersist = function() {
        flyout.unapplyPageLayoutForPersistent();
        flyout.hide();
      };
      
      var persistentCheck = checkForPersistent();
    

      var resizeCallback = function() {
        
        if (flyout.ableToPersist()) {
          flyout.persist();
        }
        else {
          flyout.unpersist();
        }
      };

      flyout.bindEvents = function() {
        if (window.addEventListener) {
          window.addEventListener('resize', resizeCallback, false);
          
          if (config.isCompactEWCRendered) {
            window.addEventListener('scroll', flyout.align, false);
          }
        }
      };

      flyout.unbindEvents = function() {
        if (window.removeEventListener) {
          window.removeEventListener('resize', resizeCallback, false);
          
          if (config.isCompactEWCRendered) {
            window.removeEventListener('scroll', flyout.align, false);
          }
        }
      };
      
      var ewcDefaultPersistence = function() {
      
        if (persistentCheck.result) {
          flyout.persist();
          if (window.ue && ue.tag) {
            ue.tag('ewc:persist');
          }
        } else {
          if (window.ue && ue.tag) {
            ue.tag('ewc:unpersist');
            if (persistentCheck.reason === 'noAui') {
              ue.tag('ewc:unpersist:noAui');
            }
            if (persistentCheck.reason === 'viewport') {
              ue.tag('ewc:unpersist:viewport');
            }
            if (persistentCheck.reason === 'emptycart') {
              ue.tag('ewc:unpersist:emptycart');
            }
            if (persistentCheck.reason === 'iOS') {
              ue.tag('ewc:unpersist:iOS');
            }
          }
        }
      };
      
      ewcDefaultPersistence();
      
      if (window.ue && ue.tag)  {
        if (flyout.hasQualifiedViewportForPersistent()) {
          ue.tag('ewc:bview');
        }
        else {
          ue.tag('ewc:sview');
        }
      }
      flyout.bindEvents();
      flyout.cache = function () {
    const cache = window.sessionStorage;
    const CACHE_KEY = "EWCBrowserCacheKey";
    const CACHE_EXPIRY = "EWCBrowserCacheExpiry"; 
    const CACHE_VALUE = "EWCBrowserCacheValue"; 
    const isSessionStorageValid = function () {
        return window && cache && cache instanceof Storage;
    };
    const isCachePresent = function (key) {
        return cache.length > 0 && cache.getItem(key);
    }
    const isValidType = function (value) {
        // Prevents accessing empty key-value and internal methods(prototypes) of storage
        // TODO: Log metrics for invalid access;
        return value && value.constructor == String;
    }
    return {
        getCache: function (key) {
            const value = isCachePresent(key);
            return (isValidType(value)) ? value : null;
        },
        setCache: function (key, value) {
            const oldValue = isCachePresent(key);
            const cacheExpiryTime = isCachePresent(CACHE_EXPIRY);
            // Set the expiry when there's no existing cache - to prevent resetting expiry on page navigation
            if (!cacheExpiryTime) {
                var currentTime = new Date();
                cache.setItem(CACHE_EXPIRY, new Date(currentTime.getTime() + 5 * 60000))
            }
            // TODO: Log length of old and new cache values when logMetrics is true
            cache.setItem(key, value);
        },
        updateCacheAndEwcContainer: function (cacheKey, newEwcContent) {
            const $ = $Nav.getNow("$");
            const $currentEwc = $("#ewc-content");
            if (!$currentEwc.length) {
                var $content = $('#nav-flyout-ewc .nav-ewc-content');
                $content.html(newEwcContent);
                this.setCache(CACHE_KEY, cacheKey);
                if (window.ue && window.ue.count) {
                    var current = window.ue.count("ewc-init-cache") || 0;
                    window.ue.count("ewc-init-cache", current + 1);
                }
            } else {
                var $newEwcContent = $('<div />');
                var EWC_CONTENT_BODY_SCROLL_SELECTOR = ".ewc-scroller--selected";
                if (newEwcContent) { // 1. Updates EWC container with new HTML 
                    const $newEwcHtml = $newEwcContent.html(newEwcContent).find("#ewc-content");
                    const offSet = $currentEwc.find(EWC_CONTENT_BODY_SCROLL_SELECTOR).position().top - $currentEwc.find(".ewc-active-cart--selected").position().top;
                    $currentEwc.html($newEwcHtml.html());
                    $currentEwc.find(EWC_CONTENT_BODY_SCROLL_SELECTOR).scrollTop(offSet);
                    if (typeof window.uex === 'function') {
                        window.uex('ld', 'ewc-reflect-new-state', {wb: 1});
                    }
                } else {
                    // 2. Fetches cached response and updates it's html with new state on EWC Update
                    const cachedEwc = this.getCache(CACHE_VALUE);
                    $newEwcContent = $newEwcContent[0];
                    $(cachedEwc).map(function (elementIndex, element) {
                         $newEwcContent.appendChild((element.id === "ewc-content") ? $currentEwc.clone()[0] : element);
                    });
                    newEwcContent = $newEwcContent.innerHTML;
                    if (window.ue && window.ue.count) {
                        var current = window.ue.count("ewc-update-cache") || 0;
                        window.ue.count("ewc-update-cache", current + 1);
                    }
                }
                $newEwcContent.remove();
            }
            this.setCache(CACHE_VALUE, newEwcContent);
        },
        removeCache: function (key) {
            return cache.removeItem(key);
        }
    }
}
;
      return flyout;
    }());
     
     
     
const CACHE_KEY = "EWCBrowserCacheKey";
const CACHE_VALUE = "EWCBrowserCacheValue"; 
const CACHE_EXPIRY = "EWCBrowserCacheExpiry"; 
var cache = config.flyout.cache();

const isCacheValid = function () {
  // Check for page types and tenure of the cache
  const clearCache = config.clearCache;
  const cacheExpiryTime = cache.getCache(CACHE_EXPIRY);
  const isCacheExpired = new Date() > new Date(cacheExpiryTime);
  const cacheKey = config.EWCBrowserCacheKey;
  const oldCacheKey = cache.getCache(CACHE_KEY);
  const isCacheValid = !clearCache && !isCacheExpired && cacheKey == oldCacheKey;
  if (!isCacheValid && window.ue && window.ue.count) {
    var current = window.ue.count("ewc-cache-invalidated") || 0;
    window.ue.count("ewc-cache-invalidated", current + 1);
  }
  return isCacheValid;
}
function loadFromCache() {
    if (window.uet && typeof window.uet === 'function') {
        window.uet('bb', 'ewc-loaded-from-cache', {wb: 1});
    }
    if (cache) {
        if (isCacheValid()) {
            var content = cache.getCache(CACHE_VALUE);
            if (content) {
                var $ewcContainer = document.getElementById("nav-flyout-ewc").getElementsByClassName("nav-ewc-content")[0];
                var $ewcContent = document.getElementById("ewc-content");
                if ($ewcContainer && !$ewcContent) {
                    $ewcContainer.innerHTML = content;
                    // Execute scripts from cache
                    const ewcJavascript = document.getElementById("ewc-content").parentNode.querySelectorAll(':scope > script');
                    ewcJavascript.forEach(function (script) {
                        var scriptTag = document.createElement("script");
                        scriptTag.innerHTML = script.innerHTML;
                        document.body.appendChild(scriptTag);
                    });
                    if (typeof window.uex === 'function') {
                        window.uex('ld', 'ewc-loaded-from-cache', {wb: 1});
                    }
                } else if (window.ue && window.ue.count && typeof window.ue.count === 'function') {
                    var currentFailure = window.ue.count("ewc-slow-cache") || 0;
                    window.ue.count("ewc-slow-cache", currentFailure + 1);
                }
            }
        } else {
            cache.removeCache(CACHE_VALUE);
            cache.removeCache(CACHE_KEY);
            cache.removeCache(CACHE_EXPIRY);
        }
    }
}
function delayBy(delayTime) {
    if (delayTime) {
        window.setTimeout(function() {
            loadFromCache();
        }, delayTime)
    } else {
        loadFromCache();
    }
}
if(config.delayRenderingTillATF) {
    (window.AmazonUIPageJS ? AmazonUIPageJS : P).when('atf').execute("EverywhereCartLoadFromCacheOnAtf", function () {
        delayBy(config.loadFromCacheWithDelay);
    });
} else {
    delayBy(config.loadFromCacheWithDelay);
}

    return config;
  }()));

  if (typeof uet === 'function') {
    uet('x2', 'ewc', {wb: 1});
  }

  if (window.ue && ue.tag) {
    ue.tag('ewc');
    ue.tag('ewc:unrec');
    ue.tag('ewc:cartsize:0');

    if ( window.P && window.P.AUI_BUILD_DATE ) {
      ue.tag('ewc:aui');
    } else {
      ue.tag('ewc:noAui');
    }
  }
}());
</script>
  </div>

  
  

</header>


<script type='text/javascript'>window.navmet.push({key:'NavBar',end:+new Date(),begin:window.navmet.main});</script>


<script type="text/javascript">
  if (window.ue_t0) {
    window.navmet.push({key:"NavMainPaintEnd",end:+new Date(),begin:window.ue_t0});
    window.navmet.push({key:"NavFirstPaintEnd",end:+new Date(),begin:window.ue_t0});
  }
</script>


<script type='text/javascript'>
    <!--
    window.$Nav && $Nav.declare('config.fixedBarBeacon',false);
    window.$Nav && $Nav.when("data").run(function(data) { data({"freshTimeout":{"template":{"name":"flyoutError","data":{"error":{"title":"<style>#nav-flyout-fresh{width:269px;padding:0;}#nav-flyout-fresh .nav-flyout-content{padding:0;}</style><a href='/amazonfresh'><img src='https://images-eu.ssl-images-amazon.com/images/G/02/omaha/images/yoda/flyout_72dpi._V270092858_.png' /></a>"}}}},"cartTimeout":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Cart","url":"/gp/cart/view.html?ref_=nav_err_cart_timeout"},"title":"Oops!","paragraph":"There is a problem loading your cart right now"}}}},"primeTimeout":{"template":{"name":"flyoutError","data":{"error":{"title":"<a href='/gp/prime?ref_=nav_prime_btn_fb'><img src='https://images-eu.ssl-images-amazon.com/images/G/02/prime/yourprime/yourprime-widget-piv-fallback._V310089192_.jpg' /></a>"}}}},"ewcTimeout":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Cart","url":"/gp/cart/view.html?ref_=nav_err_ewc_timeout"},"title":"Oops!","paragraph":"There is a problem loading your cart right now"}}}},"errorWishlist":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Wish List","url":"/gp/registry/wishlist/?ref_=nav_err_wishlist"},"title":"Oops!","paragraph":"There is a problem retrieving the list right now"}}}},"emptyWishlist":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Wish List","url":"/gp/registry/wishlist/?ref_=nav_err_empty_wishlist"},"title":"Oops!","paragraph":"Your list is empty"}}}},"yourAccountContent":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Account","url":"/gp/css/homepage.html?ref_=nav_err_youraccount"},"title":"Oops!","paragraph":"There is a problem retrieving the list right now"}}}},"shopAllTimeout":{"template":{"name":"flyoutError","data":{"error":{"paragraph":"There is a problem retrieving the list right now"}}}},"kindleTimeout":{"template":{"name":"flyoutError","data":{"error":{"paragraph":"There is a problem retrieving the list right now"}}}}}); });
window.$Nav && $Nav.when("util.templates").run("FlyoutErrorTemplate", function(templates) {
      templates.add("flyoutError", "<# if(error.title) { #><span class='nav-title'><#=error.title #></span><# } #><# if(error.paragraph) { #><p class='nav-paragraph'><#=error.paragraph #></p><# } #><# if(error.button) { #><a href='<#=error.button.url #>' class='nav-action-button' ><span class='nav-action-inner'><#=error.button.text #></span></a><# } #>");
    });

    if (typeof uet == 'function') {
    uet('bb', 'iss-init-pc', {wb: 1});
  }
  if (!window.$SearchJS && window.$Nav) {
    window.$SearchJS = $Nav.make('sx');
  }

  var opts = {
    host: "completion.amazon.co.uk/search/complete"
  , marketId: "44571"
  , obfuscatedMarketId: "A21TJRUUN4KGV"
  , searchAliases: ["aps","amazonfresh","amazon-devices","stripbooks","audible","computers","digital-text","dvd","instant-video","electronics","hpc","kitchen","furniture","popular","software","videogames","toys","beauty","baby","watches","jewelry","luggage","mobile-apps","apparel","shoes","sporting","gift-cards","grocery","mi","office-products","pets","automotive","industrial","fashion","fashion-baby","fashion-baby-boys","fashion-baby-girls","fashion-boys","fashion-boys-clothing","fashion-boys-jewelry","fashion-boys-shoes","fashion-boys-watches","fashion-girls","fashion-girls-clothing","fashion-girls-jewelry","fashion-girls-shoes","fashion-girls-watches","fashion-luggage","fashion-mens","fashion-mens-clothing","fashion-mens-jewelry","fashion-mens-shoes","fashion-mens-watches","fashion-womens","fashion-womens-clothing","fashion-womens-handbags","fashion-womens-jewelry","fashion-womens-shoes","fashion-womens-watches","appliances","pantry","lawngarden","local-services","luxury-beauty","nowstore","more","bigbazaar","home-improvement","alexa-skills","collectibles","todays-deals","under-ten-dollars","specialty-aps-sns"]
  , filterAliases: []
  , pageType: "CustomerReviews"
  , requestId: "RZ67A764XT8VEYCF2P53"
  , sessionId: "257-4714000-6327435"
  , language: "en_IN"
  , customerId: ""
  , asin: "B08L5VRVTD"
  , b2b: 0
  , fresh: 0
  , isJpOrCn: 0
  , isUseAuiIss: 1
};

var issOpts = {
    fallbackFlag: 1
  , isDigitalFeaturesEnabled: 0
  , isWayfindingEnabled: 0
  , dropdown: "select.searchSelect"
  , departmentText: "in {department}"
  , suggestionText: "Search suggestions"
  , recentSearchesTreatment: "C"
  , authorSuggestionText: "all books by {author}"
  , translatedStringsMap: {"sx-recent-searches":"Recent searches","sx-your-recent-search":"Inspired by your recent search"}
  , biaTitleText: ""
  , biaPurchasedText: ""
  , biaViewAllText: ""
  , biaViewAllManageText: ""
  , biaAndText: ""
  , biaManageText: ""
  , biaWeblabTreatment: ""
  , issNavConfig: {}
  , np: 0
  , issCorpus: []
  , cf: 1
  , removeDeepNodeISS: ""
  , trendingTreatment: "C"
  , useAPIV2: ""
  , opfSwitch: ""
  , isISSDesktopRefactorEnabled: "1"
  , useServiceHighlighting: "true"
  , isInternal: 0
  , isAPICachingDisabled: true
  , isBrowseNodeScopingEnabled: false
  , isStorefrontTemplateEnabled: false
  , disableAutocompleteOnFocus: ""
};

  if (opts.isUseAuiIss === 1 && window.$Nav) {
  window.$Nav.when('sx.iss').run('iss-mason-init', function(iss){
    var issInitObj = buildIssInitObject(opts, issOpts, true);
    new iss.IssParentCoordinator(issInitObj);

    $SearchJS.declare('canCreateAutocomplete', issInitObj);
  });
} else if (window.$SearchJS) {
  var iss;

  // BEGIN Deprecated globals
  var issHost = opts.host
    , issMktid = opts.marketId
    , issSearchAliases = opts.searchAliases
    , updateISSCompletion = function() { iss.updateAutoCompletion(); };
  // END deprecated globals


  $SearchJS.when('jQuery', 'search-js-autocomplete-lib').run('autocomplete-init', initializeAutocomplete);
  $SearchJS.when('canCreateAutocomplete').run('createAutocomplete', createAutocomplete);

} // END conditional for window.$SearchJS
  function initializeAutocomplete(jQuery) {
  var issInitObj = buildIssInitObject(opts, issOpts);
  $SearchJS.declare("canCreateAutocomplete", issInitObj);
} // END initializeAutocomplete
  function initSearchCsl(searchCSL, issInitObject) {
  searchCSL.init(
    opts.pageType,
    (window.ue && window.ue.rid) || opts.requestId
  );
  $SearchJS.declare("canCreateAutocomplete", issInitObject);
} // END initSearchCsl
  function createAutocomplete(issObject) {
  iss = new AutoComplete(issObject);

  $SearchJS.publish("search-js-autocomplete", iss);

  logMetrics();
} // END createAutocomplete
  function buildIssInitObject(opts, issOpts, isNewIss) {
    var issInitObj = {
        src: opts.host
      , sessionId: opts.sessionId
      , requestId: opts.requestId
      , mkt: opts.marketId
      , obfMkt: opts.obfuscatedMarketId
      , pageType: opts.pageType
      , language: opts.language
      , customerId: opts.customerId
      , fresh: opts.fresh
      , b2b: opts.b2b
      , aliases: opts.searchAliases
      , fb: issOpts.fallbackFlag
      , isDigitalFeaturesEnabled: issOpts.isDigitalFeaturesEnabled
      , isWayfindingEnabled: issOpts.isWayfindingEnabled
      , issPrimeEligible: issOpts.issPrimeEligible
      , deptText: issOpts.departmentText
      , sugText: issOpts.suggestionText
      , filterAliases: opts.filterAliases
      , biaWidgetUrl: opts.biaWidgetUrl
      , recentSearchesTreatment: issOpts.recentSearchesTreatment
      , authorSuggestionText: issOpts.authorSuggestionText
      , translatedStringsMap: issOpts.translatedStringsMap
      , biaTitleText: ""
      , biaPurchasedText: ""
      , biaViewAllText: ""
      , biaViewAllManageText: ""
      , biaAndText: ""
      , biaManageText: ""
      , biaWeblabTreatment: ""
      , issNavConfig: issOpts.issNavConfig
      , cf: issOpts.cf
      , ime: opts.isJpOrCn
      , mktid: opts.marketId
      , qs: opts.isJpOrCn
      , issCorpus: issOpts.issCorpus
      , deepNodeISS: {
          searchAliasAccessor: function($) {
            return (window.SearchPageAccess && window.SearchPageAccess.searchAlias()) ||
                   $('select.searchSelect').children().attr('data-root-alias');
          },
          searchAliasDisplayNameAccessor: function() {
            return (window.SearchPageAccess && window.SearchPageAccess.searchAliasDisplayName());
          }
        }
      , removeDeepNodeISS: issOpts.removeDeepNodeISS
      , trendingTreatment: issOpts.trendingTreatment
      , useAPIV2: issOpts.useAPIV2
      , opfSwitch: issOpts.opfSwitch
      , isISSDesktopRefactorEnabled: issOpts.isISSDesktopRefactorEnabled
      , useServiceHighlighting: issOpts.useServiceHighlighting
      , isInternal: issOpts.isInternal
      , isAPICachingDisabled: issOpts.isAPICachingDisabled
      , isBrowseNodeScopingEnabled: issOpts.isBrowseNodeScopingEnabled
      , isStorefrontTemplateEnabled: issOpts.isStorefrontTemplateEnabled
      , disableAutocompleteOnFocus: issOpts.disableAutocompleteOnFocus
      , asin: opts.asin
    };
  
    // If we aren't using the new ISS then we need to add these properties
    
    if (!isNewIss) {
      issInitObj.dd = issOpts.dropdown; // The element with id searchDropdownBox doesn't exist in C.
      issInitObj.imeSpacing = issOpts.imeSpacing;
      issInitObj.isNavInline = 1;
      issInitObj.triggerISSOnClick = 0;
      issInitObj.sc = 1;
      issInitObj.np = issOpts.np;
    }
  
    return issInitObj;
  } // END buildIssInitObject
  function logMetrics() {
  if (typeof uet == 'function' && typeof uex == 'function') {
      uet('be', 'iss-init-pc',
          {
              wb: 1
          });
      uex('ld', 'iss-init-pc',
          {
              wb: 1
          });
  }
} // END logMetrics
  
    
window.$Nav && $Nav.declare('config.navDeviceType','desktop');

window.$Nav && $Nav.declare('config.navDebugHighres',false);

window.$Nav && $Nav.declare('config.pageType','CustomerReviews');
window.$Nav && $Nav.declare('config.subPageType','remoteProduct');

window.$Nav && $Nav.declare('config.dynamicMenuUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Fdynamic\x2Dmenu.html');

window.$Nav && $Nav.declare('config.dismissNotificationUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Fdismissnotification.html');

window.$Nav && $Nav.declare('config.enableDynamicMenus',true);

window.$Nav && $Nav.declare('config.isInternal',false);

window.$Nav && $Nav.declare('config.isBackup',false);

window.$Nav && $Nav.declare('config.isRecognized',false);

window.$Nav && $Nav.declare('config.transientFlyoutTrigger','\x23nav\x2Dtransient\x2Dflyout\x2Dtrigger');

window.$Nav && $Nav.declare('config.subnavFlyoutUrl','\x2Fnav\x2Fajax\x2FsubnavFlyout');
window.$Nav && $Nav.declare('config.isSubnavFlyoutMigrationEnabled',true);

window.$Nav && $Nav.declare('config.recordEvUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Frecordevent.html');
window.$Nav && $Nav.declare('config.recordEvInterval',15000);
window.$Nav && $Nav.declare('config.sessionId','257\x2D4714000\x2D6327435');
window.$Nav && $Nav.declare('config.requestId','RZ67A764XT8VEYCF2P53');

window.$Nav && $Nav.declare('config.alexaListEnabled',true);

window.$Nav && $Nav.declare('config.readyOnATF',false);

window.$Nav && $Nav.declare('config.dynamicMenuArgs',{"rid":"RZ67A764XT8VEYCF2P53","isFullWidthPrime":0,"isPrime":0,"dynamicRequest":1,"weblabs":"","isFreshRegionAndCustomer":"","primeMenuWidth":310});

window.$Nav && $Nav.declare('config.customerName',false);

window.$Nav && $Nav.declare('config.customerCountryCode','IN');

window.$Nav && $Nav.declare('config.yourAccountPrimeURL',null);

window.$Nav && $Nav.declare('config.yourAccountPrimeHover',true);

window.$Nav && $Nav.declare('config.searchBackState',{});

window.$Nav && $Nav.declare('nav.inline');

(function (i) {
  if(window._navbarSpriteUrl) {
    i.onload = function() {window.uet && uet('ne')};
    i.src = window._navbarSpriteUrl;
  }
}(new Image()));

window.$Nav && $Nav.declare('config.autoFocus',false);

window.$Nav && $Nav.declare('config.responsiveTouchAgents',["ieTouch"]);

window.$Nav && $Nav.declare('config.responsiveGW',false);

window.$Nav && $Nav.declare('config.pageHideEnabled',false);

window.$Nav && $Nav.declare('config.sslTriggerType','null');
window.$Nav && $Nav.declare('config.sslTriggerRetry',0);

window.$Nav && $Nav.declare('config.doubleCart',false);

window.$Nav && $Nav.declare('config.signInOverride',true);

window.$Nav && $Nav.declare('config.signInTooltip',false);

window.$Nav && $Nav.declare('config.isPrimeMember',false);

window.$Nav && $Nav.declare('config.packardGlowTooltip',false);

window.$Nav && $Nav.declare('config.packardGlowFlyout',false);

window.$Nav && $Nav.declare('config.rightMarginAlignEnabled',true);

window.$Nav && $Nav.declare('config.flyoutAnimation',false);

window.$Nav && $Nav.declare('config.campusActivation','null');

window.$Nav && $Nav.declare('config.primeTooltip',false);

window.$Nav && $Nav.declare('config.primeDay',false);

window.$Nav && $Nav.declare('config.disableBuyItAgain',false);

window.$Nav && $Nav.declare('config.enableCrossShopBiaFlyout',false);

window.$Nav && $Nav.declare('config.pseudoPrimeFirstBrowse',null);

window.$Nav && $Nav.declare('config.sdaYourAccount',false);

window.$Nav && $Nav.declare('config.csYourAccount',false);

window.$Nav && $Nav.declare('config.cartFlyoutDisabled',true);

window.$Nav && $Nav.declare('config.isTabletBrowser',false);

window.$Nav && $Nav.declare('config.HmenuProximityArea',[200,200,200,200]);

window.$Nav && $Nav.declare('config.HMenuIsProximity',true);

window.$Nav && $Nav.declare('config.isPureAjaxALF',false);

window.$Nav && $Nav.declare('config.accountListFlyoutRedesign',false);

window.$Nav && $Nav.declare('config.navfresh',false);

window.$Nav && $Nav.declare('config.isFreshRegion',false);

if (window.ue && ue.tag) { ue.tag('navbar'); };

window.$Nav && $Nav.declare('config.blackbelt',true);

window.$Nav && $Nav.declare('config.beaconbelt',true);

window.$Nav && $Nav.declare('config.accountList',true);

window.$Nav && $Nav.declare('config.iPadTablet',false);

window.$Nav && $Nav.declare('config.searchapiEndpoint',false);

window.$Nav && $Nav.declare('config.timeline',false);

window.$Nav && $Nav.declare('config.timelineAsinPriceEnabled',false);

window.$Nav && $Nav.declare('config.timelineDeleteEnabled',false);



window.$Nav && $Nav.declare('config.extendedFlyout',false);

window.$Nav && $Nav.declare('config.flyoutCloseDelay',600);

window.$Nav && $Nav.declare('config.pssFlag',0);

window.$Nav && $Nav.declare('config.isPrimeTooltipMigrated',false);

window.$Nav && $Nav.declare('config.isDynamicWishListMigrationEnabled',true);

window.$Nav && $Nav.declare('config.hashCustomerAndSessionId','0a87a08b8cbc053ddb2d07292077cf34f4f33b14');

window.$Nav && $Nav.declare('config.isExportMode',false);

window.$Nav && $Nav.declare('config.languageCode','en_IN');

window.$Nav && $Nav.declare('config.environmentVFI','AmazonNavigationCards\x2Fdevelopment\x40B6124830925\x2DAL2_x86_64');



window.$Nav && $Nav.declare('config.isHMenuBrowserCacheDisable',false);

window.$Nav && $Nav.declare('config.signInUrlWithRefTag','https\x3A\x2F\x2Fwww.amazon.in\x2Fap\x2Fsignin\x3Fopenid.pape.max_auth_age\x3D0\x26openid.return_to\x3Dhttps\x253A\x252F\x252Fwww.amazon.in\x252FNew\x2DApple\x2DiPhone\x2D12\x2D256GB\x252Fproduct\x2Dreviews\x252FB08L5VRVTD\x252Fref\x253Dcm_cr_arp_d_viewopt_fmt\x252F\x253F_encoding\x253DUTF8\x2526formatType\x253Dcurrent_format\x2526ie\x253DUTF8\x2526pageNumber\x253D1\x2526reviewerType\x253Davp_only_reviews\x2526ref_\x253DnavSignInUrlRefTagPlaceHolder\x26openid.identity\x3Dhttp\x253A\x252F\x252Fspecs.openid.net\x252Fauth\x252F2.0\x252Fidentifier_select\x26openid.assoc_handle\x3Dinflex\x26openid.mode\x3Dcheckid_setup\x26openid.claimed_id\x3Dhttp\x253A\x252F\x252Fspecs.openid.net\x252Fauth\x252F2.0\x252Fidentifier_select\x26openid.ns\x3Dhttp\x253A\x252F\x252Fspecs.openid.net\x252Fauth\x252F2.0\x26');

window.$Nav && $Nav.declare('config.isSmile',false);

window.$Nav && $Nav.declare('config.regionalStores',["ctnow","ctnow","ctnow","ctnow"]);

window.$Nav && $Nav.declare('config.isALFRedesignPT2',false);

window.$Nav && $Nav.declare('config.isNavALFRegistryGiftList',false);

window.$Nav && $Nav.declare('config.marketplaceId','A21TJRUUN4KGV');

window.$Nav && $Nav.declare('config.exportTransitionState','none');

window.$Nav && $Nav.declare('config.enableAeeXopFlyout',false);

window.$Nav && $Nav.declare('config.isPrimeFlyoutMigrationEnabled',false);

window.$Nav && $Nav.declare('config.isAjaxMigrated',true);

window.$Nav && $Nav.declare('config.isAjaxSubnavFlyoutMigrated',true);

window.$Nav && $Nav.declare('config.isAjaxRefTagLoggerMigrated',true);

if (window.P && typeof window.P.declare === "function" && typeof window.P.now === "function") {
  window.P.now('packardGlowIngressJsEnabled').execute(function(glowEnabled) {
    if (!glowEnabled) {
      window.P.declare('packardGlowIngressJsEnabled', true);
    }
  });
  window.P.now('packardGlowStoreName').execute(function(storeName) {
    if (!storeName) {
      window.P.declare('packardGlowStoreName','generic');
    }
  });
}

window.$Nav && $Nav.declare('configComplete');

    -->
</script>


<a id="skippedLink" tabindex="-1"></a>

<script type='text/javascript'>window.navmet.MainEnd = new Date();</script>
<script type="text/javascript">
    if (window.ue_t0) {
      window.navmet.push({key:"NavMainEnd",end:+new Date(),begin:window.ue_t0});
    }
</script>
<!-- sp:end-feature:navbar -->
<!-- sp:feature:host-atf -->


<div role="main">
  <h1 class="a-spacing-top-small page-content page-min-width"><div id="cm_cr-brdcmb" class="a-section a-subheader a-breadcrumb celwidget"><ul class="a-unordered-list a-nostyle a-horizontal a-size-base"><li>
      <span class="a-list-item">
        <a class="a-link-normal" href="/New-Apple-iPhone-12-256GB/dp/B08L5VRVTD/ref=cm_cr_arp_d_bdcrb_top?ie=UTF8">Apple iPhone 12 (256GB) - White</a></span>
    </li>
    <li class="a-breadcrumb-divider">&rsaquo;</li>
    <li>
      <span class="a-list-item">
        <span class="a-color-state">Customer reviews</span></span>
    </li>
  </ul></div></h1><div class="a-fixed-right-grid page-content page-min-width a-spacing-top-medium"><div class="a-fixed-right-grid-inner" style="padding-right:305px"><div class="a-fixed-right-grid-col a-col-left" style="padding-right:1%;float:left;"><div id="cm_cr-product_info" class="a-fixed-left-grid product-details celwidget"><div class="a-fixed-left-grid-inner" style="padding-left:250px"><div class="a-text-left a-fixed-left-grid-col reviewNumericalSummary celwidget a-col-left" style="width:250px;margin-left:-250px;float:left;"><div class="a-row a-spacing-mini customerReviewsTitle"><h2 class="inline-title">Customer reviews</h2></div><div class="a-row a-spacing-small averageStarRatingIconAndCount"><div class="a-fixed-left-grid AverageCustomerReviews"><div class="a-fixed-left-grid-inner" style="padding-left:105px"><div class="a-fixed-left-grid-col a-col-left" style="width:105px;margin-left:-105px;float:left;"><i data-hook="average-star-rating" class="a-icon a-icon-star-medium a-star-medium-4-5 averageStarRating"><span class="a-icon-alt">4.5 out of 5 stars</span></i></div><div class="a-fixed-left-grid-col aok-align-center a-col-right" style="padding-left:0%;float:left;"><div class="a-row"><span data-hook="rating-out-of-text" class="a-size-medium a-color-base">4.5 out of 5</span></div></div></div></div></div><div data-hook="total-review-count" class="a-row a-spacing-medium averageStarRatingNumerical"><span class="a-size-base a-color-secondary">30,646 global ratings</span></div><div class="a-row"><div class="a-section histogram"><span class="a-declarative" data-action="reviews:filter-action:push-state" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:filter-action:push-state" data-reviews:filter-action:push-state="{&quot;scrollToSelector&quot;:&quot;#reviews-filter-info&quot;,&quot;allowLinkDefault&quot;:&quot;1&quot;}"><table id="histogramTable" class="a-normal a-spacing-none" role="presentation">








<table id="histogramTable" class="a-normal a-align-center a-spacing-base">
  














  
    
  
  











  
  

    
    <tr data-reftag="" data-reviews-state-param="{&quot;filterByStar&quot;:&quot;five_star&quot;, &quot;pageNumber&quot;:&quot;1&quot;}" aria-label="75% of reviews have 5 stars" class="a-histogram-row a-align-center">

      <td class="aok-nowrap">
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal 5star" title="75% of reviews have 5 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_5?ie=UTF8&amp;filterByStar=five_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            5 star
          </a>
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td class="a-span10">
        <a aria-disabled="true" class="a-link-normal" title="75% of reviews have 5 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_5?ie=UTF8&amp;filterByStar=five_star&amp;reviewerType=all_reviews#reviews-filter-bar">
          <div class="a-meter" role="progressbar" aria-valuenow="75%"><div class="a-meter-bar" style="width: 75%;"></div></div>
        </a>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal" title="75% of reviews have 5 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_5?ie=UTF8&amp;filterByStar=five_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            
              75%
            
          </a>
        </span>
      </td>
    </tr>

  


  














  
    
  
  











  
  

    
    <tr data-reftag="" data-reviews-state-param="{&quot;filterByStar&quot;:&quot;four_star&quot;, &quot;pageNumber&quot;:&quot;1&quot;}" aria-label="16% of reviews have 4 stars" class="a-histogram-row a-align-center">

      <td class="aok-nowrap">
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal 4star" title="16% of reviews have 4 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_4?ie=UTF8&amp;filterByStar=four_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            4 star
          </a>
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td class="a-span10">
        <a aria-disabled="true" class="a-link-normal" title="16% of reviews have 4 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_4?ie=UTF8&amp;filterByStar=four_star&amp;reviewerType=all_reviews#reviews-filter-bar">
          <div class="a-meter" role="progressbar" aria-valuenow="16%"><div class="a-meter-bar" style="width: 16%;"></div></div>
        </a>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal" title="16% of reviews have 4 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_4?ie=UTF8&amp;filterByStar=four_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            
              16%
            
          </a>
        </span>
      </td>
    </tr>

  


  














  
    
  
  











  
  

    
    <tr data-reftag="" data-reviews-state-param="{&quot;filterByStar&quot;:&quot;three_star&quot;, &quot;pageNumber&quot;:&quot;1&quot;}" aria-label="3% of reviews have 3 stars" class="a-histogram-row a-align-center">

      <td class="aok-nowrap">
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal 3star" title="3% of reviews have 3 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_3?ie=UTF8&amp;filterByStar=three_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            3 star
          </a>
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td class="a-span10">
        <a aria-disabled="true" class="a-link-normal" title="3% of reviews have 3 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_3?ie=UTF8&amp;filterByStar=three_star&amp;reviewerType=all_reviews#reviews-filter-bar">
          <div class="a-meter" role="progressbar" aria-valuenow="3%"><div class="a-meter-bar" style="width: 3%;"></div></div>
        </a>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal" title="3% of reviews have 3 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_3?ie=UTF8&amp;filterByStar=three_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            
              3%
            
          </a>
        </span>
      </td>
    </tr>

  


  














  
    
  
  











  
  

    
    <tr data-reftag="" data-reviews-state-param="{&quot;filterByStar&quot;:&quot;two_star&quot;, &quot;pageNumber&quot;:&quot;1&quot;}" aria-label="1% of reviews have 2 stars" class="a-histogram-row a-align-center">

      <td class="aok-nowrap">
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal 2star" title="1% of reviews have 2 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_2?ie=UTF8&amp;filterByStar=two_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            2 star
          </a>
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td class="a-span10">
        <a aria-disabled="true" class="a-link-normal" title="1% of reviews have 2 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_2?ie=UTF8&amp;filterByStar=two_star&amp;reviewerType=all_reviews#reviews-filter-bar">
          <div class="a-meter" role="progressbar" aria-valuenow="1%"><div class="a-meter-bar" style="width: 1%;"></div></div>
        </a>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal" title="1% of reviews have 2 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_2?ie=UTF8&amp;filterByStar=two_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            
              1%
            
          </a>
        </span>
      </td>
    </tr>

  


  














  
    
  
  











  
  

    
    <tr data-reftag="" data-reviews-state-param="{&quot;filterByStar&quot;:&quot;one_star&quot;, &quot;pageNumber&quot;:&quot;1&quot;}" aria-label="5% of reviews have 1 stars" class="a-histogram-row a-align-center">

      <td class="aok-nowrap">
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal 1star" title="5% of reviews have 1 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_1?ie=UTF8&amp;filterByStar=one_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            1 star
          </a>
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td class="a-span10">
        <a aria-disabled="true" class="a-link-normal" title="5% of reviews have 1 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_1?ie=UTF8&amp;filterByStar=one_star&amp;reviewerType=all_reviews#reviews-filter-bar">
          <div class="a-meter" role="progressbar" aria-valuenow="5%"><div class="a-meter-bar" style="width: 5%;"></div></div>
        </a>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal" title="5% of reviews have 1 stars" href="/product-reviews/B08L5VRVTD/ref=acr_dp_hist_1?ie=UTF8&amp;filterByStar=one_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            
              5%
            
          </a>
        </span>
      </td>
    </tr>

  


</table>
</table></span></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;float:left;"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:55px"><div class="a-text-center a-spacing-top-micro a-fixed-left-grid-col product-image a-col-left" style="width:65px;margin-left:-65px;float:left;"><a class="a-link-normal" href="/New-Apple-iPhone-12-256GB/dp/B08L5VRVTD/ref=cm_cr_arp_d_pdt_img_top?ie=UTF8"><img alt="Apple iPhone 12 (256GB) - White" src="https://m.media-amazon.com/images/I/317JiGToz-L._AC_US60_SCLZZZZZZZ__.jpg" data-hook="cr-product-image" height="60" width="60" data-a-hires="https://m.media-amazon.com/images/I/317JiGToz-L._AC_US120_SCLZZZZZZZ__.jpg"/></a></div><div class="a-fixed-left-grid-col product-info a-col-right" style="padding-left:2%;float:left;"><div class="a-row product-title"><h1 class="a-size-large a-text-ellipsis"><a data-hook="product-link" class="a-link-normal" href="/New-Apple-iPhone-12-256GB/dp/B08L5VRVTD/ref=cm_cr_arp_d_product_top?ie=UTF8">Apple iPhone 12 (256GB) - White</a></h1></div><div class="a-row product-by-line"><div data-hook="cr-product-byline" class="a-section">








  

  
  
    
  

  

  <span id="cr-arp-byline" class="a-size-base">
    by<span class="a-letter-space"></span><a class="a-size-base a-link-normal" href="/stores/Apple/page/88D59F86-9161-4804-A524-0A5B39CD714A?ref_=ast_bln">Apple</a>
  </span>

</div></div><div class="a-row a-spacing-top-medium product-variation-strip"><span class="a-size-base a-color-secondary">Colour: White<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Size: 256GB<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Pattern Name: iPhone 12</span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><a class="a-size-base a-link-normal" href="/New-Apple-iPhone-12-256GB/dp/B08L5VRVTD/ref=cm_cr_arp_d_product_top?ie=UTF8">Change</a></div></div></div></div></div></div></div><div class="a-fixed-left-grid ratings-solicitation"><div class="a-fixed-left-grid-inner" style="padding-left:250px"><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;float:left;"><div class="a-fixed-left-grid reviewSolicitation"><div class="a-fixed-left-grid-inner" style="padding-left:108px"><div class="a-fixed-left-grid-col a-col-left" style="width:108px;margin-left:-108px;float:left;"><span class="a-button a-button-base writeReviewButton"><span class="a-button-inner"><a href="/review/create-review/ref=cm_cr_arp_d_wr_but_lft?ie=UTF8&amp;channel=reviews-product&amp;asin=B08L5VRVTD" class="a-button-text">Write a review</a></span></span></div></div></div></div></div></div><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:800px"><div class="a-fixed-left-grid-col a-col-left" style="width:800px;margin-left:-800px;float:left;">









<div class="a-row a-expander-container a-spacing-top-medium a-expander-inline-container">
    
        
        
            <a data-csa-c-func-deps="aui-da-a-expander-toggle" data-csa-c-type="widget" data-csa-interaction-events="click" data-hook="cr-ratings-explanation-expand" aria-expanded="false" role="button" href="javascript:void(0)" data-action="a-expander-toggle" class="a-expander-header a-declarative a-expander-inline-header a-link-expander" data-a-expander-toggle="{&quot;allowLinkDefault&quot;:true, &quot;expand_prompt&quot;:&quot;&quot;, &quot;collapse_prompt&quot;:&quot;&quot;}"><i class="a-icon a-icon-expand"></i><span class="a-expander-prompt">
                How are ratings calculated?
            </span></a>
            <div aria-expanded="false" class="a-expander-content a-expander-inline-content a-expander-inner" style="display:none">
                To calculate the overall star rating and percentage breakdown by star, we don’t use a simple average. Instead, our system considers things like how recent a review is and if the reviewer bought the item on Amazon. It also analyses reviews to verify trustworthiness.
            </div>
        
    
</div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:3.5%;float:left;"></div></div></div></div><div class="a-text-right a-spacing-top-micro a-fixed-right-grid-col a-col-right" style="width:305px;margin-right:-305px;float:left;"><div id="cm_cr-buy_box" class="a-box reviews-buy-box celwidget"><div class="a-box-inner"><div class="a-row"><span class="a-button a-button-span12 a-button-primary add-to-cart"><span class="a-button-inner"><a href="/New-Apple-iPhone-12-256GB/dp/B08L5VRVTD/ref=cm_cr_arp_d_pb_opt?ie=UTF8" class="a-button-text">See All Buying Options</a></span></span></div></div></div></div></div></div><div class="a-section a-spacing-medium a-spacing-top-medium page-content"><hr id="reviews-summary" aria-hidden="true" class="a-divider-normal"/></div><noscript>
    <div class="a-section a-spacing-large a-spacing-top-mini a-text-center"><div class="a-box a-alert a-alert-warning reviews-no-js-warning" aria-live="polite" aria-atomic="true"><div class="a-box-inner a-alert-container"><i class="a-icon a-icon-alert"></i><div class="a-alert-content">This page works best with JavaScript. Disabling it will result in some disabled or missing features. You can still see all customer reviews for the product.</div></div></div></div></noscript>
</div>

<div>
  <div class="a-section a-spacing-small page-content page-min-width"><script type="text/javascript">
     if (ue) {
         uet('af');
     }
</script><script>
    window.P && P.register('af');
    window.P && P.register('sp.load.js');
</script>
      <div class="a-expander-content-fade"></div>
      <a aria-label="Toggle full review text" class="a-size-base a-link-normal" href="/gp/customer-reviews/R2BYU3Y39QIEQO/ref=cm_cr_arp_d_viewpnt?ie=UTF8&amp;ASIN=B08L5VRVTD#R2BYU3Y39QIEQO">Read more</a></div>
  </div><div class="a-row a-spacing-top-small"><span class="a-size-small a-color-tertiary"><span class="review-votes">
          806 people found this helpful</span>
      </span></div></div><div class="a-column a-span6 view-point-review critical-review a-span-last"><div id="viewpoint-R2KFN9F22D6F9Z" data-a-expander-collapsed-height="300" class="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container" style="max-height:300px"><div aria-expanded="false" class="a-expander-content a-expander-partial-collapse-content"><div class="a-row a-ws-row"><h4 class="a-size-medium view-point-title">Top critical review</h4></div><div class="a-row a-spacing-mini"><span class="a-declarative" data-action="reviews:filter-action:push-state" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:filter-action:push-state" data-reviews:filter-action:push-state="{&quot;allowLinkDefault&quot;:&quot;1&quot;}"><a data-reftag="cm_cr_arp_d_viewpnt_rgt" data-reviews-state-param="{&quot;filterByStar&quot;:&quot;critical&quot;,&quot;pageNumber&quot;:&quot;1&quot;}" class="a-size-base a-link-normal see-all" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&amp;filterByStar=critical&amp;reviewerType=avp_only_reviews&amp;formatType=current_format">All critical reviews</a><span class="a-letter-space"></span><span class="a-size-base back-carat a-text-bold">&rsaquo;&#32;</span></span></div><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AFMXTSGU2MBTA6SYJFKVWTTEEL5A/ref=cm_cr_arp_d_gw_rgt?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/7bf58633-d163-4796-81bd-c0fdc0e2a6a1._CR62,0,375,375_SX48_.jpg"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/7bf58633-d163-4796-81bd-c0fdc0e2a6a1._CR62,0,375,375_SX48_.jpg"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Navaneeth</span></div></a></div><div class="a-row"><i data-hook="review-star-rating-view-point" class="a-icon a-icon-star a-star-3 review-rating"><span class="a-icon-alt">3.0 out of 5 stars</span></i><span class="a-letter-space"></span><span data-hook="review-title" class="a-size-base review-title a-text-bold">Somehow Returned this</span></div><div class="a-row"><span class="a-size-base a-color-secondary review-date">Reviewed in India 🇮🇳 on 30 April 2022</span></div><div class="a-row a-spacing-top-mini"><span class="a-size-base">I got this product on 20th April 2022 and returned it on 28th April 2022 haha, with so much excitement I opened the product and started using it, since I was an Android to iOS user I did find some difficulties in using it but it was fine. The real problem started while using it,<br />The Phone started to overheat for minimal usages, I'd call for 5 to 10 minutes hands would be burning with phone heat, 15 minutes of social media again hands would be burning hot, I didn't get any temperature warning but heat was hot enuf for me to keep it aside for a long period of time, Due to overheat the battery used to die fast and I would hv required to charge it thrice a day. I roamed around the Apple authorized service centres and so many calls to Amazon for a replacement but nobody seems to give me any solution, then I thought I'll just use it, but again it started getting worse and I called Apple and they said to give my phone to service centre for 7 to 10 days so they can diagnosis be done and find out issue while I survive 7 to 10 days without a phone haha, then I couldn't take it anymore as I understood if I continue using this phone I wouldn't get 4 weeks yet alone 4 years and pleaded to Amazon coz I am a prime member ever since prime was out and I have ordered tons and tons of products in Amazon and never faced this issue.<br />But the hard earned money going like this was hurting so I submitted whatever documents Amazon asked me to get from Apple and finally they gave me return for this product.<br />The item has been returned and get to reach their warehouse which then oly I will get my refund initiated which is gonna take another 15 to 20 days, but I'm fine since I can wait and not lose my hard earned money. For now I hv a 7 year old phone as backup which is working ok ok but I can manage to write atleast this review.<br /><br />So whoever face this issue, and wants a replacement or return please try your best with whatever Amazon asks from you n they will provide a solution.<br /><br />I still need to buy an Apple phone next coz I bought the 2k adapter and it's return period got over haha.<br /><br />Anyways the Phone was amazing to use,<br />So performance wise 5/5<br />Camera was just amazing 5/5<br />Battery tho 1 or 2/5<br />Over heating so -2/5 or 0/5<br /><br />Overall a bad experience but still excited to get apple product.<br /><br />Btw Apple service centres help very well and listen to ur problems and provide solutions properly and handles it well.<br /><br />So if you are getting a iPhone I hope u guys don't face any situation like mine.<br /><br />Thank you n have  a great day :)</span></div></div><div
      class="a-expander-header a-expander-partial-collapse-header readMore">
      <div class="a-expander-content-fade"></div>
      <a aria-label="Toggle full review text" class="a-size-base a-link-normal" href="/gp/customer-reviews/R2KFN9F22D6F9Z/ref=cm_cr_arp_d_viewpnt?ie=UTF8&amp;ASIN=B08L5VRVTD#R2KFN9F22D6F9Z">Read more</a></div>
  </div><div class="a-row a-spacing-top-small"><span class="a-size-small a-color-tertiary"><span class="review-votes">
          9 people found this helpful</span>
      </span></div></div></div></div><hr aria-hidden="true" class="a-spacing-large a-divider-normal"/></div><a id="reviews-container" class="a-link-normal celwidget" href="#"></a><a id="reviews-filter-bar"></a>
            <div id="cm_cr-view_opt_search" class="a-row a-spacing-large celwidget reviews-sort-filter a-size-base"><div class="a-column a-span6 a-spacing-none reviews-search-section"><div data-reftag="cm_cr_arp_d_viewopt_kywd" class="a-fixed-right-grid reviews-search"><div class="a-fixed-right-grid-inner" style="padding-right:78px"><div class="a-fixed-right-grid-col a-col-left" style="padding-right:3.5%;float:left;"><span class="a-declarative" data-action="reviews:search-textbox" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:search-textbox" data-reviews:search-textbox="{}"><div class="a-search a-span12"><i class="a-icon a-icon-search"></i><input type="search" maxlength="300" id="filterByKeywordTextBox" placeholder="Search customer reviews" spellcheck="true" class="a-input-text a-span12"/></div></span></div><div class="a-fixed-right-grid-col a-col-right" style="width:78px;margin-right:-78px;float:left;"><span class="a-declarative" data-action="reviews:search-button" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:search-button" data-reviews:search-button="{}"><span class="a-button a-button-search"><span class="a-button-inner"><input class="a-button-input" type="submit"/><span class="a-button-text a-text-center" aria-hidden="true">Search</span></span></span></span></div></div></div></div></div><div id="cm_cr-view_opt_sort_filter" class="a-row a-spacing-small celwidget reviews-sort-filter a-size-base"><div class="a-section a-spacing-mini reviews-sort-order-options aok-float-left"><div class="a-row a-spacing-small"><span class="a-size-small a-color-base reviews-sort-order-label a-text-bold a-text-caps">Sort by</span></div><div class="a-row"><span class="a-dropdown-container"><select name="" autocomplete="off" id="sort-order-dropdown" tabindex="0" data-action="a-dropdown-select" class="a-native-dropdown a-declarative"><option data-reftag="cm_cr_arp_d_viewopt_srt" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;sortBy&quot;:&quot;helpful&quot;}" value="helpful" data-a-css-class="sort-order-option">Top reviews</option><option data-reftag="cm_cr_arp_d_viewopt_srt" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;sortBy&quot;:&quot;recent&quot;}" value="recent" data-a-css-class="sort-order-option">Most recent</option></select><span tabindex="-1" data-a-class="cr-sort-dropdown" class="a-button a-button-dropdown cr-sort-dropdown" aria-hidden="true"><span class="a-button-inner"><span class="a-button-text a-declarative" data-csa-c-func-deps="aui-da-a-dropdown-button" data-csa-c-type="widget" data-csa-interaction-events="click" data-action="a-dropdown-button" aria-hidden="true"><span class="a-dropdown-prompt">Top reviews</span></span><i class="a-icon a-icon-dropdown"></i></span></span></span></div></div><div class="a-section a-spacing-mini reviews-filter-by-options aok-float-left"><div class="a-row a-spacing-small"><span class="a-size-small a-color-base reviews-filter-by-label a-text-bold a-text-caps">Filter by</span></div><div class="a-row reviews-filter-by-dropdown"><div class="a-column a-span3 reviewer-type-select"><span class="a-dropdown-container"><select name="" autocomplete="off" id="reviewer-type-dropdown" tabindex="0" data-action="a-dropdown-select" class="a-native-dropdown a-declarative"><option data-reftag="cm_cr_arp_d_viewopt_rvwer" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;reviewerType&quot;:&quot;all_reviews&quot;}" value="all_reviews" data-a-css-class="reviewer-filter-option">All reviewers</option><option data-reftag="cm_cr_arp_d_viewopt_rvwer" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;reviewerType&quot;:&quot;avp_only_reviews&quot;}" value="avp_only_reviews" data-a-css-class="reviewer-filter-option" selected>Verified purchase only</option></select><span tabindex="-1" data-a-class="cr-filter-dropdown" class="a-button a-button-dropdown cr-filter-dropdown" aria-hidden="true"><span class="a-button-inner"><span class="a-button-text a-declarative" data-csa-c-func-deps="aui-da-a-dropdown-button" data-csa-c-type="widget" data-csa-interaction-events="click" data-action="a-dropdown-button" aria-hidden="true"><span class="a-dropdown-prompt">Verified purchase only</span></span><i class="a-icon a-icon-dropdown"></i></span></span></span></div><div class="a-column a-span3 star-rating-select"><span class="a-dropdown-container"><select name="" autocomplete="off" id="star-count-dropdown" tabindex="0" data-action="a-dropdown-select" class="a-native-dropdown a-declarative"><optgroup><option data-reftag="cm_cr_arp_d_viewopt_sr" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;filterByStar&quot;:&quot;all_stars&quot;}" value="all_stars" data-a-css-class="star-filter-option">All stars</option><option data-reftag="cm_cr_arp_d_viewopt_sr" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;filterByStar&quot;:&quot;five_star&quot;}" value="five_star" data-a-css-class="star-filter-option">5 star only</option><option data-reftag="cm_cr_arp_d_viewopt_sr" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;filterByStar&quot;:&quot;four_star&quot;}" value="four_star" data-a-css-class="star-filter-option">4 star only</option><option data-reftag="cm_cr_arp_d_viewopt_sr" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;filterByStar&quot;:&quot;three_star&quot;}" value="three_star" data-a-css-class="star-filter-option">3 star only</option><option data-reftag="cm_cr_arp_d_viewopt_sr" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;filterByStar&quot;:&quot;two_star&quot;}" value="two_star" data-a-css-class="star-filter-option">2 star only</option><option data-reftag="cm_cr_arp_d_viewopt_sr" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;filterByStar&quot;:&quot;one_star&quot;}" value="one_star" data-a-css-class="star-filter-option">1 star only</option></optgroup><optgroup><option data-reftag="cm_cr_arp_d_viewopt_sr" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;filterByStar&quot;:&quot;positive&quot;}" value="positive" data-a-css-class="star-filter-option">All positive</option><option data-reftag="cm_cr_arp_d_viewopt_sr" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;filterByStar&quot;:&quot;critical&quot;}" value="critical" data-a-css-class="star-filter-option">All critical</option></optgroup></select><span tabindex="-1" data-a-class="cr-filter-dropdown" class="a-button a-button-dropdown cr-filter-dropdown" aria-hidden="true"><span class="a-button-inner"><span class="a-button-text a-declarative" data-csa-c-func-deps="aui-da-a-dropdown-button" data-csa-c-type="widget" data-csa-interaction-events="click" data-action="a-dropdown-button" aria-hidden="true"><span class="a-dropdown-prompt">All stars</span></span><i class="a-icon a-icon-dropdown"></i></span></span></span></div><div class="a-column a-span3 format-type-select"><span class="a-dropdown-container"><select name="" autocomplete="off" id="format-type-dropdown" tabindex="0" data-action="a-dropdown-select" class="a-native-dropdown a-declarative"><option data-reftag="cm_cr_arp_d_viewopt_fmt" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;formatType&quot;:&quot;all_formats&quot;}" value="all_formats" data-a-css-class="format-filter-option">All formats</option><option data-reftag="cm_cr_arp_d_viewopt_fmt" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;formatType&quot;:&quot;current_format&quot;}" value="current_format" data-a-css-class="format-filter-option" data-a-html-content="Show only reviews for Colour: White |Size: 256GB |Pattern Name: iPhone 12" selected>Colour: White |Size: 256GB |Pattern Name: iPhone 12</option></select><span tabindex="-1" data-a-class="cr-filter-dropdown" class="a-button a-button-dropdown cr-filter-dropdown" aria-hidden="true"><span class="a-button-inner"><span class="a-button-text a-declarative" data-csa-c-func-deps="aui-da-a-dropdown-button" data-csa-c-type="widget" data-csa-interaction-events="click" data-action="a-dropdown-button" aria-hidden="true"><span class="a-dropdown-prompt">Colour: White |Size: 256GB |Pattern Name: iPhone 12</span></span><i class="a-icon a-icon-dropdown"></i></span></span></span></div><div class="a-column a-span3 cr-media-type-select a-span-last"><span class="a-dropdown-container"><select name="" autocomplete="off" id="media-type-dropdown" tabindex="0" data-action="a-dropdown-select" class="a-native-dropdown a-declarative"><option data-reftag="cm_cr_arp_d_viewopt_actns" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;mediaType&quot;:&quot;all_contents&quot;}" value="all_contents" data-a-css-class="cr-media-filter-option">All text, image and video reviews</option><option data-reftag="cm_cr_arp_d_viewopt_mdrvw" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;mediaType&quot;:&quot;media_reviews_only&quot;}" value="media_reviews_only" data-a-css-class="cr-media-filter-option">Image and video reviews only</option></select><span tabindex="-1" data-a-class="cr-filter-dropdown" class="a-button a-button-dropdown cr-filter-dropdown" aria-hidden="true"><span class="a-button-inner"><span class="a-button-text a-declarative" data-csa-c-func-deps="aui-da-a-dropdown-button" data-csa-c-type="widget" data-csa-interaction-events="click" data-action="a-dropdown-button" aria-hidden="true"><span class="a-dropdown-prompt">All text, image and video reviews</span></span><i class="a-icon a-icon-dropdown"></i></span></span></span></div></div></div></div><div id="filter-info-section" data-hook="cr-filter-info-section" class="a-section a-spacing-medium"><h5 data-hook="cr-filtered-by-text" class="a-spacing-micro a-color-tertiary a-text-bold a-text-caps">Filtered by</h5><div class="a-row a-spacing-micro a-size-base"><span id="reviews-filter-info-segment" data-hook="cr-filter-info-text" class="a-text-bold">Verified purchases, Colour: White<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Size: 256GB<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Pattern Name: iPhone 12</span><span class="a-letter-space"></span><span class="a-declarative" data-action="reviews:filter-action:push-state" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:filter-action:push-state" data-reviews:filter-action:push-state="{&quot;allowLinkDefault&quot;:&quot;1&quot;}"><a data-reftag="cm_cr_arp_d_show_all" data-reviews-state-param="{&quot;filterByStar&quot;:&quot;&quot;,&quot;pageNumber&quot;:&quot;1&quot;,&quot;reviewerType&quot;:&quot;all_reviews&quot;,&quot;filterByKeyword&quot;:&quot;&quot;,&quot;formatType&quot;:&quot;&quot;,&quot;mediaType&quot;:&quot;&quot;, &quot;filterByAge&quot;:&quot;&quot;}" class="a-size-base a-link-normal a-nowrap" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_show_all?ie=UTF8&amp;reviewerType=all_reviews">Clear filter</a></span></div><div data-hook="cr-filter-info-review-rating-count" class="a-row a-spacing-base a-size-base">

















    
        
            78 total ratings, 15 with reviews
        
    
    


</div><hr aria-hidden="true" class="a-spacing-medium a-divider-normal cr-full-screen-width"/></div><div class="a-section a-spacing-none reviews-content a-size-base"><div class="a-section cr-list-loading reviews-loading aok-hidden"></div><div class="a-section a-spacing-top-large a-text-center review-filter-error aok-hidden"><div class="a-box a-alert a-alert-error cr-error" role="alert"><div class="a-box-inner a-alert-container"><h4 class="a-alert-heading">There was a problem filtering reviews right now. Please try again later.</h4><i class="a-icon a-icon-alert"></i><div class="a-alert-content"></div></div></div></div><div class="a-section a-spacing-none reviews-content a-size-base"><div id="cm_cr-review_list" class="a-section a-spacing-none review-views celwidget"><h3 data-hook="arp-local-reviews-header" class="a-spacing-medium">








From India
</h3><div id="R3AGTFWRLRE0MA" data-hook="review" class="a-section review aok-relative"><div id="R3AGTFWRLRE0MA-review-card" class="a-row a-spacing-none"><div id="customer_review-R3AGTFWRLRE0MA" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AF65E3MU3MUXFJVLOEOAL46ZKHXQ/ref=cm_cr_arp_d_gw_btm?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Swapnil S Joshi</span></div></a></div><div class="a-row"><a class="a-link-normal" title="4.0 out of 5 stars" href="/gp/customer-reviews/R3AGTFWRLRE0MA/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-4 review-rating"><span class="a-icon-alt">4.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R3AGTFWRLRE0MA/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD">







  
  
    <span>Good and satisfactory upgrade for user having iphone series before 12</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in India 🇮🇳 on 9 December 2022</span><div class="a-row a-spacing-mini review-data review-format-strip"><a data-hook="format-strip" class="a-size-mini a-link-normal a-color-secondary" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_fmt?ie=UTF8&amp;formatType=current_format">Colour: White<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Size: 256GB<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Pattern Name: iPhone 12</a><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="reviews:filter-action:push-state" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:filter-action:push-state" data-reviews:filter-action:push-state="{}"><a data-reftag="cm_cr_arp_d_rvw_rvwer" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;reviewerType&quot;:&quot;avp_only_reviews&quot;}" class="a-link-normal" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_rvwer?ie=UTF8&amp;reviewerType=avp_only_reviews&amp;formatType=current_format"><span data-hook="avp-badge" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></a></span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text review-text-content">







  
  
    <span>Face scan unlock is perfect</span>
  
</span></div><div class="a-popover-preload" id="a-popover-R3AGTFWRLRE0MA_gallerySection_main">











 
  		 


<div id="R3AGTFWRLRE0MA_image_popover" data-hook="image-popover" class="a-section cr-lightbox-popover-container">

    
        
        
            <div class="cr-lightbox-image-viewer">
        <div class="cr-lightbox-main-image-container">
            <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/transparent-pixel._V192234675_.gif" class="cr-lightbox-main-image"/>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__back">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__back">
            </div>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__next">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__next">
            </div>
        </div>
    </div>
    <div class="a-section cr-lightbox-review-information">
        <div class="a-section a-spacing-mini cr-review-stars-and-title">

            <div class="a-row a-spacing-mini">
                <a href="/gp/profile/amzn1.account.AF65E3MU3MUXFJVLOEOAL46ZKHXQ/ref=cm_cr_arp_d_gw_pop?ie=UTF8" class="a-profile cr-lightbox-customer-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Swapnil S Joshi</span></div></a>
            </div>

            <i class="a-icon a-icon-star a-star-4 cr-lightbox-review-rating"><span class="a-icon-alt">4.0 out of 5 stars</span></i>
            <span class="a-size-base cr-lightbox-review-title a-text-bold">
                Good and satisfactory upgrade for user having iphone series before 12
            </span>
            <br>
            <span class="a-size-small a-color-secondary cr-lightbox-review-origin">
                
                    
                    
                        
                            Reviewed in India 🇮🇳 on 9 December 2022
                        
                    
                
            </span>
        </div>
        <span class="a-size-base cr-lightbox-review-body">
            Face scan unlock is perfect
        </span>
        <div class="a-section a-spacing-top-base">
            <span class="a-size-medium a-color-secondary">
                Images in this review 
            </span>
            <div class="a-section a-spacing-top-mini cr-lightbox-image-thumbnails">
                
                    
                        <img alt="Customer image" src="https://m.media-amazon.com/images/I/61R1dvS3jlL._SY88.jpg" class="cr-lightbox-image-thumbnail"/>
                    
                
            </div>
        </div>
    </div>
        
    
</div>



<script>
   function toggleSeeAllView() {
       P.when('A', 'cr-image-popover-controller').execute(function(A, imagePopoverController) {
          imagePopoverController.toggleSeeAllView(true);
       });
   }
</script>
</div><div id="R3AGTFWRLRE0MA_imageSection_main" class="a-section a-spacing-medium review-image-container"><div class="review-image-tile-section" data-reviewid="R3AGTFWRLRE0MA">
       <span class="a-declarative" data-action="a-modal" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-modal" data-a-modal="{&quot;name&quot;:&quot;R3AGTFWRLRE0MA_gallerySection_main&quot;}" id="R3AGTFWRLRE0MA-0"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><img alt="Customer image" src="https://m.media-amazon.com/images/I/61R1dvS3jlL._SY88.jpg" data-hook="review-image-tile" class="review-image-tile" height="88" width="100%"/><i class="a-icon a-icon-popover"></i></a></span></div>
</div><script>
        P.when('A', 'cr-image-popover-controller').execute(function(A, imagePopoverController) {
          A.on("a:popover:beforeShow:R3AGTFWRLRE0MA_gallerySection_main", function(data) {
            imagePopoverController.initImagePopover("R3AGTFWRLRE0MA", "[https://m.media-amazon.com/images/I/61R1dvS3jlL._SL1600_.jpg]", data);
          });
        });
    </script>
<div class="a-row review-comments comments-for-R3AGTFWRLRE0MA"><div data-reftag="cm_cr_arp_d_cmt_opn" data-a-expander-name="review_comment_expander" class="a-row a-expander-container a-expander-inline-container cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">One person found this helpful</span></div><!-- Components for Reactions C -->
    <div class="cr-helpful-button aok-float-left">
          <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.in/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_vote_lft%3Fie%3DUTF8%26reviewerType%3Davp_only_reviews%26csrfT%3DhBp9JxVBgyarO9VkXxNS0GbV10igkCEZTV8F8DdhzVkMAAAAAGRDx%252FcAAAAB%26formatType%3Dcurrent_format%26reviewId%3DR3AGTFWRLRE0MA&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=inflex&amp;openid.mode=checkid_setup&amp;marketPlaceId=A21TJRUUN4KGV&amp;language=en&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text"><div class="cr-helpful-text">
              Helpful</div>
          </a></span></span></div>
      </span><span class="cr-footer-line-height">
          <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hBp9JxVBgyarO9VkXxNS0GbV10igkCEZTV8F8DdhzVkMAAAAAGRDx%2FcAAAAB&amp;reviewId=R3AGTFWRLRE0MA&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hBp9JxVBgyarO9VkXxNS0GbV10igkCEZTV8F8DdhzVkMAAAAAGRDx%2FcAAAAB&amp;reviewId=R3AGTFWRLRE0MA">Report</a></span></span></span>

        <div aria-expanded="false" class="a-expander-content a-spacing-top-base a-spacing-large a-expander-inline-content a-expander-inner" style="display:none"><div class="a-row a-spacing-mini review-comments-header aok-hidden"><ul class="a-viewoptions-list a-viewoptions-section a-span12">
    <div class="a-row a-spacing-none a-grid-vertical-align a-grid-center"><div class="a-column a-span6"><span class="a-size-base a-viewoptions-list-label">Showing <span class='review-comment-count'>0</span> comments</span></div></div></ul>
</div><div class="a-section a-spacing-extra-large a-spacing-top-medium a-text-center comment-load-error aok-hidden"><div class="a-box a-alert a-alert-error cr-error" role="alert"><div class="a-box-inner a-alert-container"><h4 class="a-alert-heading">There was a problem loading comments right now. Please try again later.</h4><i class="a-icon a-icon-alert"></i><div class="a-alert-content"></div></div></div></div><div class="a-section a-spacing-none review-comments"></div><div class="a-spinner-wrapper comment-loading aok-hidden a-spacing-top-medium a-spacing-extra-large"><span class="a-spinner a-spinner-medium"></span></div><hr aria-hidden="true" class="a-spacing-none a-spacing-top-large a-divider-normal"/></div></div></div></div></div></div><div id="R10KVQXF1OBFIM" data-hook="review" class="a-section review aok-relative"><div id="R10KVQXF1OBFIM-review-card" class="a-row a-spacing-none"><div id="customer_review-R10KVQXF1OBFIM" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AFZWBQIYCQZ3RH3DTSETEPICYRPA/ref=cm_cr_arp_d_gw_btm?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/29b5d8b8-ecc6-41df-9828-828be1accf72._CR62,0,375,375_SX48_.jpg"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/29b5d8b8-ecc6-41df-9828-828be1accf72._CR62,0,375,375_SX48_.jpg"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Dipanjan Roychoudhary</span></div></a></div><div class="a-row"><a class="a-link-normal" title="5.0 out of 5 stars" href="/gp/customer-reviews/R10KVQXF1OBFIM/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R10KVQXF1OBFIM/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD">







  
  
    <span>Perfect replacement for a long time android user</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in India 🇮🇳 on 4 December 2020</span><div class="a-row a-spacing-mini review-data review-format-strip"><a data-hook="format-strip" class="a-size-mini a-link-normal a-color-secondary" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_fmt?ie=UTF8&amp;formatType=current_format">Colour: White<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Size: 256GB<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Pattern Name: iPhone 12</a><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="reviews:filter-action:push-state" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:filter-action:push-state" data-reviews:filter-action:push-state="{}"><a data-reftag="cm_cr_arp_d_rvw_rvwer" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;reviewerType&quot;:&quot;avp_only_reviews&quot;}" class="a-link-normal" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_rvwer?ie=UTF8&amp;reviewerType=avp_only_reviews&amp;formatType=current_format"><span data-hook="avp-badge" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></a></span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text review-text-content">







  
  
    <span>Okay I NEED TO CLEAR a few misconceptions about this phone because i am seeing a lot of negative reviews here which are not true, probably from IOS haters. I have been an android user since 2014 when I got my first phone, after many years i switched to Apple after complaining about their high prices  because i was disappointed with Samsung using Exynos processors for their flagship phones in India which causes heating, and Oneplus throwing one cheap model after another every six months.<br />And trust me guys its amazing. The software is butter smooth, i might never go back to android again.  FIRST OF ALL - who said the battery life is bad? I got my phone at 70 percent charge at 2 pm and after 24 hours it was 20 percent EVEN AFTER I KEPT MY DATA PACK ON THE WHOLE TIME.<br />SECONDLY- why are so many guys reviewing the phone on basis of the charger? everyone knows iphone 12 comes without an adapter. did you people not do your research before buying?<br />THIRD - the 60 Hz thing does not matter at all, flipping screen is  real quick u wont even notice the difference from a 120 Hz in android<br />and lastly - the AI is so sharp, be it the camera which automatically detects low light or even the face recognition.<br /><br />overall this phone is worth the high price. i will definitely be using it for 4-5 years. a happy customer here</span>
  
</span></div><div class="a-popover-preload" id="a-popover-R10KVQXF1OBFIM_gallerySection_main">











 
  		 


<div id="R10KVQXF1OBFIM_image_popover" data-hook="image-popover" class="a-section cr-lightbox-popover-container">

    
        
        
            <div class="cr-lightbox-image-viewer">
        <div class="cr-lightbox-main-image-container">
            <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/transparent-pixel._V192234675_.gif" class="cr-lightbox-main-image"/>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__back">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__back">
            </div>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__next">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__next">
            </div>
        </div>
    </div>
    <div class="a-section cr-lightbox-review-information">
        <div class="a-section a-spacing-mini cr-review-stars-and-title">

            <div class="a-row a-spacing-mini">
                <a href="/gp/profile/amzn1.account.AFZWBQIYCQZ3RH3DTSETEPICYRPA/ref=cm_cr_arp_d_gw_pop?ie=UTF8" class="a-profile cr-lightbox-customer-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/29b5d8b8-ecc6-41df-9828-828be1accf72._CR62,0,375,375_SX48_.jpg"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/29b5d8b8-ecc6-41df-9828-828be1accf72._CR62,0,375,375_SX48_.jpg"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Dipanjan Roychoudhary</span></div></a>
            </div>

            <i class="a-icon a-icon-star a-star-5 cr-lightbox-review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i>
            <span class="a-size-base cr-lightbox-review-title a-text-bold">
                Perfect replacement for a long time android user
            </span>
            <br>
            <span class="a-size-small a-color-secondary cr-lightbox-review-origin">
                
                    
                    
                        
                            Reviewed in India 🇮🇳 on 4 December 2020
                        
                    
                
            </span>
        </div>
        <span class="a-size-base cr-lightbox-review-body">
            Okay I NEED TO CLEAR a few misconceptions about this phone because i am seeing a lot of negative reviews here which are not true, probably from IOS haters. I have been an android user since 2014 when I got my first phone, after many years i switched to Apple after complaining about their high prices  because i was disappointed with Samsung using Exynos processors for their flagship phones in India which causes heating, and Oneplus throwing one cheap model after another every six months.<br />And trust me guys its amazing. The software is butter smooth, i might never go back to android again.  FIRST OF ALL - who said the battery life is bad? I got my phone at 70 percent charge at 2 pm and after 24 hours it was 20 percent EVEN AFTER I KEPT MY DATA PACK ON THE WHOLE TIME.<br />SECONDLY- why are so many guys reviewing the phone on basis of the charger? everyone knows iphone 12 comes without an adapter. did you people not do your research before buying?<br />THIRD - the 60 Hz thing does not matter at all, flipping screen is  real quick u wont even notice the difference from a 120 Hz in android<br />and lastly - the AI is so sharp, be it the camera which automatically detects low light or even the face recognition.<br /><br />overall this phone is worth the high price. i will definitely be using it for 4-5 years. a happy customer here
        </span>
        <div class="a-section a-spacing-top-base">
            <span class="a-size-medium a-color-secondary">
                Images in this review 
            </span>
            <div class="a-section a-spacing-top-mini cr-lightbox-image-thumbnails">
                
                    
                        <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/71CnzpJTD6L._SY88.jpg" class="cr-lightbox-image-thumbnail"/>
                    
                        <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/71qKVD+tTVL._SY88.jpg" class="cr-lightbox-image-thumbnail"/>
                    
                        <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/71ySlYrc+IL._SY88.jpg" class="cr-lightbox-image-thumbnail"/>
                    
                        <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/817-JASY9TL._SY88.jpg" class="cr-lightbox-image-thumbnail"/>
                    
                        <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/81ofRKMWXqL._SY88.jpg" class="cr-lightbox-image-thumbnail"/>
                    
                
            </div>
        </div>
    </div>
        
    
</div>



<script>
   function toggleSeeAllView() {
       P.when('A', 'cr-image-popover-controller').execute(function(A, imagePopoverController) {
          imagePopoverController.toggleSeeAllView(true);
       });
   }
</script>
</div><div id="R10KVQXF1OBFIM_imageSection_main" class="a-section a-spacing-medium review-image-container"><div class="review-image-tile-section" data-reviewid="R10KVQXF1OBFIM">
       <span class="a-declarative" data-action="a-modal" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-modal" data-a-modal="{&quot;name&quot;:&quot;R10KVQXF1OBFIM_gallerySection_main&quot;}" id="R10KVQXF1OBFIM-0"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/71CnzpJTD6L._SY88.jpg" data-hook="review-image-tile" class="review-image-tile" height="88" width="100%"/><i class="a-icon a-icon-popover"></i></a></span><span class="a-declarative" data-action="a-modal" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-modal" data-a-modal="{&quot;name&quot;:&quot;R10KVQXF1OBFIM_gallerySection_main&quot;}" id="R10KVQXF1OBFIM-1"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/71qKVD+tTVL._SY88.jpg" data-hook="review-image-tile" class="review-image-tile" height="88" width="100%"/><i class="a-icon a-icon-popover"></i></a></span><span class="a-declarative" data-action="a-modal" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-modal" data-a-modal="{&quot;name&quot;:&quot;R10KVQXF1OBFIM_gallerySection_main&quot;}" id="R10KVQXF1OBFIM-2"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/71ySlYrc+IL._SY88.jpg" data-hook="review-image-tile" class="review-image-tile" height="88" width="100%"/><i class="a-icon a-icon-popover"></i></a></span><span class="a-declarative" data-action="a-modal" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-modal" data-a-modal="{&quot;name&quot;:&quot;R10KVQXF1OBFIM_gallerySection_main&quot;}" id="R10KVQXF1OBFIM-3"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/817-JASY9TL._SY88.jpg" data-hook="review-image-tile" class="review-image-tile" height="88" width="100%"/><i class="a-icon a-icon-popover"></i></a></span><span class="a-declarative" data-action="a-modal" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-modal" data-a-modal="{&quot;name&quot;:&quot;R10KVQXF1OBFIM_gallerySection_main&quot;}" id="R10KVQXF1OBFIM-4"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/I/81ofRKMWXqL._SY88.jpg" data-hook="review-image-tile" class="review-image-tile" height="88" width="100%"/><i class="a-icon a-icon-popover"></i></a></span></div>
</div><script>
        P.when('A', 'cr-image-popover-controller').execute(function(A, imagePopoverController) {
          A.on("a:popover:beforeShow:R10KVQXF1OBFIM_gallerySection_main", function(data) {
            imagePopoverController.initImagePopover("R10KVQXF1OBFIM", "[https://images-na.ssl-images-amazon.com/images/I/71CnzpJTD6L._SL1600_.jpg, https://images-na.ssl-images-amazon.com/images/I/71qKVD+tTVL._SL1600_.jpg, https://images-na.ssl-images-amazon.com/images/I/71ySlYrc+IL._SL1600_.jpg, https://images-na.ssl-images-amazon.com/images/I/817-JASY9TL._SL1600_.jpg, https://images-na.ssl-images-amazon.com/images/I/81ofRKMWXqL._SL1600_.jpg]", data);
          });
        });
    </script>
<div class="a-row review-comments comments-for-R10KVQXF1OBFIM"><div data-reftag="cm_cr_arp_d_cmt_opn" data-a-expander-name="review_comment_expander" class="a-row a-expander-container a-expander-inline-container cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">48 people found this helpful</span></div><!-- Components for Reactions C -->
    <div class="cr-helpful-button aok-float-left">
          <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.in/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_vote_lft%3Fie%3DUTF8%26reviewerType%3Davp_only_reviews%26csrfT%3DhNves0NEeUUMF0K2JUbTXjpz8FKi%252BKXIm5%252BWZbrHq18rAAAAAGRDx%252FcAAAAB%26formatType%3Dcurrent_format%26reviewId%3DR10KVQXF1OBFIM&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=inflex&amp;openid.mode=checkid_setup&amp;marketPlaceId=A21TJRUUN4KGV&amp;language=en&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text"><div class="cr-helpful-text">
              Helpful</div>
          </a></span></span></div>
      </span><span class="cr-footer-line-height">
          <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hNves0NEeUUMF0K2JUbTXjpz8FKi%2BKXIm5%2BWZbrHq18rAAAAAGRDx%2FcAAAAB&amp;reviewId=R10KVQXF1OBFIM&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hNves0NEeUUMF0K2JUbTXjpz8FKi%2BKXIm5%2BWZbrHq18rAAAAAGRDx%2FcAAAAB&amp;reviewId=R10KVQXF1OBFIM">Report</a></span></span></span>

        <div aria-expanded="false" class="a-expander-content a-spacing-top-base a-spacing-large a-expander-inline-content a-expander-inner" style="display:none"><div class="a-row a-spacing-mini review-comments-header aok-hidden"><ul class="a-viewoptions-list a-viewoptions-section a-span12">
    <div class="a-row a-spacing-none a-grid-vertical-align a-grid-center"><div class="a-column a-span6"><span class="a-size-base a-viewoptions-list-label">Showing <span class='review-comment-count'>0</span> comments</span></div></div></ul>
</div><div class="a-section a-spacing-extra-large a-spacing-top-medium a-text-center comment-load-error aok-hidden"><div class="a-box a-alert a-alert-error cr-error" role="alert"><div class="a-box-inner a-alert-container"><h4 class="a-alert-heading">There was a problem loading comments right now. Please try again later.</h4><i class="a-icon a-icon-alert"></i><div class="a-alert-content"></div></div></div></div><div class="a-section a-spacing-none review-comments"></div><div class="a-spinner-wrapper comment-loading aok-hidden a-spacing-top-medium a-spacing-extra-large"><span class="a-spinner a-spinner-medium"></span></div><hr aria-hidden="true" class="a-spacing-none a-spacing-top-large a-divider-normal"/></div></div></div></div></div></div><div id="R256URPI6KX7L" data-hook="review" class="a-section review aok-relative"><div id="R256URPI6KX7L-review-card" class="a-row a-spacing-none"><div id="customer_review-R256URPI6KX7L" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AFRIYQYYROBHK2APF4PUMFN4VQKQ/ref=cm_cr_arp_d_gw_btm?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">sunny kumar</span></div></a></div><div class="a-row"><a class="a-link-normal" title="5.0 out of 5 stars" href="/gp/customer-reviews/R256URPI6KX7L/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R256URPI6KX7L/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD">







  
  
    <span>awesom</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in India 🇮🇳 on 13 November 2022</span><div class="a-row a-spacing-mini review-data review-format-strip"><a data-hook="format-strip" class="a-size-mini a-link-normal a-color-secondary" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_fmt?ie=UTF8&amp;formatType=current_format">Colour: White<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Size: 256GB<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Pattern Name: iPhone 12</a><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="reviews:filter-action:push-state" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:filter-action:push-state" data-reviews:filter-action:push-state="{}"><a data-reftag="cm_cr_arp_d_rvw_rvwer" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;reviewerType&quot;:&quot;avp_only_reviews&quot;}" class="a-link-normal" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_rvwer?ie=UTF8&amp;reviewerType=avp_only_reviews&amp;formatType=current_format"><span data-hook="avp-badge" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></a></span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text review-text-content">







  
  
    <span>amazing camera and battery performance</span>
  
</span></div><div class="a-popover-preload" id="a-popover-R256URPI6KX7L_gallerySection_main">











 
  		 


<div id="R256URPI6KX7L_image_popover" data-hook="image-popover" class="a-section cr-lightbox-popover-container">

    
        
        
            <div class="cr-lightbox-image-viewer">
        <div class="cr-lightbox-main-image-container">
            <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/transparent-pixel._V192234675_.gif" class="cr-lightbox-main-image"/>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__back">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__back">
            </div>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__next">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__next">
            </div>
        </div>
    </div>
    <div class="a-section cr-lightbox-review-information">
        <div class="a-section a-spacing-mini cr-review-stars-and-title">

            <div class="a-row a-spacing-mini">
                <a href="/gp/profile/amzn1.account.AFRIYQYYROBHK2APF4PUMFN4VQKQ/ref=cm_cr_arp_d_gw_pop?ie=UTF8" class="a-profile cr-lightbox-customer-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">sunny kumar</span></div></a>
            </div>

            <i class="a-icon a-icon-star a-star-5 cr-lightbox-review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i>
            <span class="a-size-base cr-lightbox-review-title a-text-bold">
                awesom
            </span>
            <br>
            <span class="a-size-small a-color-secondary cr-lightbox-review-origin">
                
                    
                    
                        
                            Reviewed in India 🇮🇳 on 13 November 2022
                        
                    
                
            </span>
        </div>
        <span class="a-size-base cr-lightbox-review-body">
            amazing camera and battery performance
        </span>
        <div class="a-section a-spacing-top-base">
            <span class="a-size-medium a-color-secondary">
                Images in this review 
            </span>
            <div class="a-section a-spacing-top-mini cr-lightbox-image-thumbnails">
                
                    
                        <img alt="Customer image" src="https://m.media-amazon.com/images/I/71zxmeU2kCL._SY88.jpg" class="cr-lightbox-image-thumbnail"/>
                    
                
            </div>
        </div>
    </div>
        
    
</div>



<script>
   function toggleSeeAllView() {
       P.when('A', 'cr-image-popover-controller').execute(function(A, imagePopoverController) {
          imagePopoverController.toggleSeeAllView(true);
       });
   }
</script>
</div><div id="R256URPI6KX7L_imageSection_main" class="a-section a-spacing-medium review-image-container"><div class="review-image-tile-section" data-reviewid="R256URPI6KX7L">
       <span class="a-declarative" data-action="a-modal" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-modal" data-a-modal="{&quot;name&quot;:&quot;R256URPI6KX7L_gallerySection_main&quot;}" id="R256URPI6KX7L-0"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><img alt="Customer image" src="https://m.media-amazon.com/images/I/71zxmeU2kCL._SY88.jpg" data-hook="review-image-tile" class="review-image-tile" height="88" width="100%"/><i class="a-icon a-icon-popover"></i></a></span></div>
</div><script>
        P.when('A', 'cr-image-popover-controller').execute(function(A, imagePopoverController) {
          A.on("a:popover:beforeShow:R256URPI6KX7L_gallerySection_main", function(data) {
            imagePopoverController.initImagePopover("R256URPI6KX7L", "[https://m.media-amazon.com/images/I/71zxmeU2kCL._SL1600_.jpg]", data);
          });
        });
    </script>
<div class="a-row review-comments comments-for-R256URPI6KX7L"><div data-reftag="cm_cr_arp_d_cmt_opn" data-a-expander-name="review_comment_expander" class="a-row a-expander-container a-expander-inline-container cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <!-- Components for Reactions C -->
    <div class="cr-helpful-button aok-float-left">
          <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.in/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_vote_lft%3Fie%3DUTF8%26reviewerType%3Davp_only_reviews%26csrfT%3DhErPaY6fNGOxLQ6uOapKgYjLpTX6iQEXs4beYzFcoZi%252FAAAAAGRDx%252FcAAAAB%26formatType%3Dcurrent_format%26reviewId%3DR256URPI6KX7L&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=inflex&amp;openid.mode=checkid_setup&amp;marketPlaceId=A21TJRUUN4KGV&amp;language=en&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text"><div class="cr-helpful-text">
              Helpful</div>
          </a></span></span></div>
      </span><span class="cr-footer-line-height">
          <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hErPaY6fNGOxLQ6uOapKgYjLpTX6iQEXs4beYzFcoZi%2FAAAAAGRDx%2FcAAAAB&amp;reviewId=R256URPI6KX7L&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hErPaY6fNGOxLQ6uOapKgYjLpTX6iQEXs4beYzFcoZi%2FAAAAAGRDx%2FcAAAAB&amp;reviewId=R256URPI6KX7L">Report</a></span></span></span>

        <div aria-expanded="false" class="a-expander-content a-spacing-top-base a-spacing-large a-expander-inline-content a-expander-inner" style="display:none"><div class="a-row a-spacing-mini review-comments-header aok-hidden"><ul class="a-viewoptions-list a-viewoptions-section a-span12">
    <div class="a-row a-spacing-none a-grid-vertical-align a-grid-center"><div class="a-column a-span6"><span class="a-size-base a-viewoptions-list-label">Showing <span class='review-comment-count'>0</span> comments</span></div></div></ul>
</div><div class="a-section a-spacing-extra-large a-spacing-top-medium a-text-center comment-load-error aok-hidden"><div class="a-box a-alert a-alert-error cr-error" role="alert"><div class="a-box-inner a-alert-container"><h4 class="a-alert-heading">There was a problem loading comments right now. Please try again later.</h4><i class="a-icon a-icon-alert"></i><div class="a-alert-content"></div></div></div></div><div class="a-section a-spacing-none review-comments"></div><div class="a-spinner-wrapper comment-loading aok-hidden a-spacing-top-medium a-spacing-extra-large"><span class="a-spinner a-spinner-medium"></span></div><hr aria-hidden="true" class="a-spacing-none a-spacing-top-large a-divider-normal"/></div></div></div></div></div></div><div id="R1KN2NUHV83U90" data-hook="review" class="a-section review aok-relative"><div id="R1KN2NUHV83U90-review-card" class="a-row a-spacing-none"><div id="customer_review-R1KN2NUHV83U90" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AFWIMRZH26JBFYFNBNCBTSHN6NEA/ref=cm_cr_arp_d_gw_btm?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Anand s.</span></div></a></div><div class="a-row"><a class="a-link-normal" title="3.0 out of 5 stars" href="/gp/customer-reviews/R1KN2NUHV83U90/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-3 review-rating"><span class="a-icon-alt">3.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R1KN2NUHV83U90/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD">







  
  
    <span>Truecaller proper work nahin karta hai aur call recording bhi nahin Hoti hai</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in India 🇮🇳 on 3 October 2022</span><div class="a-row a-spacing-mini review-data review-format-strip"><a data-hook="format-strip" class="a-size-mini a-link-normal a-color-secondary" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_fmt?ie=UTF8&amp;formatType=current_format">Colour: White<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Size: 256GB<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Pattern Name: iPhone 12</a><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="reviews:filter-action:push-state" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:filter-action:push-state" data-reviews:filter-action:push-state="{}"><a data-reftag="cm_cr_arp_d_rvw_rvwer" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;reviewerType&quot;:&quot;avp_only_reviews&quot;}" class="a-link-normal" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_rvwer?ie=UTF8&amp;reviewerType=avp_only_reviews&amp;formatType=current_format"><span data-hook="avp-badge" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></a></span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text review-text-content">







  
  
    <span>iPhone mein call recording nahin Hoti hai aur Truecaller bhi diling mein work nahin karta hai jabki yah donon features bahut avashyak hote Hain</span>
  
</span></div><div class="a-row review-comments comments-for-R1KN2NUHV83U90"><div data-reftag="cm_cr_arp_d_cmt_opn" data-a-expander-name="review_comment_expander" class="a-row a-expander-container a-expander-inline-container cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <!-- Components for Reactions C -->
    <div class="cr-helpful-button aok-float-left">
          <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.in/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_vote_lft%3Fie%3DUTF8%26reviewerType%3Davp_only_reviews%26csrfT%3DhLIoFlmJ8gi9Q8MSK9nVXHxcQZzDXLnARvrYIieMxrfyAAAAAGRDx%252FcAAAAB%26formatType%3Dcurrent_format%26reviewId%3DR1KN2NUHV83U90&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=inflex&amp;openid.mode=checkid_setup&amp;marketPlaceId=A21TJRUUN4KGV&amp;language=en&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text"><div class="cr-helpful-text">
              Helpful</div>
          </a></span></span></div>
      </span><span class="cr-footer-line-height">
          <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hLIoFlmJ8gi9Q8MSK9nVXHxcQZzDXLnARvrYIieMxrfyAAAAAGRDx%2FcAAAAB&amp;reviewId=R1KN2NUHV83U90&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hLIoFlmJ8gi9Q8MSK9nVXHxcQZzDXLnARvrYIieMxrfyAAAAAGRDx%2FcAAAAB&amp;reviewId=R1KN2NUHV83U90">Report</a></span></span></span>

        <div aria-expanded="false" class="a-expander-content a-spacing-top-base a-spacing-large a-expander-inline-content a-expander-inner" style="display:none"><div class="a-row a-spacing-mini review-comments-header aok-hidden"><ul class="a-viewoptions-list a-viewoptions-section a-span12">
    <div class="a-row a-spacing-none a-grid-vertical-align a-grid-center"><div class="a-column a-span6"><span class="a-size-base a-viewoptions-list-label">Showing <span class='review-comment-count'>0</span> comments</span></div></div></ul>
</div><div class="a-section a-spacing-extra-large a-spacing-top-medium a-text-center comment-load-error aok-hidden"><div class="a-box a-alert a-alert-error cr-error" role="alert"><div class="a-box-inner a-alert-container"><h4 class="a-alert-heading">There was a problem loading comments right now. Please try again later.</h4><i class="a-icon a-icon-alert"></i><div class="a-alert-content"></div></div></div></div><div class="a-section a-spacing-none review-comments"></div><div class="a-spinner-wrapper comment-loading aok-hidden a-spacing-top-medium a-spacing-extra-large"><span class="a-spinner a-spinner-medium"></span></div><hr aria-hidden="true" class="a-spacing-none a-spacing-top-large a-divider-normal"/></div></div></div></div></div></div><div id="R1V6FEDBUNUJG5" data-hook="review" class="a-section review aok-relative"><div id="R1V6FEDBUNUJG5-review-card" class="a-row a-spacing-none"><div id="customer_review-R1V6FEDBUNUJG5" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AFJUYZAT56UPZIWVO5XO4ZCUJBNA/ref=cm_cr_arp_d_gw_btm?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Anjula</span></div></a></div><div class="a-row"><a class="a-link-normal" title="5.0 out of 5 stars" href="/gp/customer-reviews/R1V6FEDBUNUJG5/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R1V6FEDBUNUJG5/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD">







  
  
    <span>Awesome 👍</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in India 🇮🇳 on 9 October 2022</span><div class="a-row a-spacing-mini review-data review-format-strip"><a data-hook="format-strip" class="a-size-mini a-link-normal a-color-secondary" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_fmt?ie=UTF8&amp;formatType=current_format">Colour: White<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Size: 256GB<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Pattern Name: iPhone 12</a><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="reviews:filter-action:push-state" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:filter-action:push-state" data-reviews:filter-action:push-state="{}"><a data-reftag="cm_cr_arp_d_rvw_rvwer" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;reviewerType&quot;:&quot;avp_only_reviews&quot;}" class="a-link-normal" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_rvwer?ie=UTF8&amp;reviewerType=avp_only_reviews&amp;formatType=current_format"><span data-hook="avp-badge" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></a></span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text review-text-content">







  
  
    <span>I like it so much ❤️❤️</span>
  
</span></div><div class="a-popover-preload" id="a-popover-R1V6FEDBUNUJG5_gallerySection_main">











 
  		 


<div id="R1V6FEDBUNUJG5_image_popover" data-hook="image-popover" class="a-section cr-lightbox-popover-container">

    
        
        
            <div class="cr-lightbox-image-viewer">
        <div class="cr-lightbox-main-image-container">
            <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/transparent-pixel._V192234675_.gif" class="cr-lightbox-main-image"/>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__back">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__back">
            </div>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__next">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__next">
            </div>
        </div>
    </div>
    <div class="a-section cr-lightbox-review-information">
        <div class="a-section a-spacing-mini cr-review-stars-and-title">

            <div class="a-row a-spacing-mini">
                <a href="/gp/profile/amzn1.account.AFJUYZAT56UPZIWVO5XO4ZCUJBNA/ref=cm_cr_arp_d_gw_pop?ie=UTF8" class="a-profile cr-lightbox-customer-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Anjula</span></div></a>
            </div>

            <i class="a-icon a-icon-star a-star-5 cr-lightbox-review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i>
            <span class="a-size-base cr-lightbox-review-title a-text-bold">
                Awesome 👍
            </span>
            <br>
            <span class="a-size-small a-color-secondary cr-lightbox-review-origin">
                
                    
                    
                        
                            Reviewed in India 🇮🇳 on 9 October 2022
                        
                    
                
            </span>
        </div>
        <span class="a-size-base cr-lightbox-review-body">
            I like it so much ❤️❤️
        </span>
        <div class="a-section a-spacing-top-base">
            <span class="a-size-medium a-color-secondary">
                Images in this review 
            </span>
            <div class="a-section a-spacing-top-mini cr-lightbox-image-thumbnails">
                
                    
                        <img alt="Customer image" src="https://m.media-amazon.com/images/I/818H4siLt9L._SY88.jpg" class="cr-lightbox-image-thumbnail"/>
                    
                
            </div>
        </div>
    </div>
        
    
</div>



<script>
   function toggleSeeAllView() {
       P.when('A', 'cr-image-popover-controller').execute(function(A, imagePopoverController) {
          imagePopoverController.toggleSeeAllView(true);
       });
   }
</script>
</div><div id="R1V6FEDBUNUJG5_imageSection_main" class="a-section a-spacing-medium review-image-container"><div class="review-image-tile-section" data-reviewid="R1V6FEDBUNUJG5">
       <span class="a-declarative" data-action="a-modal" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-modal" data-a-modal="{&quot;name&quot;:&quot;R1V6FEDBUNUJG5_gallerySection_main&quot;}" id="R1V6FEDBUNUJG5-0"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><img alt="Customer image" src="https://m.media-amazon.com/images/I/818H4siLt9L._SY88.jpg" data-hook="review-image-tile" class="review-image-tile" height="88" width="100%"/><i class="a-icon a-icon-popover"></i></a></span></div>
</div><script>
        P.when('A', 'cr-image-popover-controller').execute(function(A, imagePopoverController) {
          A.on("a:popover:beforeShow:R1V6FEDBUNUJG5_gallerySection_main", function(data) {
            imagePopoverController.initImagePopover("R1V6FEDBUNUJG5", "[https://m.media-amazon.com/images/I/818H4siLt9L._SL1600_.jpg]", data);
          });
        });
    </script>
<div class="a-row review-comments comments-for-R1V6FEDBUNUJG5"><div data-reftag="cm_cr_arp_d_cmt_opn" data-a-expander-name="review_comment_expander" class="a-row a-expander-container a-expander-inline-container cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <!-- Components for Reactions C -->
    <div class="cr-helpful-button aok-float-left">
          <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.in/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_vote_lft%3Fie%3DUTF8%26reviewerType%3Davp_only_reviews%26csrfT%3DhOS5mkPoVIrOOnIBSkzEvQRhk6y%252FxTI8TaHB2%252B0Z9rH%252FAAAAAGRDx%252FcAAAAB%26formatType%3Dcurrent_format%26reviewId%3DR1V6FEDBUNUJG5&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=inflex&amp;openid.mode=checkid_setup&amp;marketPlaceId=A21TJRUUN4KGV&amp;language=en&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text"><div class="cr-helpful-text">
              Helpful</div>
          </a></span></span></div>
      </span><span class="cr-footer-line-height">
          <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hOS5mkPoVIrOOnIBSkzEvQRhk6y%2FxTI8TaHB2%2B0Z9rH%2FAAAAAGRDx%2FcAAAAB&amp;reviewId=R1V6FEDBUNUJG5&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hOS5mkPoVIrOOnIBSkzEvQRhk6y%2FxTI8TaHB2%2B0Z9rH%2FAAAAAGRDx%2FcAAAAB&amp;reviewId=R1V6FEDBUNUJG5">Report</a></span></span></span>

        <div aria-expanded="false" class="a-expander-content a-spacing-top-base a-spacing-large a-expander-inline-content a-expander-inner" style="display:none"><div class="a-row a-spacing-mini review-comments-header aok-hidden"><ul class="a-viewoptions-list a-viewoptions-section a-span12">
    <div class="a-row a-spacing-none a-grid-vertical-align a-grid-center"><div class="a-column a-span6"><span class="a-size-base a-viewoptions-list-label">Showing <span class='review-comment-count'>0</span> comments</span></div></div></ul>
</div><div class="a-section a-spacing-extra-large a-spacing-top-medium a-text-center comment-load-error aok-hidden"><div class="a-box a-alert a-alert-error cr-error" role="alert"><div class="a-box-inner a-alert-container"><h4 class="a-alert-heading">There was a problem loading comments right now. Please try again later.</h4><i class="a-icon a-icon-alert"></i><div class="a-alert-content"></div></div></div></div><div class="a-section a-spacing-none review-comments"></div><div class="a-spinner-wrapper comment-loading aok-hidden a-spacing-top-medium a-spacing-extra-large"><span class="a-spinner a-spinner-medium"></span></div><hr aria-hidden="true" class="a-spacing-none a-spacing-top-large a-divider-normal"/></div></div></div></div></div></div><div id="RQQ0XR6JYXW17" data-hook="review" class="a-section review aok-relative"><div id="RQQ0XR6JYXW17-review-card" class="a-row a-spacing-none"><div id="customer_review-RQQ0XR6JYXW17" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AECOQZQBK2GKUMDNXM5GR7SV24CQ/ref=cm_cr_arp_d_gw_btm?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/35a70e63-6801-448e-9126-3ed6efb75cbd._CR0,0,500,500_SX48_.jpg"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/35a70e63-6801-448e-9126-3ed6efb75cbd._CR0,0,500,500_SX48_.jpg"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">kishor patil</span></div></a></div><div class="a-row"><a class="a-link-normal" title="5.0 out of 5 stars" href="/gp/customer-reviews/RQQ0XR6JYXW17/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/RQQ0XR6JYXW17/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD">







  
  
    <span>Nice iPhone 12</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in India 🇮🇳 on 13 October 2022</span><div class="a-row a-spacing-mini review-data review-format-strip"><a data-hook="format-strip" class="a-size-mini a-link-normal a-color-secondary" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_fmt?ie=UTF8&amp;formatType=current_format">Colour: White<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Size: 256GB<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Pattern Name: iPhone 12</a><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="reviews:filter-action:push-state" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:filter-action:push-state" data-reviews:filter-action:push-state="{}"><a data-reftag="cm_cr_arp_d_rvw_rvwer" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;reviewerType&quot;:&quot;avp_only_reviews&quot;}" class="a-link-normal" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_rvwer?ie=UTF8&amp;reviewerType=avp_only_reviews&amp;formatType=current_format"><span data-hook="avp-badge" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></a></span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text review-text-content">







  
  
    <span>Very nice iPhone 12</span>
  
</span></div><div class="a-row review-comments comments-for-RQQ0XR6JYXW17"><div data-reftag="cm_cr_arp_d_cmt_opn" data-a-expander-name="review_comment_expander" class="a-row a-expander-container a-expander-inline-container cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">One person found this helpful</span></div><!-- Components for Reactions C -->
    <div class="cr-helpful-button aok-float-left">
          <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.in/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_vote_lft%3Fie%3DUTF8%26reviewerType%3Davp_only_reviews%26csrfT%3DhNLmo6zGAuRBcu0voRg0Df%252BDYKgDTynmqbB1fiquJDwZAAAAAGRDx%252FcAAAAB%26formatType%3Dcurrent_format%26reviewId%3DRQQ0XR6JYXW17&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=inflex&amp;openid.mode=checkid_setup&amp;marketPlaceId=A21TJRUUN4KGV&amp;language=en&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text"><div class="cr-helpful-text">
              Helpful</div>
          </a></span></span></div>
      </span><span class="cr-footer-line-height">
          <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hNLmo6zGAuRBcu0voRg0Df%2BDYKgDTynmqbB1fiquJDwZAAAAAGRDx%2FcAAAAB&amp;reviewId=RQQ0XR6JYXW17&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hNLmo6zGAuRBcu0voRg0Df%2BDYKgDTynmqbB1fiquJDwZAAAAAGRDx%2FcAAAAB&amp;reviewId=RQQ0XR6JYXW17">Report</a></span></span></span>

        <div aria-expanded="false" class="a-expander-content a-spacing-top-base a-spacing-large a-expander-inline-content a-expander-inner" style="display:none"><div class="a-row a-spacing-mini review-comments-header aok-hidden"><ul class="a-viewoptions-list a-viewoptions-section a-span12">
    <div class="a-row a-spacing-none a-grid-vertical-align a-grid-center"><div class="a-column a-span6"><span class="a-size-base a-viewoptions-list-label">Showing <span class='review-comment-count'>0</span> comments</span></div></div></ul>
</div><div class="a-section a-spacing-extra-large a-spacing-top-medium a-text-center comment-load-error aok-hidden"><div class="a-box a-alert a-alert-error cr-error" role="alert"><div class="a-box-inner a-alert-container"><h4 class="a-alert-heading">There was a problem loading comments right now. Please try again later.</h4><i class="a-icon a-icon-alert"></i><div class="a-alert-content"></div></div></div></div><div class="a-section a-spacing-none review-comments"></div><div class="a-spinner-wrapper comment-loading aok-hidden a-spacing-top-medium a-spacing-extra-large"><span class="a-spinner a-spinner-medium"></span></div><hr aria-hidden="true" class="a-spacing-none a-spacing-top-large a-divider-normal"/></div></div></div></div></div></div><div id="RR2VI8VXESJZS" data-hook="review" class="a-section review aok-relative"><div id="RR2VI8VXESJZS-review-card" class="a-row a-spacing-none"><div id="customer_review-RR2VI8VXESJZS" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AEOALYYENGLKIJ7AHBGP7MSRJGOQ/ref=cm_cr_arp_d_gw_btm?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Keshav Kakarla</span></div></a></div><div class="a-row"><a class="a-link-normal" title="5.0 out of 5 stars" href="/gp/customer-reviews/RR2VI8VXESJZS/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/RR2VI8VXESJZS/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD">







  
  
    <span>Just amazing</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in India 🇮🇳 on 17 May 2022</span><div class="a-row a-spacing-mini review-data review-format-strip"><a data-hook="format-strip" class="a-size-mini a-link-normal a-color-secondary" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_fmt?ie=UTF8&amp;formatType=current_format">Colour: White<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Size: 256GB<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Pattern Name: iPhone 12</a><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="reviews:filter-action:push-state" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:filter-action:push-state" data-reviews:filter-action:push-state="{}"><a data-reftag="cm_cr_arp_d_rvw_rvwer" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;reviewerType&quot;:&quot;avp_only_reviews&quot;}" class="a-link-normal" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_rvwer?ie=UTF8&amp;reviewerType=avp_only_reviews&amp;formatType=current_format"><span data-hook="avp-badge" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></a></span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text review-text-content">







  
  
    <span>iPhone 12 is just amazing, now available with more discounts</span>
  
</span></div><div class="a-row review-comments comments-for-RR2VI8VXESJZS"><div data-reftag="cm_cr_arp_d_cmt_opn" data-a-expander-name="review_comment_expander" class="a-row a-expander-container a-expander-inline-container cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <!-- Components for Reactions C -->
    <div class="cr-helpful-button aok-float-left">
          <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.in/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_vote_lft%3Fie%3DUTF8%26reviewerType%3Davp_only_reviews%26csrfT%3DhH3EhtKukofhkyJEirCwaIXQlSBpeSl0R5n4f13tclXVAAAAAGRDx%252FcAAAAB%26formatType%3Dcurrent_format%26reviewId%3DRR2VI8VXESJZS&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=inflex&amp;openid.mode=checkid_setup&amp;marketPlaceId=A21TJRUUN4KGV&amp;language=en&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text"><div class="cr-helpful-text">
              Helpful</div>
          </a></span></span></div>
      </span><span class="cr-footer-line-height">
          <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hH3EhtKukofhkyJEirCwaIXQlSBpeSl0R5n4f13tclXVAAAAAGRDx%2FcAAAAB&amp;reviewId=RR2VI8VXESJZS&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hH3EhtKukofhkyJEirCwaIXQlSBpeSl0R5n4f13tclXVAAAAAGRDx%2FcAAAAB&amp;reviewId=RR2VI8VXESJZS">Report</a></span></span></span>

        <div aria-expanded="false" class="a-expander-content a-spacing-top-base a-spacing-large a-expander-inline-content a-expander-inner" style="display:none"><div class="a-row a-spacing-mini review-comments-header aok-hidden"><ul class="a-viewoptions-list a-viewoptions-section a-span12">
    <div class="a-row a-spacing-none a-grid-vertical-align a-grid-center"><div class="a-column a-span6"><span class="a-size-base a-viewoptions-list-label">Showing <span class='review-comment-count'>0</span> comments</span></div></div></ul>
</div><div class="a-section a-spacing-extra-large a-spacing-top-medium a-text-center comment-load-error aok-hidden"><div class="a-box a-alert a-alert-error cr-error" role="alert"><div class="a-box-inner a-alert-container"><h4 class="a-alert-heading">There was a problem loading comments right now. Please try again later.</h4><i class="a-icon a-icon-alert"></i><div class="a-alert-content"></div></div></div></div><div class="a-section a-spacing-none review-comments"></div><div class="a-spinner-wrapper comment-loading aok-hidden a-spacing-top-medium a-spacing-extra-large"><span class="a-spinner a-spinner-medium"></span></div><hr aria-hidden="true" class="a-spacing-none a-spacing-top-large a-divider-normal"/></div></div></div></div></div></div><div id="RSWKR5OZWQUOO" data-hook="review" class="a-section review aok-relative"><div id="RSWKR5OZWQUOO-review-card" class="a-row a-spacing-none"><div id="customer_review-RSWKR5OZWQUOO" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AHGTUUKKYLPWYK2ORD6LWMWWLBOA/ref=cm_cr_arp_d_gw_btm?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Aakash Massey</span></div></a></div><div class="a-row"><a class="a-link-normal" title="5.0 out of 5 stars" href="/gp/customer-reviews/RSWKR5OZWQUOO/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/RSWKR5OZWQUOO/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD">







  
  
    <span>Superb phone nice seller</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in India 🇮🇳 on 29 March 2022</span><div class="a-row a-spacing-mini review-data review-format-strip"><a data-hook="format-strip" class="a-size-mini a-link-normal a-color-secondary" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_fmt?ie=UTF8&amp;formatType=current_format">Colour: White<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Size: 256GB<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Pattern Name: iPhone 12</a><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="reviews:filter-action:push-state" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:filter-action:push-state" data-reviews:filter-action:push-state="{}"><a data-reftag="cm_cr_arp_d_rvw_rvwer" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;reviewerType&quot;:&quot;avp_only_reviews&quot;}" class="a-link-normal" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_rvwer?ie=UTF8&amp;reviewerType=avp_only_reviews&amp;formatType=current_format"><span data-hook="avp-badge" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></a></span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text review-text-content">







  
  
    <span>Wonderful original phone i got superb service by seller must go battery also good</span>
  
</span></div><div class="a-popover-preload" id="a-popover-RSWKR5OZWQUOO_gallerySection_main">











 
  		 


<div id="RSWKR5OZWQUOO_image_popover" data-hook="image-popover" class="a-section cr-lightbox-popover-container">

    
        
        
            <div class="cr-lightbox-image-viewer">
        <div class="cr-lightbox-main-image-container">
            <img alt="Customer image" src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/transparent-pixel._V192234675_.gif" class="cr-lightbox-main-image"/>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__back">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__back">
            </div>
        </div>
        <div class="cr-lightbox-navigator-container cr-lightbox-navigator-container__next">
            <div class="cr-lightbox-navigator-button cr-lightbox-navigator-button__next">
            </div>
        </div>
    </div>
    <div class="a-section cr-lightbox-review-information">
        <div class="a-section a-spacing-mini cr-review-stars-and-title">

            <div class="a-row a-spacing-mini">
                <a href="/gp/profile/amzn1.account.AHGTUUKKYLPWYK2ORD6LWMWWLBOA/ref=cm_cr_arp_d_gw_pop?ie=UTF8" class="a-profile cr-lightbox-customer-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Aakash Massey</span></div></a>
            </div>

            <i class="a-icon a-icon-star a-star-5 cr-lightbox-review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i>
            <span class="a-size-base cr-lightbox-review-title a-text-bold">
                Superb phone nice seller
            </span>
            <br>
            <span class="a-size-small a-color-secondary cr-lightbox-review-origin">
                
                    
                    
                        
                            Reviewed in India 🇮🇳 on 29 March 2022
                        
                    
                
            </span>
        </div>
        <span class="a-size-base cr-lightbox-review-body">
            Wonderful original phone i got superb service by seller must go battery also good
        </span>
        <div class="a-section a-spacing-top-base">
            <span class="a-size-medium a-color-secondary">
                Images in this review 
            </span>
            <div class="a-section a-spacing-top-mini cr-lightbox-image-thumbnails">
                
                    
                        <img alt="Customer image" src="https://m.media-amazon.com/images/I/81x-0YMjbZL._SY88.jpg" class="cr-lightbox-image-thumbnail"/>
                    
                
            </div>
        </div>
    </div>
        
    
</div>



<script>
   function toggleSeeAllView() {
       P.when('A', 'cr-image-popover-controller').execute(function(A, imagePopoverController) {
          imagePopoverController.toggleSeeAllView(true);
       });
   }
</script>
</div><div id="RSWKR5OZWQUOO_imageSection_main" class="a-section a-spacing-medium review-image-container"><div class="review-image-tile-section" data-reviewid="RSWKR5OZWQUOO">
       <span class="a-declarative" data-action="a-modal" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-modal" data-a-modal="{&quot;name&quot;:&quot;RSWKR5OZWQUOO_gallerySection_main&quot;}" id="RSWKR5OZWQUOO-0"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><img alt="Customer image" src="https://m.media-amazon.com/images/I/81x-0YMjbZL._SY88.jpg" data-hook="review-image-tile" class="review-image-tile" height="88" width="100%"/><i class="a-icon a-icon-popover"></i></a></span></div>
</div><script>
        P.when('A', 'cr-image-popover-controller').execute(function(A, imagePopoverController) {
          A.on("a:popover:beforeShow:RSWKR5OZWQUOO_gallerySection_main", function(data) {
            imagePopoverController.initImagePopover("RSWKR5OZWQUOO", "[https://m.media-amazon.com/images/I/81x-0YMjbZL._SL1600_.jpg]", data);
          });
        });
    </script>
<div class="a-row review-comments comments-for-RSWKR5OZWQUOO"><div data-reftag="cm_cr_arp_d_cmt_opn" data-a-expander-name="review_comment_expander" class="a-row a-expander-container a-expander-inline-container cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">One person found this helpful</span></div><!-- Components for Reactions C -->
    <div class="cr-helpful-button aok-float-left">
          <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.in/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_vote_lft%3Fie%3DUTF8%26reviewerType%3Davp_only_reviews%26csrfT%3DhC8nZ5QppCqcr35fm7BzIPxG%252BXnZtTuzs1dVLlmsJZRbAAAAAGRDx%252FcAAAAB%26formatType%3Dcurrent_format%26reviewId%3DRSWKR5OZWQUOO&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=inflex&amp;openid.mode=checkid_setup&amp;marketPlaceId=A21TJRUUN4KGV&amp;language=en&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text"><div class="cr-helpful-text">
              Helpful</div>
          </a></span></span></div>
      </span><span class="cr-footer-line-height">
          <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hC8nZ5QppCqcr35fm7BzIPxG%2BXnZtTuzs1dVLlmsJZRbAAAAAGRDx%2FcAAAAB&amp;reviewId=RSWKR5OZWQUOO&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hC8nZ5QppCqcr35fm7BzIPxG%2BXnZtTuzs1dVLlmsJZRbAAAAAGRDx%2FcAAAAB&amp;reviewId=RSWKR5OZWQUOO">Report</a></span></span></span>

        <div aria-expanded="false" class="a-expander-content a-spacing-top-base a-spacing-large a-expander-inline-content a-expander-inner" style="display:none"><div class="a-row a-spacing-mini review-comments-header aok-hidden"><ul class="a-viewoptions-list a-viewoptions-section a-span12">
    <div class="a-row a-spacing-none a-grid-vertical-align a-grid-center"><div class="a-column a-span6"><span class="a-size-base a-viewoptions-list-label">Showing <span class='review-comment-count'>0</span> comments</span></div></div></ul>
</div><div class="a-section a-spacing-extra-large a-spacing-top-medium a-text-center comment-load-error aok-hidden"><div class="a-box a-alert a-alert-error cr-error" role="alert"><div class="a-box-inner a-alert-container"><h4 class="a-alert-heading">There was a problem loading comments right now. Please try again later.</h4><i class="a-icon a-icon-alert"></i><div class="a-alert-content"></div></div></div></div><div class="a-section a-spacing-none review-comments"></div><div class="a-spinner-wrapper comment-loading aok-hidden a-spacing-top-medium a-spacing-extra-large"><span class="a-spinner a-spinner-medium"></span></div><hr aria-hidden="true" class="a-spacing-none a-spacing-top-large a-divider-normal"/></div></div></div></div></div></div><div id="R19BSIYHSSO5SN" data-hook="review" class="a-section review aok-relative"><div id="R19BSIYHSSO5SN-review-card" class="a-row a-spacing-none"><div id="customer_review-R19BSIYHSSO5SN" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AG7TULCHPA56NGLMKPMFMJKF7TYA/ref=cm_cr_arp_d_gw_btm?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Chronos</span></div></a></div><div class="a-row"><a class="a-link-normal" title="3.0 out of 5 stars" href="/gp/customer-reviews/R19BSIYHSSO5SN/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-3 review-rating"><span class="a-icon-alt">3.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R19BSIYHSSO5SN/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD">







  
  
    <span>iPhone 12 screen is a major bummer!!</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in India 🇮🇳 on 13 February 2021</span><div class="a-row a-spacing-mini review-data review-format-strip"><a data-hook="format-strip" class="a-size-mini a-link-normal a-color-secondary" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_fmt?ie=UTF8&amp;formatType=current_format">Colour: White<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Size: 256GB<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Pattern Name: iPhone 12</a><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="reviews:filter-action:push-state" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:filter-action:push-state" data-reviews:filter-action:push-state="{}"><a data-reftag="cm_cr_arp_d_rvw_rvwer" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;reviewerType&quot;:&quot;avp_only_reviews&quot;}" class="a-link-normal" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_rvwer?ie=UTF8&amp;reviewerType=avp_only_reviews&amp;formatType=current_format"><span data-hook="avp-badge" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></a></span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text review-text-content">







  
  
    <span>It’s such a disappointment. I have been using iPhone since it’s first version.<br /><br />So naturally upgraded from iPhone X to 12. But the excitement quickly died down as soon as I saw the screen. There is a warm greenish tint to it which makes the colors off.<br /><br />Selfie portraits aren’t good either. Too sharp for portraits. May be I should have gone for the 12 Pro Max as it handles much better because of the telephoto lens.<br /><br />Hope apple fixes the screen issues soon</span>
  
</span></div><div class="a-row review-comments comments-for-R19BSIYHSSO5SN"><div data-reftag="cm_cr_arp_d_cmt_opn" data-a-expander-name="review_comment_expander" class="a-row a-expander-container a-expander-inline-container cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <div class="a-row a-spacing-small"><span data-hook="helpful-vote-statement" class="a-size-base a-color-tertiary cr-vote-text">7 people found this helpful</span></div><!-- Components for Reactions C -->
    <div class="cr-helpful-button aok-float-left">
          <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.in/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_vote_lft%3Fie%3DUTF8%26reviewerType%3Davp_only_reviews%26csrfT%3DhLDVUAQvE2QLsNlzXploThC2pHQaERsZHilyOlG7ygvZAAAAAGRDx%252FcAAAAB%26formatType%3Dcurrent_format%26reviewId%3DR19BSIYHSSO5SN&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=inflex&amp;openid.mode=checkid_setup&amp;marketPlaceId=A21TJRUUN4KGV&amp;language=en&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text"><div class="cr-helpful-text">
              Helpful</div>
          </a></span></span></div>
      </span><span class="cr-footer-line-height">
          <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hLDVUAQvE2QLsNlzXploThC2pHQaERsZHilyOlG7ygvZAAAAAGRDx%2FcAAAAB&amp;reviewId=R19BSIYHSSO5SN&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hLDVUAQvE2QLsNlzXploThC2pHQaERsZHilyOlG7ygvZAAAAAGRDx%2FcAAAAB&amp;reviewId=R19BSIYHSSO5SN">Report</a></span></span></span>

        <div aria-expanded="false" class="a-expander-content a-spacing-top-base a-spacing-large a-expander-inline-content a-expander-inner" style="display:none"><div class="a-row a-spacing-mini review-comments-header aok-hidden"><ul class="a-viewoptions-list a-viewoptions-section a-span12">
    <div class="a-row a-spacing-none a-grid-vertical-align a-grid-center"><div class="a-column a-span6"><span class="a-size-base a-viewoptions-list-label">Showing <span class='review-comment-count'>0</span> comments</span></div></div></ul>
</div><div class="a-section a-spacing-extra-large a-spacing-top-medium a-text-center comment-load-error aok-hidden"><div class="a-box a-alert a-alert-error cr-error" role="alert"><div class="a-box-inner a-alert-container"><h4 class="a-alert-heading">There was a problem loading comments right now. Please try again later.</h4><i class="a-icon a-icon-alert"></i><div class="a-alert-content"></div></div></div></div><div class="a-section a-spacing-none review-comments"></div><div class="a-spinner-wrapper comment-loading aok-hidden a-spacing-top-medium a-spacing-extra-large"><span class="a-spinner a-spinner-medium"></span></div><hr aria-hidden="true" class="a-spacing-none a-spacing-top-large a-divider-normal"/></div></div></div></div></div></div><div id="R3R6R5TNHSWZA6" data-hook="review" class="a-section review aok-relative"><div id="R3R6R5TNHSWZA6-review-card" class="a-row a-spacing-none"><div id="customer_review-R3R6R5TNHSWZA6" class="a-section celwidget"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AEWSVAPQVMYFCIO3ZSCUYYTFBBQA/ref=cm_cr_arp_d_gw_btm?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif" class="a-lazy-loaded" data-src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/3d08a3e2-504a-4b45-80b9-b2aa647166a1._CR0,24.0,829,829_SX48_.jpg"/><noscript><img src="https://images-eu.ssl-images-amazon.com/images/S/amazon-avatars-global/3d08a3e2-504a-4b45-80b9-b2aa647166a1._CR0,24.0,829,829_SX48_.jpg"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">akshay salve</span></div></a></div><div class="a-row"><a class="a-link-normal" title="5.0 out of 5 stars" href="/gp/customer-reviews/R3R6R5TNHSWZA6/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i></a><span class="a-letter-space"></span><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R3R6R5TNHSWZA6/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&amp;ASIN=B08L5VRVTD">







  
  
    <span>iphone 12 256gb</span>
  
</a></div><span data-hook="review-date" class="a-size-base a-color-secondary review-date">Reviewed in India 🇮🇳 on 13 April 2022</span><div class="a-row a-spacing-mini review-data review-format-strip"><a data-hook="format-strip" class="a-size-mini a-link-normal a-color-secondary" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_fmt?ie=UTF8&amp;formatType=current_format">Colour: White<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Size: 256GB<i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i>Pattern Name: iPhone 12</a><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="reviews:filter-action:push-state" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:filter-action:push-state" data-reviews:filter-action:push-state="{}"><a data-reftag="cm_cr_arp_d_rvw_rvwer" data-reviews-state-param="{&quot;pageNumber&quot;:&quot;1&quot;,&quot;reviewerType&quot;:&quot;avp_only_reviews&quot;}" class="a-link-normal" href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_rvw_rvwer?ie=UTF8&amp;reviewerType=avp_only_reviews&amp;formatType=current_format"><span data-hook="avp-badge" class="a-size-mini a-color-state a-text-bold">Verified Purchase</span></a></span></div><div class="a-row a-spacing-small review-data"><span data-hook="review-body" class="a-size-base review-text review-text-content">







  
  
    <span>nice phone, good battery life.</span>
  
</span></div><div class="a-row review-comments comments-for-R3R6R5TNHSWZA6"><div data-reftag="cm_cr_arp_d_cmt_opn" data-a-expander-name="review_comment_expander" class="a-row a-expander-container a-expander-inline-container cr-vote-action-bar"><span class="cr-vote" data-hook="review-voting-widget">
  <!-- Components for Reactions C -->
    <div class="cr-helpful-button aok-float-left">
          <span class="a-button a-button-base"><span class="a-button-inner"><a href="https://www.amazon.in/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_vote_lft%3Fie%3DUTF8%26reviewerType%3Davp_only_reviews%26csrfT%3DhOTBGALb2%252Bw%252BWPgSl9HgLX6P4ICILeH9yXGYln5RLU1BAAAAAGRDx%252FcAAAAB%26formatType%3Dcurrent_format%26reviewId%3DR3R6R5TNHSWZA6&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=inflex&amp;openid.mode=checkid_setup&amp;marketPlaceId=A21TJRUUN4KGV&amp;language=en&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" data-hook="vote-helpful-button" class="a-button-text"><div class="cr-helpful-text">
              Helpful</div>
          </a></span></span></div>
      </span><span class="cr-footer-line-height">
          <span><i class="a-icon a-icon-text-separator" role="img" aria-label="|"></i><span class="a-declarative" data-action="cr-popup" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-cr-popup" data-cr-popup="{&quot;width&quot;:&quot;580&quot;,&quot;title&quot;:&quot;ReportAbuse&quot;,&quot;url&quot;:&quot;/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hOTBGALb2%2Bw%2BWPgSl9HgLX6P4ICILeH9yXGYln5RLU1BAAAAAGRDx%2FcAAAAB&amp;reviewId=R3R6R5TNHSWZA6&quot;,&quot;height&quot;:&quot;380&quot;}"><a class="a-size-base a-link-normal a-color-secondary report-abuse-link a-text-normal" href="/hz/reviews-render/report-review?ie=UTF8&amp;ref=cm_cr_arp_d_rvw_hlp&amp;csrfT=hOTBGALb2%2Bw%2BWPgSl9HgLX6P4ICILeH9yXGYln5RLU1BAAAAAGRDx%2FcAAAAB&amp;reviewId=R3R6R5TNHSWZA6">Report</a></span></span></span>

        <div aria-expanded="false" class="a-expander-content a-spacing-top-base a-spacing-large a-expander-inline-content a-expander-inner" style="display:none"><div class="a-row a-spacing-mini review-comments-header aok-hidden"><ul class="a-viewoptions-list a-viewoptions-section a-span12">
    <div class="a-row a-spacing-none a-grid-vertical-align a-grid-center"><div class="a-column a-span6"><span class="a-size-base a-viewoptions-list-label">Showing <span class='review-comment-count'>0</span> comments</span></div></div></ul>
</div><div class="a-section a-spacing-extra-large a-spacing-top-medium a-text-center comment-load-error aok-hidden"><div class="a-box a-alert a-alert-error cr-error" role="alert"><div class="a-box-inner a-alert-container"><h4 class="a-alert-heading">There was a problem loading comments right now. Please try again later.</h4><i class="a-icon a-icon-alert"></i><div class="a-alert-content"></div></div></div></div><div class="a-section a-spacing-none review-comments"></div><div class="a-spinner-wrapper comment-loading aok-hidden a-spacing-top-medium a-spacing-extra-large"><span class="a-spinner a-spinner-medium"></span></div><hr aria-hidden="true" class="a-spacing-none a-spacing-top-large a-divider-normal"/></div></div></div></div></div></div><div class="a-form-actions a-spacing-top-extra-large"><span class="a-declarative" data-action="reviews:page-action" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-reviews:page-action" data-reviews:page-action="{&quot;allowLinkDefault&quot;:&quot;1&quot;}"><div id="cm_cr-pagination_bar" data-hook="pagination-bar" data-reftag="cm_cr_arp_d_paging_btm" class="a-text-center celwidget a-text-base" role="navigation"><ul class="a-pagination"><li class="a-disabled"><span class="larr">←</span><span class="a-letter-space"></span><span class="a-letter-space"></span>Previous page</li><li class="a-last"><a href="/New-Apple-iPhone-12-256GB/product-reviews/B08L5VRVTD/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&amp;pageNumber=2&amp;reviewerType=avp_only_reviews&amp;formatType=current_format">Next page<span class="a-letter-space"></span><span class="a-letter-space"></span><span class="larr">→</span></a></li></ul></div></span></div></div></div><div class="a-spinner-wrapper reviews-load-progess aok-hidden a-spacing-top-large"><span class="a-spinner a-spinner-medium"></span></div></div><div id="reviews-spacing" class="a-section"></div></div><script type="text/javascript">
     if (ue) {
         uet('cf');
     }
</script><script>window.P.register('cf');</script>
<div class="a-fixed-right-grid-col right-column a-col-right" style="width:305px;margin-right:-305px;float:left;">



















<a name="Ask"></a>
<div class="a-section askReviewsPageAskWidget">
  <h4 class="a-spacing-mini a-text-bold">
    Questions? Get fast answers from reviewers
  </h4>
  <form class="askQuestionForm" method="POST" action="/ask/questions/asin/B08L5VRVTD/create">
    <input type="hidden" name="askQuestionSource" value="SIMPLE_STACK_SEE_ALL_REVIEWS_PAGE"/>
    <input type="hidden" name="askQuestionSourcePage" value="REVIEW_PAGE"/>
    <input type="hidden" name="askErrorUrl" value="/gp/customer-reviews/product/B08L5VRVTD#Ask"/>
    <input type='hidden' name='__token_' value='hKxl7jdmBHL/7MB8MafjzHp1L5d8EEE7kg/CSsxVfDq9AAAAAGRDx/cAAAAB' />
    <div class="a-input-text-wrapper a-span12 a-spacing-base"><textarea maxlength="150" placeholder="What do you want to know about Apple iPhone 12 (256GB) - White?" name="askQuestionText" style="height:70px;"></textarea></div>

    <span class="a-button a-button-base askSubmitQuestion"><span class="a-button-inner"><input class="a-button-input" type="submit" value="Ask"/><span class="a-button-text" aria-hidden="true">
      Ask
    </span></span></span>
    <div class="a-section a-spacing-micro cdFailedQuestionMessage badQuestion">Please make sure that you've entered a valid question.  You can edit your question or post anyway.</div>
    <div class="a-section a-spacing-micro cdFailedQuestionMessage emptyQuestion">Please enter a question.</div>
    
      






    
<a class="a-link-normal askSeeAllQuestionsLink" href="/ask/questions/asin/B08L5VRVTD/ref=ask_rp_reva_ql_hza">
    See all 1000+ answered questions
</a>

    
  </form>
  






</div>
<hr aria-hidden="true" class="a-divider-normal"/><div id="cm_cr_customer_service_widget" class="a-row celwidget"><span class="a-size-base">Need customer service? <a class="a-link-normal" target="_blank" href="/gp/help/customer/contact-us/ref=cm_cr_arp_d_cs?ie=UTF8&amp;initialIssue=cust-review">Click here</a></span></div></div></div></div><div id="cm_cr-footer_dp_link" class="a-section a-spacing-top-large celwidget"><span class="a-size-base back-carat a-text-bold">&lsaquo;&#32;</span><a class="a-size-base a-link-normal a-text-bold" href="/New-Apple-iPhone-12-256GB/dp/B08L5VRVTD/ref=cm_cr_arp_d_pl_foot_top?ie=UTF8">See all details for Apple iPhone 12 (256GB) - White</a></div></div><!--&&&Portal&Delimiter&&&--><!-- sp:end-feature:host-atf -->
<!-- sp:feature:nav-btf -->
<!-- NAVYAAN BTF START -->




  



  <script type='text/javascript'>(function ($Nav) {
"use strict";

if (typeof $Nav === 'undefined' || $Nav === null || typeof $Nav.when !== 'function') {
    return;
}

$Nav.when('$', 'data', 'flyout.yourAccount', 'sidepanel.csYourAccount',
          'config')
    .run("BuyitAgain-YourAccount-SidePanel",
    function ($, data, yaFlyout, csYourAccount, config) {
        if (config.disableBuyItAgain) {
            return;
        }
        var render = function (data) {
            if (data.dramResult) {
                var widgetHtml = data.dramResult;
                navbar.sidePanel({
                    flyoutName: 'yourAccount',
                    data: {html: widgetHtml}
                });
            }
        };

        var renderBuyItAgain = function (biaData) {
            if (csYourAccount) {
                csYourAccount.register(render, biaData);
            } else {
                render(biaData);
            }
        };

        var truncateAndRestructureYaFlyout = function() {
            if (window.P) {
                P.when('A', 'a-truncate').execute(function(A, truncate) {
                    var truncateElements = A.$('.a-truncate');
                    A.each(truncateElements, function(element) {
                        truncate.get(element).update();
                    });
                    var recommendationsWidget = document.getElementById('bia-hcb-widget');
                    if (recommendationsWidget) { 
                        var navFlyout = recommendationsWidget.parentElement;
                        var navFlyoutPaddingBottom = parseInt(window.getComputedStyle(navFlyout).getPropertyValue('padding-bottom'));
                        var navFlyoutContentHeight = navFlyout.clientHeight - navFlyoutPaddingBottom;
                        while (recommendationsWidget.offsetHeight > navFlyoutContentHeight && recommendationsWidget.offsetHeight > 0){
                            var recommendations = recommendationsWidget.querySelectorAll('.biaNavFlyoutFaceout');
                            if (recommendations.length <= 1) {
                                break;
                            }
                            var lastRecommendation = recommendations[recommendations.length - 1];
                            lastRecommendation.parentElement.removeChild(lastRecommendation);
                        }
                    }
               });
            }
        };

        yaFlyout.sidePanel.onData(truncateAndRestructureYaFlyout);
        yaFlyout.onShow(truncateAndRestructureYaFlyout);

    yaFlyout.onRender(function() {
            $.ajax({
                url: '/gp/bia/external/bia-hcb-ajax-handler.html',
                data: {"biaHcbRid":"RZ67A764XT8VEYCF2P53"},
                dataType: 'json',
                timeout: 4*1000,
                success: renderBuyItAgain,
                error: function (jqXHR, textStatus, errorThrown) {
                }
            });
        });
    });
})(window.$Nav);</script>


<script type="text/javascript">
  window.$Nav && $Nav.when("data").run(function (data) {
    data({
      "accountListContent": { "html": "<div id='nav-al-container'><div id='nav-al-signin'><div id='nav-flyout-ya-signin' class='nav-flyout-content nav-flyout-accessibility'><a href='https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_viewopt_fmt%2F%3F_encoding%3DUTF8%26formatType%3Dcurrent_format%26ie%3DUTF8%26pageNumber%3D1%26reviewerType%3Davp_only_reviews%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' rel='nofollow' class='nav-action-signin-button' data-nav-role='signin' data-nav-ref='nav_signin'><span class='nav-action-inner'>Sign in</span></a><div id='nav-flyout-ya-newCust' class='nav_pop_new_cust nav-flyout-content nav-flyout-accessibility'>New customer? <a href='https://www.amazon.in/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_viewopt_fmt%2F%3F_encoding%3DUTF8%26formatType%3Dcurrent_format%26ie%3DUTF8%26pageNumber%3D1%26reviewerType%3Davp_only_reviews%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' rel='nofollow' class='nav-a'>Start here.</a></div></div></div><div id='nav-al-wishlist' class='nav-al-column nav-tpl-itemList nav-flyout-content nav-flyout-accessibility'><div class='nav-title' id='nav-al-title'>Your Lists</div><a href='/hz/wishlist/ls?triggerElementID=createList&ref_=nav_ListFlyout_navFlyout_createList_lv_redirect' class='nav-link nav-item'><span class='nav-text'>Create a Wish List</span></a> <a href='/wishlist/universal?ref_=nav_ListFlyout_gno_listpop_uwl' class='nav-link nav-item'><span class='nav-text'>Wish from Any Website</span></a> <a href='/baby-reg/homepage?ref_=nav_ListFlyout_gno_listpop_br' class='nav-link nav-item'><span class='nav-text'>Baby Wishlist</span></a> <a href='/discover/?ref_=nav_ListFlyout_sbl' class='nav-link nav-item'><span class='nav-text'>Discover Your Style</span></a> <a href='/showroom?ref_=nav_ListFlyout_srm_your_desk_wl_in' class='nav-link nav-item'><span class='nav-text'>Explore Showroom</span></a></div><div id='nav-al-your-account' class='nav-al-column nav-template nav-flyout-content nav-tpl-itemList nav-flyout-accessibility'><div class='nav-title'>Your Account</div><a href='/gp/css/homepage.html?ref_=nav_AccountFlyout_ya' class='nav-link nav-item'><span class='nav-text'>Your Account</span></a> <a id='nav_prefetch_yourorders' href='/gp/css/order-history?ref_=nav_AccountFlyout_orders' class='nav-link nav-item'><span class='nav-text'>Your Orders</span></a> <a href='/hz/wishlist/ls?requiresSignIn=1&ref_=nav_AccountFlyout_wl' class='nav-link nav-item'><span class='nav-text'>Your Wish List</span></a> <a href='/gp/yourstore?ref_=nav_AccountFlyout_recs' class='nav-link nav-item'><span class='nav-text'>Your Recommendations</span></a> <a href='/gp/primecentral?ref_=nav_AccountFlyout_prime' class='nav-link nav-item'><span class='nav-text'>Your Prime Membership</span></a> <a href='/gp/redirect.html?location=https%3A%2F%2Fwww.primevideo.com%2F%3Fref_%3D_apv&source=nav_linktree&token=13D4F90D28CD96790B94E6091246BB1B2AE9FA05' class='nav-link nav-item'><span class='nav-text'>Your Prime Video</span></a> <a href='/auto-deliveries?ref_=nav_AccountFlyout_sns' class='nav-link nav-item'><span class='nav-text'>Your Subscribe & Save Items</span></a> <a href='/hz5/yourmembershipsandsubscriptions?ref_=nav_AccountFlyout_digital_subscriptions' class='nav-link nav-item'><span class='nav-text'>Memberships & Subscriptions</span></a> <a href='/gp/browse.html?node=21102587031&ref_=nav_ya_flyout_b2b_reg' class='nav-link nav-item'><span class='nav-text'>Your Free Amazon Business Account</span></a> <a href='/b/?node=2838698031&ld=AZINSOAYAFlyout&ref_=nav_AccountFlyout_sell' class='nav-link nav-item'><span class='nav-text'>Your Seller Account</span></a> <a href='/hz/mycd/myx?pageType=content&ref_=nav_AccountFlyout_myk' class='nav-link nav-item'><span class='nav-text'>Manage Your Content and Devices</span></a></div></div>" },
      "signinContent": { "html": "<div id='nav-signin-tooltip'><a href='https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_viewopt_fmt%2F%3F_encoding%3DUTF8%26formatType%3Dcurrent_format%26ie%3DUTF8%26pageNumber%3D1%26reviewerType%3Davp_only_reviews%26ref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' class='nav-action-signin-button' data-nav-role='signin' data-nav-ref='nav_custrec_signin'><span class='nav-action-inner'>Sign in</span></a><div class='nav-signin-tooltip-footer'>New customer? <a href='https://www.amazon.in/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2FNew-Apple-iPhone-12-256GB%2Fproduct-reviews%2FB08L5VRVTD%2Fref%3Dcm_cr_arp_d_viewopt_fmt%2F%3F_encoding%3DUTF8%26formatType%3Dcurrent_format%26ie%3DUTF8%26pageNumber%3D1%26reviewerType%3Davp_only_reviews%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' class='nav-a'>Start here.</a></div></div>" },
      "templates": {"itemList":"<# var hasColumns = (function () {  var checkColumns = function (_items) {    if (!_items) {      return false;    }    for (var i=0; i<_items.length; i++) {      if (_items[i].columnBreak || (_items[i].items && checkColumns(_items[i].items))) {        return true;      }    }    return false;  };  return checkColumns(items);}()); #><# if(hasColumns) { #>  <# if(items[0].image && items[0].image.src) { #>    <div class='nav-column nav-column-first nav-column-image'>  <# } else if (items[0].greeting) { #>    <div class='nav-column nav-column-first nav-column-greeting'>  <# } else { #>    <div class='nav-column nav-column-first'>  <# } #><# } #><# var renderItems = function(items) { #>  <# jQuery.each(items, function (i, item) { #>    <# if(hasColumns && item.columnBreak) { #>      <# if(item.image && item.image.src) { #>        </div><div class='nav-column nav-column-notfirst nav-column-break nav-column-image'>      <# } else if (item.greeting) { #>        </div><div class='nav-column nav-column-notfirst nav-column-break nav-column-greeting'>      <# } else { #>        </div><div class='nav-column nav-column-notfirst nav-column-break'>      <# } #>    <# } #>    <# if(item.dividerBefore) { #>      <div class='nav-divider'></div>    <# } #>    <# if(item.text || item.content) { #>      <# if(item.url) { #>        <a href='<#=item.url #>' class='nav-link      <# } else {#>        <span class='      <# } #>      <# if(item.panelKey) { #>        nav-hasPanel      <# } #>      <# if(item.items) { #>        nav-title      <# } #>      <# if(item.decorate == 'carat') { #>        nav-carat      <# } #>      <# if(item.decorate == 'nav-action-button') { #>        nav-action-button      <# } #>      nav-item'      <# if(item.extra) { #>        <#=item.extra #>      <# } #>      <# if(item.id) { #>        id='<#=item.id #>'      <# } #>      <# if(item.dataNavRole) { #>        data-nav-role='<#=item.dataNavRole #>'      <# } #>      <# if(item.dataNavRef) { #>        data-nav-ref='<#=item.dataNavRef #>'      <# } #>      <# if(item.panelKey) { #>        data-nav-panelkey='<#=item.panelKey #>'        role='navigation'        aria-label='<#=item.text#>'      <# } #>      <# if(item.subtextKey) { #>        data-nav-subtextkey='<#=item.subtextKey #>'      <# } #>      <# if(item.image && item.image.height > 16) { #>        style='line-height:<#=item.image.height #>px;'      <# } #>      >      <# if(item.decorate == 'carat') { #>        <i class='nav-icon'></i>      <# } #>      <# if(item.image && item.image.src) { #>        <img class='nav-image' src='<#=item.image.src #>' style='height:<#=item.image.height #>px; width:<#=item.image.width #>px;' />      <# } #>      <# if(item.text) { #>        <span class='nav-text<# if(item.classname) { #> <#=item.classname #><# } #>'><#=item.text#><# if(item.badgeText) { #>          <span class='nav-badge'><#=item.badgeText#></span>        <# } #></span>      <# } else if (item.content) { #>        <span class='nav-content'><# jQuery.each(item.content, function (j, cItem) { #><# if(cItem.url && cItem.text) { #><a href='<#=cItem.url #>' class='nav-a'><#=cItem.text #></a><# } else if (cItem.text) { #><#=cItem.text#><# } #><# }); #></span>      <# } #>      <# if(item.subtext) { #>        <span class='nav-subtext'><#=item.subtext #></span>      <# } #>      <# if(item.url) { #>        </a>      <# } else {#>        </span>      <# } #>    <# } #>    <# if(item.image && item.image.src) { #>      <# if(item.url) { #>        <a href='<#=item.url #>'>       <# } #>      <img class='nav-image'      <# if(item.id) { #>        id='<#=item.id #>'      <# } #>      src='<#=item.image.src #>' <# if (item.alt) { #> alt='<#= item.alt #>'<# } #>/>      <# if(item.url) { #>        </a>       <# } #>    <# } #>    <# if(item.items) { #>      <div class='nav-panel'> <# renderItems(item.items); #> </div>    <# } #>  <# }); #><# }; #><# renderItems(items); #><# if(hasColumns) { #>  </div><# } #>","subnav":"<# if (obj && obj.type === 'vertical') { #>  <# jQuery.each(obj.rows, function (i, row) { #>    <# if (row.flyoutElement === 'button') { #>      <div class='nav_sv_fo_v_button'        <# if (row.elementStyle) { #>          style='<#= row.elementStyle #>'        <# } #>      >        <a href='<#=row.url #>' class='nav-action-button nav-sprite'>          <#=row.text #>        </a>      </div>    <# } else if (row.flyoutElement === 'list' && row.list) { #>      <# jQuery.each(row.list, function (j, list) { #>        <div class='nav_sv_fo_v_column <#=(j === 0) ? 'nav_sv_fo_v_first' : '' #>'>          <ul class='<#=list.elementClass #>'>          <# jQuery.each(list.linkList, function (k, link) { #>            <# if (k === 0) { link.elementClass += ' nav_sv_fo_v_first'; } #>            <li class='<#=link.elementClass #>'>              <# if (link.url) { #>                <a href='<#=link.url #>' class='nav_a'><#=link.text #></a>              <# } else { #>                <span class='nav_sv_fo_v_span'><#=link.text #></span>              <# } #>            </li>          <# }); #>          </ul>        </div>      <# }); #>    <# } else if (row.flyoutElement === 'link') { #>      <# if (row.topSpacer) { #>        <div class='nav_sv_fo_v_clear'></div>      <# } #>      <div class='<#=row.elementClass #>'>        <a href='<#=row.url #>' class='nav_sv_fo_v_lmargin nav_a'>          <#=row.text #>        </a>      </div>    <# } #>  <# }); #><# } else if (obj) { #>  <div class='nav_sv_fo_scheduled'>    <#= obj #>  </div><# } #>","htmlList":"<# jQuery.each(items, function (i, item) { #>  <div class='nav-item'>    <#=item #>  </div><# }); #>"}
    })
  })
</script>

<script type="text/javascript">
  window.$Nav && $Nav.declare('config.flyoutURL', null);
  window.$Nav && $Nav.declare('btf.lite');
  window.$Nav && $Nav.declare('btf.full');
  window.$Nav && $Nav.declare('btf.exists');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).register('navCF');
</script>


<!-- NAVYAAN BTF END -->
<!-- sp:end-feature:nav-btf -->
<!-- sp:feature:host-btf -->


  <input type="hidden" name="reviews-page-loaded"/></div>
<!-- sp:end-feature:host-btf -->
<!-- sp:feature:aui-preload -->
<!-- sp:end-feature:aui-preload -->
<!-- sp:feature:nav-footer -->

  <!-- NAVYAAN FOOTER START -->
  <!-- WITH MOZART -->

<div id='rhf' class='copilot-secure-display' style='clear: both;' role='complementary' aria-label='Your recently viewed items and featured recommendations'> <div class='rhf-frame' style='display: none;'> <br> <div id='rhf-container'> <div class='rhf-loading-outer'> <table class='rhf-loading-middle'> <tr> <td class='rhf-loading-inner'> <img src='https://m.media-amazon.com/images/G/31/personalization/ybh/loading-4x-gray._CB485916689_.gif'> </td> </tr> </table> </div> <div id='rhf-context'> <script type='application/json'> { "rhfHandlerParams":{"currentPageType":"CustomerReviews","currentSubPageType":"remoteProduct","excludeAsin":"B08L5VRVTD","fieldKeywords":"","k":"","keywords":"","search":"","auditEnabled":"","previewCampaigns":"","forceWidgets":"","searchAlias":""} } </script> </div> </div> <noscript> <div class='rhf-border'> <div class='rhf-header'> Your recently viewed items and featured recommendations </div> <div class='rhf-footer'> <div class='rvi-container'> <div class='ybh-edit'> <div class='ybh-edit-arrow'> &#8250; </div> <div class='ybh-edit-link'> <a href='/gp/history'> View or edit your browsing history </a> </div> </div> <span class='no-rvi-message'> After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in. </span> </div> </div> </div> </noscript> <div id='rhf-error' style='display: none;'> <div class='rhf-border'> <div class='rhf-header'> Your recently viewed items and featured recommendations </div> <div class='rhf-footer'> <div class='rvi-container'> <div class='ybh-edit'> <div class='ybh-edit-arrow'> &#8250; </div> <div class='ybh-edit-link'> <a href='/gp/history'> View or edit your browsing history </a> </div> </div> <span class='no-rvi-message'> After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in. </span> </div> </div> </div> </div> <br> </div> </div>
<div class="navLeftFooter nav-sprite-v1" id="navFooter">
  
<a href="#" id="navBackToTop" aria-label="Back to top" onclick="document.body.scrollTop = 0; document.documentElement.scrollTop = 0; event.preventDefault();">
  <div class="navFooterBackToTop">
  <span class="navFooterBackToTopText">
    Back to top
  </span>
  </div>
</a>

  
<div class="navFooterVerticalColumn navAccessibility" role="presentation">
  <div class="navFooterVerticalRow navAccessibility" style="display: table-row;">
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Get to Know Us</div>
        <ul>
            <li class="nav_first">
              <a href="https://www.aboutamazon.in/?utm_source=gateway&utm_medium=footer" class="nav_a">About Us</a>
            </li>
            <li >
              <a href="https://amazon.jobs" class="nav_a">Careers</a>
            </li>
            <li >
              <a href="https://press.aboutamazon.in/?utm_source=gateway&utm_medium=footer" class="nav_a">Press Releases</a>
            </li>
            <li class="nav_last ">
              <a href="https://www.amazon.science" class="nav_a">Amazon Science</a>
            </li>
        </ul>
      </div>
        <div class="navFooterColSpacerInner navAccessibility"></div>
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Connect with Us</div>
        <ul>
            <li class="nav_first">
              <a href="https://www.amazon.in/gp/redirect.html/ref=footer_fb?location=http://www.facebook.com/AmazonIN&token=2075D5EAC7BB214089728E2183FD391706D41E94&6" class="nav_a">Facebook</a>
            </li>
            <li >
              <a href="https://www.amazon.in/gp/redirect.html/ref=footer_twitter?location=http://twitter.com/AmazonIN&token=A309DFBFCB1E37A808FF531934855DC817F130B6&6" class="nav_a">Twitter</a>
            </li>
            <li class="nav_last ">
              <a href="https://www.amazon.in/gp/redirect.html?location=https://www.instagram.com/amazondotin&token=264882C912E9D005CB1D9B61F12E125D5DF9BFC7&source=standards" class="nav_a">Instagram</a>
            </li>
        </ul>
      </div>
        <div class="navFooterColSpacerInner navAccessibility"></div>
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Make Money with Us</div>
        <ul>
            <li class="nav_first">
              <a href="/b/?node=2838698031&ld=AZINSOANavDesktopFooter_C&ref_=nav_footer_sell_C" class="nav_a">Sell on Amazon</a>
            </li>
            <li >
              <a href="https://accelerator.amazon.in/?ref_=map_1_b2b_GW_FT" class="nav_a">Sell under Amazon Accelerator</a>
            </li>
            <li >
              <a href="https://brandservices.amazon.in/?ref=AOINABRLGNRFOOT&ld=AOINABRLGNRFOOT" class="nav_a">Protect and Build Your Brand</a>
            </li>
            <li >
              <a href="https://sell.amazon.in/grow-your-business/amazon-global-selling.html?ld=AZIN_Footer_V1&ref=AZIN_Footer_V1" class="nav_a">Amazon Global Selling</a>
            </li>
            <li >
              <a href="https://affiliate-program.amazon.in/?utm_campaign=assocshowcase&utm_medium=footer&utm_source=GW&ref_=footer_assoc" class="nav_a">Become an Affiliate</a>
            </li>
            <li >
              <a href="https://services.amazon.in/services/fulfilment-by-amazon/benefits.html/ref=az_footer_fba?ld=AWRGINFBAfooter" class="nav_a">Fulfilment by Amazon</a>
            </li>
            <li >
              <a href="https://advertising.amazon.in/?ref=Amz.in" class="nav_a">Advertise Your Products</a>
            </li>
            <li class="nav_last ">
              <a href="https://www.amazonpay.in/merchant" class="nav_a">Amazon Pay on Merchants</a>
            </li>
        </ul>
      </div>
        <div class="navFooterColSpacerInner navAccessibility"></div>
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Let Us Help You</div>
        <ul>
            <li class="nav_first">
              <a href="/gp/help/customer/display.html?nodeId=GDFU3JS5AL6SYHRD&ref_=footer_covid" class="nav_a">COVID-19 and Amazon</a>
            </li>
            <li >
              <a href="/gp/css/homepage.html?ref_=footer_ya" class="nav_a">Your Account</a>
            </li>
            <li >
              <a href="/gp/css/returns/homepage.html?ref_=footer_hy_f_4" class="nav_a">Returns Centre</a>
            </li>
            <li >
              <a href="/gp/help/customer/display.html?nodeId=201083470&ref_=footer_swc" class="nav_a">100% Purchase Protection</a>
            </li>
            <li >
              <a href="/gp/browse.html?node=6967393031&ref_=footer_mobapp" class="nav_a">Amazon App Download</a>
            </li>
            <li class="nav_last ">
              <a href="/gp/help/customer/display.html?nodeId=200507590&ref_=footer_gw_m_b_he" class="nav_a">Help</a>
            </li>
        </ul>
      </div>
  </div>
</div>
<div class="nav-footer-line"></div>

  <div class="navFooterLine navFooterLinkLine navFooterPadItemLine">
    <span>
      <div class="navFooterLine navFooterLogoLine">
        <a  aria-label="Amazon India Home"  href="/ref=footer_logo">
        <div class="nav-logo-base nav-sprite"></div>
        </a>
      </div>
</span>
    
      <span class="icp-container-desktop"><div
          class="navFooterLine">
<style type="text/css">
  #icp-touch-link-language { display: none; }
</style>


<a href="/customer-preferences/edit?ie=UTF8&preferencesReturnUrl=%2F&ref_=footer_lang" aria-label="Choose a language for shopping." class="icp-button" id="icp-touch-link-language">
  <div class="icp-nav-globe-img-2 icp-button-globe-2"></div><span class="icp-color-base">English</span><span class="nav-arrow icp-up-down-arrow"></span>
</a>


</div></span>
    
  </div>
  
<div class="navFooterLine navFooterLinkLine navFooterPadItemLine">
  <ul><li class="nav_first"><a href="https://www.amazon.com.au/ref=footer_au" class="nav_a">Australia</a></li><li><a href="https://www.amazon.com.br/ref=footer_br" class="nav_a">Brazil</a></li><li><a href="https://www.amazon.ca/ref=footer_ca" class="nav_a">Canada</a></li><li><a href="https://www.amazon.cn/ref=footer_cn" class="nav_a">China</a></li><li><a href="https://www.amazon.fr/ref=footer_fr" class="nav_a">France</a></li><li><a href="https://www.amazon.de/ref=footer_de" class="nav_a">Germany</a></li><li><a href="https://www.amazon.it/ref=footer_it" class="nav_a">Italy</a></li><li><a href="https://www.amazon.co.jp/ref=footer_jp" class="nav_a">Japan</a></li><li><a href="https://www.amazon.com.mx/ref=footer_mx" class="nav_a">Mexico</a></li><li><a href="https://www.amazon.nl/ref=footer_nl" class="nav_a">Netherlands</a></li><li><a href="https://www.amazon.pl/ref=footer_pl" class="nav_a">Poland</a></li><li><a href="https://www.amazon.sg/ref=footer_sg" class="nav_a">Singapore</a></li><li><a href="https://www.amazon.es/ref=footer_es" class="nav_a">Spain</a></li><li><a href="https://www.amazon.com.tr/ref=footer_tr" class="nav_a">Turkey</a></li><li><a href="https://www.amazon.ae/ref=footer_ae" class="nav_a">United Arab Emirates</a></li><li><a href="https://www.amazon.co.uk/ref=footer_uk" class="nav_a">United Kingdom</a></li><li class="nav_last"><a href="https://www.amazon.com/ref=footer_us" class="nav_a">United States</a></li></ul>
  
</div>

  
  <div class="navFooterLine navFooterLinkLine navFooterDescLine"  aria-label="More on Amazon">
    <table class="navFooterMoreOnAmazon" cellspacing="0" summary="More on Amazon">
      <tr>
<td class="navFooterDescItem"><a href=https://www.abebooks.com/ class="nav_a">AbeBooks<br><span class="navFooterDescText">Books, art<br>& collectibles</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=https://aws.amazon.com/what-is-cloud-computing/?sc_channel=EL&sc_campaign=IN_amazonfooter class="nav_a">Amazon Web Services<br><span class="navFooterDescText">Scalable Cloud<br>Computing Services</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=https://www.audible.in/ class="nav_a">Audible<br><span class="navFooterDescText">Download<br>Audio Books</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=https://www.dpreview.com/ class="nav_a">DPReview<br><span class="navFooterDescText">Digital<br>Photography</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=https://www.imdb.com/ class="nav_a">IMDb<br><span class="navFooterDescText">Movies, TV<br>& Celebrities</span></a></td></tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescItem"><a href=https://www.shopbop.com/ class="nav_a">Shopbop<br><span class="navFooterDescText">Designer<br>Fashion Brands</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=/business?ref=footer_aingw class="nav_a">	
Amazon Business<br><span class="navFooterDescText">Everything For<br>Your Business</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=/now?ref=footer_amznow class="nav_a">Prime Now<br><span class="navFooterDescText"> 2-Hour Delivery<br>on Everyday Items</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href=/music/prime?ref=footer_apm class="nav_a">Amazon Prime Music<br><span class="navFooterDescText">100 million songs, ad-free<br>Over 15 million podcast episodes </span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem">&nbsp;</td>
</tr>

    </table>
  </div>

  
<div class="navFooterLine navFooterLinkLine navFooterPadItemLine navFooterCopyright">
  <ul><li class="nav_first"><a href="/gp/help/customer/display.html?nodeId=200545940&ref_=footer_cou" class="nav_a">Conditions of Use & Sale</a></li><li ><a href="/gp/help/customer/display.html?nodeId=200534380&ref_=footer_privacy" class="nav_a">Privacy Notice</a></li><li class="nav_last"><a href="/gp/help/customer/display.html?nodeId=202075050&ref_=footer_iba" class="nav_a">Interest-Based Ads</a></li></ul><span>© 1996-2023, Amazon.com, Inc. or its affiliates</span>
</div>

  
</div>
<div id="sis_pixel_r2" aria-hidden="true" style="height:1px; position: absolute; left: -1000000px; top: -1000000px;"></div><script>(function(a,b){a.attachEvent?a.attachEvent("onload",b):a.addEventListener&&a.addEventListener("load",b,!1)})(window,function(){setTimeout(function(){var el=document.getElementById("sis_pixel_r2");el&&(el.innerHTML='<iframe id="DAsis" src="//aax-eu.amazon-adsystem.com/s/iu3?d=amazon.in&slot=navFooter&a2=01014adb3402311617379f9f35431fc79d104ef906f3d021df00a933afb4e11385ed&old_oo=0&ts=1682163703706&s=AVR2csNhJvRbAS8Dz_NS6OTOusFnJCEfrpr89zEOcGoc&gdpr_consent=&gdpr_consent_avl=&cb=1682163703706" width="1" height="1" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" tabindex="-1" sandbox></iframe>')},300)});</script>

  <!-- NAVYAAN FOOTER END -->

<!-- sp:end-feature:nav-footer -->
<!-- sp:feature:configured-sitewide-assets -->
<script src="https://m.media-amazon.com/images/I/01LFiHt-uUL.js?AUIClients/TMCJavascriptAssets" crossorigin="anonymous"></script>
<script src="https://m.media-amazon.com/images/I/21vyYUWVeBL.js?AUIClients/MSAVowelsJavascriptAssets" crossorigin="anonymous"></script>
<!-- sp:end-feature:configured-sitewide-assets -->
<!-- sp:feature:csm:body-close -->
<div id='be' style="display:none;visibility:hidden;"><form name='ue_backdetect' action="get"><input type="hidden" name='ue_back' value='1' /></form>


<script type="text/javascript">
window.ue_ibe = (window.ue_ibe || 0) + 1;
if (window.ue_ibe === 1) {
(function(e,c){function h(b,a){f.push([b,a])}function g(b,a){if(b){var c=e.head||e.getElementsByTagName("head")[0]||e.documentElement,d=e.createElement("script");d.async="async";d.src=b;d.setAttribute("crossorigin","anonymous");a&&a.onerror&&(d.onerror=a.onerror);a&&a.onload&&(d.onload=a.onload);c.insertBefore(d,c.firstChild)}}function k(){ue.uels=g;for(var b=0;b<f.length;b++){var a=f[b];g(a[0],a[1])}ue.deffered=1}var f=[];c.ue&&(ue.uels=h,c.ue.attach&&c.ue.attach("load",k))})(document,window);


if (window.ue && window.ue.uels) {
        var cel_widgets = [ { "c":"celwidget" },{ "s":"#nav-swmslot > div", "id_gen":function(elem, index){ return 'nav_sitewide_msg'; } } ];

                ue.uels("https://images-eu.ssl-images-amazon.com/images/I/31bJewCvY-L.js");
}
var ue_mbl=ue_csm.ue.exec(function(h,a){function s(c){b=c||{};a.AMZNPerformance=b;b.transition=b.transition||{};b.timing=b.timing||{};if(a.csa){var d;b.timing.transitionStart&&(d=b.timing.transitionStart);b.timing.processStart&&(d=b.timing.processStart);d&&(csa("PageTiming")("mark","nativeTransitionStart",d),csa("PageTiming")("mark","transitionStart",d))}h.ue.exec(t,"csm-android-check")()&&b.tags instanceof Array&&(c=-1!=b.tags.indexOf("usesAppStartTime")||b.transition.type?!b.transition.type&&-1<
b.tags.indexOf("usesAppStartTime")?"warm-start":void 0:"view-transition",c&&(b.transition.type=c));n=null;"reload"===e._nt&&h.ue_orct||"intrapage-transition"===e._nt?u(b):"undefined"===typeof e._nt&&f&&f.timing&&f.timing.navigationStart&&a.history&&"function"===typeof a.History&&"object"===typeof a.history&&a.history.length&&1!=a.history.length&&(b.timing.transitionStart=f.timing.navigationStart);p&&e.ssw(q,""+(b.timing.transitionStart||n||""));c=b.transition;d=e._nt?e._nt:void 0;c.subType=d;a.ue&&
a.ue.tag&&a.ue.tag("has-AMZNPerformance");e.isl&&a.uex&&a.uex("at","csm-timing");v()}function w(c){a.ue&&a.ue.count&&a.ue.count("csm-cordova-plugin-failed",1)}function t(){return a.cordova&&a.cordova.platformId&&"android"==a.cordova.platformId}function u(){if(p){var c=e.ssw(q),a=function(){},x=e.count||a,a=e.tag||a,k=b.timing.transitionStart,g=c&&!c.e&&c.val;n=c=g?+c.val:null;k&&g&&k>c?(x("csm.jumpStart.mtsDiff",k-c||0),a("csm-rld-mts-gt")):k&&g?a("csm-rld-mts-leq"):g?k||a("csm-rld-mts-no-new"):a("csm-rld-mts-no-old")}f&&
f.timing&&f.timing.navigationStart?b.timing.transitionStart=f.timing.navigationStart:delete b.timing.transitionStart}function v(){try{a.P.register("AMZNPerformance",function(){return b})}catch(c){}}function r(){if(!b)return"";ue_mbl.cnt=null;var c=b.timing,d=b.transition,d=["mts",l(c.transitionStart),"mps",l(c.processStart),"mtt",d.type,"mtst",d.subType,"mtlt",d.launchType];a.ue&&a.ue.tag&&(c.fr_ovr&&a.ue.tag("fr_ovr"),c.fcp_ovr&&a.ue.tag("fcp_ovr"),d.push("fr_ovr",l(c.fr_ovr),"fcp_ovr",l(c.fcp_ovr)));
for(var c="",e=0;e<d.length;e+=2){var f=d[e],g=d[e+1];"undefined"!==typeof g&&(c+="&"+f+"="+g)}return c}function l(a){if("undefined"!==typeof a&&"undefined"!==typeof m)return a-m}function y(a,d){b&&(m=d,b.timing.transitionStart=a,b.transition.type="view-transition",b.transition.subType="ajax-transition",b.transition.launchType="normal",ue_mbl.cnt=r)}var e=h.ue||{},m=h.ue_t0,q="csm-last-mts",p=1===h.ue_sswmts,n,f=a.performance,b;if(a.P&&a.P.when&&a.P.register)return 1===a.ue_fnt&&(m=a.aPageStart||
h.ue_t0),a.P.when("CSMPlugin").execute(function(a){a.buildAMZNPerformance&&a.buildAMZNPerformance({successCallback:s,failCallback:w})}),{cnt:r,ajax:y}},"mobile-timing")(ue_csm,ue_csm.window);

(function(d){d._uess=function(){var a="";screen&&screen.width&&screen.height&&(a+="&sw="+screen.width+"&sh="+screen.height);var b=function(a){var b=document.documentElement["client"+a];return"CSS1Compat"===document.compatMode&&b||document.body["client"+a]||b},c=b("Width"),b=b("Height");c&&b&&(a+="&vw="+c+"&vh="+b);return a}})(ue_csm);

(function(a){function c(a){d("log",a)}var d=csa("Errors",{producerId:"csa"});a.ue_err.buffer&&d&&(a.ue_err.buffer.forEach(c),a.ue_err.buffer.push=c);var b=document.ue_backdetect;b&&b.ue_back&&a.ue&&(a.ue.bfini=b.ue_back.value);a.uet&&a.uet("be");a.onLdEnd&&(window.addEventListener?window.addEventListener("load",a.onLdEnd,!1):window.attachEvent&&window.attachEvent("onload",a.onLdEnd));a.ueh&&a.ueh(0,window,"load",a.onLd,1);a.ue&&a.ue.tag&&(a.ue_furl?(b=a.ue_furl.replace(/\./g,"-"),a.ue.tag(b)):a.ue.tag("nofls"))})(ue_csm);

(function(g,h){function d(a,d){var b={};if(!e||!f)try{var c=h.sessionStorage;c?a&&("undefined"!==typeof d?c.setItem(a,d):b.val=c.getItem(a)):f=1}catch(g){e=1}e&&(b.e=1);return b}var b=g.ue||{},a="",f,e,c,a=d("csmtid");f?a="NA":a.e?a="ET":(a=a.val,a||(a=b.oid||"NI",d("csmtid",a)),c=d(b.oid),c.e||(c.val=c.val||0,d(b.oid,c.val+1)),b.ssw=d);b.tabid=a})(ue_csm,ue_csm.window);

ue_csm.ue.exec(function(e,f){var a=e.ue||{},b=a._wlo,d;if(a.ssw){d=a.ssw("CSM_previousURL").val;var c=f.location,b=b?b:c&&c.href?c.href.split("#")[0]:void 0;c=(b||"")===a.ssw("CSM_previousURL").val;!c&&b&&a.ssw("CSM_previousURL",b);d=c?"reload":d?"intrapage-transition":"first-view"}else d="unknown";a._nt=d},"NavTypeModule")(ue_csm,window);
ue_csm.ue.exec(function(c,a){function g(a){a.run(function(e){d.tag("csm-feature-"+a.name+":"+e);d.isl&&c.uex("at")})}if(a.addEventListener)for(var d=c.ue||{},f=[{name:"touch-enabled",run:function(b){var e=function(){a.removeEventListener("touchstart",c,!0);a.removeEventListener("mousemove",d,!0)},c=function(){b("true");e()},d=function(){b("false");e()};a.addEventListener("touchstart",c,!0);a.addEventListener("mousemove",d,!0)}}],b=0;b<f.length;b++)g(f[b])},"csm-features")(ue_csm,window);


(function(a,e){function c(a){d("recordCounter",a.c,a.v)}var b=e.images,d=csa("Metrics",{producerId:"csa"});b&&b.length&&a.ue.count("totalImages",b.length);a.ue.cv.buffer&&d&&(a.ue.cv.buffer.forEach(c),a.ue.cv.buffer.push=c)})(ue_csm,document);
(function(b){function c(){var d=[];a.log&&a.log.isStub&&a.log.replay(function(a){e(d,a)});a.clog&&a.clog.isStub&&a.clog.replay(function(a){e(d,a)});d.length&&(a._flhs+=1,n(d),p(d))}function g(){a.log&&a.log.isStub&&(a.onflush&&a.onflush.replay&&a.onflush.replay(function(a){a[0]()}),a.onunload&&a.onunload.replay&&a.onunload.replay(function(a){a[0]()}),c())}function e(d,b){var c=b[1],f=b[0],e={};a._lpn[c]=(a._lpn[c]||0)+1;e[c]=f;d.push(e)}function n(b){q&&(a._lpn.csm=(a._lpn.csm||0)+1,b.push({csm:{k:"chk",
f:a._flhs,l:a._lpn,s:"inln"}}))}function p(a){if(h)a=k(a),b.navigator.sendBeacon(l,a);else{a=k(a);var c=new b[f];c.open("POST",l,!0);c.setRequestHeader&&c.setRequestHeader("Content-type","text/plain");c.send(a)}}function k(a){return JSON.stringify({rid:b.ue_id,sid:b.ue_sid,mid:b.ue_mid,mkt:b.ue_mkt,sn:b.ue_sn,reqs:a})}var f="XMLHttpRequest",q=1===b.ue_ddq,a=b.ue,r=b[f]&&"withCredentials"in new b[f],h=b.navigator&&b.navigator.sendBeacon,l="//"+b.ue_furl+"/1/batch/1/OE/",m=b.ue_fci_ft||5E3;a&&(r||h)&&
(a._flhs=a._flhs||0,a._lpn=a._lpn||{},a.attach&&(a.attach("beforeunload",a.exec(g,"fcli-bfu")),a.attach("pagehide",a.exec(g,"fcli-ph"))),m&&b.setTimeout(a.exec(c,"fcli-t"),m),a._ffci=a.exec(c))})(window);


(function(k,c){function l(a,b){return a.filter(function(a){return a.initiatorType==b})}function f(a,c){if(b.t[a]){var g=b.t[a]-b._t0,e=c.filter(function(a){return 0!==a.responseEnd&&m(a)<g}),f=l(e,"script"),h=l(e,"link"),k=l(e,"img"),n=e.map(function(a){return a.name.split("/")[2]}).filter(function(a,b,c){return a&&c.lastIndexOf(a)==b}),q=e.filter(function(a){return a.duration<p}),s=g-Math.max.apply(null,e.map(m))<r|0;"af"==a&&(b._afjs=f.length);return a+":"+[e[d],f[d],h[d],k[d],n[d],q[d],s].join("-")}}
function m(a){return a.responseEnd-(b._t0-c.timing.navigationStart)}function n(){var a=c[h]("resource"),d=f("cf",a),g=f("af",a),a=f("ld",a);delete b._rt;b._ld=b.t.ld-b._t0;b._art&&b._art();return[d,g,a].join("_")}var p=20,r=50,d="length",b=k.ue,h="getEntriesByType";b._rre=m;b._rt=c&&c.timing&&c[h]&&n})(ue_csm,window.performance);


(function(c,d){var b=c.ue,a=d.navigator;b&&b.tag&&a&&(a=a.connection||a.mozConnection||a.webkitConnection)&&a.type&&b.tag("netInfo:"+a.type)})(ue_csm,window);


(function(c,d){function h(a,b){for(var c=[],d=0;d<a.length;d++){var e=a[d],f=b.encode(e);if(e[k]){var g=b.metaSep,e=e[k],l=b.metaPairSep,h=[],m=void 0;for(m in e)e.hasOwnProperty(m)&&h.push(m+"="+e[m]);e=h.join(l);f+=g+e}c.push(f)}return c.join(b.resourceSep)}function s(a){var b=a[k]=a[k]||{};b[t]||(b[t]=c.ue_mid);b[u]||(b[u]=c.ue_sid);b[f]||(b[f]=c.ue_id);b.csm=1;a="//"+c.ue_furl+"/1/"+a[v]+"/1/OP/"+a[w]+"/"+a[x]+"/"+h([a],y);if(n)try{n.call(d[p],a)}catch(g){c.ue.sbf=1,(new Image).src=a}else(new Image).src=
a}function q(){g&&g.isStub&&g.replay(function(a,b,c){a=a[0];b=a[k]=a[k]||{};b[f]=b[f]||c;s(a)});l.impression=s;g=null}if(!(1<c.ueinit)){var k="metadata",x="impressionType",v="foresterChannel",w="programGroup",t="marketplaceId",u="session",f="requestId",p="navigator",l=c.ue||{},n=d[p]&&d[p].sendBeacon,r=function(a,b,c,d){return{encode:d,resourceSep:a,metaSep:b,metaPairSep:c}},y=r("","?","&",function(a){return h(a.impressionData,z)}),z=r("/",":",",",function(a){return a.featureName+":"+h(a.resources,
A)}),A=r(",","@","|",function(a){return a.id}),g=l.impression;n?q():(l.attach("load",q),l.attach("beforeunload",q));try{d.P&&d.P.register&&d.P.register("impression-client",function(){})}catch(B){c.ueLogError(B,{logLevel:"WARN"})}}})(ue_csm,window);



var ue_pty = "CustomerReviews";

var ue_spty = "remoteProduct";

var ue_pti = "B08L5VRVTD";


var ue_adb = 4;
var ue_adb_rtla = 1;
ue_csm.ue.exec(function(y,a){function t(){if(d&&f){var a;a:{try{a=d.getItem(g);break a}catch(c){}a=void 0}if(a)return b=a,!0}return!1}function u(){if(a.fetch)fetch(m).then(function(a){if(!a.ok)throw Error(a.statusText);return a.text?a.text():null}).then(function(b){b?(-1<b.indexOf("window.ue_adb_chk = 1")&&(a.ue_adb_chk=1),n()):h()})["catch"](h);else e.uels(m,{onerror:h,onload:n})}function h(){b=k;l();if(f)try{d.setItem(g,b)}catch(a){}}function n(){b=1===a.ue_adb_chk?p:k;l();if(f)try{d.setItem(g,
b)}catch(c){}}function q(){a.ue_adb_rtla&&c&&0<c.ec&&!1===r&&(c.elh=null,ueLogError({m:"Hit Info",fromOnError:1},{logLevel:"INFO",adb:b}),r=!0)}function l(){e.tag(b);e.isl&&a.uex&&uex("at",b);s&&s.updateCsmHit("adb",b);c&&0<c.ec?q():a.ue_adb_rtla&&c&&(c.elh=q)}function v(){return b}if(a.ue_adb){a.ue_fadb=a.ue_fadb||10;var e=a.ue,k="adblk_yes",p="adblk_no",m="https://m.media-amazon.com/images/G/01/csm/showads.v2.js?ad_size=_Ad300x250_&adstype=-sponsored-links-&advertiser=_googleads_",b="adblk_unk",
d;a:{try{d=a.localStorage;break a}catch(z){}d=void 0}var g="csm:adb",c=a.ue_err,s=e.cookie,f=void 0!==a.localStorage,w=Math.random()>1-1/a.ue_fadb,r=!1,x=t();w||!x?u():l();a.ue_isAdb=v;a.ue_isAdb.unk="adblk_unk";a.ue_isAdb.no=p;a.ue_isAdb.yes=k}},"adb")(document,window);




(function(c,l,m){function h(a){if(a)try{if(a.id)return"//*[@id='"+a.id+"']";var b,d=1,e;for(e=a.previousSibling;e;e=e.previousSibling)e.nodeName===a.nodeName&&(d+=1);b=d;var c=a.nodeName;1!==b&&(c+="["+b+"]");a.parentNode&&(c=h(a.parentNode)+"/"+c);return c}catch(f){return"DETACHED"}}function f(a){if(a&&a.getAttribute)return a.getAttribute(k)?a.getAttribute(k):f(a.parentElement)}var k="data-cel-widget",g=!1,d=[];(c.ue||{}).isBF=function(){try{var a=JSON.parse(localStorage["csm-bf"]||"[]"),b=0<=a.indexOf(c.ue_id);
a.unshift(c.ue_id);a=a.slice(0,20);localStorage["csm-bf"]=JSON.stringify(a);return b}catch(d){return!1}}();c.ue_utils={getXPath:h,getFirstAscendingWidget:function(a,b){c.ue_cel&&c.ue_fem?!0===g?b(f(a)):d.push({element:a,callback:b}):b()},notifyWidgetsLabeled:function(){if(!1===g){g=!0;for(var a=f,b=0;b<d.length;b++)if(d[b].hasOwnProperty("callback")&&d[b].hasOwnProperty("element")){var c=d[b].callback,e=d[b].element;"function"===typeof c&&"function"===typeof a&&c(a(e))}d=null}},extractStringValue:function(a){if("string"===
typeof a)return a}}})(ue_csm,window,document);


(function(a){a.ue_cel||(a.ue_cel=function(){function f(a,c){c?c.r=v:c={r:v,c:1};!ue_csm.ue_sclog&&c.clog&&d.clog?d.clog(a,c.ns||q,c):c.glog&&d.glog?d.glog(a,c.ns||q,c):d.log(a,c.ns||q,c)}function m(a,d){"function"===typeof g&&g("log",{schemaId:s+".RdCSI.1",eventType:a,clientData:d},{ent:{page:["requestId"]}})}function c(){var a=n.length;if(0<a){for(var c=[],b=0;b<a;b++){var F=n[b].api;F.ready()?(F.on({ts:d.d,ns:q}),e.push(n[b]),f({k:"mso",n:n[b].name,t:d.d()})):c.push(n[b])}n=c}}function h(){if(!h.executed){for(var a=
0;a<e.length;a++)e[a].api.off&&e[a].api.off({ts:d.d,ns:q});A();f({k:"eod",t0:d.t0,t:d.d()},{c:1,il:1});h.executed=1;for(a=0;a<e.length;a++)n.push(e[a]);e=[];b(t);b(x)}}function A(a){f({k:"hrt",t:d.d()},{c:1,il:1,n:a});l=Math.min(w,r*l);y()}function y(){b(x);x=k(function(){A(!0)},l)}function u(){h.executed||A()}var p=a.window,k=p.setTimeout,b=p.clearTimeout,r=1.5,w=p.ue_cel_max_hrt||3E4,s="robotdetection",n=[],e=[],q=a.ue_cel_ns||"cel",t,x,d=a.ue,E=a.uet,B=a.uex,v=d.rid,C=p.csa,g,l=p.ue_cel_hrt_int||
3E3,z=p.requestAnimationFrame||function(a){a()};!a.ue_cel_lclia&&C&&(g=C("Events",{producerId:s}));if(d.isBF)f({k:"bft",t:d.d()});else{"function"==typeof E&&E("bb","csmCELLSframework",{wb:1});k(c,0);d.onunload(h);if(d.onflush)d.onflush(u);t=k(h,6E5);y();"function"==typeof B&&B("ld","csmCELLSframework",{wb:1});return{registerModule:function(a,b){n.push({name:a,api:b});f({k:"mrg",n:a,t:d.d()});c()},reset:function(a){f({k:"rst",t0:d.t0,t:d.d()});n=n.concat(e);e=[];for(var r=n.length,g=0;g<r;g++)n[g].api.off(),
n[g].api.reset();v=a||d.rid;c();b(t);t=k(h,6E5);h.executed=0},timeout:function(a,d){return k(function(){z(function(){h.executed||a()})},d)},log:f,csaEventLog:m,off:h}}}())})(ue_csm);
(function(a){a.ue_pdm||!a.ue_cel||a.ue.isBF||(a.ue_pdm=function(){function f(){try{var d=b.screen;if(d){var c={w:d.width,aw:d.availWidth,h:d.height,ah:d.availHeight,cd:d.colorDepth,pd:d.pixelDepth};e&&e.w===c.w&&e.h===c.h&&e.aw===c.aw&&e.ah===c.ah&&e.pd===c.pd&&e.cd===c.cd||(e=c,e.t=s(),e.k="sci",E(e),!C&&g&&l("sci",{h:(e.h||"0")+""}))}var k=r.body||{},h=r.documentElement||{},m={w:Math.max(k.scrollWidth||0,k.offsetWidth||0,h.clientWidth||0,h.scrollWidth||0,h.offsetWidth||0),h:Math.max(k.scrollHeight||
0,k.offsetHeight||0,h.clientHeight||0,h.scrollHeight||0,h.offsetHeight||0)};q&&q.w===m.w&&q.h===m.h||(q=m,q.t=s(),q.k="doi",E(q));w=a.ue_cel.timeout(f,n);x+=1}catch(p){b.ueLogError&&ueLogError(p,{attribution:"csm-cel-page-module",logLevel:"WARN"})}}function m(){u("ebl","default",!1)}function c(){u("efo","default",!0)}function h(){u("ebl","app",!1)}function A(){u("efo","app",!0)}function y(){b.setTimeout(function(){r[H]?u("ebl","pageviz",!1):u("efo","pageviz",!0)},0)}function u(a,d,c){t!==c&&(E({k:a,
t:s(),s:d},{ff:!0===c?0:1}),!C&&g&&l(a,{t:(s()||"0")+"",s:d}));t=c}function p(){d.attach&&(z&&d.attach(D,y,r),I&&P.when("mash").execute(function(a){a&&a.addEventListener&&(a.addEventListener("appPause",h),a.addEventListener("appResume",A))}),d.attach("blur",m,b),d.attach("focus",c,b))}function k(){d.detach&&(z&&d.detach(D,y,r),I&&P.when("mash").execute(function(a){a&&a.removeEventListener&&(a.removeEventListener("appPause",h),a.removeEventListener("appResume",A))}),d.detach("blur",m,b),d.detach("focus",
c,b))}var b=a.window,r=a.document,w,s,n,e,q,t=null,x=0,d=a.ue,E=a.ue_cel.log,B=a.uet,v=a.uex,C=a.ue_cel_lclia,g=b.csa,l=a.ue_cel.csaEventLog,z=!!d.pageViz,D=z&&d.pageViz.event,H=z&&d.pageViz.propHid,I=b.P&&b.P.when;"function"==typeof B&&B("bb","csmCELLSpdm",{wb:1});return{on:function(a){n=a.timespan||500;s=a.ts;p();a=b.location;E({k:"pmd",o:a.origin,p:a.pathname,t:s()});f();"function"==typeof v&&v("ld","csmCELLSpdm",{wb:1})},off:function(a){clearTimeout(w);k();d.count&&d.count("cel.PDM.TotalExecutions",
x)},ready:function(){return r.body&&a.ue_cel&&a.ue_cel.log},reset:function(){e=q=null}}}(),a.ue_cel&&a.ue_cel.registerModule("page module",a.ue_pdm))})(ue_csm);
(function(a){a.ue_vpm||!a.ue_cel||a.ue.isBF||(a.ue_vpm=function(){function f(){var a=y(),b={w:k.innerWidth,h:k.innerHeight,x:k.pageXOffset,y:k.pageYOffset};c&&c.w==b.w&&c.h==b.h&&c.x==b.x&&c.y==b.y||(b.t=a,b.k="vpi",c=b,r(c,{clog:1}),!q&&t&&x("vpi",{t:(c.t||"0")+"",h:(c.h||"0")+"",y:(c.y||"0")+"",w:(c.w||"0")+"",x:(c.x||"0")+""}));h=0;u=y()-a;p+=1}function m(){h||(h=a.ue_cel.timeout(f,A))}var c,h,A,y,u=0,p=0,k=a.window,b=a.ue,r=a.ue_cel.log,w=a.uet,s=a.uex,n=b.attach,e=b.detach,q=a.ue_cel_lclia,t=
k.csa,x=a.ue_cel.csaEventLog;"function"==typeof w&&w("bb","csmCELLSvpm",{wb:1});return{on:function(a){y=a.ts;A=a.timespan||100;f();n&&(n("scroll",m),n("resize",m));"function"==typeof s&&s("ld","csmCELLSvpm",{wb:1})},off:function(a){clearTimeout(h);e&&(e("scroll",m),e("resize",m));b.count&&(b.count("cel.VPI.TotalExecutions",p),b.count("cel.VPI.TotalExecutionTime",u),b.count("cel.VPI.AverageExecutionTime",u/p))},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){c=void 0},getVpi:function(){return c}}}(),
a.ue_cel&&a.ue_cel.registerModule("viewport module",a.ue_vpm))})(ue_csm);
(function(a){if(!a.ue_fem&&a.ue_cel&&a.ue_utils){var f=a.ue||{},m=a.window,c=m.document;!f.isBF&&!a.ue_fem&&c.querySelector&&m.getComputedStyle&&[].forEach&&(a.ue_fem=function(){function h(a,d){return a>d?3>a-d:3>d-a}function A(a,d){var c=m.pageXOffset,b=m.pageYOffset,k;a:{try{if(a){var g=a.getBoundingClientRect(),e,r=0===a.offsetWidth&&0===a.offsetHeight;c:{for(var f=a.parentNode,w=g.left||0,n=g.top||0,p=g.width||0,q=g.height||0;f&&f!==document.body;){var l;d:{try{var s=void 0;if(f)var G=f.getBoundingClientRect(),
s={x:G.left||0,y:G.top||0,w:G.width||0,h:G.height||0};else s=void 0;l=s;break d}catch(v){}l=void 0}var t=window.getComputedStyle(f),u="hidden"===t.overflow,y=u||"hidden"===t.overflowX,z=u||"hidden"===t.overflowY,J=n+q-1<l.y+1||n+1>l.y+l.h-1;if((w+p-1<l.x+1||w+1>l.x+l.w-1)&&y||J&&z){e=!0;break c}f=f.parentNode}e=!1}k={x:g.left+c||0,y:g.top+b||0,w:g.width||0,h:g.height||0,d:(r||e)|0}}else k=void 0;break a}catch(A){}k=void 0}if(k&&!a.cel_b)a.cel_b=k,C({n:a.getAttribute(x),w:a.cel_b.w,h:a.cel_b.h,d:a.cel_b.d,
x:a.cel_b.x,y:a.cel_b.y,t:d,k:"ewi",cl:a.className},{clog:1});else{if(c=k)c=a.cel_b,b=k,c=b.d===c.d&&1===b.d?!1:!(h(c.x,b.x)&&h(c.y,b.y)&&h(c.w,b.w)&&h(c.h,b.h)&&c.d===b.d);c&&(a.cel_b=k,C({n:a.getAttribute(x),w:a.cel_b.w,h:a.cel_b.h,d:a.cel_b.d,x:a.cel_b.x,y:a.cel_b.y,t:d,k:"ewi"},{clog:1}))}}function y(b,g){var h;h=b.c?c.getElementsByClassName(b.c):b.id?[c.getElementById(b.id)]:c.querySelectorAll(b.s);b.w=[];for(var f=0;f<h.length;f++){var e=h[f];if(e){if(!e.getAttribute(x)){var r=e.getAttribute("cel_widget_id")||
(b.id_gen||v)(e,f)||e.id;e.setAttribute(x,r)}b.w.push(e);k(Q,e,g)}}!1===B&&(E++,E===d.length&&(B=!0,a.ue_utils.notifyWidgetsLabeled()))}function u(a,c){g.contains(a)||C({n:a.getAttribute(x),t:c,k:"ewd"},{clog:1})}function p(a){K.length&&ue_cel.timeout(function(){if(q){for(var c=R(),d=!1;R()-c<e&&!d;){for(d=S;0<d--&&0<K.length;){var b=K.shift();T[b.type](b.elem,b.time)}d=0===K.length}U++;p(a)}},0)}function k(a,c,d){K.push({type:a,elem:c,time:d})}function b(a,c){for(var b=0;b<d.length;b++)for(var e=
d[b].w||[],g=0;g<e.length;g++)k(a,e[g],c)}function r(){M||(M=a.ue_cel.timeout(function(){M=null;var c=t();b(W,c);for(var g=0;g<d.length;g++)k(X,d[g],c);0===d.length&&!1===B&&(B=!0,a.ue_utils.notifyWidgetsLabeled());p(c)},n))}function w(){M||N||(N=a.ue_cel.timeout(function(){N=null;var a=t();b(Q,a);p(a)},n))}function s(){return z&&D&&g&&g.contains&&g.getBoundingClientRect&&t}var n=50,e=4.5,q=!1,t,x="data-cel-widget",d=[],E=0,B=!1,v=function(){},C=a.ue_cel.log,g,l,z,D,H=m.MutationObserver||m.WebKitMutationObserver||
m.MozMutationObserver,I=!!H,F,G,O="DOMAttrModified",L="DOMNodeInserted",J="DOMNodeRemoved",N,M,K=[],U=0,S=null,W="removedWidget",X="updateWidgets",Q="processWidget",T,V=m.performance||{},R=V.now&&function(){return V.now()}||function(){return Date.now()};"function"==typeof uet&&uet("bb","csmCELLSfem",{wb:1});return{on:function(b){function e(){if(s()){T={removedWidget:u,updateWidgets:y,processWidget:A};if(I){var a={attributes:!0,subtree:!0};F=new H(w);G=new H(r);F.observe(g,a);G.observe(g,{childList:!0,
subtree:!0});G.observe(l,a)}else z.call(g,O,w),z.call(g,L,r),z.call(g,J,r),z.call(l,L,w),z.call(l,J,w);r()}}g=c.body;l=c.head;z=g.addEventListener;D=g.removeEventListener;t=b.ts;d=a.cel_widgets||[];S=b.bs||5;f.deffered?e():f.attach&&f.attach("load",e);"function"==typeof uex&&uex("ld","csmCELLSfem",{wb:1});q=!0},off:function(){s()&&(G&&(G.disconnect(),G=null),F&&(F.disconnect(),F=null),D.call(g,O,w),D.call(g,L,r),D.call(g,J,r),D.call(l,L,w),D.call(l,J,w));f.count&&f.count("cel.widgets.batchesProcessed",
U);q=!1},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){d=a.cel_widgets||[]}}}(),a.ue_cel&&a.ue_fem&&a.ue_cel.registerModule("features module",a.ue_fem))}})(ue_csm);
(function(a){!a.ue_mcm&&a.ue_cel&&a.ue_utils&&!a.ue.isBF&&(a.ue_mcm=function(){function f(a,b){var h=a.srcElement||a.target||{},f={k:m,w:(b||{}).ow||(A.body||{}).scrollWidth,h:(b||{}).oh||(A.body||{}).scrollHeight,t:(b||{}).ots||c(),x:a.pageX,y:a.pageY,p:p.getXPath(h),n:h.nodeName};y&&"function"===typeof y.now&&a.timeStamp&&(f.dt=(b||{}).odt||y.now()-a.timeStamp,f.dt=parseFloat(f.dt.toFixed(2)));a.button&&(f.b=a.button);h.href&&(f.r=p.extractStringValue(h.href));h.id&&(f.i=h.id);h.className&&h.className.split&&
(f.c=h.className.split(/\s+/));u(f,{c:1})}var m="mcm",c,h=a.window,A=h.document,y=h.performance,u=a.ue_cel.log,p=a.ue_utils;return{on:function(k){c=k.ts;a.ue_cel_stub&&a.ue_cel_stub.replayModule(m,f);h.addEventListener&&h.addEventListener("mousedown",f,!0)},off:function(a){h.addEventListener&&h.removeEventListener("mousedown",f,!0)},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){}}}(),a.ue_cel&&a.ue_cel.registerModule("mouse click module",a.ue_mcm))})(ue_csm);
(function(a){a.ue_mmm||!a.ue_cel||a.ue.isBF||(a.ue_mmm=function(f){function m(a,c){var b={x:a.pageX||a.x||0,y:a.pageY||a.y||0,t:p()};!c&&l&&(b.t-l.t<A||b.x==l.x&&b.y==l.y)||(l=b,v.push(b))}function c(){if(v.length){E=F.now();for(var a=0;a<v.length;a++){var c=v[a],b=a;z=v[g];D=c;var e=void 0;if(!(e=2>b)){e=void 0;a:if(v[b].t-v[b-1].t>h)e=0;else{for(e=g+1;e<b;e++){var f=z,k=D,l=v[e];H=(k.x-f.x)*(f.y-l.y)-(f.x-l.x)*(k.y-f.y);if(H*H/((k.x-f.x)*(k.x-f.x)+(k.y-f.y)*(k.y-f.y))>y){e=0;break a}}e=1}e=!e}(I=
e)?g=b-1:C.pop();C.push(c)}B=F.now()-E;q=Math.min(q,B);t=Math.max(t,B);x=(x*d+B)/(d+1);d+=1;n({k:u,e:C,min:Math.floor(1E3*q),max:Math.floor(1E3*t),avg:Math.floor(1E3*x)},{c:1});v=[];C=[];g=0}}var h=100,A=20,y=25,u="mmm1",p,k,b=a.window,r=b.document,w=b.setInterval,s=a.ue,n=a.ue_cel.log,e,q=1E3,t=0,x=0,d=0,E,B,v=[],C=[],g=0,l,z,D,H,I,F=f&&f.now&&f||Date.now&&Date||{now:function(){return(new Date).getTime()}};return{on:function(a){p=a.ts;k=a.ns;s.attach&&s.attach("mousemove",m,r);e=w(c,3E3)},off:function(a){k&&
(l&&m(l,!0),c());clearInterval(e);s.detach&&s.detach("mousemove",m,r)},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){v=[];C=[];g=0;l=null}}}(window.performance),a.ue_cel&&a.ue_cel.registerModule("mouse move module",a.ue_mmm))})(ue_csm);



ue_csm.ue.exec(function(b,c){var e=function(){},f=function(){return{send:function(b,d){if(d&&b){var a;if(c.XDomainRequest)a=new XDomainRequest,a.onerror=e,a.ontimeout=e,a.onprogress=e,a.onload=e,a.timeout=0;else if(c.XMLHttpRequest){if(a=new XMLHttpRequest,!("withCredentials"in a))throw"";}else a=void 0;if(!a)throw"";a.open("POST",b,!0);a.setRequestHeader&&a.setRequestHeader("Content-type","text/plain");a.send(d)}},isSupported:!0}}(),g=function(){return{send:function(c,d){if(c&&d)if(navigator.sendBeacon(c,
d))b.ue_sbuimp&&b.ue&&b.ue.ssw&&b.ue.ssw("eelsts","scs");else throw"";},isSupported:!!navigator.sendBeacon&&!(c.cordova&&c.cordova.platformId&&"ios"==c.cordova.platformId)}}();b.ue._ajx=f;b.ue._sBcn=g},"Transportation-clients")(ue_csm,window);
ue_csm.ue.exec(function(b,k){function B(){for(var a=0;a<arguments.length;a++){var c=arguments[a];try{var g;if(c.isSupported){var f=u.buildPayload(l,e);g=c.send(K,f)}else throw dummyException;return g}catch(d){}}a={m:"All supported clients failed",attribution:"CSMSushiClient_TRANSPORTATION_FAIL",f:"sushi-client.js",logLevel:"ERROR"};C(a,k.ue_err_chan||"jserr");b.ue_err.buffer&&b.ue_err.buffer.push(a)}function m(){if(e.length){for(var a=0;a<n.length;a++)n[a]();B(d._sBcn||{},d._ajx||{});e=[];h={};l=
{};v=w=r=x=0}}function L(){var a=new Date,c=function(a){return 10>a?"0"+a:a};return Date.prototype.toISOString?a.toISOString():a.getUTCFullYear()+"-"+c(a.getUTCMonth()+1)+"-"+c(a.getUTCDate())+"T"+c(a.getUTCHours())+":"+c(a.getUTCMinutes())+":"+c(a.getUTCSeconds())+"."+String((a.getUTCMilliseconds()/1E3).toFixed(3)).slice(2,5)+"Z"}function y(a){try{return JSON.stringify(a)}catch(c){}return null}function D(a,c,g,f){var q=!1;f=f||{};s++;if(s==E){var p={m:"Max number of Sushi Logs exceeded",f:"sushi-client.js",
logLevel:"ERROR",attribution:"CSMSushiClient_MAX_CALLS"};C(p,k.ue_err_chan||"jserr");b.ue_err.buffer&&b.ue_err.buffer.push(p)}if(p=!(s>=E))(p=a&&-1<a.constructor.toString().indexOf("Object")&&c&&-1<c.constructor.toString().indexOf("String")&&g&&-1<g.constructor.toString().indexOf("String"))||M++;p&&(d.count&&d.count("Event:"+g,1),a.producerId=a.producerId||c,a.schemaId=a.schemaId||g,a.timestamp=L(),c=Date.now?Date.now():+new Date,g=Math.random().toString().substring(2,12),a.messageId=b.ue_id+"-"+
c+"-"+g,f&&!f.ssd&&(a.sessionId=a.sessionId||b.ue_sid,a.requestId=a.requestId||b.ue_id,a.obfuscatedMarketplaceId=a.obfuscatedMarketplaceId||b.ue_mid),(c=y(a))?(c=c.length,(e.length==N||r+c>O)&&m(),r+=c,a={data:u.compressEvent(a)},e.push(a),(f||{}).n?0===F?m():v||(v=k.setTimeout(m,F)):w||(w=k.setTimeout(m,P)),q=!0):q=!1);!q&&b.ue_int&&console.error("Invalid JS Nexus API call");return q}function G(){if(!H){for(var a=0;a<z.length;a++)z[a]();for(a=0;a<n.length;a++)n[a]();e.length&&(b.ue_sbuimp&&b.ue&&
b.ue.ssw&&(a=y({dct:l,evt:e}),b.ue.ssw("eeldata",a),b.ue.ssw("eelsts","unk")),B(d._sBcn||{}));H=!0}}function I(a){z.push(a)}function J(a){n.push(a)}var E=1E3,N=499,O=524288,t=function(){},d=b.ue||{},C=d.log||t,Q=b.uex||t;(b.uet||t)("bb","ue_sushi_v1",{wb:1});var K=b.ue_surl||"https://unagi-na.amazon.com/1/events/com.amazon.csm.nexusclient.gamma",R=["messageId","timestamp"],A="#",e=[],h={},l={},r=0,x=0,M=0,s=0,z=[],n=[],H=!1,v,w,F=void 0===b.ue_hpsi?1E3:b.ue_hpsi,P=void 0===b.ue_lpsi?1E4:b.ue_lpsi,
u=function(){function a(a){h[a]=A+x++;l[h[a]]=a;return h[a]}function c(b){if(!(b instanceof Function)){if(b instanceof Array){for(var f=[],d=b.length,e=0;e<d;e++)f[e]=c(b[e]);return f}if(b instanceof Object){f={};for(d in b)b.hasOwnProperty(d)&&(f[h[d]?h[d]:a(d)]=-1===R.indexOf(d)?c(b[d]):b[d]);return f}return"string"===typeof b&&(b.length>(A+x).length||b.charAt(0)===A)?h[b]?h[b]:a(b):b}}return{compressEvent:c,buildPayload:function(){return y({cs:{dct:l},events:e})}}}();(function(){if(d.event&&d.event.isStub){if(b.ue_sbuimp&&
b.ue&&b.ue.ssw){var a=b.ue.ssw("eelsts").val;if(a&&"unk"===a&&(a=b.ue.ssw("eeldata").val)){var c;a:{try{c=JSON.parse(a);break a}catch(g){}c=null}c&&c.evt instanceof Array&&c.dct instanceof Object&&(e=c.evt,l=c.dct,e&&l&&(m(),b.ue.ssw("eeldata","{}"),b.ue.ssw("eelsts","scs")))}}d.event.replay(function(a){a[3]=a[3]||{};a[3].n=1;D.apply(this,a)});d.onSushiUnload.replay(function(a){I(a[0])});d.onSushiFlush.replay(function(a){J(a[0])})}})();d.attach("beforeunload",G);d.attach("pagehide",G);d._cmps=u;d.event=
D;d.event.reset=function(){s=0};d.onSushiUnload=I;d.onSushiFlush=J;try{k.P&&k.P.register&&k.P.register("sushi-client",t)}catch(S){b.ueLogError(S,{logLevel:"WARN"})}Q("ld","ue_sushi_v1",{wb:1})},"Nxs-JS-Client")(ue_csm,window);


ue_csm.ue_unrt = 1500;
(function(d,b,t){function u(a,g){var c=a.srcElement||a.target||{},b={k:v,t:g.t,dt:g.dt,x:a.pageX,y:a.pageY,p:e.getXPath(c),n:c.nodeName};a.button&&(b.b=a.button);c.type&&(b.ty=c.type);c.href&&(b.r=e.extractStringValue(c.href));c.id&&(b.i=c.id);c.className&&c.className.split&&(b.c=c.className.split(/\s+/));h+=1;e.getFirstAscendingWidget(c,function(a){b.wd=a;d.ue.log(b,r)})}function w(a){if(!x(a.srcElement||a.target)){m+=1;n=!0;var g=f=d.ue.d(),c;p&&"function"===typeof p.now&&a.timeStamp&&(c=p.now()-
a.timeStamp,c=parseFloat(c.toFixed(2)));s=b.setTimeout(function(){u(a,{t:g,dt:c})},y)}}function z(a){if(a){var b=a.filter(A);a.length!==b.length&&(q=!0,k=d.ue.d(),n&&q&&(k&&f&&d.ue.log({k:B,t:f,m:Math.abs(k-f)},r),l(),q=!1,k=0))}}function A(a){if(!a)return!1;var b="characterData"===a.type?a.target.parentElement:a.target;if(!b||!b.hasAttributes||!b.attributes)return!1;var c={"class":"gw-clock gw-clock-aria s-item-container-height-auto feed-carousel using-mouse kfs-inner-container".split(" "),id:["dealClock",
"deal_expiry_timer","timer"],role:["timer"]},d=!1;Object.keys(c).forEach(function(a){var e=b.attributes[a]?b.attributes[a].value:"";(c[a]||"").forEach(function(a){-1!==e.indexOf(a)&&(d=!0)})});return d}function x(a){if(!a)return!1;var b=(e.extractStringValue(a.nodeName)||"").toLowerCase(),c=(e.extractStringValue(a.type)||"").toLowerCase(),d=(e.extractStringValue(a.href)||"").toLowerCase();a=(e.extractStringValue(a.id)||"").toLowerCase();var f="checkbox color date datetime-local email file month number password radio range reset search tel text time url week".split(" ");
if(-1!==["select","textarea","html"].indexOf(b)||"input"===b&&-1!==f.indexOf(c)||"a"===b&&-1!==d.indexOf("http")||-1!==["sitbreaderrightpageturner","sitbreaderleftpageturner","sitbreaderpagecontainer"].indexOf(a))return!0}function l(){n=!1;f=0;b.clearTimeout(s)}function C(){b.ue.onunload(function(){ue.count("armored-cxguardrails.unresponsive-clicks.violations",h);ue.count("armored-cxguardrails.unresponsive-clicks.violationRate",h/m*100||0)})}if(b.MutationObserver&&b.addEventListener&&Object.keys&&
d&&d.ue&&d.ue.log&&d.ue_unrt&&d.ue_utils){var y=d.ue_unrt,r="cel",v="unr_mcm",B="res_mcm",p=b.performance,e=d.ue_utils,n=!1,f=0,s=0,q=!1,k=0,h=0,m=0;b.addEventListener&&(b.addEventListener("mousedown",w,!0),b.addEventListener("beforeunload",l,!0),b.addEventListener("visibilitychange",l,!0),b.addEventListener("pagehide",l,!0));b.ue&&b.ue.event&&b.ue.onSushiUnload&&b.ue.onunload&&C();(new MutationObserver(z)).observe(t,{childList:!0,attributes:!0,characterData:!0,subtree:!0})}})(ue_csm,window,document);


ue_csm.ue.exec(function(g,e){if(e.ue_err){var f="";e.ue_err.errorHandlers||(e.ue_err.errorHandlers=[]);e.ue_err.errorHandlers.push({name:"fctx",handler:function(a){if(!a.logLevel||"FATAL"===a.logLevel)if(f=g.getElementsByTagName("html")[0].innerHTML){var b=f.indexOf("var ue_t0=ue_t0||+new Date();");if(-1!==b){var b=f.substr(0,b).split(String.fromCharCode(10)),d=Math.max(b.length-10-1,0),b=b.slice(d,b.length-1);a.fcsmln=d+b.length+1;a.cinfo=a.cinfo||{};for(var c=0;c<b.length;c++)a.cinfo[d+c+1+""]=
b[c]}b=f.split(String.fromCharCode(10));a.cinfo=a.cinfo||{};if(!(a.f||void 0===a.l||a.l in a.cinfo))for(c=+a.l-1,d=Math.max(c-5,0),c=Math.min(c+5,b.length-1);d<=c;d++)a.cinfo[d+1+""]=b[d]}}})}},"fatals-context")(document,window);


(function(m,a){function c(k){function f(b){b&&"string"===typeof b&&(b=(b=b.match(/^(?:https?:)?\/\/(.*?)(\/|$)/i))&&1<b.length?b[1]:null,b&&b&&("number"===typeof e[b]?e[b]++:e[b]=1))}function d(b){var e=10,d=+new Date;b&&b.timeRemaining?e=b.timeRemaining():b={timeRemaining:function(){return Math.max(0,e-(+new Date-d))}};for(var c=a.performance.getEntries(),k=e;g<c.length&&k>n;)c[g].name&&f(c[g].name),g++,k=b.timeRemaining();g>=c.length?h(!0):l()}function h(b){if(!b){b=m.scripts;var c;if(b)for(var d=
0;d<b.length;d++)(c=b[d].getAttribute("src"))&&"undefined"!==c&&f(c)}0<Object.keys(e).length&&(p&&ue_csm.ue&&ue_csm.ue.event&&ue_csm.ue.event({domains:e,pageType:a.ue_pty||null,subPageType:a.ue_spty||null,pageTypeId:a.ue_pti||null},"csm","csm.CrossOriginDomains.2"),a.ue_ext=e)}function l(){!0===k?d():a.requestIdleCallback?a.requestIdleCallback(d):a.requestAnimationFrame?a.requestAnimationFrame(d):a.setTimeout(d,100)}function c(){if(a.performance&&a.performance.getEntries){var b=a.performance.getEntries();
!b||0>=b.length?h(!1):l()}else h(!1)}var e=a.ue_ext||{};a.ue_ext||c();return e}function q(){setTimeout(c,r)}var s=a.ue_dserr||!1,p=!0,n=1,r=2E3,g=0;a.ue_err&&s&&(a.ue_err.errorHandlers||(a.ue_err.errorHandlers=[]),a.ue_err.errorHandlers.push({name:"ext",handler:function(a){if(!a.logLevel||"FATAL"===a.logLevel){var f=c(!0),d=[],h;for(h in f){var f=h,g=f.match(/amazon(\.com?)?\.\w{2,3}$/i);g&&1<g.length||-1!==f.indexOf("amazon-adsystem.com")||-1!==f.indexOf("amazonpay.com")||-1!==f.indexOf("cloudfront-labs.amazonaws.com")||
d.push(h)}a.ext=d}}}));a.ue&&a.ue.isl?c():a.ue&&ue.attach&&ue.attach("load",q)})(document,window);





var ue_wtc_c = 3;
ue_csm.ue.exec(function(b,e){function l(){for(var a=0;a<f.length;a++)a:for(var d=s.replace(A,f[a])+g[f[a]]+t,c=arguments,b=0;b<c.length;b++)try{c[b].send(d);break a}catch(e){}g={};f=[];n=0;k=p}function u(){B?l(q):l(C,q)}function v(a,m,c){r++;if(r>w)d.count&&1==r-w&&(d.count("WeblabTriggerThresholdReached",1),b.ue_int&&console.error("Number of max call reached. Data will no longer be send"));else{var h=c||{};h&&-1<h.constructor.toString().indexOf(D)&&a&&-1<a.constructor.toString().indexOf(x)&&m&&-1<
m.constructor.toString().indexOf(x)?(h=b.ue_id,c&&c.rid&&(h=c.rid),c=h,a=encodeURIComponent(",wl="+a+"/"+m),2E3>a.length+p?(2E3<k+a.length&&u(),void 0===g[c]&&(g[c]="",f.push(c)),g[c]+=a,k+=a.length,n||(n=e.setTimeout(u,E))):b.ue_int&&console.error("Invalid API call. The input provided is over 2000 chars.")):d.count&&(d.count("WeblabTriggerImproperAPICall",1),b.ue_int&&console.error("Invalid API call. The input provided does not match the API protocol i.e ue.trigger(String, String, Object)."))}}function F(){d.trigger&&
d.trigger.isStub&&d.trigger.replay(function(a){v.apply(this,a)})}function y(){z||(f.length&&l(q),z=!0)}var t=":1234",s="//"+b.ue_furl+"/1/remote-weblab-triggers/1/OE/"+b.ue_mid+":"+b.ue_sid+":PLCHLDR_RID$s:wl-client-id%3DCSMTriger",A="PLCHLDR_RID",E=b.wtt||1E4,p=s.length+t.length,w=b.mwtc||2E3,G=1===e.ue_wtc_c,B=3===e.ue_wtc_c,H=e.XMLHttpRequest&&"withCredentials"in new e.XMLHttpRequest,x="String",D="Object",d=b.ue,g={},f=[],k=p,n,z=!1,r=0,C=function(){return{send:function(a){if(H){var b=new e.XMLHttpRequest;
b.open("GET",a,!0);G&&(b.withCredentials=!0);b.send()}else throw"";}}}(),q=function(){return{send:function(a){(new Image).src=a}}}();e.encodeURIComponent&&(d.attach&&(d.attach("beforeunload",y),d.attach("pagehide",y)),F(),d.trigger=v)},"client-wbl-trg")(ue_csm,window);


(function(k,d,h){function f(a,c,b){a&&a.indexOf&&0===a.indexOf("http")&&0!==a.indexOf("https")&&l(s,c,a,b)}function g(a,c,b){a&&a.indexOf&&(location.href.split("#")[0]!=a&&null!==a&&"undefined"!==typeof a||l(t,c,a,b))}function l(a,c,b,e){m[b]||(e=u&&e?n(e):"N/A",d.ueLogError&&d.ueLogError({message:a+c+" : "+b,logLevel:v,stack:"N/A"},{attribution:e}),m[b]=1,p++)}function e(a,c){if(a&&c)for(var b=0;b<a.length;b++)try{c(a[b])}catch(d){}}function q(){return d.performance&&d.performance.getEntriesByType?
d.performance.getEntriesByType("resource"):[]}function n(a){if(a.id)return"//*[@id='"+a.id+"']";var c;c=1;var b;for(b=a.previousSibling;b;b=b.previousSibling)b.nodeName==a.nodeName&&(c+=1);b=a.nodeName;1!=c&&(b+="["+c+"]");a.parentNode&&(b=n(a.parentNode)+"/"+b);return b}function w(){var a=h.images;a&&a.length&&e(a,function(a){var b=a.getAttribute("src");f(b,"img",a);g(b,"img",a)})}function x(){var a=h.scripts;a&&a.length&&e(a,function(a){var b=a.getAttribute("src");f(b,"script",a);g(b,"script",a)})}
function y(){var a=h.styleSheets;a&&a.length&&e(a,function(a){if(a=a.ownerNode){var b=a.getAttribute("href");f(b,"style",a);g(b,"style",a)}})}function z(){if(A){var a=q();e(a,function(a){f(a.name,a.initiatorType)})}}function B(){e(q(),function(a){g(a.name,a.initiatorType)})}function r(){var a;a=d.location&&d.location.protocol?d.location.protocol:void 0;"https:"==a&&(z(),w(),x(),y(),B(),p<C&&setTimeout(r,D))}var s="[CSM] Insecure content detected ",t="[CSM] Ajax request to same page detected ",v="WARN",
m={},p=0,D=k.ue_nsip||1E3,C=5,A=1==k.ue_urt,u=!0;ue_csm.ue_disableNonSecure||(d.performance&&d.performance.setResourceTimingBufferSize&&d.performance.setResourceTimingBufferSize(300),r())})(ue_csm,window,document);


var ue_aa_a = "";
if (ue.trigger && (ue_aa_a === "C" || ue_aa_a === "T1")) {
    ue.trigger("UEDATA_AA_SERVERSIDE_ASSIGNMENT_CLIENTSIDE_TRIGGER_190249", ue_aa_a);
}
(function(f,b){function g(){try{b.PerformanceObserver&&"function"===typeof b.PerformanceObserver&&(a=new b.PerformanceObserver(function(b){c(b.getEntries())}),a.observe(d))}catch(h){k()}}function m(){for(var h=d.entryTypes,a=0;a<h.length;a++)c(b.performance.getEntriesByType(h[a]))}function c(a){if(a&&Array.isArray(a)){for(var c=0,e=0;e<a.length;e++){var d=l.indexOf(a[e].name);if(-1!==d){var g=Math.round(b.performance.timing.navigationStart+a[e].startTime);f.uet(n[d],void 0,void 0,g);c++}}l.length===
c&&k()}}function k(){a&&a.disconnect&&"function"===typeof a.disconnect&&a.disconnect()}if("function"===typeof f.uet&&b.performance&&"object"===typeof b.performance&&b.performance.getEntriesByType&&"function"===typeof b.performance.getEntriesByType&&b.performance.timing&&"object"===typeof b.performance.timing&&"number"===typeof b.performance.timing.navigationStart){var d={entryTypes:["paint"]},l=["first-paint","first-contentful-paint"],n=["fp","fcp"],a;try{m(),g()}catch(p){f.ueLogError(p,{logLevel:"ERROR",
attribution:"performanceMetrics"})}}})(ue_csm,window);


if (window.csa) {
    csa("Events")("setEntity", {
        page:{pageType: "CustomerReviews", subPageType: "remoteProduct", pageTypeId: "B08L5VRVTD"}
    });
}
csa.plugin(function(c){var m="transitionStart",n="pageVisible",e="PageTiming",t="visibilitychange",s="$latency.visible",i=c.global,r=(i.performance||{}).timing,a=["navigationStart","unloadEventStart","unloadEventEnd","redirectStart","redirectEnd","fetchStart","domainLookupStart","domainLookupEnd","connectStart","connectEnd","secureConnectionStart","requestStart","responseStart","responseEnd","domLoading","domInteractive","domContentLoadedEventStart","domContentLoadedEventEnd","domComplete","loadEventStart","loadEventEnd"],o=i.Math,u=o.max,l=o.floor,d=i.document||{},g=(r||{}).navigationStart,f=g,v=0,p=null;if(i.Object.keys&&[].forEach&&!c.config["KillSwitch."+e]){if(!r||null===g||g<=0||void 0===g)return c.error("Invalid navigation timing data: "+g);p=new S({schemaId:"<ns>.PageLatency.5",producerId:"csa"}),"boolean"!=typeof d.hidden&&"string"!=typeof d.visibilityState||!d.removeEventListener?c.emit(s):h()?(c.emit(s),E(n,g)):c.on(d,t,function e(){h()&&(f=c.time(),d.removeEventListener(t,e),E(m,f),E(n,f),c.emit(s))}),c.once("$unload",I),c.once("$load",I),c.on("$pageTransition",function(){f=c.time()}),c.register(e,{mark:E,instance:function(e){return new S(e)}})}function S(e){var i,r=null,a=e.ent||{page:["pageType","subPageType","requestId"]},o=e.logger||c("Events",{producerId:e.producerId});if(!e||!e.producerId||!e.schemaId)return c.error("The producer id and schema Id must be defined for PageLatencyInstance.");function d(){return i||f}function n(){r=c.UUID()}this.mark=function(n,t){if(null!=n)return t=t||c.time(),n===m&&(i=t),c.once(s,function(){o("log",{messageId:r,__merge:function(e){e.markers[n]=function(e,n){return u(0,n-(e||f))}(d(),t),e.markerTimestamps[n]=l(t)},markers:{},markerTimestamps:{},navigationStartTimestamp:d()?new Date(d()).toISOString():null,schemaId:e.schemaId},{ent:a})}),t},n(),c.on("$beforePageTransition",n)}function E(e,n){e===m&&(f=n);var t=p.mark(e,n);c.emit("$timing:"+e,t)}function I(){if(!v){for(var e=0;e<a.length;e++)r[a[e]]&&E(a[e],r[a[e]]);v=1}}function h(){return!d.hidden||"visible"===d.visibilityState}});csa.plugin(function(f){var u,c,l="length",a="parentElement",t="target",i="getEntriesByName",e="perf",n=null,r="_csa_flt",o="_csa_llt",s="previousSibling",d="_osrc",g="_elt",h="_eid",m=10,p=5,v=15,y=100,E=f.global,S=f.timeout,b=E.Math,x=b.max,L=b.floor,O=b.ceil,_=E.document,w=E.performance||{},T=(w.timing||{}).navigationStart,I=Date.now,N=Object.values||(f.types||{}).ovl,k=f("PageTiming"),B=f("SpeedIndexBuffers"),Y=[],C=[],F=[],H=[],M=[],R=[],V=.1,W=.1,$=0,P=0,X=!0,D=0,J=0,j=1==f.config["SpeedIndex.ForceReplay"],q=0,Q=1,U=0,z={},A=[],G=0,K={buffered:1};function Z(e){f.global.ue_csa_ss_tag||f.emit("$csmTag:"+e,0,K)}function ee(){for(var e=I(),n=0;u;){if(0!==u[l]){if(!1!==u.h(u[0])&&u.shift(),n++,!j&&n%m==0&&I()-e>p)break}else u=u.n}$=0,u&&($||(!0===_.hidden?(j=1,ee()):f.timeout(ee,0)))}function ne(e,n,t,i,r){U=L(e),Y=n,C=t,F=i,R=r;var o=_.createTreeWalker(_.body,NodeFilter.SHOW_TEXT,null,null),a={w:E.innerWidth,h:E.innerHeight,x:E.pageXOffset,y:E.pageYOffset};_.body[g]=e,H.push({w:o,vp:a}),M.push({img:_.images,iter:0}),Y.h=te,(Y.n=C).h=ie,(C.n=F).h=re,(F.n=H).h=oe,(H.n=M).h=ae,(M.n=R).h=fe,u=Y,ee()}function te(e){e.m.forEach(function(e){for(var n=e;n&&(e===n||!n[r]||!n[o]);)n[r]||(n[r]=e[r]),n[o]||(n[o]=e[o]),n[g]=n[r]-T,n=n[s]})}function ie(e){e.m.forEach(function(e){var n=e[t];d in n||(n[d]=e.oldValue)})}function re(n){n.m.forEach(function(e){e[t][g]=n.t-T})}function oe(e){for(var n,t=e.vp,i=e.w,r=m;(n=i.nextNode())&&0<r;){r-=1;var o=(n[a]||{}).nodeName;"SCRIPT"!==o&&"STYLE"!==o&&"NOSCRIPT"!==o&&"BODY"!==o&&0!==(n.nodeValue||"").trim()[l]&&de(n[a],ue(n),t)}return!n}function ae(e){for(var n={w:E.innerWidth,h:E.innerHeight,x:E.pageXOffset,y:E.pageYOffset},t=m;e.iter<e.img[l]&&0<t;){var i,r=e.img[e.iter],o=se(r),a=o&&ue(o)||ue(r);o?(o[g]=a,i=le(o.querySelector('[aria-posinset="1"] img')||r)||a,r=o):i=le(r)||a,J&&c<i&&(i=a),de(r,i,n),e.iter+=1,t-=1}return e.img[l]<=e.iter}function fe(e){var n=[],i=0,r=0,o=P,t=L(e.y/y),a=O((e.y+E.innerHeight)/y);A.slice(t,a).forEach(function(e){(e.elems||[]).forEach(function(e){e.lt in n||(n[e.lt]={}),e.id in n[e.lt]||(i+=(n[e.lt][e.id]=e).a)})}),Z("startVL"),N(n).forEach(function(e){N(e).forEach(function(e){var n=1-r/i,t=x(e.lt,o);G+=n*(t-o),o=t,function(e,n){var t;for(;V<=1&&V-.01<=e;)ge("visuallyLoaded"+(t=(100*V).toFixed(0)),n.lt),"50"!==t&&"90"!==t||f("Content",{target:n.e})("mark","visuallyLoaded"+t,T+O(n.lt||0)),V+=W}((r+=e.a)/i,e)})}),Z("endVL"),P=e.t-T,R[l]<=1&&(ge("speedIndex",G),ge("visuallyLoaded0",U)),X&&(X=!1,ge("atfSpeedIndex",G))}function ue(e){for(var n=e[a],t=v;n&&0<t;){if(n[g]||0===n[g])return x(n[g],U);n=n.parentElement,t-=1}}function ce(e,n){if(e){if(!e.indexOf("data:"))return ue(n);var t=w[i](e)||[];if(0<t[l])return x(O(t[0].responseEnd||0),U)}}function le(e){return ce(e[d],e)||ce(e.currentSrc,e)||ce(e.src,e)}function se(e){for(var n=10,t=e.parentElement;t&&0<n;){if(t.classList&&t.classList.contains("a-carousel-viewport"))return t;t=t.parentElement,n-=1}return null}function de(e,n,t){if((n||0===n)&&!e[h]){var i=e.getBoundingClientRect(),r=i.width*i.height,o=i.width/2,a=Q++;if(0!=r&&!(o<i.right-t.w||i.right<o)){for(var f={e:e,lt:n,a:r,id:a},u=L((i.top+t.y)/y),c=O((i.top+t.y+i.height)/y),l=u;l<=c;l++)l in A||(A[l]={elems:[],lt:0}),A[l].elems.push(f);e[h]=a}}}function ge(e,n){k("mark",e,T+O((z[e]=n)||0))}function he(e){q||(Z("browserQuite"+e),B("getBuffers",ne),q=1)}T&&N&&w[i]?(Z(e+"Yes"),B("registerListener",function(){J&&(clearTimeout(D),D=S(he.bind(n,"Mut"),2500))}),f.once("$unload",function(){j=1,he("Ud")}),f.once("$load",function(){J=1,c=I()-T,D=S(he.bind(n,"Ld"),2500)}),f.once("$timing:functional",he.bind(n,"Fn")),B("replayModuleIsLive"),f.register("SpeedIndex",{getMarkers:function(e){e&&e(JSON.parse(JSON.stringify(z)))}})):Z(e+"No")});csa.plugin(function(e){var m=!!e.config["LCP.elementDedup"],t=!1,n=e("PageTiming"),r=e.global.PerformanceObserver,a=e.global.performance;function i(){return a.timing.navigationStart}function o(){t||function(o){var l=new r(function(e){var t=e.getEntries();if(0!==t.length){var n=t[t.length-1];if(m&&""!==n.id&&n.element&&"IMG"===n.element.tagName){for(var r={},a=t[0],i=0;i<t.length;i++)t[i].id in r||(""!==t[i].id&&(r[t[i].id]=!0),a.startTime<t[i].startTime&&(a=t[i]));n=a}l.disconnect(),o({startTime:n.startTime,renderTime:n.renderTime,loadTime:n.loadTime})}});try{l.observe({type:"largest-contentful-paint",buffered:!0})}catch(e){}}(function(e){e&&(t=!0,n("mark","largestContentfulPaint",Math.floor(e.startTime+i())),e.renderTime&&n("mark","largestContentfulPaint.render",Math.floor(e.renderTime+i())),e.loadTime&&n("mark","largestContentfulPaint.load",Math.floor(e.loadTime+i())))})}r&&a&&a.timing&&(e.once("$unload",o),e.once("$load",o),e.register("LargestContentfulPaint",{}))});csa.plugin(function(r){var e=r("Metrics",{producerId:"csa"}),n=r.global.PerformanceObserver;n&&(n=new n(function(r){var t=r.getEntries();if(0===t.length||!t[0].processingStart||!t[0].startTime)return;!function(r){r=r||0,n.disconnect(),0<=r?e("recordMetric","firstInputDelay",r):e("recordMetric","firstInputDelay.invalid",1)}(t[0].processingStart-t[0].startTime)}),function(){try{n.observe({type:"first-input",buffered:!0})}catch(r){}}())});csa.plugin(function(d){var e="Metrics",g=0;function r(i){var c,t,e=i.producerId,r=i.logger,s=r||d("Events",{producerId:e}),o=(i||{}).dimensions||{},u={},n=-1;if(!e&&!r)return d.error("Either a producer id or custom logger must be defined");function a(){n!==g&&(c=d.UUID(),t=d.UUID(),u={},n=g)}this.recordMetric=function(r,n){var e=i.logOptions||{ent:{page:["pageType","subPageType","requestId"]}};e.debugMetric=i.debugMetric,a(),s("log",{messageId:c,schemaId:i.schemaId||"<ns>.Metric.3",metrics:{},dimensions:o,__merge:function(e){e.metrics[r]=n}},e)},this.recordCounter=function(r,e){var n=i.logOptions||{ent:{page:["pageType","subPageType","requestId"]}};if("string"!=typeof r||"number"!=typeof e||!isFinite(e))return d.error("Invalid type given for counter name or counter value: "+r+"/"+e);a(),r in u||(u[r]={});var c=u[r];"f"in c||(c.f=e),c.c=(c.c||0)+1,c.s=(c.s||0)+e,c.l=e,s("log",{messageId:t,schemaId:i.schemaId||"<ns>.InternalCounters.2",c:{},__merge:function(e){r in e.c||(e.c[r]={}),c.fs||(c.fs=1,e.c[r].f=c.f),1<c.c&&(e.c[r].s=c.s,e.c[r].l=c.l,e.c[r].c=c.c)}},n)}}d.config["KillSwitch."+e]||(new r({producerId:"csa"}).recordMetric("baselineMetricEvent",1),d.on("$beforePageTransition",function(){g++}),d.register(e,{instance:function(e){return new r(e||{})}}))});csa.plugin(function(t){var a,r=(t.global.performance||{}).timing,s=(r||{}).navigationStart||t.time();function e(){a=t.UUID()}function n(i){var r=(i=i||{}).producerId,e=i.logger,o=e||t("Events",{producerId:r});if(!r&&!e)return t.error("Either a producer id or custom logger must be defined");this.mark=function(e,r){var n=(void 0===r?t.time():r)-s;o("log",{messageId:a,schemaId:i.schemaId||"<ns>.Timer.1",markers:{},__merge:function(r){r.markers[e]=n}},i.logOptions)}}r&&(e(),t.on("$beforePageTransition",e),t.register("Timers",{instance:function(r){return new n(r||{})}}))});csa.plugin(function(t){var e="takeRecords",i="disconnect",n="function",o=t("Metrics",{producerId:"csa"}),c=t("PageTiming"),a=t.global,u=t.timeout,r=t.on,f=a.PerformanceObserver,m=0,l=!1,s=0,d=a.performance,h=a.document,v=null,y=!1,g=t.blank;function p(){l||(l=!0,clearTimeout(v),typeof f[e]===n&&f[e](),typeof f[i]===n&&f[i](),o("recordMetric","documentCumulativeLayoutShift",m),c("mark","cumulativeLayoutShiftLastTimestamp",Math.floor(s+d.timing.navigationStart)))}f&&d&&d.timing&&h&&(f=new f(function(t){v&&clearTimeout(v);t.getEntries().forEach(function(t){t.hadRecentInput||(m+=t.value,s<t.startTime&&(s=t.startTime))}),v=u(p,5e3)}),function(){try{f.observe({type:"layout-shift",buffered:!0}),v=u(p,5e3)}catch(t){}}(),g=r(h,"click",function(t){y||(y=!0,o("recordMetric","documentCumulativeLayoutShiftToFirstInput",m),g())}),r(h,"visibilitychange",function(){"hidden"===h.visibilityState&&p()}),t.once("$unload",p))});csa.plugin(function(e){var t,n=e.global,r=n.PerformanceObserver,c=e("Metrics",{producerId:"csa"}),o=0,i=0,a=-1,l=n.Math,f=l.max,u=l.ceil;if(r){t=new r(function(e){e.getEntries().forEach(function(e){var t=e.duration;o+=t,i+=t,a=f(t,a)})});try{t.observe({type:"longtask",buffered:!0})}catch(e){}t=new r(function(e){0<e.getEntries().length&&(i=0,a=-1)});try{t.observe({type:"largest-contentful-paint",buffered:!0})}catch(e){}e.on("$unload",g),e.on("$beforePageTransition",g)}function g(){c("recordMetric","totalBlockingTime",u(i||0)),c("recordMetric","totalBlockingTimeInclLCP",u(o||0)),c("recordMetric","maxBlockingTime",u(a||0)),i=o=0,a=-1}});csa.plugin(function(r){var e="CacheDetection",o="csa-ctoken-",n=r.store,t=r.deleteStored,c=r.config,a=c[e+".RequestID"],i=c[e+".Callback"],s=r.global,u=s.document||{},d=s.Date,f=r("Events"),l=r("Events",{producerId:"csa"});function p(e){try{var n=u.cookie.match(RegExp("(^| )"+e+"=([^;]+)"));return n&&n[2].trim()}catch(e){}}!function(){var e=function(){var e=p("cdn-rid");if(e)return{r:e,s:"cdn"}}()||function(){if(r.store(o+a))return{r:r.UUID().toUpperCase().replace(/-/g,"").slice(0,20),s:"device"}}()||{},n=e.r,c=e.s;if(!!n){var t=p("session-id");!function(e,n,c,t){f("setEntity",{page:{pageSource:"cache",requestId:e,cacheRequestId:a,cacheSource:t},session:{id:c}})}(n,0,t,c),"device"===c&&l("log",{schemaId:"<ns>.CacheImpression.1"},{ent:"all"}),i&&i(n,t,c)}}(),n(o+a,d.now()+36e5),r.once("$load",function(){var c=d.now();t(function(e,n){return 0==e.indexOf(o)&&parseInt(n)<c})})});csa.plugin(function(u){var i,t="Content",e="MutationObserver",n="addedNodes",a="querySelectorAll",f="matches",o="getAttributeNames",r="getAttribute",s="dataset",c="widget",l="producerId",d="slotId",h="iSlotId",g={ent:{element:1,page:["pageType","subPageType","requestId"]}},p=5,m=u.config[t+".BubbleUp.SearchDepth"]||35,y=u.config[t+".SearchPage"]||0,v="csaC",b=v+"Id",E="logRender",w={},I=u.config,O=I[t+".Selectors"]||[],C=I[t+".WhitelistedAttributes"]||{href:1,class:1},N=I[t+".EnableContentEntities"],S=I["KillSwitch.ContentRendered"],k=u.global,A=k.document||{},U=A.documentElement,L=k.HTMLElement,R={},_=[],j=function(t,e,n,i){var r=this,o=u("Events",{producerId:t||"csa"});e.type=e.type||c,r.id=e.id,r.l=o,r.e=e,r.el=n,r.rt=i,r.dlo=g,r.op=W(n,"csaOp"),r.log=function(t,e){o("log",t,e||g)},e.id&&o("setEntity",{element:e})},x=j.prototype;function D(t){var e=(t=t||{}).element,n=t.target;return e?function(t,e){var n;n=t instanceof L?K(t)||Y(e[l],t,z,u.time()):R[t.id]||H(e[l],0,t,u.time());return n}(e,t):n?M(n):u.error("No element or target argument provided.")}function M(t){var e=function(t){var e=null,n=0;for(;t&&n<m;){if(n++,P(t,b)){e=t;break}t=t.parentElement}return e}(t);return e?K(e):new j("csa",{id:null},null,u.time())}function P(t,e){if(t&&t.dataset)return t.dataset[e]}function T(t,e,n){_.push({n:n,e:t,t:e}),B()}function q(){for(var t=u.time(),e=0;0<_.length;){var n=_.shift();if(w[n.n](n.e,n.t),++e%10==0&&u.time()-t>p)break}i=0,_.length&&B()}function B(){i=i||u.raf(q)}function X(t,e,n){return{n:t,e:e,t:n}}function Y(t,e,n,i){var r=u.UUID(),o={id:r},c=M(e);return e[s][b]=r,n(o,e),c&&c.id&&(o.parentId=c.id),H(t,e,o,i)}function $(t){return isNaN(t)?null:Math.round(t)}function H(t,e,n,i){N&&(n.schemaId="<ns>.ContentEntity.2"),n.id=n.id||u.UUID();var r=new j(t,n,e,i);return function(t){return!S&&((t.op||{}).hasOwnProperty(E)||y)}(r)&&function(t,e){var n={},i=u.exec($);t.el&&(n=t.el.getBoundingClientRect()),t.log({schemaId:"<ns>.ContentRender.2",timestamp:e,width:i(n.width),height:i(n.height),positionX:i(n.left+k.pageXOffset),positionY:i(n.top+k.pageYOffset)})}(r,i),u.emit("$content.register",r),R[n.id]=r}function K(t){return R[(t[s]||{})[b]]}function W(n,i){var r={};return o in(n=n||{})&&Object.keys(n[s]).forEach(function(t){if(!t.indexOf(i)&&i.length<t.length){var e=function(t){return(t[0]||"").toLowerCase()+t.slice(1)}(t.slice(i.length));r[e]=n[s][t]}}),r}function z(t,e){o in e&&(function(t,e){var n=W(t,v);Object.keys(n).forEach(function(t){e[t]=n[t]})}(e,t),d in t&&(t[h]=t[d]),function(e,n){(e[o]()||[]).forEach(function(t){t in C&&(n[t]=e[r](t))})}(e,t))}U&&A[a]&&k[e]&&(O.push({selector:"*[data-csa-c-type]",entity:z}),O.push({selector:".celwidget",entity:function(t,e){z(t,e),t[d]=t[d]||e[r]("cel_widget_id")||e.id,t.legacyId=e[r]("cel_widget_id")||e.id,t.type=t.type||c}}),w[1]=function(t,e){t.forEach(function(t){t[n]&&t[n].constructor&&"NodeList"===t[n].constructor.name&&Array.prototype.forEach.call(t[n],function(t){_.unshift(X(2,t,e))})})},w[2]=function(o,c){a in o&&f in o&&O.forEach(function(t){for(var e=t.selector,n=o[f](e),i=o[a](e),r=i.length-1;0<=r;r--)_.unshift(X(3,{e:i[r],s:t},c));n&&_.unshift(X(3,{e:o,s:t},c))})},w[3]=function(t,e){var n=t.e;K(n)||Y("csa",n,t.s.entity,e)},w[4]=function(){u.register(t,{instance:D})},new k[e](function(t){T(t,u.time(),1)}).observe(U,{childList:!0,subtree:!0}),T(U,u.time(),2),T(null,u.time(),4),u.on("$content.export",function(e){Object.keys(e).forEach(function(t){x[t]=e[t]})}))});csa.plugin(function(o){var i,t="ContentImpressions",e="KillSwitch.",n="IntersectionObserver",r="getAttribute",s="dataset",c="intersectionRatio",a="csaCId",m=1e3,l=o.global,f=o.config,u=f[e+t],v=f[e+t+".ContentViews"],g=((l.performance||{}).timing||{}).navigationStart||o.time(),d={};function h(t){t&&(t.v=1,function(t){t.vt=o.time(),t.el.log({schemaId:"<ns>.ContentView.3",timeToViewed:t.vt-t.el.rt,pageFirstPaintToElementViewed:t.vt-g})}(t))}function I(t){t&&!t.it&&(t.i=o.time()-t.is>m,function(t){t.it=o.time(),t.el.log({schemaId:"<ns>.ContentImpressed.2",timeToImpressed:t.it-t.el.rt,pageFirstPaintToElementImpressed:t.it-g})}(t))}!u&&l[n]&&(i=new l[n](function(t){var n=o.time();t.forEach(function(t){var e=function(t){if(t&&t[r])return d[t[s][a]]}(t.target);if(e){o.emit("$content.intersection",{meta:e.el,t:n,e:t});var i=t.intersectionRect;t.isIntersecting&&0<i.width&&0<i.height&&(v||e.v||h(e),.5<=t[c]&&!e.is&&(e.is=n,e.timer=o.timeout(function(){I(e)},m))),t[c]<.5&&!e.it&&e.timer&&(l.clearTimeout(e.timer),e.is=0,e.timer=0)}})},{threshold:[0,.5,.99]}),o.on("$content.register",function(t){var e=t.el;e&&(d[t.id]={el:t,v:0,i:0,is:0,vt:0,it:0},i.observe(e))}))});csa.plugin(function(e){e.config["KillSwitch.ContentLatency"]||e.emit("$content.export",{mark:function(t,n){var o=this;o.t||(o.t=e("Timers",{logger:o.l,schemaId:"<ns>.ContentLatency.1",logOptions:o.dlo})),o.t("mark",t,n)}})});csa.plugin(function(t){function n(i,e,o){var c={};function r(t,n,e){t in c&&o<=n-c[t].s&&(function(n,e,i){if(!p)return;S(function(t){T(n,t),t.w[n][e]=a((t.w[n][e]||0)+i)})}(t,i,n-c[t].d),c[t].d=n),e||delete c[t]}this.update=function(t,n){n.isIntersecting&&e<=n.intersectionRatio?function(t,n){t in c||(c[t]={s:n,d:n})}(t,u()):r(t,u())},this.stopAll=function(t){var n=u();for(var e in c)r(e,n,t)},this.reset=function(){var t=u();for(var n in c)c[n].s=t,c[n].d=t}}var e=t.config,u=t.time,i="ContentInteractionsSummary",o=e[i+".FlushInterval"]||5e3,c=e[i+".FlushBackoff"]||1.5,r=t.global,s=t.on,a=Math.floor,f=(r.document||{}).documentElement||{},l=((r.performance||{}).timing||{}).responseStart||t.time(),d=o,m=0,p=!0,v=t.UUID(),g=t("Events",{producerId:"csa"}),I=new n("it0",0,0),w=new n("it50",.5,1e3),h=new n("it100",.99,0),A={},b={};function $(){I.stopAll(!0),w.stopAll(!0),h.stopAll(!0),U()}function C(){I.reset(),w.reset(),h.reset(),U()}function U(){d&&(clearTimeout(m),m=t.timeout($,d),d*=c)}function E(n){S(function(t){T(n,t),t.w[n].mc=(t.w[n].mc||0)+1})}function S(t){g("log",{messageId:v,schemaId:"<ns>.ContentInteractionsSummary.1",w:{},__merge:t},{ent:{page:["requestId"]}})}function T(t,n){t in n.w||(n.w[t]={})}s("$content.intersection",function(t){if(t&&t.meta&&t.e){var n=t.meta.id;if(n in A){var e=t.e.boundingClientRect||{};e.width<5||e.height<5||(I.update(n,t.e),w.update(n,t.e),h.update(n,t.e),!t.e.isIntersecting||n in b||(b[n]=1,function(n,e){S(function(t){T(n,t),t.w[n].ttfv=a(e)})}(n,u()-l)))}}}),s("$content.register",function(t){(t.e||{}).slotId&&(A[t.id]={},function(e){S(function(t){var n=e.id;T(n,t),t.w[n].sid=(e.e||{}).slotId,t.w[n].cid=(e.e||{}).contentId})}(t))}),s("$beforePageTransition",function(){$(),C(),v=t.UUID(),U()}),s("$beforeunload",function(){I.stopAll(),w.stopAll(),h.stopAll(),d=null}),s("$visible",function(t){t?C():($(),clearTimeout(m)),p=t},{buffered:1}),s(f,"click",function(t){for(var n=t.target,e=25;n&&0<e;){var i=(n.dataset||{}).csaCId;i&&E(i),n=n.parentElement,e-=1}},{capture:!0,passive:!0}),U()});csa.plugin(function(o){var t,n,i="normal",s="reload",e="history",d="new-tab",a="ajax",r=1,c=2,u="lastActive",l="lastInteraction",f="used",p="csa-tabbed-browsing",g="visibilityState",v={"back-memory-cache":1,"tab-switch":1,"history-navigation-page-cache":1},b="<ns>.TabbedBrowsing.2",m="visible",y=o.global,I=o("Events",{producerId:"csa"}),h=y.location||{},T=y.document,w=y.JSON,z=((y.performance||{}).navigation||{}).type,P=o.store,S=o.on,k=o.storageSupport(),x=!1,A={},C={},O={},$={},j=!1,q=!1,B=!1;function E(i){try{return w.parse(P(p,void 0,{session:i})||"{}")||{}}catch(i){o.error('Could not parse storage value for key "'+p+'": '+i)}return{}}function J(i,t){P(p,w.stringify(t||{}),{session:i})}function N(i){var t=C.tid||i.id,n=A[u]||{};n.tid===t&&(n.pid=i.id),$={pid:i.id,tid:t,lastInteraction:C[l]||{},initialized:!0},O={lastActive:n,lastInteraction:A[l]||{},time:o.time()}}function D(i){var t=i===d,n=T.referrer,e=!(n&&n.length)||!~n.indexOf(h.origin||""),a=t&&e,r={type:i,toTabId:$.tid,toPageId:$.pid,transitTime:o.time()-A.time||null};a||function(i,t,n){var e=i===s,a=t?A[u]||{}:C,r=A[l]||{},o=C[l]||{},d=t?r:o;n.fromTabId=a.tid,n.fromPageId=a.pid,e||!d.id||d[f]||(n.interactionId=d.id||null,r.id===d.id&&(r[f]=!0),o.id===d.id&&(o[f]=!0))}(i,t,r),I("log",{navigation:r,schemaId:b},{ent:{page:["pageType","subPageType","requestId"]}})}function F(i){B=function(i){return i&&i in v}(i.transitionType),function(){A=E(!1),C=E(!0);var i=A[l],t=C[l],n=!1,e=!1;i&&t&&i.id===t.id&&i[f]!==t[f]&&(n=!i[f],e=!t[f],t[f]=i[f]=!0,n&&J(!1,A),e&&J(!0,C))}(),N(i),j=!0,function(i){var t,n;t=H(),n=K(),(t||n)&&N(i)}(i)}function G(){x&&!B?D(a):(x=!0,D(z===c||B?e:z===r?C.initialized?s:d:C.initialized?i:d))}function H(){return!(!j||!t)&&(C[l]={id:t.messageId,used:!(A[l]={id:t.messageId,used:!1})},!(t=null))}function K(){var i=!1;if(q=T[g]===m,j){var t=A[u]||{};i=function(i,t,n){var e=!1,a=i[u];return q?a&&a.tid===$.tid&&a[m]&&a.pid===n||(i[u]={visible:!0,pid:n,tid:t},e=!0):a&&a.tid===$.tid&&a[m]&&(e=!(a[m]=!1)),e}(A,C.tid||t.tid||$.tid,C.pid||t.pid||$.pid)}return i}k.local&&k.session&&w&&T&&g in T&&(n=function(){try{return y.self!==y.top}catch(i){return!0}}(),S("$pageChange",function(i){n||(F(i),G(),J(!1,O),J(!0,$),C=$,A=O)},{buffered:1}),S("$content.interaction",function(i){t=i,H()&&(J(!1,A),J(!0,C))}),S(T,"visibilitychange",function(){!n&&K()&&J(!1,A)},{capture:!1,passive:!0}))});csa.plugin(function(c){var e=c("Metrics",{producerId:"csa"});c.on(c.global,"pageshow",function(c){c&&c.persisted&&e("recordMetric","bfCache",1)})});csa.plugin(function(n){var e,t,i,o,r,a,c,u,f,s,l,d,m,p,g,v,h="hasFocus",b="$app.",y="avail",S="client",T="document",$="inner",I="offset",P="screen",w="scroll",D="Width",E="Height",F=y+D,O=y+E,q=S+D,x=S+E,z=$+D,C=$+E,H=I+D,K=I+E,M=w+D,W=w+E,X=n.config["KillSwitch.PageInteractionsSummary"],Y=n("Events",{producerId:"csa"}),j=1,k=n.global||{},A=n.time,B=n.on,G=n.once,J=k[T]||{},L=k[P]||{},N=k.Math||{},Q=N.abs,R=N.max,U=N.ceil,V=((k.performance||{}).timing||{}).responseStart,Z=function(){return J[h]()},_=1,nn=100,en={},tn=1;function on(){c=t=o=r=e,i=0,a=u=f=s=0,cn(),an()}function rn(){V&&!o&&(c=U((o=l)-V),tn=1)}function an(){u=U(R(u,m+v)),d&&(f=U(R(f,d+g))),tn=1}function cn(){l=A(),d=Q(k.pageXOffset||0),m=Q(k.pageYOffset||0),p=0<d||0<m,g=k[z]||0,v=k[C]||0}function un(){cn(),rn(),function(){var n=m-i;t&&!(t&&t<=l)||(n&&(++a,tn=1),i=m,n),t=l+nn}(),an()}function fn(){if(r){var n=U(A()-r);s+=n,r=e,tn=0<n}}function sn(){r=r||A()}function ln(n,e,t,i){e[n+D]=U(t||0),e[n+E]=U(i||0)}function dn(n){var e=n===en,t=Z();if(t||tn){if(!e){if(!j)return;j=0,t&&fn()}var i=function(){var n={},e=J.documentElement||{},t=J.body||{};return ln("availableScreen",n,L[F],L[O]),ln(T,n,R(t[M]||0,t[H]||0,e[q]||0,e[M]||0,e[H]||0),R(t[W]||0,t[K]||0,e[x]||0,e[W]||0,e[K]||0)),ln(P,n,L.width,L.height),ln("viewport",n,k[z],k[C]),n}(),o=function(){var n={scrollCounts:a,reachedDepth:u,horizontalScrollDistance:f,dwellTime:s};return"number"==typeof c&&(n.clientTimeToFirstScroll=c),n}();e?tn=0:(on(),V=A(),t&&(r=V)),Y("log",{activity:o,dimensions:i,schemaId:"<ns>.PageInteractionsSummary.1"},{ent:{page:["pageType","subPageType","requestId"]}})}}function mn(){fn(),dn(en)}function pn(n,e){return function(){_=e,n()}}function gn(){Z=function(){return _},_&&!r&&(r=A())}"function"!=typeof J[h]||X||(on(),p&&rn(),B(k,w,un,{passive:!0}),B(k,"blur",mn),B(k,"focus",pn(sn,1)),G(b+"android",gn),G(b+"ios",gn),B(b+"pause",pn(mn,0)),B(b+"resume",pn(sn,1)),B(b+"resign",pn(mn,0)),B(b+"active",pn(sn,1)),Z()&&(r=V||A()),G("$beforeunload",dn),B("$beforeunload",dn),B("$document.hidden",mn),B("$beforePageTransition",dn),B("$afterPageTransition",function(){tn=j=1}))});csa.plugin(function(e){var o,n,r="<ns>.Navigator.4",a=e.global,i=a.navigator||{},d=i.connection||{},c=a.Math.round,t=e("Events",{producerId:"csa"});function l(){o={network:{downlink:void 0,downlinkMax:void 0,rtt:void 0,type:void 0,effectiveType:void 0,saveData:void 0},language:void 0,doNotTrack:void 0,hardwareConcurrency:void 0,deviceMemory:void 0,cookieEnabled:void 0,webdriver:void 0},v(),o.language=i.language||null,o.doNotTrack=function(){switch(i.doNotTrack){case"1":return"enabled";case"0":return"disabled";case"unspecified":return i.doNotTrack;default:return null}}(),o.hardwareConcurrency="hardwareConcurrency"in i?c(i.hardwareConcurrency||0):null,o.deviceMemory="deviceMemory"in i?c(i.deviceMemory||0):null,o.cookieEnabled="cookieEnabled"in i?i.cookieEnabled:null,o.webdriver="webdriver"in i?i.webdriver:null}function u(){t("log",{network:(n={},Object.keys(o.network).forEach(function(e){n[e]=o.network[e]+""}),n),language:o.language,doNotTrack:o.doNotTrack,hardwareConcurrency:o.hardwareConcurrency,deviceMemory:o.deviceMemory,cookieEnabled:o.cookieEnabled,webdriver:o.webdriver,schemaId:r},{ent:{page:["pageType","subPageType","requestId"]}})}function v(){!function(n){Object.keys(o.network).forEach(function(e){o.network[e]=n[e]})}({downlink:"downlink"in d?c(d.downlink||0):null,downlinkMax:"downlinkMax"in d?c(d.downlinkMax||0):null,rtt:"rtt"in d?(d.rtt||0).toFixed():null,type:d.type||null,effectiveType:d.effectiveType||null,saveData:"saveData"in d?d.saveData:null})}function k(){v(),u()}function w(){l(),u()}l(),u(),e.on("$afterPageTransition",w),e.on(d,"change",k)});
if (window.ue && window.ue.uels) {
    ue.uels("https://c.amazon-adsystem.com/bao-csm/forensics/a9-tq-forensics.min.js");
}


ue.exec(function(d,c){function g(e,c){e&&ue.tag(e+c);return!!e}function n(){for(var e=RegExp("^https://(.*\.(images|ssl-images|media)-amazon\.com|"+c.location.hostname+")/images/","i"),d={},h=0,k=c.performance.getEntriesByType("resource"),l=!1,b,a,m,f=0;f<k.length;f++)if(a=k[f],0<a.transferSize&&a.transferSize>=a.encodedBodySize&&(b=e.exec(String(a.name)))&&3===b.length){a:{b=a.serverTiming||[];for(a=0;a<b.length;a++)if("provider"===b[a].name){b=b[a].description;break a}b=void 0}b&&(l||(l=g(b,"_cdn_fr")),
a=d[b]=(d[b]||0)+1,a>h&&(m=b,h=a))}g(m,"_cdn_mp")}d.ue&&"function"===typeof d.ue.tag&&c.performance&&c.location&&n()},"cdnTagging")(ue_csm,window);


}
/* ◬ */
</script>

</div>

<noscript>
    <img height="1" width="1" style='display:none;visibility:hidden;' src='//fls-eu.amazon.in/1/batch/1/OP/A21TJRUUN4KGV:257-4714000-6327435:RZ67A764XT8VEYCF2P53$uedata=s:%2Frd%2Fuedata%3Fnoscript%26id%3DRZ67A764XT8VEYCF2P53:0' alt=""/>
</noscript>

<script>window.ue && ue.count && ue.count('CSMLibrarySize', 63500)</script>
<!-- sp:end-feature:csm:body-close -->
</div></body></html>
<!--       _
       .__(.)< (MEOW)
        \___)   
 ~~~~~~~~~~~~~~~~~~-->
<!-- sp:eh:ZNZJENrt7lMe9XhtRrQJu/HuUo2j6kCuRn4bIQyrJEYY66UER5t2hdrjfqjb5QEQUqEnVuidcBDIl7Giq6sztCVxsBF+xjjnhwuNAA7QaeU81h6LBQJLzZMuhX4= -->


"""




#print(html)
# Parsing the HTML response using BeautifulSoup
soup = BeautifulSoup(html_red, 'html.parser')
for review in soup.find_all('div',attrs={'data-hook': 'review'}):
    print((review.find('a',attrs={'data-hook':'review-title'}).span.string))
    print((review.find('span',attrs={'data-hook':'review-body'}).span.string))
    color = review.find('a', attrs={'data-hook': 'format-strip'}).text.split('Size:')[0].strip()
    size = review.find('a', attrs={'data-hook': 'format-strip'}).text.split('Size:')[1].split('Pattern Name:')[0].strip()

    print("Size: ", size)
    print(color)
    if review.find('span',attrs={'class':'a-declarative'}) is not None:
        print("verified Purchase")
    else:
        print("Not Verified Purchase")
    print("          ")

