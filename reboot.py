"""

Aut  : Lamine Ka
Desc : This program will automatically connect to the router and reboot it for me

"""
import requests
from threading import Thread
import os, time

print("---------------------------------------")
print("|                                     |")
print("|                                     |")
print("| D-Link router rebooter by Lamine Ka |")
print("|                                     |")
print("|                                     |")
print("---------------------------------------\n\n")


name = os.getlogin() # pc username
path = "C:/Users/"+str(name)+"/AppData/Local" # location of the file containing the password

def reboot(user, pwd):

	cmds = "Command: r = (reboot)  ;  c = (change password)\n"
	print(cmds)

	cmd = input("> ")

	if cmd.lower() == "r" or cmd.lower() == "reboot":

		if user and pwd:

			print("Router rebooting...\n")
			#time.sleep(3)
			req = requests.get("http://"+user+":"+pwd+"@192.168.1.1/rebootinfo.cgi")
			status = req.status_code

			if status == 200:

				count_thread = Thread(target=count_down)
				count_thread.start()

			else:
				print("Ohh snap! something went wrong, make sure you have entered the router's password")


	elif cmd.lower() == "c":
		
		pwd = input("Enter new password: ")
		pwd_repeat = input("Repeat password: ")

		if pwd == pwd_repeat:

			o = open(path+"/router_reboot_password.txt", "w")
			password = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"+pwd
			o.write(password)
			o.close()
			print("password saved!\n")
			run()


	else:
		print(cmds)
		run()

def count_down():
	t = 75
	while t > 0:
		time.sleep(1)
		print("\nRouter will finish rebooting in "+str(t)+" seconds", end='\r')
		t -= 1
	print("\nDone!")


# in case the user uses the default password

def run():
	if os.path.isfile(path+"/router_reboot_password.txt"):

		pwd_open = open(path+"/router_reboot_password.txt", "r")
		user_pwd = pwd_open.read()
		user_pwd = user_pwd.replace("03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4", "")
		pwd_open.close()

		reboot("admin", user_pwd)

	else:

		reboot("admin", "admin")


if __name__ == '__main__':
	run()
	os.system("pause")
