#get multiline text as input and change the case of text

list = []


while True:
	line = raw_input('enter the multiline text and after write "EOF" to show results')
	list.append(line) 
	if line == 'EOF':
		break

print list
new_list = [line.swapcase() for line in list ]
print new_list


#


