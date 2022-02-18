print("***********OUTPUT*********")

print("prime numbers from range 1 to 100 : ")
for i in range(2,100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i,end =" ")
print("\n")


print(" \n***********OUTPUT********* \n")
print(" perfect numbers from 1 to 100 :")
for perfect in range(1,100):
    sum = 0
    for l in range(1,perfect):
        if(perfect % l == 0):
            sum = sum + l
    if (sum == perfect):
        print(sum,end =" ")










