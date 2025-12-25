#super method: METHODS THAT is used to get access to the parent class
class Car:
    def __init__(self, type):
        self.type=type
        
    @staticmethod
    def start():
        print("Start the car:")
    @staticmethod    
    def end():
        print("Stop the car: ")

class Toyota(Car):
    def __init__(self, brand,type):
        self.brand=brand
        super().__init__(type)


car1=Toyota("Porshche","Electric")
print(car1.type)

