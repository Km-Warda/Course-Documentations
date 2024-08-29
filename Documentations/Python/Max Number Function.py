def max_num(N1,N2,N3):
    if N1 >= N2 and N1 >= N3:
        return N1
    elif N2 >= N1 and N2 >= N3:
        return N2
    else:
        return N3
    
List1 = [1, 2, 3]
print("Enter your 3 Numbers")
List1[0] = input("First Number = ")
List1[1] = input("Second Number = ")
List1[2] = input("Third Number = ")
print("Biggest Number is " + str(max_num(List1[0],List1[1],List1[2])))
