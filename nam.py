
from builtins import exec, input, len, print, int, range, str, open, exit
exec('')
xnhac = '\x1b[1;36m'
do = '\x1b[1;31m'
luc = '\x1b[1;32m'
vang = '\x1b[1;33m'
xduong = '\x1b[1;34m'
hong = '\x1b[1;35m'
trang = '\x1b[1;39m'
whiteb = '\x1b[1;39m'
red = '\x1b[0;31m'
redb = '\x1b[1;31m'
end = '\x1b[0m'
dev = '\x1b[1;39m[\x1b[1;31m×\x1b[1;39m]\x1b[1;39m'
thanh_xau = red + '[' + vang + 'Nam-TooL' + red + '] ' + trang + '➩ ' + luc
thanh_dep = trang + '~' + red + '[' + luc + 'Nam-TooL' + red + '] ' + trang + '➩ ' + luc
import requests
import json
import os
import sys
from sys import platform
from datetime import datetime
from time import sleep, strftime
def clear():
    if platform[0:3] == 'lin':
        os.system('clear')
    else:
        os.system('cls')
clear()
def banner():
	print('███╗░░██╗████████╗░█████╗░░█████╗░██╗░░░░░')
	print('████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░')
	print('██╔██╗██║░░░██║░░░██║░░██║██║░░██║██║░░░░░')
	print('██║╚████║░░░██║░░░██║░░██║██║░░██║██║░░░░░')
	print('██║░╚███║░░░██║░░░╚█████╔╝╚█████╔╝███████╗')
	print('╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝')
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
bug_duoc_cai_lon = {
    'pass': 'namprohehe' }
banner()
def is_connected():
    import socket
    socket(('1.1.1.1', 53))
    return True
    if OSError:
        pass
    return False
print('\x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗')
print('\x1b[38;5;208m║ \x1b[38;5;207mTOOL TRAO ĐỔI SUB    \x1b[38;5;208m ║')
print('\x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝')
print('\x1b[38;5;226m[1] \x1b[38;5;46mTOOL \x1b[38;5;51mTDS TIKTOK + TIKTOK NOW')
print('\x1b[38;5;226m[2] \x1b[38;5;46mTOOL \x1b[38;5;51mTDS BẰNG PAGE PRO5')
print('\x1b[38;5;226m[3] \x1b[38;5;46mTOOL \x1b[38;5;51mTDS FACEBOOK FULL JOD')
print('\x1b[38;5;46m-----------------------------------------------------------------')
import requests

chon = int(input('\x1b[38;5;46m▶ Nhập Số \x1b[1;32m: \x1b[38;5;226m'))

urls = [
    'https://raw.githubusercontent.com/Nguyennam2201/Nguyennam2201/main/tdstiktok.py',
    'https://raw.githubusercontent.com/Nguyennam2201/Nguyennam2201/main/tdspage.py',
    'https://raw.githubusercontent.com/Nguyennam2201/Nguyennam2201/main/tds.py',
    'https://raw.githubusercontent.com/Nguyennam2201/Nguyennam2201/main/mail.py',
]

if 1 <= chon <= 3:
    url = urls[chon - 1]
    exec(requests.get(url).text)
else:
    print('Sai Lựa Chọn')
    exit()