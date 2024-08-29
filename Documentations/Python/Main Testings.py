var = "John"
print("This is " + var + " and says hello")
print("This is ".upper() + var.upper() + " and says hello".upper())
print("var".upper().isupper())
print(len(var))
print("##############")

var = "This is John"
print(var.index("J"))
print(var.index("is"))
print(var.index("This"))
print(var.replace ("John", "Mark"))

print(abs(-5))

from math import *
print(floor(3.9))
print(sqrt(9))
name = input("Enter Your name ")
print(name)