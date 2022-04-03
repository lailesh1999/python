"""----------------------------------------------------------------------------------
customer_database.py
Write a python program to add few customer details into the database and retrieve the information and print in systematic manner

Regno: 2117031
03/04/2022

---------------------------------------------------------------------------------"""
import sqlite3 as s

conn = s.connect('customer.db')
cursor = conn.cursor()

cursor.execute("create table if not exists customer(id integer primary key NOT NULL ,"
               "name text NOT NULL,address text NOT NULL,salary integer NOT NULL) ")

def insertion():
    id = int(input("ENTER CUSTOMER ID:"))
    name = input("ENTER THE NAME:")
    address = input("ENTER ADDRESS:")
    salary = int(input("ENTER THE SALARY:"))
    if cursor.execute("insert into customer values(?,?,?,?)",(id,name,address,salary)):
        print("DATA INSERTED")
    else:
        print("NOT INSERTED DATA")

def display():
    cursor.execute("select * from customer")
    data = cursor.fetchall()
    print("=============================================")
    print("ID \t\t NAME\t\t ADDRESS\t\t SALARY")
    print("=============================================")
    for row in data:
        print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t\t{row[3]}")

while True:
    print("1)INSERT DATA 2) DISPLAY DATA 3)COMMIT DATA 4)EXIT")
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
        print("INVALID CHOICE")


