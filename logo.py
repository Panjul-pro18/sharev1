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


def logo():
	print(f"  {war}_________.__          __________ \n /   _____/|  |__   ____\______   \ \n \_____  \ |  |  \_/ __ \|       _/      \n {N}/        \|   Y  \  ___/|    |   \ \n/_______  /|___|__/\_____>____|___/ \n        \/{K} http://Panjulpro18.org{N} ")
	print("\n \x1b[0;32m------------------------------------------------- \n [Facebook : Panjul Pro    \n [ Github   : github.com/Panjul-Pro18  \n [ youtube  : Panjul- pro18.   \n -------------------------------------------------\n")
	print(" \x1b[0;31m !! GUNAKAN SEPERLUNYA SAJA YA !! \x1b[0m ")
	
			