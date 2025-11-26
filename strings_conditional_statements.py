#marking conditions

marks =int(input("enter the marks:"))

if(marks >= 90):
   print("A")

elif(marks>=80):
   print("B")

elif (marks>=70):
    print("B-")

elif(marks>=60 ):
   print("c")

else:
   print("D")   


#nested conditions
age= int(input("enter the age: "))

if(age>= 18):
   if(age>=80):
      print("can't drive")
   else:
     print("can drive")
else:
   print("can't drive ")


# number is odd or even
number= int (input("enter the number:"))

if(number%2==0):
   print("even")
else:
   print("odd")

#gretest number

a= int(input("a:"))
b= int(input("b:"))
c= int(input("c:"))

if(a>b and a>c):
   print("a is the biggest")
elif(b>c and b>a):
   print("b is the biggest")
else:
  print("C is the biggest")

    #multiple of 7

number2= int(input("inter the new number:"))
if(number2%7==0):
   print("multiple of 7")
else:
   print("not multiple of 7")





