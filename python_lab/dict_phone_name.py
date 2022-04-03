'''----------------------------------------------------------------------------------
dict_phone_name.py
Write a Python program to input 'n' names and phone numbers to store it a dictionary
and print the phone number of a particular name

Regno: 2117031
04/02/2022

--------------------------------------------------------------------------------- '''

n = int(input("ENTER THE NO OF PEOPLE:"))
dict = {}
for i in range(n):
    keys = input("ENTER THE NAME:")
    values = int(input("ENTER PHONE NUMBER:"))
    dict[keys]= values

for i in dict:
    print(i,end=':')
    print(dict[i])

flag = 0
name = input("ENTER THE NAME TO FIND PHONE NUMBER:")
for key in dict:
    if name in key:
        print(f"PHONE NUMBER OF {name} = {dict[key]}")
        flag = 1
if flag == 0:
    print("NAME IS NOT FOUND")