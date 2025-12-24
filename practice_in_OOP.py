class Student:
    def __init__(self, name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
            print(sum/3)
    @staticmethod
    def city():
        print("Hof")
    


s1=Student("Rasel",[85,95,79])
s2=Student("Masud",[90,86,96])
print(s1.name)
s1.average()
s1.city()









        