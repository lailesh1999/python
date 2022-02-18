limit = int(input("Enter the limit to display odd and even number"))
even =[]
odd =[]
for i in range(2,limit):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("EVEN NUMBER")
print(even)
print("ODD NUMBERS")
print(odd)
