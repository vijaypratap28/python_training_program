import calendar

#taking input from user and print the value called intractive python
value = raw_input()
print value
#string datatype and print word in string
str = 'ram is a good boy!'
for i in value:
	print i
#indexing string
str = '123456789'
print str[0:5]
tuple = (1,2,3,4,5,6,7,8)
print tuple
print tuple[2:-3]
list = ['january','february','march','april','may','june','july','august','september','october','november','december']
value = int(raw_input('enter number between 1 to 4:='))
end = value*3
start = end-3
print list[start:end]
dict = {'name':'ram','address':'bangalore'}
print dict
print dict['address']
for k, v in dict.iteritems():
    print k, v
print dict.keys()
##print dict.iteritems()
print dict.values()
list = [1,2,3,4,5,6,7,8,9]
print list
list.append('w')
print "after append your final list is:",list
list.insert(2,320)
print "after insert your final list is:",list
for number in list:
	print number
#swapping two number
a = 10
b = 20
a,b = b,a
print a
print b
#swapping complete
#last name will be print
name = 'ram'
name = 123
name = 123333.98
print name
days_in_month={'january':(1,2,3),'february':28,'march':31,'april':30,'may':31,'june':30,'july':31,'august':31,'september':30,'october':31,'november':30,'december':31}
print days_in_month['january']






cal = calendar.month(2008, 1)
print "Here is the calendar:"
print cal
print days_in_month.keys()
print days_in_month.values()

for key, value in days_in_month.iteritems():
    print key, value


list = [1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i']
print list
del list[1:9]
print list




dict = {'number':(1,2,3,4,5),'name':'vijay'}
print dict['number'].index(4)



