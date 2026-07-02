# task3_oop.py

class Person:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name : {self.name}")


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show(self):
        print(f"Student Name : {self.name}")
        print(f"Course : {self.course}")


class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show(self):
        print(f"Teacher Name : {self.name}")
        print(f"Subject : {self.subject}")


student = Student("Rahul", "Python")

teacher = Teacher("Amit", "Computer Science")

student.show()

print()

teacher.show()