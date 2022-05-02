"""----------------------------------------------------------------------------------
distnace_feet.py
Write a class Distance with instance variables feet and inches. Include necessary
methods. Test the class

Regno: 2117031
02/04/2022

---------------------------------------------------------------------------------"""


class Distance:
    def __init__(self, feet=None, inches=None):
        self.feet = feet
        self.inches= inches

    def input_data(self):
        self.feet = float(input("Enter the feet: "))
        self.inches = float(input("Enter the inches: "))

    # def add_distance(self, distance):
    #     newfeet = (distance.feet + self.feet) + int((distance.inches + self.inches) / 12)
    #     newinches = (distance.inches + self.inches) % 12
    #     return Distance(feet=newfeet, inches=newinches)

    def display(self):
        print(f"The feet : {self.feet}")
        print(f"The inches : {self.inches}")

    def __add__(self, other):
        f = self.feet + other.feet
        i = self.inches + other.inches
        return Distance(f,i)

    def addObj(self,others):
        f = self.feet + others.feet
        i = self.inches + others.inches
        return Distance(f, i)

obj1 = Distance()
obj1.input_data()
obj1.display()

obj2 = Distance()
obj2.input_data()
obj2.display()

print("adding two objects")
obj3 = obj1 + obj2
obj3.display()


new_obj =obj1.addObj(obj2)
new_obj.display()


