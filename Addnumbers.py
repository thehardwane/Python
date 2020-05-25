x=2
y=3.5
sum=x+y
print('sum is {0}'.format(type(sum)))

print('a{}'.format(type(sum)))

string='abcdef'
name='Din esh'
x=(1,2,3)
print(f'tuple {x}')
re=100/777
print('revese string is {0} \nsum is {1} \nlength is {2}\n Upper case {3}'.format(string[4:1:-1],sum,len(string),string[1]))
print('Split {0}'.format(name.split()))
print("result {r:1.4f}".format(r=re))
my_list=[1,'abc',3.4,1,'abc']
my_dict={'a':1,'b':3}

print('list is {0} \ndict is {1} \nset is {2} \nset is {3}'.format(my_list,my_dict,set(my_list),set(my_dict)))

f = open("myfile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f=open('myfile.txt','r')
print(f.read())