#!/usr/bin/python3

"""
Aut: Lamine KA (@lamiinek)

Des: This version of the script, give the option to let the router reboot till the internet connection is working properly.
     The default loop interval is 3 minutes
"""

import sys, time
import requests
import socket



class Reboot_router:

	def __init__(self):
		self.con = False

		self.reboot()


	def reboot(self):
		url = "192.168.1.1/rebootinfo.cgi"
		user = "admin"
		passw = "xxxxx"

		opts = input("Options: \n\tr = reboot\n\trl = loop reboot till connected\n\tc = cancel\n> ").lower()

		if opts == "r":
			
			print("Rebooting")
			req = requests.get("http://"+user+":"+passw+"@"+url)

		elif opts == "rl":
			
			print("Loop Reboot mode started!\n")
			delay = 180 # 3 minutes
			while self.con == False:
				self.check_internet()
				time.sleep(delay)

		elif opts == "c":
			
			print("Cancelled")

	def check_internet(self):
		host = "www.google.sn"
		try:
			h = socket.gethostbyname(host)
			s = socket.create_connection((h, 80), 2)
			print(time.strftime("%H:%M:%S")+" - connected")
			self.con = True
		except:
			print(time.strftime("%H:%M:%S")+" - No internet access")


rr = Reboot_router()
