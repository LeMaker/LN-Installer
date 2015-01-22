import getpass, os, re
from subprocess import Popen, PIPE

os.chdir("/home/bananapi/Documents/LNcommon")
os.system("sudo python3 setup.py install")

os.chdir("/home/bananapi/Documents/LNdigitalIO")
os.system("sudo python3 setup.py install")

os.chdir("/home/bananapi/Documents/LN_Digital_Emulator")
os.system("sudo python3 setup.py install")

os.chdir("/home/bananapi/Documents/LN_Digital_Scratch_Handler")
os.system("sudo python3 setup.py install")

os.chdir("/home/bananapi/Documents/LN-Installer")

if not os.path.exists("/home/bananapi/LN-Scratch"):
        os.makedirs("/home/bananapi/LN-Scratch")
os.system("cp ./examples/* /home/bananapi/LN-Scratch")

if not os.path.exists("/home/bananapi/python3-LNcommon"):
        os.makedirs("/home/bananapi/python3-LNcommon")
os.system("cp ./docs/html -R /home/bananapi/python3-LNcommon/")

if not os.path.exists("/home/bananapi/photos"):
        os.makedirs("/home/bananapi/photos")
os.system("cp ./icons/* /home/bananapi/photos")

if not os.path.exists("/home/bananapi/Desktop"):
        os.makedirs("/home/bananapi/Desktop")
os.system("cp LN-Digital-Emulator.desktop /home/bananapi/Desktop")
os.system("cp LN-Scratch-Handler.desktop /home/bananapi/Desktop")
os.system("cp LN-Scratch.desktop /home/bananapi/Desktop")

os.system("sudo apt-get install python3-pyside")
os.system("sudo apt-get install xterm")
