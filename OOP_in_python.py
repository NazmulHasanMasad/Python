#To map with Real world scenarios, we Started using objects in code, This is called the object oriented programming
#Class and object in python_class is a blue print of creating objects
#creating class

class Student:
    college_name="Hof university of applied science"
#constructor: init function

   
#parameterized constructor 
    def __init__(self, fullname, roll, age ):
        print("add new student")
        self.name= fullname
        self.roll=roll
        self.age=age

# class and instance attributes:
#methods : Methods are functions that belong to objects
    def welcome(self):
        print("Welcome student", self.name)

    
#with constructor we can pass the value of the object 
#creating object(instance of class)
s1=Student("Masud", 942,30)
s2=Student("Rasel", 945, 45)
print(s1.name, s1.age, s1.roll)
print(s2.name, s2.age, s2.roll)
print(s2.college_name)


# class and instance attributes:
#methods : Methods are functions that belong to objects
def welcome(self):
    print("Welcome student")

s2.welcome()






