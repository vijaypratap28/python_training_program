#calculate average of list of integer using definition!
def average(*a):

	b = sum(*a)
	length = len(*a)
	avrg = float(b/length)
	return avrg	
	
a = average([1,2,3,4,5,6,7,8,12,34,56,78,90])
print a

