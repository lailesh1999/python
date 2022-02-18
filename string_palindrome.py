str = input("Enter the string ")
str_rev=""
count = len(str)
while count > 0:
     count = count - 1
     str_rev = str_rev + str[count]
print(str_rev)
if str == str_rev:
    print("String is a palindrome")
else:
    print("String is not palindrome")
