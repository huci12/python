import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

google_ip = socket.gethostbyname("google.com")
sock.connect((google_ip,80))

sock.send("GET / HTTP/1.1\n".encode())
sock.send("\n".encode())

buffer = sock.recv(4096)
buffer = buffer.decode().replace("\r\n" , "\n")

print(buffer)

'''
HTTP/1.1 200 OK
Date: Sat, 02 May 2020 06:03:42 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2020-05-02-06; expires=Mon, 01-Jun-2020 06:03:42 GMT; path=/; domain=.google.com; Secure
Set-Cookie: NID=203=JhdChPZ2xmj4y7zzWA9pygmfQYfnwBWY0Ltrn7yzmYXn6r_GbwPOuT2ZJOf0p1W6QgFpwPOGD2PSm8vi_BZT_7Gz1CUa7khxXCQl173fPAH7bZmGtUhLKAVueoxSrVvK-DpnoMeGOyLGjSn_REuZYFhBku-LKLRDI1sUN0CHvj4; expires=Sun, 01-Nov-2020 06:03:42 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

5b0c
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png"
itemprop="image"><title>Google</title><script nonce="UahpL5Qljt0cuIN0ns85Jw==">(function(){window.google={kEI:'Pg2tXviIK5rh-AbFla74Aw',kEXPI:'0,202123,3,4,1151617,5662,731,223,755,4349,207,3204,10,1051,175,364,926,509,4,60,576,241,383,246,5,304,655,395,196,616,27,198,285,5,39,328,58,40,1119,754,219,417139,706743,1197730,419,78,329040,1294,12383,4855,32692,15247,861,17450,11240,369,8819,8384,4858,1362,9291,3024,2819,1924,1849,4,1265,7913,3,1807,4020,978,7931,5295,2056,920,873,262,2,953,1710,1,1264,6430,11306,3222,235,4284,1394,1381,520,399,2277,8,2796,1593,1165,114,2212,241,289,149,1103,840,517,1137,279,106,158,4100,312,1137,2,2063,606,789,1050,184,2297,1947,747,1482,93,330,1282,16,2927,2247,473,1339,748,1039,3227,773,2072,7,5599,469,8078,2662,642,1408,1042,2458,1226,1462,3934,1275,108,3409,906,2,941,972,1642,2397,4970,449,225,996,781,889,1086,1349,3,2,4,340,230,970,865,373,1638,1907,707,148,43,146,3313,2041,8,440,27,2224,2571,27,1344,47,83,1010,651,4,1528,17,414,204,8,16,283,353,1009,224,51,751,210,271,224,374,276,395,2,10,10,29,750,673,10,386,648,320,4,1336,118,49,125,332,335,118,226,573,126,4,25,610,130,60,234,2,20,126,131,206,678,827,8,165,3,40,832,415,53,210,502,1225,5,1593,45,112,359,228,502,707,264,148,1338,135,13,5819561,3308,1802585,6996022,549,333,444,1,2,80,1,900,896,1,8,1,2,2551,1,748,141,59,736,563,1,4265,1,1,1,1,137,1,1193,1401,3,420,32,45,10,2,3,1,2,2,4,1,1,4,8,4,15,4,1,1,19,9,1,1,4,4,1,5,16,3,1,1,1,4,1,2,1,3,1,28,16,4,4,2,1,3,8,2,4,1,1,1,4,18,3,23962262',kBL:'N_3N'};google.sn='webhp';google.kHL='ko';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var c;a&&(!a.getAttribute||!(c=a.getAttribute("eid")));)a=a.parentNode;return c||google.kEI};google.getLEI=function(a){for(var c=null;a&&(!a.getAttribute||!(c=a.getAttribute("leid")));)a=a.parentNode;return c};google.ml=function(){return null};google.time=function(){return Date.now()};google.log=function(a,c,b,d,g){if(b=google.logUrl(a,c,b,d,g)){a=new Image;var e=google.lc,f=google.li;e[f]=a;a.onerror=a.onload=a.onabort=function(){delete e[f]};google.vel&&google.vel.lu&&google.vel.lu(b);a.src=b;google.li=f+1}};google.logUrl=function(a,c,b,d,g){var e="",f=google.ls||"";b||-1!=c.search("&ei=")||(e="&ei="+google.getEI(d),-1==c.search("&lei=")&&(d=google.getLEI(d))&&(e+="&lei="+d));d="";!b&&google.cshid&&-1==c.search("&cshid=")&&"slh"!=a&&(d="&cshid="+google.cshid);b=b||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+c+e+f+"&zx="+google.time()+d;/^http:/i.test(b)&&"https:"==window.location.protocol&&(google.ml(Error("a"),!1,{src:b,glmm:1}),b="");return b};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};(function(){
document.documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"==c||"q"==c&&!a.elements.q.value?!0:!
'''