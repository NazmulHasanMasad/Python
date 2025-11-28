#break and continue

i=0
while i<=5:
    if(i==3):
        i +=1
        continue  
    print(i)
    i+=1


print("break")
j=0
while j<=5:
    print(j)
    if(j==3):
        break
    j +=1
 

# loops in python
print("for loops")
list=[2,4,5,6,7,8,9,10]

for val in list:
    print(val)
else:
    print("all are printed")

   

   #practice
tuples=(1,2,3,4,5,6,7,8,9,10)
x=3
for val in tuples:
    if(val==10):
        print("found")
        break
   

#range functions:returns a sequence of numbers, starting from 0 by default, increments by 1 and stops before a specified number.
range(25)

for i in range(2,20,2):
    print(i)

#multiplication of number n

range(11)
for val in range(1,11):
    print(5*val)