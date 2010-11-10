import os

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
		"airmon-ng stop wlan0"
		"service network-manager start",))
	os.system(houselist)
	os.sys.exit()

#def clrpcrap():
#	os.system("service network-manager stop")
#	os.system("airmon-ng stop mon4")
#	os.system("airmon-ng stop mon3")
#	os.system("airmon-ng stop mon2")
#	os.system("airmon-ng stop mon1")
#	os.system("airmon-ng stop mon0")
#	os.system("airmon-ng stop wlan0")

