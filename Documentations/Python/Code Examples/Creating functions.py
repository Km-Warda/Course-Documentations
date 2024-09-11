def Hello_function():
	print("Hello")

Hello_function()


def Hello_function(name, last_name):
	print("Hello " + name + " " + last_name)

Hello_function("Adam", "White")


def cube(num):
	return num*num*num

print(cube(3))
result = cube(3)
print("Result is " + str(result))