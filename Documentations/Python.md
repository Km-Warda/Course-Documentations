## Defining Variables
```
var = "John"
print("This is " + var + " and says hello")
```
## Numbers Operations 
`print(10 + 3)` Adding
`print(10 - 3)` Subtracting 
`print(10 * 3)` Multiplying
`print(10 / 3)` Division
`print(10 % 3)` Modules "Spits out the reminder of a division" 
`pow(5,2)` Raises a number to a power
`abs(-5)` Gives the absolute value
## Inputs from user
```
name= input("Enter Your name ")
```
## Lists
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

## Functions
- len() 
	Shows number of characters
```
len(var) 
```

- upper() & lower()
	Converts text characters into lower & upper case  
```
print("This is ".upper() + var.upper())
```

- isupper() & islower()
	Checks if the characters are lower or upper case and return a bool value
```
print(var.isupper())
```

- index()
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

- replace()
	Can be given two parameters to replace a character with another
```
var = "This is John"
print(var.replace ("John", "Mark"))
```

- str()
	Converts a number type variable into string type
```
num = 5
print(str(num) + "is an odd number")
```
***Note:*** to use the `+` operation when dealing with strings, we need to convert the number into a string, meaning `print(num + "is an odd number")` gives an error.

- int()
	Converts a string type variable into integers and numbers type
```
print(int(13))
```

- float()
	Converts a string type variable into numbers type
```
print(float(13))
```

- max() & min
	 Shows the maximum and minimum number of the given values
```
print(max(5,3))
print(min(5,3))
```

- round()
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

- floor()
	Rounds a number to smallest integer "removes decimal points"
```
print(floor(3.7))
>> 3 
```

- ceil()
	Rounds a number to the bigger integer no matter what
```
print(ceil(3.2))
>> 4 
```

- sqrt()
	Gives a square root of a number 
```
print(sqrt(9))
```

### Lists Functions
- extend()
	Adds two lists elements together.
```
list1.extend(list2)
print(list1)
```

- append()
	Adds an element to the list.
```
list1.append("new_element")
print(list1)
```

- insert()
	Adds an element to the given index and pushes existing elements after it.
```
list1.insert(3, "new_element")
print(list1)
```

- remove()
	Removes first occurrence of a given element
```
list1.remove("new_element")
print(list1)
```

- clear()
	Removes all the elements from the list.
```
list1.clear()
print(list1)
```

- pop()
	Drops the last element from the list
```
list1.pop()
print(list1)
```

- Index()
	Locates the index of an element in a list
```
print(list1.index("element"))
```
