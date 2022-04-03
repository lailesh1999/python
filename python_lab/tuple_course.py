"""----------------------------------------------------------------------------------
tuple_course.py
Write a python program using tuple to satisfy following business requirements:
    a) List the number of courses opted by student “John”
    b) List all the courses opted by student “John”
    c) Student “John” is also interested in elective course mentioned above. Print the updated tuple including electives.
    d) Check whether student “john” is allowed to change his course from SE to Computer network. Consider the list of courses opted by a student “john” and available electives as a part of student Management System.
    Courses: (“Python Programming”, ”RDBMS”, ”Web Technology”,
    “Software Engineering”)
    Electives:(”Business Intelligence”, Big Data Analytics”)

Regno: 2117031
02/02/2022
---------------------------------------------------------------------------------"""

courses = ("python", "RDBMS", "web technology", "software engineering")
electives = ("business Inteligence", "big data analytics")

print("1.LIST NUMBER OF COURSE OPTED BY STUDENT JOHN")
print("2.LIST ALL THE COURSES OPTED BY STUDENT JOHN")
print("3.STUDENT JOHN IS ALSO INTRESTED IN ELECTIVE COURSE MENTIONED ABOVE.UPDATE TUPLE INCLUDING ELECTIVES")
print("4.CHECK WHETHER STUDENT JOHN IS ALLOWED TO CHANGE IN COURSE FROM SE to COMPUTER NETWORK")
print("5.EXIT")
while True:
    ch = int(input("Enter your choice\n"))
    if ch == 1:
        print("NUMBER OF COURSES OPTED BY JOHN:", len(courses))
    elif ch == 2:
        print("COURSES OPTED BY STUDENT JOHN")
        i = 0
        for course in courses:
            i += 1
            print(f"{i}){course}")
    elif ch == 3:
        listcourse = list(courses)
        listele = list(electives)
        for ele in listele:
            listcourse.append(ele)
        course = tuple(listcourse)
        print("John courses after adding electives:\n")
        print(course)
    elif ch == 4:
        listcourse = list(course)
        for i in range(0, len(listcourse)):
            if listcourse[i] == 'software engineering':
                listcourse[i] = 'COMPUTER NETWORKS'
            courses = tuple(listcourse)
        print("John courses after chaging:\n")
        print(courses)
    elif ch == 5:
        break
    else:
        print("INVALID CHOICE!!!")
