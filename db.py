import sqlite3 as s

conn = s.connect('test.db')

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS COMPANY")
cursor.execute('''CREATE TABLE COMPANY(
                ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                AGE INT NOT NULL,
                ADDRESS CHAR(50),
                SALARY INT )''')

cursor.execute("insert into company values(101,'lailesh',23,'banglore',20000)")
cursor.execute("insert into company values(102,'royal',45,'mysore',34567)")
cursor.execute("insert into company values(103,'yathis',23,'maglore',45000)")
cursor.execute("insert into company values(104,'suresh',22,'banglore',65000)")
cursor.execute("insert into company values(105,'floy',34,'delhi',56000)")


sql1 = "update company set name = 'ramesh' where id =104"
cursor.execute(sql1)

sql4= "delete from company where id = 103"
cursor.execute(sql4)

sql3 = "SELECT * FROM COMPANY where salary > 30"
try:
    cursor.execute(sql3)
    res = cursor.fetchall()
    print("==========================================================")
    print("ID \t\t NAME \t\t AGE \t\t ADDRESS \t\t SALARY ")
    print("==========================================================")
    for row in res:
        print(row[0],"\t", row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\n")
except s.Error as e:
    print(e)

conn.commit()
print('sucessfully created TABLE ')
conn.close()