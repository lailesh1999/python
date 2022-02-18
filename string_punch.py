a = input("enter the string ")
d=""
punctuation = "!()-[]{};:''`\,<>./?@$%^&*-~"
for i in a:
    if i not in  punctuation:
        d = d + i
print(d)












