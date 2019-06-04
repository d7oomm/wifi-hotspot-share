#!/usr/bin/python

import os
os.system("clear")
print("""
__        ___ _____ _ 
\ \      / (_)  ___(_)
 \ \ /\ / /| | |_  | |
  \ V  V / | |  _| | |
   \_/\_/  |_|_|   |_|
 _   _       _                   _   
| | | | ___ | |_ ___ _ __   ___ | |_ 
| |_| |/ _ \| __/ __| '_ \ / _ \| __|
|  _  | (_) | |_\__ \ |_) | (_) | |_ 
|_| |_|\___/ \__|___/ .__/ \___/ \__|
                    |_|              
____  _                    
/ ___|| |__   __ _ _ __ ___ 
\___ \| '_ \ / _` | '__/ _ /
 ___) | | | | (_| | | |  __/
|____/|_| |_|\__,_|_|  \___|
                                                  
""")
print("                      Script By : Engima D7ooM Al-kurdi")
print("                           Snapchat:@scorpion.egram")
hotspot = input("Enter Name Hotspot:")
password = input("Enter ur Password:")
x = "nmcli device wifi hotspot con-name " + hotspot + " ssid " + hotspot + " band bg password " + password
os.system(x)
print("Hope Enjoy :)")
