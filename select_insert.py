
import re
conn = MySQLdb.connect(host="localhost",user="root",passwd="asm123",db="accesspoint_database")

p = re.compile(ur'(?:[0-9a-fA-F]:?){12}')

file = open('/home/asm/vijay/diag.out','rb').read()

mac = re.findall(p, file)

x = conn.cursor()
x.execute("SELECT *  FROM information")
x.execute (" INSERT INTO information VALUES ('%s') ", (mac))
row = x.fetchall()



for a in mac:
    print a
