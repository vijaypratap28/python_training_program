#  created by Vijay pratap singh
#  Created Date 18-01-2017
#  A Python script to compare the attached two files and find out status 'ok' and 'FAIL'.
#  The filenames should be passed via command line inputs only. 



import sys
import re

class compare:
	def __init__(self):
		argument1 = sys.argv[1]
		argument2 = sys.argv[2]

		with open(argument1,'r')as first_file, open(argument2,'r')as second_file:
			source = first_file.readlines()
			counter1 = 0
			print "******************************"
			for line in source:
				matching_words = re.match('tempest', line)
		
		
				if matching_words:
			
					counter1 += 1
			print "Total number of lines starting with 'tempest' in first  file :",counter1
	

			destination = second_file.readlines()
			counter2 = 0
			print "******************************"
			for lines in destination:
				matchingwords1 = re.match('tempest', lines)
		
				if matchingwords1:
			
					counter2 +=1
			print "Total number of lines starting with 'tempest' in second  file :",counter2



			#dict1 = []
           		#dict2 = []
			#for i in source:
			#	dict1.append(i)
			#print dict1
			#for j in destination:
			#	dict2.append(j)



comparefile = compare()









