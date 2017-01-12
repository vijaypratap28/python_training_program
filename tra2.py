#to print pattern!

var = '*'
value = int(raw_input('enter range'))
for i in range(value):
	print 'the pattern is :',var * i


# the code will display the key, value and key-value pair!
my_dict = {'name':'vijay','company':'ASM','job':'SE'}
print 'list in the dict :',my_dict.keys()
print 'values in the dict',my_dict.values()
print my_dict.items()


#access value from the dictionary using key! and assign value in the dictionary1

print my_dict['company']
my_dict['addresss'] = 'richmond circle'
print my_dict

# dispaly second largest element from the list!

list = [1,2,4,6,7,13,16]
print list
list.sort()
print list[-2]

#operation on string1
str = 'my name is vijay'
print 'element in your list is :',str
print 'display in upper case:',str.upper()
print 'display in lower case:',str.lower()
print str.swapcase()
print str.title()

#used split and join function

mystr = str.split(" ")
print mystr
mystr.append(500)
print mystr
#used while loop and if loop
value = raw_input('enter text:')
list1 = []
while True:
	list1.append(value)
	if 'EOF':
		break
print list1
#  all arithmatic operation using if , elif and else loop!

a = int(raw_input('enter first number:'))
b = int(raw_input('enter second number:'))

value = raw_input('enter the arithmatic operation which you want to perform:(+,-.*,/,%,//)')
if value == '+':
	print a+b
elif value == '-':
	print a-b
elif value == '*':
	print a*b
elif value == '/':
	print a/b
elif value == '%':
	print a%b
elif value == '//':
	print a//b
else:
	print "wrong input!"
