# OOPs (Object Oriented Programming) in Python


# class- blueprint or template
# __init__ method -constructor, value initialize - fix
# self parameter - reference or connection build between class & object - fix

# class Student:  # student class
#     def __init__(self, full_name, class_grade, percentage):  # method
#         self.name = full_name      # attribute
#         self.grade = class_grade   # attribute
#         self.percentage = percentage

#     def student_details(self):  # method
#         print(f"{self.name} is in class {self.grade}, with in {self.percentage}%")    


# # Object - instance of class
# student1 = Student("Ram", 11, 95)
# # print(student1.name, student1.grade)

# student2 = Student("Amit", 8, 98)
# print(student2.name, student2.grade)

# print(student1.percentage)

# student1.student_details()
# student2.student_details()

# print(student1.__dict__, student2.__dict__)

# # Modify object property
# print(student1.percentage)
# student1.percentage = 97   # modify
# print(student1.percentage)


# # delet object property
# print(student1.__dict__)
# del student1.percentage
# print(student1.__dict__)

# # delete object
# del student1
# print(student1)


#  class 

class Student:
    def __init__(self , name , grade, percentage, team): # method
        self.name = name   # attribute
        self.grade = grade
        self.percentage = percentage
        self.team = team

    def student_details(self):  # method
        print(f"{self.name} is in class {self.grade} with {self.percentage}% and is in team {self.team}")  

team1 = 'A'
team2 = 'B'

 # Object

student1 = Student("amit", 8, 98, team1) 

student2 = Student("prity", 10, 96, team2)

student1.student_details()
student2.student_details()


# 4 features in OOPs
#1. Abstraction
#2. Encapsulation 
#3. Inheritance
#4. Polymorphism

# Abstraction
# hiding unnecesary details from users through class, methods

print("\nAbstraction")
# class 
class Student:
    def __init__(self , name , grade, percentage): # method
        self.name = name   # attribute
        self.grade = grade
        self.percentage = percentage

# Abstraction method - hidden from users
    def student_details(self):  # method
        print(f"{self.name} is in class {self.grade} with {self.percentage+2}%")  


 # Object

student1 = Student("amit", 8, 97) 

student2 = Student("prity", 10, 96)

student1.student_details()
student2.student_details()

# Encapsulation 
#  Restrict access to certain attributes or method to protect data and enforce controlled access

print("\nEncapsulation")

# class -
class Student:
    def __init__(self, name, grade, percentage):
        self.name = name   #attributes
        self.grade = grade
        self.__percentage = percentage  # double underscore limits access and private attribute
    
    def get_percentage(self):
        return self.__percentage

    def student_details(self): # method
        print(f"{self.name} is in class {self.grade} with {self.__percentage}%") 

# object -
student1 = Student("amit", 8, 96)   
student2 = Student("prity", 10, 94)


# print(student1.__percentage) # error

print(f"{student1.name} is in class {student1.grade} with {student1.get_percentage()}%.")
# or
# print(student1.get_percentage())



# Inheritance (parent - child)
# allows one class (child) to reuse the properties and methods of another class (parent).
# This avoids duplication and helps in code reuse.

print("\nInheritance")
# parent class -
class Student:
    def __init__(self, name, grade, percentage):
        self.name = name   #attributes
        self.grade = grade
        self.percentage = percentage 

    def student_details(self): # method
        print(f"{self.name} is in class {self.grade} with {self.percentage}% in {self.stream} stream") 

# child class -
class GraduateStudent(Student):  # Graduatestudent child class inherit properties and method from Student parent class
    def __init__(self, name, grade, percentage, stream): # old parameters from parent class and new parameters in child class
        super().__init__(name, grade, percentage)  # call parent class init
        self.stream = stream # new attribute in child class

    def student_details(self):
        return super().student_details() # method inherit from parent class
        #  print(f"stream is {self.stream}")

# Object-
Grad_student1 = GraduateStudent('Amit', 12, 98, 'PCM')
# print(Grad_student1.stream)
# print(Grad_student1.percentage)

Grad_student1.student_details()


# Polymorphism - (same method but different output)
# allows methods in different classes to have same name but different behaviour depending on objects

print("\nPolymorphism")

class Student:  # student class
     def __init__(self, full_name, class_grade, percentage):  # method
         self.name = full_name      # attributes
         self.grade = class_grade   
         self.percentage = percentage

     def student_details(self):  # method
         print(f"{self.name} is in class {self.grade}, with in {self.percentage}%")    


# child class -
class GraduateStudent(Student):  
    def __init__(self, name, grade, percentage, stream): 
        super().__init__(name, grade, percentage)  # call parent class init
        self.stream = stream # new attribute in child class

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.percentage}% and from stream {self.stream}")

# Object- student class
student1 = Student("prity", 10, 96)

# object - GraduateStudent class
Grad_student1 = GraduateStudent("Amit", 12, 98, 'PCM')

student1.student_details()
Grad_student1.student_details()

