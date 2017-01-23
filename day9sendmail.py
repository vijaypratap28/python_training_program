import pexpect
import smtplib
import getpass
m_p = pexpect.spawn('python day8smail.py')
m_p.timeout = 600
m_p.expect('gmail')
m_p.sendline('vijaypratap069@gmail.com')
password = getpass.getpass()

m_p.expect('to')
m_p.sendline('vickysinghsinghel28@gmail.com')
m_p.expect('sub')
m_p.sendline('hello')
m_p.close()
