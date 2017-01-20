import MySQLdb as m
host = 'localhost'
username = 'root'
password = 'root123'
database = 'mydb'

db_con = m.connect(host,username,password,database)
db_cur = db_con.cursor()#it will print list of list!
sql = "select * from info"
db_cur.execute(sql)
data = db_cur.fetchall()
for row in data:
	print row[0]
	print row[1]
	print row[2]
