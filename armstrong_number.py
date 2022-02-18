number = int(input("Enter the number to check armstrong number "))
sum =0
temp=number
times = len(str(number))
while temp > 0:
    rem = temp % 10
    sum = rem ** times + sum
    temp = temp//10


print(sum)
if sum == number:
    print("Armstrong number")
else:
    print("not armstrong number ")
