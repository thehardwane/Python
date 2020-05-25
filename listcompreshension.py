#list comprehension
mylist=[num**3 for num in range(1,10,2)]
print(f'list {mylist}')

#list comprehension using if 
mylist=[num**2 for num in range(1,10) if num%2 ==0]
print(f'list {mylist}')

#list comprehension using if else
mylist=[num if num%2==0 else'odd' for num in range(1,10) ]
print(f'list {mylist}')

#list comprehension using nested loops
mylist=[num*num1 for num in [1,2,3] for num1 in [10,20,30]]
print(f'list {mylist}')

