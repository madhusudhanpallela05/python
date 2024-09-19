my_list = []
n=int(input('Enter the no of elements in the lists'))
print(f'Enter the {n} of elements in the lists')
while n:
    my_list.append(input())
    n=n-1
print(my_list)
n=tuple(my_list)
print(n)
m=set(my_list)
print(m)
