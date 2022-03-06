import os
print("Welcome to the checkra1n.py terminal")
print("Type help for all the commands")
console = "$ "
while console != "exit":
  print(console)
  if console == "help":
    print("List of commands:")
    print("Help - this command")
    print("checkra1n - for jailbreaking")
    print("checkra1n -t ~ for a terminal ui")
    print("checkra1n -x ~ install alloc8 into NOR")
    rest = """  --demote                      demote device to enable JTAG
          --dump=address,length         dump memory to stdout
          --hexdump=address,length      hexdump memory to stdout
          --dump-rom                    dump SecureROM
          --dump-nor=file               dump NOR to file
          --flash-nor=file              flash NOR (header and firmware only) from file
          --24kpwn                      install 24Kpwn exploit to NOR
          --remove-24kpwn               remove 24Kpwn exploit from NOR
          --remove-alloc8               remove alloc8 exploit from NOR
          --decrypt-gid=hexdata         AES decrypt with GID key
          --encrypt-gid=hexdata         AES encrypt with GID key
          --decrypt-uid=hexdata         AES decrypt with UID key
          --encrypt-uid=hexdata         AES encrypt with UID key"""
    print(rest)
  elif console != "help":
    os.system("python ipwndfu " + console)
