## Numbers Operations 
`print(10 + 3)` Adding
`print(10 - 3)` Subtracting 
`print(10 * 3)` Multiplying
`print(10 / 3)` Division
`print(10 % 3)` Modules "Spits out the reminder of a division" 
`pow(5,2)` Raises a number to a power
`abs(-5)` Gives the absolute value
## Defining Variables
```
var = "John"
print("This is " + var + " and says hello")
```
## Inputs from user
```
name= input("Enter Your name ")
```
## Lists And Tuples
- Lists are for storying different entries, and can be edited with functions or giving different entries.
```
Worker1_data = ["John", 25, True]
print("Name= " + Worker1_data[0])

print("Male= " + str(Worker1_data[2]))
>> Name= John
>> Male= True

print(Worker1_data[0:2])
>> ['John', 25]

Worker1_data[1]= "Mike"
print(Worker1_data[1])
>> Mike
```

- Tuples are like lists but are immutable "not editable", mainly for data that won't be changed.
```
tuble = ("element one", "element two", "element three")
coordinates = (42,15,26)
```
- We can create a list of tubles
```
coordinates = [(42,15,26), (13,2,8)]
```
## Dictionaries
- Dictionaries are used for storing key-value pairs
- We can get the value of the key by the function `get()`
```
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    4: "April"
}
  
print(monthConversions.get("Jan"))
```
- We can create a default value for the `get()` functions to be outputted if no value was found to the key.
```
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    4: "April"
}

var = Luv
print(monthConversions.get(var, "Not a valid Key"))
```
## Defining & Calling Functions
- Basic function defining and calling
```
def Hello_function():
	print("Hello")

Hello_function()
```
- Passing a parameter
```
def Hello_function(name, last_name):
	print("Hello " + name + " " + last_name)

Hello_function("Adam", "White")
```
- Return statement
```
def cube(num):
	return num*num*num
print(cube(3))
```
***Note:*** `return` breaks the function, and no code after it will be interpreted under the function.
## If Statements
- `if` statements runs the code if the condition set is true, and `else` runs the code if it's false.
```
if key:
	print("Key is True")
else:
	print("Key is false")
```
- We can use logical operators such as `and`, `or`, `and not` , etc..
```
if key1 and key2:
	print("Both keys are True")
else:
	print("Not Both Keys are false")
```
- We can use `eleif` for giving additional conditions
```
if key1 and key2:
	print("Both keys are True")
elif key1 and not(key2):
	print("Only key1 is True")
elif not(key1) and key2:
	print("Only key2 is True")
else:
	print("Both Keys aren't true")
```
- We can use operators that results in a True or False output, such as `>=`, `==`, or `!=`  in the if statement
```
if num1 >= num2
	print("numbuer 1 > number 2")
```
## While Loop
- `while` keeps running the code in a loop while the given condition is `True`.
```
i = 1
while i <= 5:
    print("Code Runned "+ str(i) + " times")
    i += 1

# The Code will run 5 times, printing 5 lines
```
## For Loops
- `for` loops over the code for each element of an entry, such as elements in lists or letters in strings 
```
for letter in "Long Word":
	print(letter)

list = [1,2,3]
for number in list:
	print(number)
for element in list:
	print(element)
```
***Note:*** The variable `letter` & `number` stated above can be changed to any variable, these aren't static values.
- We can use the function `range()` to specify a range of values
```
for num in range(10):
	print(num)
for num in range(6, 10):
	print(num)
```

## Python Functions
###### len()
Shows number of characters
```
len(var) 
```

###### upper() & lower()
Converts text characters into lower & upper case  
```
print("This is ".upper() + var.upper())
```

###### isupper() & islower()
Checks if the characters are lower or upper case and return a bool value
```
print(var.isupper())
```

###### index()
Can be given a parameter to refer to the index of its first appearance, can be given one character or words
```
var = "This is John"
print(var.index("J"))
>> 8
print(var.index("This"))
>> 0
print(var.index("is"))
>> 2 
### NOT 4 because it appeared first in "This"
```

###### replace()
Can be given two parameters to replace a character with another
```
var = "This is John"
print(var.replace ("John", "Mark"))
```

###### str()
Converts a number type variable into string type
```
num = 5
print(str(num) + "is an odd number")
```
***Note:*** to use the `+` operation when dealing with strings, we need to convert the number into a string, meaning `print(num + "is an odd number")` gives an error.

###### int()
Converts a string type variable into integers and numbers type
```
print(int(13))
```

###### float()
Converts a string type variable into numbers type
```
print(float(13))
```

###### max() & min
Shows the maximum and minimum number of the given values
```
print(max(5,3))
print(min(5,3))
```
###### round()
Rounds a number to nearest possible integer
```
print(round(3.7))
>> 4
```

#### Math Functions
Import the math functions by:
```
from math import *
```

###### floor()
Rounds a number to smallest integer "removes decimal points"
```
print(floor(3.7))
>> 3 
```

###### ceil()
Rounds a number to the bigger integer no matter what
```
print(ceil(3.2))
>> 4 
```

###### sqrt()
Gives a square root of a number 
```
print(sqrt(9))
```

### Lists Functions
###### extend()
Adds two lists elements together.
```
list1.extend(list2)
print(list1)
```

###### append()
Adds an element to the list.
```
list1.append("new_element")
print(list1)
```

###### insert()
Adds an element to the given index and pushes existing elements after it.
```
list1.insert(3, "new_element")
print(list1)
```

###### remove()
Removes first occurrence of a given element
```
list1.remove("new_element")
print(list1)
```

###### clear()
Removes all the elements from the list.
```
list1.clear()
print(list1)
```

###### pop()
Drops the last element from the list
```
list1.pop()
print(list1)
```

###### index()
Locates the index of an element in a list
```
print(list1.index("element"))
```

###### count()
Counts how many times an element reoccur in a list
```
print(list1.count("element"))
```

###### sort()
Sorts a list in ascending order (alphabetical or numerical).
```
list1.sort()
print(list1)
```
##### reverse()
Sorts a list in descending order (alphabetical or numerical).
```
list1.reverse()
print(list1)
```

