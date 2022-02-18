class student:
    def input(self):
        self.student = input("Enter the student name")
        self.reg_no = int(input("Enter the register number "))
        self.course = input("Enter the course")
        self.m1 = int(input("Enter the marks1 "))
        self.m2 = int(input("Enter the marks2 "))
        self.m3 = int(input("Enter the marks3 "))
    def display(self):
        print("Student name:",self.student)
        print("Student regno:", self.reg_no)
        print("Student course:", self.course)
        print("MARKS 1:", self.m1)
        print("MARKS 2:", self.m2)
        print("MARKS 3:", self.m3)
        total = self.m1 + self.m2 + self.m3
        avg = total/3
        print("AVERAGE:",round(avg))
        if self.m1 < 35 or self.m2 < 35 or self.m3 < 35:
            print("RESULT FAIL")
        else:
            print("RESULT PASS")
            if  avg >= 35 or  avg <= 60:
                print("SECOND CLASS")
            elif avg >= 60 or avg <= 70:
                print("FIRST CLASS")
            elif avg >= 70 or avg <= 90:
                print("DISTINCTION")
            else:
                print("OUT STANDING")

st = student()
st.input()
st.display()
