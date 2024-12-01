#!/usr/bin/env python3

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MAC CHANGER")

print("""
1. Change MAC Address
2. Revert to Previous State
3. Exit
""")

while True:

	prcs = input("Press the number of the transaction you want to select: ")
	
	if prcs == "1":
		print("\033[93m[+] Changing MAC address...\033[0m")
		os.system("ifconfig eth0 down")
		os.system("macchanger -r eth0")
		os.system("ifconfig eth0 up")
		print("\033[92m[✔] MAC address changed successfully!\033[0m\n")
	
	elif prcs == "2":
		print("\033[93m[+] Reverting to the previous MAC address...\033[0m")
		os.system("ifconfig eth0 down")
		os.system("macchanger -p eth0")
		os.system("ifconfig eth0 up")

	elif prcs == "3":
		print("\033[91m[-] Exiting the program...\033[0m\n")
		break
	
	else:
		print("You made the wrong decision! Restarting...")
		os.system("python3 mac_changer.py")


print("see you later\033[92m")
