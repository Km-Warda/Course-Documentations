num = input("Divide 10 by number: ")

try:
    result = 10 / int(num)
    print(result)
except:
    print("You can't divide by zero")