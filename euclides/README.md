    M = int(input("Input the greatest number: "))
    N = int(input("Input another number "))
    #modulo
    R = M % N
    #itererar oändligt tills R = 0
    while True:
        if R == 0:
            break
        else:
            temp = R
            R = N % R
            N = temp
    print("Greates common denomenator is: ", N)