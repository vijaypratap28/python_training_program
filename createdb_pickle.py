import pickle
import sys
import os
import re
import shutil

sys1=sys.argv[1]
sys2=sys.argv[2]


username="vijay"  
password="bhopal"


i=1
list1=[]
list2=[]
my_list1=[]



st=[]
db=''
tb=''
list_db=[]

if((username==sys1)&(password==sys2)):
	
 while True:
   data=raw_input("mysql1>")
   str1=data
#-------------------> showing databases ------------------>

   if str1:
     reg1=re.search(r'(show databases;)',str1,re.I)
     if reg1:
	list_db=os.listdir("/home/asm/databases/")
	print "+--------------------+"
	print "|    databases       |"	
	print "+--------------------+"
	for i in list_db:
		#list_db=i
		print "|{:20}|".format(i)			
	print "+--------------------+"
   	print "%d rows in set"%len(list_db)

#--------------------> use databases ------------------->		
   if str1:
	database_name=''
	#table_name=''
	reg1=re.search(r'(use.*)',str1,re.I)
	if reg1:
	  use=str(reg1.group())
	  l3=use.split()
	  us=str(l3[1])
	  database_name=us.strip(';')
	  if database_name:
	    print "Reading table information for completion of table and column names\n"
	    print "database changed to --- ",database_name
	  
	  while True:
	    str2=raw_input("mysql2>")

	    #-----------------> show tables from database----------------->
	   
	    if str2:
	      try:
	              reg1=re.search(r'(show tables;.*)',str2,re.I|re.M)
	      
		      if reg1:
			stb="/home/asm/databases/"+str(database_name)+"/"
			st=os.walk(stb).next()[1]
			print "+-----------------------+"
			print "|tables_in_{:12} |".format(database_name)
			print "+-----------------------+"
			if st!="":
				
				for i in st:
				  if i!="":
				       print "|{:23}|".format(i)
				     
				print "+-----------------------+"	  
			else:
				print "no table found in this databases\n"
				
				
			continue
	      except IOError:	
		      print "invalid syntax\n"
		      continue
	     #-----------------> select data from table--------------->	

	    if str2:	
		reg2=re.search(r'(select from .*)',str2,re.I|re.M)
		try:
			if reg2:
			  	use=str(reg2.group())
		  		l3=use.split()
		  		us=str(l3[2])
		  		table_name=us.strip(';')
				s2="/home/asm/databases/"+str(database_name)+"/"+str(table_name)+"/"	
				f1=open(os.path.join(s2,"dat.txt"),'r')
				my_list1=pickle.load(f1)
				if my_list1=="":
					print "empty table data\n"
					
				else:   
					print "\n"
					print "+---------------------+"
					for i in my_list1:
						print "|{:21}|".format(i)
					print "+---------------------+"
				f1.close()
				
		except IOError:			
			print "no table data found\n"
			continue

	     #------------------> insert into table ------------>
	
	    if str2:
		  #print str2
		  reg2=re.search(r'(insert into .*)',str2,re.I|re.M)
		  try:
			  if reg2:
				use=str(reg2.group())
		  		l3=use.split()
		  		us=str(l3[2])
		  		table_name=us.strip(';')
				#print reg1
				s1="/home/asm/databases/"+str(database_name)+"/"+str(table_name)+"/"
				#print s1
				f=open(os.path.join(s1,"dat.txt"),'w')
				ele=input("how many element u have to insert into database\n")
				for i in range(ele):
					data=raw_input("enter data\n")
					list1.append(data)
				pickle.dump(list1,f)
				f.close()
				continue
	   	  except IOError:	  	
			
				print "invalid syntax found\n"
				continue
		
	     #-------------create table------------------------->
	
	    if str2:
			reg1=re.search(r'(create table.*)',str2,re.I|re.M)
			if reg1:
				tbname=str(reg1.group())		
				l2=tbname.split() 	
				tb=str(l2[2])
				table_name=tb.strip(';')
				#print "table created successfully----- ",table_name
				s1="/home/asm/databases/"+str(database_name)+"/"+str(table_name)
				try:				
					if not os.path.exists(s1):
						table_name=os.makedirs(s1)
						print "table  created successfully ---- ",table_name
						continue
				except IOError:	
					print "already same table is there\n"
				 	continue


	    if str2:
			reg1=re.search(r'(drop from .*)',str2,re.I|re.M)
			if reg1:
				tbname=str(reg1.group())		
				l2=tbname.split() 	
				tb=str(l2[2])
				table_name=tb.strip(';')
				#print "table created successfully----- ",table_name
				s1="/home/asm/databases/"+str(database_name)+"/"+str(table_name)
				try:				
					if os.path.isdir(s1):
						table_name=shutil.rmtree(s1)
						print "table  deleted successfully ---- ",table_name
						continue
				except IOError:	
					print "already same table is there\n"
				 	continue	



	    if str2:
			reg1=re.search(r'(exit.*)',str2,re.I|re.M)
			if reg1:
				print "exit from database"
				break




				
#--------------------------------------> create databases------------------------>
					
   if str1:
			reg1=re.search(r'(create database.*)',str1,re.I|re.M)
			if reg1:
				tbname=str(reg1.group())		
				l2=tbname.split() 	
				tb=str(l2[2])
				database_name=tb.strip(';')
				print list_db
				#print "table created successfully----- ",tb
				s1="/home/asm/databases/"+str(database_name)+"/"
				if not os.path.exists(s1):
					new_database=os.makedirs(s1)
					print "database created successfully---- ",database_name
				else:
					print "already same table is there\n"

				
#------------------------------------>drop database-------------------------------->				
		
   if str1:
	reg1=re.search(r'(drop database .*)',str1,re.I|re.M)
	if reg1:
			tbname=str(reg1.group())		
			l2=tbname.split() 	
			tb=str(l2[2])
			del_db=tb.strip(';')

			#print "table created successfully----- ",table_name
			s1="/home/asm/databases/"+str(del_db)
			try:				
				if os.path.isdir(s1):
					table_name=shutil.rmtree(s1)
					print "table  deleted successfully ---- ",del_db
					continue
			except IOError:	
				print "already same table is there\n"
				








