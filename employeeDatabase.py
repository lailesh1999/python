import sqlite3
from datetime import datetime as dd


class Employee:

    def getSSN(self):
        return self.SSN

    def getFirstName(self):
        return self.FirstName

    def getLastName(self):
        return self.LastName

    def setSSN(self):
        self.SSN = int(input("ENTER THE SSN "))

    def setFirstName(self):
        self.FirstName = input("ENTER THE FIRST NAME")

    def setLastName(self):
        self.LastName = input("ENTER THE SECOND NAME")


class HourlyEmployee(Employee):

    def getSalary(self):
        return self.salary

    def setSalary(self):
        self.salary = int(input("ENTER THE SALARY of hourly employee"))

    def HourlyEmployee(self):
        self.hours = int(input(" ENTER THE HOURS OF WORKING "))

    def GrossSalary(self):
        self.grossSalary = (self.salary * self.hours)
        return self.grossSalary

    def NetSalary(self):
        self.netSalary = self.grossSalary - 5000
        return self.netSalary


class SalariedEmployee1(Employee):

    # def __init__(self, sal=None):
    #     super().__init__()
    #     # self.Salary = sal

    def getSalary(self):
        return self.Salary

    def setSalary(self):
        self.Salary = int(input("ENTER THE SALARY"))

    def SalariedEmployee(self):
        self.days = int(input(" ENTER NUMBER OF DAYS PRESENT "))

    def GrossSalary(self):
        self.grossSalary = (self.Salary * self.days)
        return self.grossSalary

    def NetSalary(self):
        self.netSalary = self.grossSalary - 5000
        return self.netSalary


class displayDATA():
    def display(self):
        con = sqlite3.connect('emp.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM EMPLOYEE")
        res = cursor.fetchall()
        print("========================================================")
        print("SSN \t\t FIRST NAME \t \t LAST NAME \t\t SALARY")
        print("========================================================")
        for row in res:
            print(row[0], "\t\t", row[1], "\t\t\t", row[2], "\t\t", row[3])
class writeFile:
    def writeFile(self):
        con = sqlite3.connect('emp.db')
        cursor = con.cursor()
        today = dd.now()
        regiater_number = 2117031
        program = 1
        today_date = dd.strftime(today, '%d-%B-%Y')
        file_name = f"programoutput_{today_date}_{regiater_number}_{program}"
        try:
            f1 = open(f"{file_name}.txt", 'x')
        except FileExistsError:
            print("FILE IS ALREADY FOUND FILE CREATION IS NOT POSSIBLE YOU CAN WRITE FILE")
        file = open(f"{file_name}.txt", 'w')
        cursor.execute("SELECT * FROM EMPLOYEE")
        res = cursor.fetchall()
        sr = "SSN \t\t\t\t FIRST NAME \t\t\t \t LAST NAME \t\t\t\t SALARY \n"
        file.writelines(sr)
        for row in res:
            a = row[0]
            b = row[1]
            c = row[2]
            d = row[3]
            file.write(str(a))
            file.write("\t\t\t\t\t")
            file.write(str(b))
            file.write("\t\t\t\t\t")
            file.write(str(c))
            file.write("\t\t\t\t\t")
            file.write(str(d))
            file.write("\t\t\t\t\t")
            file.write("\n")
        print(f"SUCCESSFULLY INSERTED  DATABASE VALUE IN TO FILE {file_name}.txt")
while True:
    print("1)HOURLY EMPLOYEE 2) SALARIED EMPLOYEE 3)DISPLAY FROM DATABASE 4)DATABASE RECORDS INTO FILE 5)EXIT")
    c = int(input("ENTER YOUR CHOICE"))
    if (c == 1):
        hr = HourlyEmployee()
        hr.setSSN()
        hr.setFirstName()
        hr.setLastName()
        hr.setSalary()
        hr.HourlyEmployee()
        SSN = hr.getSSN()
        FirstName = hr.getFirstName()
        LastName = hr.getLastName()
        salary1 = hr.getSalary()
        grossSalary12 = hr.GrossSalary()
        netSalary1 = hr.NetSalary()
        con = sqlite3.connect('emp.db')
        cursor = con.cursor()
        # cursor.execute("Drop table if exists employee")
        # cursor.execute('''create table employee(SSN int,FirstName text,LastName text,salary int)''')
        cursor.execute("insert into employee(SSN,FirstName,LastName,salary) values(?,?,?,?)",
                       (SSN, FirstName, LastName, salary1,))
        cursor.execute("SELECT * FROM EMPLOYEE")
        print(cursor.fetchall())
        con.commit()
        a = input('DO YOU WANT TO DISPLAY RECENT  RECORDS OF HOURLY EMPLOYE Y or N')
        if a == 'Y':
            print("SSN:", SSN)
            print("FIRST NAME:", FirstName)
            print("SECOND NAME:", LastName)
            print("SALARY:", salary1)
            print("GROSS SALARY:", grossSalary12)
            print("NET SALARY:", netSalary1)
    elif c == 2:
        sal = SalariedEmployee1()
        sal.setSSN()
        sal.setFirstName()
        sal.setLastName()
        sal.setSalary()
        sal.SalariedEmployee()
        SSN = sal.getSSN()
        FirstName = sal.getFirstName()
        LastName = sal.getLastName()
        salary1 = sal.getSalary()
        grossSalary12 = sal.GrossSalary()
        netSalary1 = sal.NetSalary()
        con = sqlite3.connect('emp.db')
        cursor = con.cursor()
        # cursor.execute("Drop table if exists employee")
        # cursor.execute('''create table employee(SSN int,FirstName text,LastName text,salary int)''')
        cursor.execute("insert into employee(SSN,FirstName,LastName,salary) values(?,?,?,?)",
                       (SSN, FirstName, LastName, salary1,))
        con.commit()
        a = input('DO YOU WANT TO DISPLAY RECENT  RECORDS OF salaried EMPLOYE Y or N')
        if a == 'Y':
            print("SSN:", SSN)
            print("FIRST NAME:", FirstName)
            print("SECOND NAME:", LastName)
            print("SALARY:", salary1)
            print("GROSS SALARY:", grossSalary12)
            print("NET SALARY:", netSalary1)
    elif c == 3:
        d1 = displayDATA()
        d1.display()
    elif c == 4:
        ww =writeFile()
        ww.writeFile()
    elif c == 5:
        exit()
    else:
        print("!!!------INVALID CHOICE PLEASE ENTER VALID ONE-----!!!")







