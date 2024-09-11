def expo(num,exp):
    result = 1
    for index in range(exp):
        result = result * num
    return result

print(expo(2,5))