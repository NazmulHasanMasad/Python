#tuples is a built in data type that is immutable
tup=(1,2,3)
print(type(tup))
print(tup[0])

#empty tuples
tuples=()

#in tuples with single values it is important to give comma

tup1=(1,)
print(tup1)
print(type(tup1))

tup2=(1)
print(type(tup2))

#slicing in tuples
print(tup[1:3])


#Methods in tuple
tup3=(1,2,3,4,2,5)
print(tup3.index(5))
print(tup3.count(2))

#practice 1:
 #movies= [input("enter your first movie name:"),input("enter your second movie name:"),input("enter your third movie name:"),]


#print(movies)

#practice2 : list is containing palindrome or not
print ("practice 2")
list=[1,2,3,2,1]
list1=list.copy()
list1.reverse()
print(list1)

if(list==list1):
    print("Palindrome")
else:
    print("not palindrome")


#count number of students with A

tup4= ("A","B","C","D","E", "A", "B", "A", "A", "B")
print(tup4.count("A"))


grade= ["A","B","C","D","E", "A", "B", "A", "A", "B"]
grade.sort();
print("grade:", grade)