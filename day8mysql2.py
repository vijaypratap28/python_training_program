import MySQLdb as m
import sys


host = 'localhost'
username = 'root'
password = 'root123'
database = 'mydb'

db_con = m.connect(host,username,password,database)
db_cur = db_con.cursor(m.cursors.DictCursor)#it will produce list of dictionary!
sql = "select * from info"
db_cur.execute(sql)
data = db_cur.fetchall()
for row in data:
	print row['name']
	print row['age']
	print row['address']
