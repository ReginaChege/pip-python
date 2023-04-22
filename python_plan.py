
# Given a Python list, write a program to remove all occurrences of item 20.
List1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in List1:
    List1.remove(20)
    print(List1)


#  Reverse a list in Python
List1 = [5, 20, 15, 20, 25, 50, 20]
List1.reverse()
print(List1)


# Write a program to remove the item present at index 4 and add it 
# to the 2nd position and at the end of the list.
list1 = [54, 44, 27, 79, 91, 41]
print(list1.pop(-2))
print(list1.insert(2,30))
print(list1)

# Tuple
# Copy specific elements from one tuple to a new tuple
names = ("Regina","Wairimu","Chege","is","a","student")
names2=names[2:5]
print(names2)

# Counts the number of occurrences of item 50 from a tuple
names = ("Regina","Wairimu","Chege","Chege","is","a","student")
print(names.count("Chege"))

#  Access value 20 from the tuple
ages=(12,56,90,20,89,67,56,54,23,24)
print(ages[3:4])

# set
# Return a new set of identical items from two sets
kitchen={"knife","spoon","coster","soup","desert","wine"}
kitchen2={"pan","water","bottle","fruits"}
kitchen.update(kitchen2)
print(kitchen)

# Return a new set of identical items from two sets
kitchen={"knife","spoon","coster","soup","desert","wine"}
kitchen2={"desert","water","coster","fruits"}
print(kitchen.intersection(kitchen2))

#  Update the first set with items that don’t exist in the second set
kitchen={"knife","spoon","coster","soup","desert","wine"}
kitchen2={"desert","water","coster","fruits"}
print(kitchen.difference_update(kitchen2))


def odd():
    n=1
    sum=0
    while(n>=100):
        if(n%2==0):
            print(f"{n} is divisible by 2")
        else:
            print(f"{n} is not divisible by 2")    
odd()

# Write a Python function that takes a list of integers as input and returns the product of all the
#  numbers in the list
def list_integer(numberss):
    product=1
    for n in numberss:
        product*=n
    return product
numberss=[1,2,3,4,5,6,7,8,9,10]
result = list_integer(numberss)
print(result)

 
# Write a Python program that takes a list of strings as input and returns
#  the longest string in the list.
def longString(names):
    empty=""
    for s in names:
        if len(s)> len(empty):
            empty=s
    return empty

names=['Regina','Gisemba','Annete']
output=longString(names)
print(output)
        

        
            
#  Write a Python function that takes a list of strings as input 
# and returns a new list of the strings sorted alphabetically.
def different(classes):
     return sorted(classes)

classes = ["Hopper","AnatiB","Ada"]
stringSorted = different(classes)
print(stringSorted)


# Write a Python function that takes a string as input and returns a list
#  of all the words in the string that have more than three letters.
def long_words(string):
    words=string.split
    long_words=[]
    for word in string:
        if len(word)>3:
            long_words.append(word)
            return long_words

string="The begining is always today"
output=long_words(string)
print(output)





    
    











