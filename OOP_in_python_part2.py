#del keyword:used to delete object properties or the entire object itself
#private attribute and methods :
#private attribute: self.__pass
#private methods: def __hello():

class Student:
    def __init__(self,acc_no,pas):
        print("Allahu akbar")
        self.account_number=acc_no
        self.__pas=pas
    def __hello(self):
        print("Hello person")
    def welcome(self):
        __hello()
    

s1=Student("12345","abcde")

print(s1.account_number)



##
class Person:
    def __hello(self):
        print("Hello person")

    def welcome(self):
        self.__hello()

p1=Person()
print(p1.welcome())



