#write function
with open("practice.txt","w+") as m:
     m.read()
     m.write("Why the fuck its not working\n")
     m.write(" I am learning python\n")
     m.write(" I will build projects with python\n")
     m.close()

#replace function
with open("practice.txt","r") as s:
    new_data=s.read()
    new_data=new_data.replace("fuck","hell")
    print(new_data)

#Find function
def check():
    word= "Fuck"
    with open("practice.txt","r") as f:
        data=f.read()
        if data.find(word) != -1:
            print("found")
        else:
          print("Not found")

check()


#finding the first occurence:

def check_for_line():
    word1= "learning"
    data=True
    line=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if word1 in data:
                print(line)
                return
            line+=1
    return -1
check_for_line()


#finding the even number 
count=0
with open("even.txt", "w+") as f:
    f.read()
    data=f.write("1,2,4,5,7,8,9,10,20,25,48,35,95")

    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
        else:
            num += data[i]
    
   










