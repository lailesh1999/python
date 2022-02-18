courses = ("python","RDBMS","web technology","software engineering")
electives = ("business Inteligence","big data analytics")
while True:
    print("1.LIST NUMBER OF COURSE OPTED BY STUDENT JOHN")
    print("2.LIST ALL THE COURSES OPTED BY STUDENT JOHN")
    print("3.STUDENT JOHN IS ALSO INTRESTED IN ELECTIVE COURSE MENTIONED ABOVE.UPDATE TUPLE INCLUDING ELECTIVES")
    print("4.CHECK WHETHER STUDENT JOHN IS ALLOWED TO CHANGE IN COURSE FROM SE to COMPUTER NETWORK")
    print("5.EXIT")
    ch =int(input("Enter your choice\n"))
    if ch == 1:
        print("NUMBER OF COURSES OPTED BY JOHN:",len(courses))
    elif ch == 2:
        print("COURSES OPTED BY STUDENT JOHN")
        for i in range(0,len(courses)):
            print(courses[i])
    elif ch == 3:
        listcourse = list(courses)
        listele = list(electives)
        for i in range(0,len(listele)):
            listcourse.append(listele[i])
        courses = tuple(listcourse)
        print(courses)
    elif ch == 4:
        listcourse = list(courses)
        for i in range(0,len(listcourse)):
            if listcourse[i] == 'software engineering':
                listcourse[i] = 'COMPUTER NETWORKS'
            courses = tuple(listcourse)
        print(listcourse)
    elif ch == 5:
        break
    else:
        print("INVALID CHOICE!!!")







