 #list in python
marks=[80.5, 91.6, 85.0,54.8,29.0]
print(marks)
print(len(marks))
print(marks[4])
print(type(marks))


#lists is mutable in python, strings is immutable 
students=["Moga", "31", "Ruppur", "Enginner"]
students[0]= "Rasel"
print(students)



#slicing is to get the part of string or list.
print(marks[1:4])
print(marks[-3:-1])


#list methods
marks.append(4)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(2, 70)
print(marks)


#sorting in list with strings
names=["Masud", "Rasel", "Afjal", "Naim"]
names.sort()
print(names)

#remove means remove the first occurences of an element in the list
marks.remove(4)
print(marks)

#pop method is for remove element on that particular index
marks.pop(1)
print(marks)
