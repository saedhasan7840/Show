#ROOT JAHID
import os as O, sys as S, time as T, urllib as U, threading as TH
from os import system as Ex
from threading import active_count as A
from os import system as N


N('x'+'d'+'g'+'-'+'o'+'p'+'e'+'n'+' '+'h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'t'+'.'+'m'+'e'+'/'+'R'+'o'+'o'+'t'+'J'+'a'+'h'+'i'+'d')

try:
 import requests as R
except:
 O.system('pip install requests')
 import requests as R

M=400
J=[]
L=input('\n</> Post Link : ')

def H(P):
 C=L.split('/')[3]
 I=L.split('/')[4]
 D(C,I,P)

def D(C,I,P):
 S=R.Session()
 Q={'http':P,'https':P}
 try:
  R1=S.get("https://t.me/"+C+"/"+I,timeout=10,proxies=Q)
  SC=R1.headers['set-cookie'].split(';')[0]
 except:
  return False

 H1={
  "Accept":"*/*",
  "Accept-Encoding":"gzip, deflate, br",
  "Accept-Language":"en-US,en;q=0.9",
  "Connection":"keep-alive",
  "Content-Length":"5",
  "Content-type":"application/x-www-form-urlencoded",
  "Cookie":SC,
  "Host":"t.me",
  "Origin":"https://t.me",
  "Referer":"https://t.me/"+C+"/"+I+"?embed=1",
  "Sec-Fetch-Dest":"empty",
  "Sec-Fetch-Mode":"cors",
  "Sec-Fetch-Site":"same-origin",
  "User-Agent":"Chrome"
 }
 data1={"_rl":"1"}

 try:
  P1=S.post("https://t.me/"+C+"/"+I+"?embed=1",json=data1,headers=H1,proxies=Q)
  VK=P1.text.split('data-view="')[1].split('"')[0]
  CV=P1.text.split('<span class="tgme_widget_message_views">')[1].split('</span>')[0]
  if "K" in CV: CV=CV.replace("K","00").replace(".","")
 except:
  return False

 H2={
  "Accept":"*/*",
  "Accept-Encoding":"gzip, deflate, br",
  "Accept-Language":"en-US,en;q=0.9",
  "Connection":"keep-alive",
  "Cookie":SC,
  "Host":"t.me",
  "Referer":"https://t.me/"+C+"/"+I+"?embed=1",
  "Sec-Fetch-Dest":"empty",
  "Sec-Fetch-Mode":"cors",
  "Sec-Fetch-Site":"same-origin",
  "User-Agent":"Chrome",
  "X-Requested-With":"XMLHttpRequest"
 }

 try:
  VR=S.get("https://t.me/v/?views="+VK,timeout=10,headers=H2,proxies=Q)
  if VR.text=="true":
   print(f'[✔️] TG VIEW SUCCESS : {CV}')
 except:
  return False

 H3={
  "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
  "Accept-Encoding":"gzip, deflate, br",
  "Accept-Language":"en-US,en;q=0.9",
  "Cache-Control":"max-age=0",
  "Connection":"keep-alive",
  "Cookie":SC,
  "Host":"t.me",
  "Sec-Fetch-Dest":"document",
  "Sec-Fetch-Mode":"navigate",
  "Sec-Fetch-Site":"none",
  "Sec-Fetch-User":"?1",
  "Upgrade-Insecure-Requests":"1",
  "User-Agent":"Chrome"
 }

 try:
  S.get("https://t.me/"+C+"/"+I,headers=H3,timeout=10,proxies=Q)
 except:
  return False

def F():
 try:
  HP=R.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=0",proxies=U.request.getproxies(),timeout=5).text
  OP=R.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=0",proxies=U.request.getproxies(),timeout=5).text
  SP=R.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=0",proxies=U.request.getproxies(),timeout=5).text
 except Exception as e:
  print(e)
  return False
 with open("/sdcard/proxies.txt","w") as P:
  P.write(HP+"\n"+OP)
 with open("/sdcard/socks.txt","w") as S:
  S.write(SP)

def V(P):
 Q={'http':P,'https':P}
 try:
  H(P)
 except:
  return False

def K():
 if F()==False: return
 with open("/sdcard/proxies.txt","r") as PR:
  PS=PR.readlines()
 for P in PS:
  P=P.strip()
  if not P: continue
  while A()>M: pass
  THR=TH.Thread(target=V,args=(P,))
  J.append(THR)
  THR.start()

 with open("/sdcard/socks.txt","r") as SR:
  SS=SR.readlines()
 for P in SS:
  P=P.strip()
  if not P: continue
  while A()>M: pass
  SP="socks5://"+P
  THR=TH.Thread(target=V,args=(SP,))
  J.append(THR)
  THR.start()
 return True

def RPT(X=False):
 if X:
  while True:
   K()
 else:
  K()

RPT(True)
