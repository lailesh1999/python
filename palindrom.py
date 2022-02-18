number = int(input("Enter the number to check number is palindrome or not"))
temp = number
rev = 0
while temp>0:
    rem = temp % 10
    rev = rev * 10 + rem
    temp = temp//10
print(rev)
if number == rev:
    print("number is plaindrome")
else:
    print("Number is not palindrome")