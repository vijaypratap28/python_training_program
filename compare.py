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
				#print lines
		
				if matchingwords1:
			
					counter2 +=1
					#print matchingwords1
			print "Total number of lines starting with 'tempest' in second  file :",counter2



			
           		dict1 = {}
			for i in source:
				if i.find('tempest') == 0:
					key1 = i[:i.find('...')]
					value1 = i[i.find('...'):]
					dict1[key1] = value1
					for keys in key1:
						pass#print keys
					for values in value1:
						pass#print values
					#print dict1.items()
					#print dict1.keys()
					#print dict1.values()
			
			

			dict2 = {}
			for j in destination:
				if j.find('tempest') == 0:
					key2 = j[:j.find('...')]
					value2 = j[j.find('...'):]
					dict2[key2] = value2
					for key in key2:
						pass#print key
					for value in value2:
						print value
						#print dict1.items()
					#print dict1.keys()
					print dict2.values()
			
			
			



comparefile = compare()









