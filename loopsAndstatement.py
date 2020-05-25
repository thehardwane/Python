num=[1,2,3,4,5,6,7,8,9,10]
constant=1

for x in num:
    constant= x*constant
    #print('{}'.format(constant))

print('{}'.format(constant))

#nested loop

mylist=[ ]
for x in[1,2,3]:
    for y in[200,300,100]:
        mylist.append(x*y)
       
 
print('list {}'.format(mylist))
