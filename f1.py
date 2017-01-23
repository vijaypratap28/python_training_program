#  created by Vijay pratap singh
#  Created Date 18-01-2017
#  A Python script to compare the attached two files and find out status 'ok' and 'FAIL'.
#  .Total number of lines starting with 'tempest' in first  file (Done)
#  .Total number of lines starting with 'tempest' in second  file (Done)
#  .Total number of lines 'tempest' to '...' matching status same  ( both are 'ok' or both are 'FAIL' ) (In Progress ...)
#  The filenames should be passed via command line inputs only. 



import sys
import re
argument1 = sys.argv[1]
argument2 = sys.argv[2]
class compare:
	def __init__(self):
		       	
    		
		with open(argument1,'r')as first_file, open(argument2,'r')as second_file:
			source = first_file.readlines()
			counter1 = 0
			list1 = []
			print "******************************"
			for line in source:
				matching_words = re.match('tempest', line)
				
		
				if matching_words:
					list1.append(line)
					counter1 += 1
			#for i in list1:		
				#print i		
			print "Total number of lines starting with 'tempest' in first  file :",counter1
	

			destination = second_file.readlines()
			counter2 = 0
			list2 = []
			print "******************************"
			for lines in destination:
				matchingwords1 = re.match('tempest', lines)
				#print lines
		
				if matchingwords1:
					list2.append(lines)			
					counter2 +=1
					#print matchingwords1
			print "Total number of lines starting with 'tempest' in second  file :",counter2
			first_dict1 = {}
			first_list1 = []
			for line in source: 
				store = re.search(r'(tempest.*)',line)
				if store:
					templine1 = str(store.group())
				  	line_split1 = templine1.split(' ... ')
				  	first_lines = line_split1[0]
				  	second_lines = line_split1[1]
			  
			  		line_strip1 = second_lines.strip('\r')
			  		first_dict1[first_lines]=line_strip1 			  
			  		first_list1.append(str(first_lines)+' ... '+str(line_strip1))
			first_dict2 = {}
			first_list2 = []
			for lines in destination:
				store1 = re.search(r'(tempest.*)', lines)
				if store1:
					templine2 = str(store1.group())
					line_split2 = templine2.split(' ... ')
					firstlined = line_split2[0]
					secondlined = line_split2[1]

					line_strip1 = second_lined.strip('\r')
			  		first_dict2[first_lined]=line_strip1 			  
			  		first_list2.append(str(first_lined)+' ... '+str(line_strip1))
			

			counter1 = 0
			file1 = open("same_staus.txt",'w+')
			for i in first_list1:
				for j in second_list2:
					if i==j:
						file1.writelines(i+'\n')
						counter += 1
			print "No of lines having status same:", counter1
			file1.close()



			counter22 = 0
			file2 = open("difference_status.txt",'w+')
			for key in first_dict1:
				for key1 in first_dict2:
					if (key==key1):
						if(first_dict1[key]!=first_dict2[key1]):
							file2.writelines(key+'\n')
							counter22 += 1
			print "No of lines having status difference",counter22
			file2.close()


			counter3 = 0
			counter4 = 0
			file3 = open("any_status.txt", 'w+')
			for key in first_dict1:
				if (first_dict1[key]!='ok')&(first_dict1[key]!='FAIL'):
					file3.writelines(key+'\n')
					counter3 += 1
			for key in first_dict2:
				if (first_dict2[key] != 'ok')&(first_dict2[key]!= 'FAIL'):
					file3.writelines(key+'\n')
					counter4 +=1

			print "No of lines having status anything:",counter3+counter4
			file3.close()



			counter5 = 0
			file4 = open("avail_in_first_not_in_second.txt",'w+')
			for key in first_dict1:
				if first_dict2.has_key(key):
					continue
				else:
					f.writelines(key+'\n')
					counter5 += 1
			print "No of lines available in source not in destination",counter5
			file4.close()
			

			
		
		


				
				
			  
			
		



comparefile = compare()


