import getpass, os, re
from subprocess import Popen, PIPE

os.chdir("/usr/local/lib/python3.2/dist-packages")
os.system("sudo rm -r LNcommon")
os.system("sudo rm -r LNdigitalIO")
os.system("sudo rm -r LN_Digital_Emulator")
os.system("sudo rm -r LN_Digital_Scratch_Handler")

os.chdir("/usr/local/bin")
os.system("sudo rm -r LN-Digital-Emulator")
os.system("sudo rm -r LN-Digital-Scratch-Handler")

os.chdir("/home/bananapi")
os.system("sudo rm -r LN-Scratch")
os.system("sudo rm -r python3-LNcommon")

os.chdir("/home/bananapi/photos")
os.system("sudo rm /home/bananapi/photos/Lemakerlogo.xpm")
os.system("sudo rm /home/bananapi/photos/LN_Digital_Emulator.png")
os.system("sudo rm /home/bananapi/photos/LN_Digital_Scratch_Handler.png")

os.chdir("/home/bananapi/Desktop")
os.system("sudo rm /home/bananapi/Desktop/LN-Digital-Emulator.desktop")
os.system("sudo rm /home/bananapi/Desktop/LN-Scratch-Handler.desktop")
os.system("sudo rm /home/bananapi/Desktop/LN-Scratch.desktop")
