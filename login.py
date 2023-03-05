import marshal
import os,re,sys,bs4,time,json,random,datetime,requests, calendar, random
from random import choice

from src import login as Login
from src import logo as Logo
from src import menu as Menu

K = "\x1b[0;33m"
N = "\x1b[0m" 
M = "\x1b[0;31m"
H = "\x1b[0;32m"

war = random.choice(['\x1b[0;33m', '\x1b[0m', '\x1b[0;31m', '\x1b[0;32m'])



def login():
	os.system("clear")
	try:
		tokenz = open("token","r").read()
		cokie = open("coki","r").read()
		Menu.menu()
	except (KeyError,IOError):
		print(f" [*] delete token ? Type : {K} python run.py cok{N}")
		input(" ENTER : ")
		os.system("clear")
		Logo.logo()
		print(f" [{K}#{N}] setelah anda login otomatis akun anda akan mengikuti akun admin")
		cookie = input(" [?] cookie fb : ")
		try:
			get_tok = requests.get('https://business.facebook.com/business_locations',headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			tokenz = re.search("(EAAG\w+)", get_tok.text).group(1)
			coki = {"cookie":cookie}
			open('coki','w').write(cookie)
			open('token','w').write(tokenz)
			exit(f" \n \t\tJALANKAN ULANG TOLLS {K}python run.py{N}")
		except requests.exceptions.ConnectionError:
			exit("koneksi eror")
		except (KeyError,IOError,AttributeError):
			exit(" [+] coki kadaluwarsa")