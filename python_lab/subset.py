'''----------------------------------------------------------------------------------
subset.py
Write a python program to check whether the given is subset of a set or a super set of a set

Regno: 2117031
03/04/2022

--------------------------------------------------------------------------------- '''

set1 = set()
set2 = set()

num_char = int(input("ENTER THE NUMBER OF CHARACTER IN SET 1 :"))
for i in range(num_char):
        ele = input(f"ENTER CHARACTER {i+1}:")
        set1.add(ele)

num_char = int(input("ENTER THE NUMBER OF CHARACTER IN SET 2 :"))
for i in range(num_char):
        ele = input(f"ENTER CHARACTER {i+1}:")
        set2.add(ele)

print(f"SET 1 ={set1}")
print(f"SET 2 ={set2}")

if set1.issubset(set2):
    print("SET1 IS SUBSET OF SET2")
else:
    print("SET1 IS NOT SUBSET OF SET2")

if set1.issuperset(set2):
    print("SET1 IS SUPERSET OF SET2")
else:
    print("SET1 IS NOT SUPERSET SET2")