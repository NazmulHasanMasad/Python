#operator overloading : 
#when the same operator is allowed to have different meaning according to the context

class ComplexNumbers:
    def __init__(self, real, img):
        self.real=real
        self.img=img

#complex numbers example: i+3j
    def showNumber(self):
        print(self.real,"i +",self.img,"j" )

#dunder functions  add 
    def __add__(self,num2):
        new_real=self.real+num2.real
        new_img=self.img+num2.img
        return ComplexNumbers(new_real, new_img)


#dunder functions  subtraction
    def __sub__(self,num2):
        new_real=self.real-num2.real
        new_img=self.img-num2.img
        return ComplexNumbers(new_real, new_img)


n1=ComplexNumbers(2, 4)
print(n1.showNumber())

n2=ComplexNumbers(5, 8)
print(n2.showNumber())

n3= n1+n2
n3.showNumber()


n3= n1-n2
n3.showNumber()


#dunder functions


 


