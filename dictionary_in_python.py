#dictionaries in python store data in key:value pairs, they are unordered, mutable and dont allow duplicate keys

information = {

"name" : "Masud rpc",
"Age"  : " 31",
"Job"  : "Manager ",
"Topics" : " Electrical engineer "



}

print(information["name"])
print(information["Topics"])

information["name"] = "Moga"
information["surname"]="Rahman" 
print(information["surname"])

null_dic={}

null_dic["name"]="Rasel"
print(null_dic["name"])

#nested dictionary

student ={
    "name" : "Roman",
    "subjects" : {
        "Phy":95,
        "Che":85,
        "Mat":69
    }
}

print(student["subjects"]["Mat"])


#Mathods in deictionary

print(list(student.keys()))

#total number of keys in Dictionary

print(len(list(student.keys())))


print(student.values())
print(student.items())

print("New code ")
print(student.get("subjects"))
student.update({"city": "Dhaka"} )
print(student)
student.update({"conditions": "Good"})
print(student)

new_dic={
"bestfriend": "Masad",
"bestFriend2": "RASEL"

}
student.update(new_dic)
print(student)


