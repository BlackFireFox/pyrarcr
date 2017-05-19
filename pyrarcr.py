#!/usr/bin/env python3

#####      ##### ##### #####             ####   ####   #
#   # #  # #   # #   # #   # #### ####   #  #      #  ##
##### #### ##### ##### ##### #    #      #  #   ####   #
#       #  #  #  #   # #  #  #    #      #  #   #      #
#       #  #   # #   # #   # #### #      #### # #### # #

#finds the password of a desired rar or zip file using a brute-force algorithm
##will fail to find the password if the password has a character that isnt in
##the english alphabet or isnt a number (you can change the char. list though)

#importing needed modules
import time,os,sys,shutil,itertools

name=os.path.basename(__file__)

#checking if the user's operating system is compatible with pyrarcr
if os.name!="posix":
 print("ERROR:",name,"isn't compatible with your system.")
 sys.exit(-1)
#checking if the user has unrar/p7zip installed
for which in ["unrar","p7zip"]:
 if not shutil.which(which):
  print("ERROR:",which,"isn't installed.\nExiting...")
  sys.exit(-1)

#defining the function
def rc(rf):
 alphabet="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890"
 start=time.time()
 tryn=0
 for a in range(1,len(alphabet)+1):
  for b in itertools.product(alphabet,repeat=a):
   k="".join(b)
   if rf[-4:]==".rar":
    print("Trying:",k,end="\r")
    kf=os.popen("unrar t -y -p%s %s 2>&1|grep 'All OK'"%(k,rf))
    tryn+=1
    for rkf in kf.readlines():
     if rkf=="All OK\n":
      print("Found password:",repr(k))
      print("Tried combination count:",tryn)
      print("It took",round(time.time()-start,3),"seconds")
      print("Exiting...")
      os.system("paplay Positive.ogg")
      #time.sleep(2)
      sys.exit(1)
   elif rf[-4:]==".zip" or rf[-3:]==".7z":
    print("Trying:",k,end="\r")
    kf=os.popen("7za t -p%s %s 2>&1|grep 'Everything is Ok'"%(k,rf))
    tryn+=1
    for rkf in kf.readlines():
     if rkf=="Everything is Ok\n":
      print("Found password:",repr(k))
      print("Tried combination count:",tryn)
      print("It took",round(time.time()-start,3),"seconds")
      print("Exiting...")
      os.system("paplay Positive.ogg")
      #time.sleep(2)
      sys.exit(1)
   else:
    print("ERROR: File isnt a RAR, ZIP or 7z file.\nExiting...")

def rcd(rf,d):
 try:
  di=open(d,"r")
  words=di.read()
  di.close()
 except:
  di=open(d,encoding="ISO-8859-1")
  words=di.read()
  di.close()
 start=time.time()
 tryn=0
 for line in words.splitlines():
  k=line
  if rf[-4:]==".rar":
   print("Trying:",k,"          ",end="\r")
   kf=os.popen("unrar t -y -p%s %s 2>&1|grep 'All OK'"%(k,rf))
   tryn+=1
   for rkf in kf.readlines():
    if rkf=="All OK\n":
     print("Found password:",repr(k))
     print("Tried combination count:",tryn)
     print("It took",round(time.time()-start,3),"seconds")
     print("Exiting...")
     os.system("paplay Positive.ogg")
     #time.sleep(2)
     sys.exit(1)
  elif rf[-4:]==".zip" or rf[-3:]==".7z":
   print("Trying:",k,"          ",end="\r")
   kf=os.popen("7za t -p%s %s 2>&1|grep 'Everything is Ok'"%(k,rf))
   tryn+=1
   for rkf in kf.readlines():
    if rkf=="Everything is Ok\n":
     print("Found password:",repr(k))
     print("Tried combination count:",tryn)
     print("It took",round(time.time()-start,3),"seconds")
     print("Exiting...")
     os.system("paplay Positive.ogg")
     #time.sleep(2)
     sys.exit(1)
  else:
   print("ERROR: File isnt a RAR, ZIP or 7z file.\nExiting...")

#checking if the file exists/running the function
if len(sys.argv)==2 or len(sys.argv)==4:
 if os.path.exists(sys.argv[1]):
  if len(sys.argv)==4:
   if sys.argv[2]=="d":
    if os.path.exists(sys.argv[3]):
     rcd(sys.argv[1],sys.argv[3])
    else:
     print("'"+sys.argv[3]+"' doesn't exist.\nExiting...")
     sys.exit(1)
   else:
    print("Usage:",name,"[rar file]")
    print("Example:",name,"foobar.rar")
    print("For use dictionary:",name,"[rar file] d [dictionary file]")
    print("Example:",name,"foo.rar d bar.txt")
    print("WARNING! The dictionary file must have the keywords one under the other.")
    print("Example:\nKeyWord1\nw00d\nkey\nwat3r")
    sys.exit(1)
  else:
   rc(sys.argv[1])
 else:
  print("ERROR: '"+argv[1]+"' doesn't exist.\nExiting...")
else:
 print("Usage:",name,"[rar file]")
 print("Example:",name,"foobar.rar")
 print("For use dictionary:",name,"[rar file] d [dictionary file]")
 print("Example:",name,"foo.rar d bar.txt")
 print("WARNING! The dictionary file must have the keywords one under the other.")
 print("Example:\nKeyWord1\nw00d\nkey\nwat3r")
