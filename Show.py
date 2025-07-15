#-----------------[ MODULE ]-------------------#
import os
def modules():
	os.system('pkg update -y && pkg upgrade -y')
	os.system('clear')
	try: 
		import rich
	except ModuleNotFoundError:
		print("\33[1;96m>>\x1b[1;97m RICH IS BEING INSTALLED \033[1;37m")
		os.system('pip install rich --quiet')
		print("\33[1;96m>>\x1b[1;97m RICH HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	try:
		import bs4
	except ModuleNotFoundError:
		print("\33[1;96m>>\x1b[1;97m BS4 IS BEING INSTALLED \033[1;37m")
		os.system('pip install bs4 --quiet')
		print("\33[1;96m>>\x1b[1;97m BS4 HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	try:
		import requests
	except ModuleNotFoundError:
		print("\33[1;96m>>\x1b[1;97m REQUESTS IS BEING INSTALLED \033[1;37m")
		os.system('pip install requests --quiet')
		print("\33[1;96m>>\x1b[1;97m REQUESTS HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	exit()
try:
	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket,marshal
	import os, requests, marshal, zlib, base64
	from bs4 import BeautifulSoup as bs
	from bs4 import BeautifulSoup
	import urllib3,rich,base64
	from rich.table import Table as me
	from rich.console import Console as sol
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
	from rich.console import Group as gp
	from rich.panel import Panel as nel
	from rich.panel import Panel
	from rich.tree import Tree
	from rich.panel import Panel as nel
	from rich.panel import Panel as panel
	from rich import print as cetak
	from rich.markdown import Markdown as mark
	from rich.columns import Columns as col
	from rich import print as prints
	from rich import pretty
	from rich.text import Text as tekz
	from time import localtime as lt	
	import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	pretty.install()
	CON=sol()
except ModuleNotFoundError:
	modules()	
#------------[ COLOR ]--------------#
P = '\x1b[1;97m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
Z = "\x1b[38;5;83m"
X = "\x1b[38;5;46m"
m = '\x1b[1;91m'
b = '\33[1;96m'	
#---------------------[IP]---------------------#
try:
	net = requests.get("http://ip-api.com/json/").json()["isp"]
	ipxx = requests.get("https://api.ipify.org").text    
except requests.exceptions.ConnectionError:
	print('\033[1;37m—————————————————————————\x1b[1;97m')
	print("\33[1;96m>>\x1b[1;97m CHECK YOUR INTERNET")
	time.sleep(1)
	exit()
#------------------[ CUTS ]---------------#
def clear():
    os.system('clear')
def back():
    encodee()	
def line():
    print('\033[1;37m—————————————————————————————————————————————\x1b[1;97m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)    
#------------------[ LOGO ]-----------------#
logo =f"""  
  _____________   ____
 /   _____/\   \ /   /
 \_____  \  \   Y   /   
 /        \  \     /   \33[1;97mOWNER   : SAURAV DADA
/_______  /   \___/    \33[1;97mGITHUB  : Saureyy 
        \/             \33[1;97mVERSION : \33[1;96mENCODE\33[1;97m
\033[1;37m—————————————————————————————————————————————\x1b[1;97m
-fuwk3rrr saura'v herrr'w - laud3y !-
\033[1;37m—————————————————————————————————————————————\x1b[1;97m"""       
#-------------[ ENCODE encodee ]------------------#           		
def encodee():
	clear()
	print(logo)
	print("\33[1;96m>>\x1b[1;97m YOUR INTERNET   :\033[1;99m "+net)
	print("\33[1;96m>>\x1b[1;97m IP ADDRESS      :\033[1;36m "+ipxx)
	line()
	print(f"""\33[1;96m>>\x1b[1;97m 1 \33[1;96m×\x1b[1;97m ENCRYPT BASE16""")
	print(f"""\33[1;96m>>\x1b[1;97m 2 \33[1;96m×\x1b[1;97m ENCRYPT BASE32""")    
	print(f"""\33[1;96m>>\x1b[1;97m 3 \33[1;96m×\x1b[1;97m ENCRYPT BASE64""")    
	print(f"""\33[1;96m>>\x1b[1;97m 4 \33[1;96m×\x1b[1;97m ENCRYPT MARSHAL""")    
	print(f"""\33[1;96m>>\x1b[1;97m 5 \33[1;96m×\x1b[1;97m ENCRYPT MARSHAL-ZLIB-BASE16""") 
	print(f"""\33[1;96m>>\x1b[1;97m 6 \33[1;96m×\x1b[1;97m ENCRYPT MARSHAL-ZLIB-BASE32""") 
	print(f"""\33[1;96m>>\x1b[1;97m 7 \33[1;96m×\x1b[1;97m ENCRYPT MARSHAL-ZLIB-BASE64""") 
	print(f"""\33[1;96m>>\x1b[1;97m 0 \33[1;96m×\x1b[1;97m EXIT THE TOOL""")    
	line()    
	saureyxx=input('\33[1;96m>>\x1b[1;97m CHOOSE : ')
	if saureyxx in ['1']:
		x1()        
	elif saureyxx in ['2']:
		x2()    	
	elif saureyxx in ['3']:
		x3()
	elif saureyxx in ['4']:
		x4()   
	elif saureyxx in ['5']:
		x5()
	elif saureyxx in ['6']:
		x6()
	elif saureyxx in ['7']:
		x7()   
	else:
		exit ()        	    
#__________________|  All Method |__________________#
def x1():
    line();saureyxx = input('\33[1;96m>>\x1b[1;97m FILE NAME : ')
    line()
    ups = open(saureyxx, 'rb').read()
    ui = base64.b16encode(ups)
    output = saureyxx.replace('.py', '') + '_enc.py'
    cok = open(output, 'w').write('#THHEE FWAKERR LEEGGENND SSAURAVVV HHEREE-!\n#——————————————————————————————————————\n import base64\nexec(base64.b16decode(' + str(ui) + '))')
    print(f"\33[1;96m>>\x1b[1;97m SUCCESSFULLY ENCRYPTED : %s" % saureyxx)
    line()
    print(f"\33[1;96m>>\x1b[1;97m SAVED AS : \33[1;96m%s" % output)
    line()
    xxz = input('\33[1;96m>>\x1b[1;97m PRESS ENTER TO BACK');back()

def x2():
	line()
	saureyxx = input('\33[1;96m>>\x1b[1;97m FILE NAME : ')
	line()
	ups = open(saureyxx, 'rb').read()
	ui = base64.b32encode(ups)
	output = saureyxx.replace('.py', '') + '_enc.py'
	cok = open(output, 'w').write('#THHEE FWAKERR LEEGGENND SSAURAVVV HHEREE-!\n#——————————————————————————————————————\nimport base64\nexec(base64.b32decode(' + str(ui) + '))')
	print(f"\33[1;96m>>\x1b[1;97m SUCCESSFULLY ENCRYPTED : %s" % saureyxx)
	line()
	print(f"\33[1;96m>>\x1b[1;97m SAVED AS : \33[1;96m%s" % output)
	line()  
	xxz = input('\33[1;96m>>\x1b[1;97m PRESS ENTER TO BACK');back()
	
def x3():
	line()
	saureyxx = input('\33[1;96m>>\x1b[1;97m FILE NAME : ')
	line()
	ups = open(saureyxx, 'rb').read()
	ui = base64.b64encode(ups)
	output = saureyxx.replace('.py', '') + '_enc.py'
	cok = open(output, 'w').write('#THHEE FWAKERR LEEGGENND SSAURAVVV HHEREE-!\n#——————————————————————————————————————\nimport base64\nexec(base64.b64decode(' + str(ui) + '))')
	print(f"\33[1;96m>>\x1b[1;97m SUCCESSFULLY ENCRYPTED : %s" % saureyxx)
	line()
	print(f"\33[1;96m>>\x1b[1;97m SAVED AS : \33[1;96m%s" % output)
	line()
	xxz = input('\33[1;96m>>\x1b[1;97m PRESS ENTER TO BACK');back()
	
def x4():
	line()
	saureyxx = input('\33[1;96m>>\x1b[1;97m FILE NAME : ')
	line()
	fileopen = open(saureyxx, 'rb').read()
	a = compile(fileopen, 'dg', 'exec')
	m = marshal.dumps(a)
	s = repr(m)
	output = saureyxx.replace('.py', '') + '_enc.py'
	cok = open(output, 'w').write('#THHEE FWAKERR LEEGGENND SSAURAVVV HHEREE-!\n#——————————————————————————————————————\nimport marshal\nexec(marshal.loads(' + s + '))')
	print(f"\33[1;96m>>\x1b[1;97m SUCCESSFULLY ENCRYPTED : %s" % saureyxx)
	line()
	print(f"\33[1;96m>>\x1b[1;97m SAVED AS : \33[1;96m%s" % output)
	line()
	xxz = input('\33[1;96m>>\x1b[1;97m PRESS ENTER TO BACK');back()

def x5():
	line()
	saureyxx = input('\33[1;96m>>\x1b[1;97m FILE NAME : ')
	line()
	fileopen = open(saureyxx, 'rb').read()
	a = compile(fileopen, 'dg', 'exec')
	m = marshal.dumps(a)
	z = zlib.compress(m)
	b = base64.b16encode(z)
	output = saureyxx.replace('.py', '') + '_enc.py'
	cok = open(output, 'w').write('#THHEE FWAKERR LEEGGENND SSAURAVVV HHEREE-!\n#——————————————————————————————————————\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode(' + str(b) + '))))')
	print(f"\33[1;96m>>\x1b[1;97m SUCCESSFULLY ENCRYPTED : %s" % saureyxx)
	line
	print(f"\33[1;96m>>\x1b[1;97m SAVED AS : \33[1;96m%s" % output)
	line()
	xxz = input('\33[1;96m>>\x1b[1;97m PRESS ENTER TO BACK');back()
	
def x6():
	line()
	saureyxx = input('\33[1;96m>>\x1b[1;97m FILE NAME : ')
	line()
	fileopen = open(saureyxx, 'rb').read()
	a = compile(fileopen, 'dg', 'exec')
	m = marshal.dumps(a)
	z = zlib.compress(m)
	b = base64.b32encode(z)
	output = saureyxx.replace('.py', '') + '_enc.py'
	cok = open(output, 'w').write('#THHEE FWAKERR LEEGGENND SSAURAVVV HHEREE-!\n#——————————————————————————————————————\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode(' + str(b) + '))))') 
	print(f"\33[1;96m>>\x1b[1;97m SUCCESSFULLY ENCRYPTED : %s" % saureyxx)
	line()
	print(f"\33[1;96m>>\x1b[1;97m SAVED AS : \33[1;96m%s" % output)
	line()
	xxz = input('\33[1;96m>>\x1b[1;97m PRESS ENTER TO BACK');back()
	
def x7():
	line()
	saureyxx = input('\33[1;96m>>\x1b[1;97m FILE NAME : ')
	line()
	fileopen = open(saureyxx, 'rb').read()
	a = compile(fileopen, 'dg', 'exec')
	m = marshal.dumps(a)
	z = zlib.compress(m)
	b = base64.b64encode(z)
	output = saureyxx.replace('.py', '') + '_enc.py'
	cok = open(output, 'w').write('#THHEE FWAKERR LEEGGENND SSAURAVVV HHEREE-!\n#——————————————————————————————————————\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode(' + str(b) + '))))')
	print(f"\33[1;96m>>\x1b[1;97m SUCCESSFULLY ENCRYPTED : %s" % saureyxx)
	line()
	print(f"\33[1;96m>>\x1b[1;97m SAVED AS : \33[1;96m%s" % output)
	line()	
	xxz = input('\33[1;96m>>\x1b[1;97m PRESS ENTER TO BACK');back()
#-----------------------[ SYSTEM ]--------------------#
if __name__=='__main__':
	try:os.mkdir('/sdcard/Saureyy')	    
	except:pass
	try:os.mkdir('data')
	except:pass
	encodee()	
