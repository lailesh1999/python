"""----------------------------------------------------------------------------------
file_lines.py
There is a file with several text messages. Each message is in its own line. Write a Python program to count the number of lines in the file and the total number of words contained in those messages. Assume the messages contain only alphabets, and numbers.

Regno: 2117031
02/04/2022

---------------------------------------------------------------------------------"""
file = open('text.txt','r')
content = file.readlines()
number_of_lines = len(content)
word_length = 0

for line in content:
    word_length +=len(line.split(' '))
print(f"The number of lines are : {number_of_lines}")
print(f"The number of words in the file are : {word_length}")

