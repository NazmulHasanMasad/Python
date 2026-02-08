#abstraction:Hiding the implementation details of a class and only showing the essential feathers to the users.

class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
        
    def start_car(self):
        self.acc=True
        self.clutch=True
        print("Start car")


car1=car()
car1.start_car()