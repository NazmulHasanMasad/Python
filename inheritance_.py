class Car:
    @staticmethod
    def start():
        print("Start the car:")
    @staticmethod    
    def end():
        print("Stop the car: ")

#single level of inheritance  
class Toyota(Car):
    def __init__(self, brand):
        self.brand=brand

       
#multilevel of inheritance
class Porsche(Toyota):
    def __init__(self,type):
        self.type=type
        

car1= Porsche("disel")
car1.start()
car2=Toyota("Porshche")


#multiple inheritance
class A:
    varA="Class A"

class B:
    varB="Class B"

class C(A,B):
    varC="Class C"

c1= C()

print(c1.varA)
print(c1.varB)
print(c1.varC)










    
