Worker1_data = ["John", 25, True]
print("Name= " + Worker1_data[0])
print("Male= " + str(Worker1_data[2]))
# Needs conversion into string

print(Worker1_data[0:2])

Worker1_data[1]= "Mike"
print(Worker1_data[1])

list1 = [1,2,3]
list2 = [4,5,6]
print(list1.extend(list2))
# Outpuuts None, the extend doesn't return a value, it adds to the list

list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1)
list1.append("new_element")
print(list1)
list1.insert(3, "new_element")
print(list1)
print(list1.count("new_element"))
list1.remove("new_element")
print(list1)
list1.pop()
print(list1)
print(list1.index(5))
list1.sort()
print(list1)

# Outputs the new list1, it's saved and updated

list3 = list2
print(list3)
