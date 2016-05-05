#!/usr/bin/python3

"""
Aut: Lamine KA (@lamiinek)

Des: This version of the script, give the option to let the router reboot till the internet connection is working properly.
     The default loop interval is 2 minutes and 15 secs
"""

import sys, time
import requests
import socket



class Reboot_router:

	def __init__(self):

		self.url = "192.168.1.1/rebootinfo.cgi"
		self.user = "admin"
		self.passw = "xxxx"
		self.con = False

		self.reboot()


	def reboot(self):

		opts = input("Options: \n\tr = reboot\n\trl = loop reboot till connected\n\tc = cancel\n> ").lower()

		if opts == "r":
			
			print("Rebooting")
			req = requests.get("http://"+self.user+":"+self.passw+"@"+self.url)

		elif opts == "rl":
			
			print("Loop Reboot mode started!\n")
			delay = 135 # 2 minutes 15 secs
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
			#reboot
			requests.get("http://"+self.user+":"+self.passw+"@"+self.url)


rr = Reboot_router()
