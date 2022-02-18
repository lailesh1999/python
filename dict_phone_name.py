n = int(input("ENTER THE NO OF PEOPLE"))

dict = {}

for i in range(n):
    keys = input("ENTER THE NAME:")
    values = int(input("ENTER PHONE NUMBER"))
    dict[keys]= values
for i in dict:
    print(i,end=':')
    print(dict[i])
