# In Python, a list is a collection data type that is ordered and mutable. It allows you to store multiple items in a single variable. Lists can contain items of different data types, and you can modify them after creation (e.g., by adding, removing, or changing elements). Lists are defined by placing elements inside square brackets [], separated by commas.


my_list = [2,3,4,5,6,7,8]
print(my_list)

my_list.append(10)
print(my_list)

my_list.insert(3,"Hello")
print(my_list)

my_list.remove(6)
print(my_list)

my_list.pop()
print(my_list)

length = len(my_list)
print(length)

Slice = my_list[1:5]
print(Slice)