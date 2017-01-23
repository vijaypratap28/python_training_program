import json
my_list = [1,2,3,4,5]
my_dict = {'name':'vijay'}
my_str = 'asm tech'
f = open('test.txt', 'r')
print json.loads(my_list, f)
json.load(my_dict, f)
print my_list
print my_dict
f.close()
