import os
#import mydearpygui
import time
while True:
	print("Welcome to checkra1n.py")
	print("by Sakurai07")
	print("#########################")
	print("[0]. Install dependencies (MUST DO once)")
	print("[1]. Jailbreak")
	print("[2]. GUI Jailbreak")
	print("[3]. Github")
	print("[4]. Guide")
	print("[5]. exit")
	print("type help for help")
	choice = input("$ ")
	print(choice)
	if choice == "1":
		os.system("python confirm.py")
	#os.system("dir")
	#os.system("python ipwndfu")
	elif choice == "3":
		print("https://github.com/sakurai07/checkra1n.py")
	elif choice == "4":
		print("Go to the github repository or check README.md")
	elif choice == "0":
		os.system("pip install -r requirements.txt")
		os.system("install.lnk")
	elif choice == "2":
		os.system("python gui.py")
	elif choice == "help":
		os.system("type README.md")
	elif choice == "5":
		break

