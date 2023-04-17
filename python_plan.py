
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












