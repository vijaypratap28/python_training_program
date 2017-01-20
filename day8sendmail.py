#created by vijay pratap singh
#created date 20-01-2017
# to send mail take three argument form the command line.



import sys
import smtplib
import getpass
#from mail_server import Gmailclass
host = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(host, port)
server.ehlo()
server.starttls()
server.ehlo()
v1 = sys.argv[1]
v2 = sys.argv[2]
v3 = sys.argv[3]
username = raw_input("gmail")
password = getpass.getpass()
server.login(username,password)
to = v1
sub = v3
file = open(v2,'r')
mes = file.read()
message = "subject: %s\n\n %s" %(sub,mes)
server.sendmail(username,to,message)
