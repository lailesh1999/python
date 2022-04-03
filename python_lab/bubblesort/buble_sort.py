'''----------------------------------------------------------------------------------
buble_sort.py
Write a Python program to sort the elements in the array using bubble sort technique and display the elements in descending order

Regno: 2117031
021/02/2022

--------------------------------------------------------------------------------- '''
import module_sort

n =int(input("Enter the size of an array"))
a = []
for i in range(0,n):
    ele = int(input("ENTER THE ELEMENT"))
    a.append(ele)
module_sort.bubble_sort(a)
print(a)


