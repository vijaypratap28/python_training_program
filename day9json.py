import json
my_list = [1,2,3,4,5]
my_dict = {'name':'vijay'}
my_str = 'asm tech'
f = open('test.txt', 'w')
print json.dumps(my_list, f)
json.dump(my_dict, f)

f.close()
