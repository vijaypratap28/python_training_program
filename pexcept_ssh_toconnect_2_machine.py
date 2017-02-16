import pexpect

child = pexpect.spawn('/usr/bin/ssh root@192.168.32.1')


child.expect('password:', timeout=120) 

child.sendline('pass123') 


child.expect ('prompt# ')
