import{n as d,s as v}from"./scheduler.8fdumybZ.js";const u=[];function p(e,t=d){let s;const o=new Set;function r(n){if(v(e,n)&&(e=n,s)){const c=!u.length;for(const i of o)i[1](),u.push(i,e);if(c){for(let i=0;i<u.length;i+=2)u[i][0](u[i+1]);u.length=0}}}function l(n){r(n(e))}function a(n,c=d){const i=[n,c];return o.add(i),o.size===1&&(s=t(r,l)||d),n(e),()=>{o.delete(i),o.size===0&&s&&(s(),s=null)}}return{set:r,update:l,subscribe:a}}const m=globalThis.__sveltekit_smkp5f?.base??"/resume",E=globalThis.__sveltekit_smkp5f?.assets??m,A="1710364711214",I="sveltekit:snapshot",w="sveltekit:scroll",y="sveltekit:states",N="sveltekit:pageurl",U="sveltekit:history",L="sveltekit:navigation",_={tap:1,hover:2,viewport:3,eager:4,off:-1,false:-1},g=location.origin;function O(e){if(e instanceof URL)return e;let t=document.baseURI;if(!t){const s=document.getElementsByTagName("base");t=s.length?s[0].href:document.URL}return new URL(e,t)}function Y(){return{x:pageXOffset,y:pageYOffset}}function f(e,t){return e.getAttribute(`data-sveltekit-${t}`)}const b={..._,"":_.hover};function k(e){let t=e.assignedSlot??e.parentNode;return t?.nodeType===11&&(t=t.host),t}function x(e,t){for(;e&&e!==t;){if(e.nodeName.toUpperCase()==="A"&&e.hasAttribute("href"))return e;e=k(e)}}function P(e,t){let s;try{s=new URL(e instanceof SVGAElement?e.href.baseVal:e.href,document.baseURI)}catch{}const o=e instanceof SVGAElement?e.target.baseVal:e.target,r=!s||!!o||T(s,t)||(e.getAttribute("rel")||"").split(/\s+/).includes("external"),l=s?.origin===g&&e.hasAttribute("download");return{url:s,external:r,target:o,download:l}}function V(e){let t=null,s=null,o=null,r=null,l=null,a=null,n=e;for(;n&&n!==document.documentElement;)o===null&&(o=f(n,"preload-code")),r===null&&(r=f(n,"preload-data")),t===null&&(t=f(n,"keepfocus")),s===null&&(s=f(n,"noscroll")),l===null&&(l=f(n,"reload")),a===null&&(a=f(n,"replacestate")),n=k(n);function c(i){switch(i){case"":case"true":return!0;case"off":case"false":return!1;default:return}}return{preload_code:b[o??"off"],preload_data:b[r??"off"],keepfocus:c(t),noscroll:c(s),reload:c(l),replace_state:c(a)}}function h(e){const t=p(e);let s=!0;function o(){s=!0,t.update(a=>a)}function r(a){s=!1,t.set(a)}function l(a){let n;return t.subscribe(c=>{(n===void 0||s&&c!==n)&&a(n=c)})}return{notify:o,set:r,subscribe:l}}function R(){const{set:e,subscribe:t}=p(!1);let s;async function o(){clearTimeout(s);try{const r=await fetch(`${E}/_app/version.json`,{headers:{pragma:"no-cache","cache-control":"no-cache"}});if(!r.ok)return!1;const a=(await r.json()).version!==A;return a&&(e(!0),clearTimeout(s)),a}catch{return!1}}return{subscribe:t,check:o}}function T(e,t){return e.origin!==g||!e.pathname.startsWith(t)}function G(e){e.client}const K={url:h({}),page:h({}),navigating:p(null),updated:R()};export{U as H,L as N,N as P,w as S,y as a,I as b,V as c,K as d,m as e,x as f,P as g,_ as h,T as i,G as j,g as o,O as r,Y as s};