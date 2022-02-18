num  = int(input("Enter the  umber to check the prime"))
flag=0
a =[]
for i in range(2,int(num/2)):
    if num % i == 0:
        flag = 1
if flag == 1:
    print(" not prime")
else:
    print(" prime number")
num1  = int(input("Enter the  umber to check the perfect"))
sum = 0
for k in range(1,num1):
    if(num1 % k == 0):

        sum = sum + k
if num == sum:
    print("number perfect")
else:
    print("number is not perfect")




