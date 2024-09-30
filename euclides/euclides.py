M = int(input("Ange det största nummret: "))
N = int(input("Ange det andra nummret: "))
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
print("Minsta gemensamma nämnare är: ", N)