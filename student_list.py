students = [['lailesh', ['python', 'rdbms']],
            ['ranson', ['python', 'stats']],
            ['royal', ['rdbms', 'python', 'stats']],
            ['lanwil', ['rdbms']],
            ['loy', ['python']],
            ['roy', ['rdbms']]]
print('''
    1) List number of student who enrolled for python course.
    2) List number of student who enrolled for RDBMS Course Only
    3) List number of student who enrolled for RDBMS Python Only
    4) List number and name of the student for both RDBMS Python Only
    5) List number and name of the student for either RDBMS or Python not
    for both
    6) List number and name of the student for either RDBMS or Python.
    7) Exit
    ''')
while True:

    choice = int(input("ENTER THE CHOICE:"))
    if choice == 1:
        count = 0
        for student in students:
            if 'python' in student[1]:
                count += 1
        print("NUMBER OF STUDENT ENROLLED FOR PYTHON COURSE:", count)
    if choice == 2:
        count = 0
        for student in students:
            if len(student[1]) == 1 and 'rdbms' in student[1]:
                count += 1
        print("STUDENT WHO ENROLLED FOR RDBMS COURSE ONLY:", count)
    if choice == 3:
        count = 0
        for student in students:
            if (len(student[1]) == 1) and ('rdbms' in student[1] or 'python' in student[1]):
                count += 1
                print(student[0])
        print("STUDENT ENROLLED FOR RDBMS AND PYTHON ONLY", count)
    if choice == 4:
        count = 0
        for student in students:
            if (len(student[1]) == 2) and ('rdbms' in student[1] and 'python' in student[1]):
                count += 1
                print("NAME OF THE STUDENT:", student[0])
        print("NUMBER OF STUDENT FOR BOTH RDBMS PYTHON:", count)
    if choice == 5:
        count = 0
        for student in students:
            both_are_their = 0
            if 'python' in student[1]:
                both_are_their += 1
            if 'rdbms' in student[1]:
                both_are_their += 1
            if both_are_their == 1:
                count += 1
                print(student[0])
        print(count)

    if choice == 6:
        count = 0
        for student in students:
            if ('python' in student[1]) or ('rdbms' in student[1]):
                print(student[0])
                count += 1
        print(count)
    if choice == 7:
        break
