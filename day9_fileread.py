import pickle
f = open(myfile.txt, 'r')

my_list = pickle.load(f)
my_dict = pickle.load(f) 
print my_list
print my_dict
f.close()
