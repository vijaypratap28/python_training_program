import json
my_dict = {'name':'vijay', 'company':'asm', 'pack':['python', 'ajs', 'html']}
print json.dumps(my_dict, indent = 12)
print json.dumps(my_dict, indent = 12, sort_keys = True)
