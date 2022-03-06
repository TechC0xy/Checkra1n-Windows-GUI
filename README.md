# Welcome to Checkra1n-Windows-GUI
This version of the file checkran can be used directly on windows and can be used directly on this repository.
# Checkra1n For Windows By c0xy Tech Team
 checkra1n for windows, written in python

well it's checkm8 only

# RUN ALL OF THIS USING ADMIN COMMAND PROMPT

# Preinstall
git from https://git-scm.com/

python from https://python.org
### IMPORTANT
cd to the libusb folder after cloning/downloading and copy **libusb.dll** to c:/windows/system32 and c:/windows/syswow64 (only if 64bit) then run **infinstaller.exe** from libusb folder and install the .inf file by right clicking. AFter that copy **Libusb0.sys** to c:/windows/system32/Drivers and c:/windows/syswow64 (only if 64bit)

# Must do
after cloning cd into the folder and type `python main.py`
type 0 into `$ ` to install dependencies

# Optional (recomended)
Run command prompt as administrator and cd to the folder, type `cpbin` ~ this allows you to run checkra1n from anywhere by typing checkra1n from cmd

# Steps
For the menu, simply follow installation
for the instant checkra1n cd to the folder and type `cpbin.lnk` (allows you to just type checkra1n from anywhere, boot flags not supported yet)
For a bad GUI version cd to the folder and type `python gui.py`
For webra1n (css + html to come soon) cd to the folder and type `python index.py`

# Installation:
```
git clone https://github.com/TechC0xy/Checkra1n-Windows-GUI
cd Checkra1n.py
python main.py
```

# Features
- Webra1n
- Gui
- Cli
- DFU tool ~ `python dfu.py`
- Menu
- Open source

# TO DO:
- ~~[ ] Implement pyboot~~ Taken out
- [x] Add mydearpygui
- [ ] Make theming

# Compatability
s5l8947x - Apple TV 3rd Gen

s5l8950x: iPhone 5/5C

s5l8955x: iPad 4th Gen

s5l8960x: iPad Air, iPhone 5S, iPad mini 2, iPad mini 3

t8002: Apple Watch Series 1/2

t8004: Apple Watch Series 3

t8010: iPad 6/7th Gen, iPhone 7, iPhone 7 Plus, iPod Touch 7th Gen

t8011: iPad Pro (10.5 inch), iPad Pro (12.9 inch) 2nd Gen, Apple TV 4k

t8015: iPhone 8/8+, iPhone X

Or anything else that supports the checkm8 exploit

# Troubleshooting:
1. restart your computer at least 3 times after installing drivers
2. re-try the jailbreak

# Errors:
 **1.** File "C:\Users\users\Downloads\ipwndfu-master\ipwndfu-master\ipwndfu", line 47, in <module>
    device = dfu.acquire_device()
  File "C:\Users\users\Downloads\ipwndfu-master\ipwndfu-master\dfu.py", line 16, in acquire_device
    for device in usb.core.find(find_all=True, idVendor=0x5AC, idProduct=0x1227, backend=backend):
  File "C:\Users\users\Downloads\ipwndfu-master\ipwndfu-master\usb\core.py", line 1263, in find
  
  # Credit
  XiaoChen(c0xyTech）China
  
  Dr238(c0xyTech)China
