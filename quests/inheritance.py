class Person:
    def __init__(self,name,age,function="?"):
        self.name = name 
        self.age = age 
        self.function = function

    def show(self):
        print(f"{self.name} {self.age} {self.function}")

    def say(self):
        print(f"{self.name} say")

class Student(Person):
    def __init__(self,name,age):
        Person.__init__(self,name, age)

    def study(self):
        print("student is studies")

    def show(self):
        print(f"my name is {self.name} and i am  student")

class Teacher(Person):
    def __init__(self,name,age,function ,classes):
        Person.__init__(self,name,age,function)
        self.classes = classes
    
    def show(self):
        print(f"{self.name} {self.age} {self.classes }")

    def teach(self):
        print("teach students")


class Director(Person):
    def __init__(self,name,age,val,function="management"):
        Person.__init__(self,name,age,function,)
        self.val = val 

    def show(self):
        print(f"{self.name} {self.age} {self.val} {self.function}")

