# to generate prime no till input no!
def primeno(a):
	for num in range(2,a+1):
        	if all(num%i!=0 for i in range(2,num)):
                        
                    print num
                        
num = int(raw_input('enter a number:'))                	
a = primeno(num)

