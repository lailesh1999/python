string1 = input("Enter the string")
sub_string = input("Enter the sub string to check number of occurance")

def count_sub(string2,sub_string1):
    count = 0
    for i in range(len(string2)):
        if(string2[i:i+len(sub_string1)] == sub_string1):
            count = count + 1
    return  count

print("NUMBER OF OCCURANCE OF SUB STRING",count_sub(string1,sub_string))