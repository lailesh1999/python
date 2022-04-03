"""----------------------------------------------------------------------------------
student_database.py
Write a python application to generate student report card enter all the details of the student required. Calculate the marks, average,and resuls, then update the information accordingly.

---------------------------------------------------------------------------------"""
import sqlite3 as s
conn = s.connect('student.db')

cursor = conn.cursor()
cursor.execute(
    '''create table if not exists student(id integer primary key,name text,mark1 integer,mark2 integer,
    mark3 integer,total integer ,average real,result text)''')


def insertion():
    id = int(input("Enter the student id"))
    name = input("Enter the name")
    mark1 = int(input("Enter the 1st Mark"))
    mark2 = int(input("Enter the 2nd Mark"))
    mark3 = int(input("Enter the 3rd Mark"))
    total = mark1 + mark2 + mark3
    average = round(total / 3, 2)
    result = None
    if mark1 < 35 or mark2 < 35 or mark3 < 35:
        result = "failed"
    elif average >= 90:
        result = "Distinction"
    elif average >= 70:
        result = "First"
    elif average >= 50:
        result = "Second"
    elif  average >= 35:
        result = "Passed"

    if cursor.execute("insert into student values(?,?,?,?,?,?,?,?)",(id,name,mark1,mark2,mark3,total,average,result)):
        print("DATA INSERTED")
    else:
        print("NOT INSERTED DATA")
def display():
    id = int(input("ENTER THE STUDENT ID TO DISPLAY RECORDS"))
    try:
            cursor.execute(f"select * from student where id = {id}")
            data = cursor.fetchone()
            print(f"{data[1]} Report Card")
            print(f"Register Number: \t {data[0]}")
            print(f"Name: \t {data[1]}")
            print(f"Mark 1: \t {data[2]}")
            print(f"Mark 2: \t {data[3]}")
            print(f"Mark 3: \t {data[4]}")
            print(f"Total: \t {data[5]}")
            print(f"Average: \t {data[6]}")
            print(f"Result: \t {data[7]}")
    except TypeError:
        print("STUDENT DATA IS NOT FOUND ")

while True:

    print("1)INSERT DATA\t 2) DISPLAY DATA 3)COMMIT DATA 4) EXIT")
    c = int(input("ENTER YOUR CHOICE:"))
    if c == 1:
        insertion()
    elif c == 2:
        display()
    elif c == 3:
        conn.commit()
    elif c == 4:
        exit()
    else:
        print("WRONG CHOICE")

