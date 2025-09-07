# Data structures: List
my_list = []
#Appending
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
# Inserting
my_list.insert(1,15)
print(my_list)
#Extending
my_list2 = [50,60,70]
my_list.extend(my_list2)
print(my_list)
#Removng 
my_list.remove(70)
print(my_list)
#Sorting
my_list.sort()
print(my_list)
#Indexing
print(my_list.index(30))
