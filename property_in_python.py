#property: We use any decorator in the class to use the method as a property, to change automatically
class Student:
    def __init__(self,phy,che,Math):
        self.phy=phy
        self.che=che
        self.Math=Math

    @property
    def percentage(self):
        return str((self.che+self.Math+self.phy)/3)+"%"
    

s1=Student(97,98,95)
print(s1.phy)
print(s1.percentage)
s1.phy=85
print(s1.percentage)
