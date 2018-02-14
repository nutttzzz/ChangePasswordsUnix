import os
import sys
import random
currentUser=os.environ['USER']
if (os.environ['USER']!="root"):
    print os.environ['USER']+" cannot preform password changing only to its own account, ReRun Script As Root QUITING~"
    sys.exit(1)
if len(sys.argv)<2:
    print sys.argv[0]+" <random password length>"
    sys.exit(1)
try :int(sys.argv[1])
except:
    print sys.argv[0]+" <random password length>"
    sys.exit(1)
users = os.listdir("/home")
users+=["root"]
command = "echo \"{0}:{1}\" | sudo chpasswd"
reference="{0}:{1}"
def genPasswords(leng):
    strPass=""
    for i in range(0,leng):
            charxx=  random.randrange(48,57) if random.randrange(0,2) else random.randrange(65,91)
            strPass+= chr(charxx)
    return strPass
os.system("rm passwords")
for i in [(command.format(x,genPasswords(int(sys.argv[1])))+"\n") for c,x in enumerate(users)]:
    os.system(i)
    os.system("echo \""+i.split(":")[0].split("\"")[1]+":"+i.split(":")[1].split("\"")[0]+"\" >> passwords")
print "command Ran Successfully"
