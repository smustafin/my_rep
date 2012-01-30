import requests
import os
import json
log="smustafin"
pasw="12as34df"
user="smustafin"
reqq=""
user=raw_input("Pass username: ")
while 1:
 try:
  ch=input("""Pass 1 and Enter for show info about user\nPass 2 and Enter for show user`s repos\n""")
  if ch==1: 
   reqq='/users/%s' % (user)  
   break
  if ch==2: 
   reqq='/users/%s/repos' % (user) 
   os.system('clear')
   print "wait..."
   break
  os.system('clear')
  print "Pass again...."
 except NameError:  
  os.system('clear')
  print "Pass again...."
 except SyntaxError:  
  os.system('clear')
  print "Pass again...."
os.system('clear')
print "wait..."
host="https://api.github.com%s" % (reqq)
r = requests.get(host, auth=(log,pasw))
print r.headers['content-type']
print "\n"
print r.content
print "\n"
# all content divided on small part / bad English )
slov=json.loads(r.content)
try:
 print "email=", slov['email']
except KeyError:
 print "Not found"
 
