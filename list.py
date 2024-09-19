# LAST LOVE 
my_list = []
n=int(input('Enter the no of elements in the lists'))
print(f'Enter the {n} of elements in the lists')
while n:
    my_list.append(input())
    n=n-1
print(my_list)
print(type(my_list))
#to find the length of list use len()
print(len(my_list)
#convertig list into another
n=tuple(my_list)
print(type(my_list))
print(n)
m=set(my_list)
print(type(my_list))
print(m)
o=list(my_list)
print(type(my_list))
print(o)
# creating list by using list() constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)




# 

# for accesing elements 
print(my_list[1])
print(my_list[-1])


# for accesing elements  in bettem the given index

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

# checking if the element is there or not
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# change the value inside the list
thislist[1] = "blackcurrant"
print(thislist)

# in beween
thislist[1:4] = ["blackcurrant", "watermelon","madhu"]

print(thislist)

# changhe and insert at the same time
thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)

#change and delete 
thislist[1:3] = ["watermelon"]
print(thislist)
# pop defaultly removes last item
thislist.pop()
print(thislist)


#insert by using index 
thislist.insert(2, "watermelon")
print(thislist)

# to insert the elements in to th list from another list 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# can extend any type like tuple set and dict 
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# to remove the elements from list
thislist.remove("banana")
print(thislist)


# to remove from specified index
thislist.pop(1)
print(thislist)

# del do same as deletion by index
del thislist[0]
print(thislist)

# to delete entire list 
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) # gives an eroor as there no list exits


# to clear the elememnts in the list 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# to print the elements one by one 
thislist = ["apple", "banana", "cherry"] # by list items 
for x in thislist:
  print(x)



thislist = ["apple", "banana", "cherry"] # same as while loop
for i in range(len(thislist)):
  print(thislist[i])   # by index


#A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

ruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

#you want a new list, containing only the fruits with the letter "a" in the name.
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# same in one line 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# gets the value if it is true

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)


# to set the all elemnts into upper cases
newlist = [x.upper() for x in fruits]
print(newlist)


# sort the list
thislist.sort()
print(thislist)
# sort the list reverse 
thislist.sort(reverse = True)
print(thislist)


#You can also customize your own function by using the keyword argument key = function.

#The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)


# capitals a4re sorted first
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#small are sorted first

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# to get reverse order
thislist.reverse()
print(thislist)


# to copy the list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# cop[y the list by using copy keyword
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# coping by using slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
