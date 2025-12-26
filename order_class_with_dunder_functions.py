class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self, o2):
        return self.price>o2.price
    


o1=Order("chips", 20)
o2=Order("Tea",25)

print(o1>o2)
