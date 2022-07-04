#GNU nano 6.3
#!/bin/env python3
# Author : Muhammad Ristawakal N And Sopian Ansari (Noname_$1084)
# Github : https://github.com/MristawakalN And https://github.com/Sopian20
#			( Trying Modules )
import os,sys,time
from time import sleep
try:
	import pafy,requests,qrcode,pytube
	from requests import post

except ModuleNotFoundError:
	print ("[•_•] Menginstall Modules Yang Di Perlukan !!!")
	time.sleep(1)
	os.system ("pip install -r requirements.txt")
	os.system ("pkg install neofetch")
	print ("[^_^] Modules Yang Di Perlukan Sudah Terinstall ✓")
	time.sleep(2)
#			( Import Modules )
import requests,pafy,qrcode,pytube
import youtube_dl
from qrcode import make
# Run/Running menu,logo,system,dll.
os.system("clear")
time.sleep(2)
while True:
	nama = input("\033[37;1m[\033[31;1m•\033[37;1m] \033[35;1mMasukan Nama: \033[32;1m")
	if nama == "" or nama == " ":
		print ("\033[31;1m[•_•] \033[37;1mGak Boleh Kosong !")
	else:
		os.system("clear")
		print ("\033[37;1m[\033[32;1m√\033[37;1m] \033[31;1mSelamat Datang \033[32;1m"+ nama)
		time.sleep(2)
		os.system("clear")
		break
logo_sopian = ("""\033[34;1m
'##:::'##:'########::'######:::'#######::'##::::'##:'########:'########
. ##:'##::... ##..::'##... ##:'##.... ##: ##:::: ##: ##.....:: ##....##
:. ####:::::: ##:::: ##:::..:: ##:::: ##: ##:::: ##: ##::::::: ##::::##
::. ##::::::: ##:::: ##::::::: ##:::: ##: ##:::: ##: ######::: ########
::: ##::::::: ##:::: ##::::::: ##:::: ##:. ##:: ##:: ##...:::: ##... ##
::: ##::::::: ##:::: ##::: ##: ##:::: ##::. ## ##::: ##::::::: ##::.. ##
::: ##::::::: ##::::. ######::. #######::::. ###:::: ########: ##:::.. ##
:::..::::::::..::::::......::::.......::::::...:::::........::..:::::.:::""")
author = ("""
\033[1;37m\033[31m[•]\033[1;37m AUTHOR\033[31m          :\033[1;37m\033[1;37m Muhammad Ristawakal N.
\033[1;37m\033[31m[•]\033[1;37m AUTHOR\033[31m          :\033[1;37m\033[1;37m Noname_$1084
\033[1;37m\033[31m[•]\033[1;37m Github Author 1\033[31m :\033[1;37m\033[1;37m github.com/MristawakalN
\033[1;37m\033[31m[•]\033[1;37m Github Author 2\033[31m :\033[1;37m\033[1;37m github.com/Sopian20\n""")
menu = ("""
\033[31;1m 1. \033[37;1mYouTube mp4  \033[34;1m ( \033[32;1mdownload \033[34;1m)\033[34;1m
\033[31;1m 2. \033[37;1mYouTube mp3  \033[34;1m ( \033[32;1mdownload \033[34;1m)\033[34;1m
\033[31;1m 3. \033[37;1mQr code      \033[34;1m ( \033[32;1mcreate   \033[34;1m)
\033[31;1m 4. \033[37;1mAbout        \033[34;1m ( \033[32;1minfo sc  \033[34;1m)
\033[31;1m 5. \033[37;1mQuit Program \033[34;1m ( \033[32;1mexit sc  \033[34;1m)\n""")

print (logo_sopian)
time.sleep(1)
print ("\033[1;30m<═════════════[\033[1;33;41m • \033[1;37mAuthor\033[1;33m• \033[0m\033[1;30m]══════════════>")
time.sleep(1)
print (author)
time.sleep(1)
print ("\033[1;30m<═════════════[\033[1;33;41m • \033[1;37mMENU \033[1;33m• \033[0m\033[1;30m]══════════════>")
time.sleep(1)
print (menu)
time.sleep(1)
print ("\033[1;30m<═════════════[\033[1;33;41m • \033[1;37mPILIH\033[1;33m• \033[0m\033[1;30m]══════════════>\n")
time.sleep(1)

loading = "\n\033[1;30m<═════════════[\033[1;33;41m • \033[1;37mDOWNLOADING\033[1;33m• \033[0m\033[1;30m]══════════════>\033[37;1m\n"

