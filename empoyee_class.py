class Employee:
    def __init__(self,role, department,salary):
        self.role=role
        self.department=department
        self.sal=salary
    def showDetails(self):
        print(self.role)
        print(self.department)
        print(self.sal)
class Engineer(Employee):
    def __init__(self, name, age):
        self.name=name
        self.age=age
        super().__init__("MANAGER", "SECURITY", "$10000")
    
        


    





E1=Employee("Software engineer","Security", "$10000")
E1.showDetails()
E2=Engineer("Masud",30)
E2.showDetails()