while True:
	pilih = input("\033[37;1m[\033[31;1m•\033[37;1m] Nomor ? \t: \033[31;1m")
	if pilih == "" or pilih == " ":
		print ("\033[31;1m[•_•] \033[37;1mGak Boleh Kosong !")
	elif pilih == "1" or pilih == "01":
		print ("\n\033[37;1mExample : https//youtube.com/qp10skw29 ( Video )")
		while True:
			yt = input("\033[37;1m[\033[31;1m•\033[37;1m] Masukkan Link : \033[32;1m")
			if yt == "" or yt == " ":
				print ("\033[31;1m[•_•] \033[37;1mGak Boleh Kosong !")
			else:
				try:
					api = requests.get("https://api.ipify.org").text
				except requests.exceptions.ConnectionError:
					print ("\033[31;1m[•_•] \033[37;1mConnection Error !!!")
					sys.exit(0)
				print (loading)
				sopian = {}
				with youtube_dl.YoutubeDL(sopian) as ugel:
					ugel.download([yt])
				print ("\n\033[1;30m<═════════════[\033[1;33;41m • \033[1;37mDONE ✓\033[1;33m• \033[0m\033[1;30m]══════════════>\n")
				time.sleep(2)
				y_or_n = input("\033[37;1m[\033[31;1m•\033[37;1m] Apakah Ingin Lanjut ? (\033[32;1my\033[37;1m/\033[32;1mn\033[37;1m) : \033[32;1m")
				if y_or_n == "y" or y_or_n == "Y":
					time.sleep(1)
				elif y_or_n == "n" or y_or_n == "N":
					break
				else:
					continue
	elif pilih == "2" or pilih == "03":
		print ("\n\033[37;1mExample : https//youtube.com/qp10skw29 ( Music )")
		while True:
			yt2 = input("\033[37;1m[\033[31;1m•\033[37;1m] Masukkan Link : \033[32;1m")
			if yt2 == "" or yt2 == " ":
				print ("\033[31;1m[•_•] \033[37;1mGak Boleh Kosong !")
			else:
				try:
					api = requests.get("https://api.ipify.org").text
				except requests.exceptions.ConnectionError:
					print ("\033[31;1m[•_•] \033[37;1mConnection Error !!!")
					sys.exit(0)
				print (loading)
				youtube = {
					'format': 'bestaudio/best',
					'postprocessors': [{
						'key': 'FFmpegExtractAudio',
						'preferredcodec': 'mp3',
						'preferredquality': '192',
						}]
					}
				with youtube_dl.YoutubeDL(youtube) as music:
					music.download([yt2])
				print ("\n\033[1;30m<═════════════[\033[1;33;41m • \033[1;37mDONE ✓\033[1;33m• \033[0m\033[1;30m]══════════════>\n")
				time.sleep(2)
				y_or_n = input("\033[37;1m[\033[31;1m•\033[37;1m] Apakah Ingin Lanjut ? (\033[32;1my\033[37;1m/\033[32;1mn\033[37;1m) : \033[32;1m")
				if y_or_n == "y" or y_or_n == "Y":
					time.sleep(1)
				elif y_or_n == "n" or y_or_n == "N":
					break
				else:
					continue
	elif pilih == "3" or pilih == "03":
		print ("\n\033[37;1mExample : https//youtube.com/qp10skw29 ( Picture )")
		while True:
			qr = str(input("\033[37;1m[\033[31;1m•\033[37;1m] Masukkan Link : \033[32;1m"))
			if qr == "" or qr == " ":
				print ("\033[31;1m[•_•] \033[37;1mGak Boleh Kosong !")
			else:
				code = str(input("\033[37;1m[\033[31;1m•\033[37;1m] Masukkan Nama : \033[32;1m"))
				if code == "" or code == " ":
					print ("[•_•] Gak Boleh Kosong !")
				else:
					try:
						api = requests.get("https://api.ipify.org").text
					except requests.exceptions.ConnectionError:
						print ("\033[31;1m[•_•] \033[37;1mConnection Error !!!")
						sys.exit(0)
					print (loading)
					url = qrcode.make(qr)
					url.save(f"{code}.png")
					url.show(f"{code}.png")
					os.system(f"cp {code}.png /sdcard")
					os.system(f"rm {code}.png")
					print ("\n\033[1;30m<═════════════[\033[1;33;41m • \033[1;37mDONE ✓\033[1;33m• \033[0m\033[1;30m]══════════════>\n")
					time.sleep(2)
					y_or_n = input("\033[37;1m[\033[31;1m•\033[37;1m] Apakah Ingin Lanjut ? (\033[32;1my\033[37;1m/\033[32;1mn\033[37;1m) : \033[32;1m")
					if y_or_n == "y" or y_or_n == "Y":
						time.sleep(1)
					elif y_or_n == "n" or y_or_n == "N":
						break
					else:
						continue
	elif pilih == "4" or pilih == "04":
		os.system ("clear")
		print ("\033[37;1m[=======[ ABOUT DEVICE SYSTEM ]=======]\n")
		time.sleep(1)
		os.system("neofetch --ascii_distro mint")
		time.sleep(1)
		print ("""
[=======[ ABOUT PROGRAMMER SCRIPT ]=======]\033[37;1m
 ____________________________________________
[ Author ] : [ Muhammad Ristawakal Nuhung    ]
[ Author ] : [ Sopian Ansari                 ]
[ Tools  ] : [ YT COVERT                     ]
[ Versi  ] : [ 1.0 ( Project )               ]
[ Kontak ] : [ (+6285823104520) UgeL         ]
[ Kontak ] : [ (+6285693492107) Sopia        ]
[ Alamat ] : [ Kota Kendari, Des. Aopa       ]
[ Alamat ] : [ Kota Bogor, Des. papanggungan ]
 ————————————————————————————————————————————
""")
		time.sleep(1)
		enter = input("""[•] Enter From Back In Menu [•]
 """)
		if enter == "" or enter == " ":
			print ("\033[1;30m<═════════════[\033[1;33;41m • \033[1;37mMENU \033[1;33m• \033[0m\033[1;30m]══════════════>")
			time.sleep(1)
			print (menu)
		else:
			print ("\033[1;30m<═════════════[\033[1;33;41m • \033[1;37mMENU \033[1;33m• \033[0m\033[1;30m]══════════════>")
			time.sleep(1)
			print (menu)
	else:
		print ("\033[31;1m[•_•] \033[37;1mInput Invalid !")
