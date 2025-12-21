from gettext import install
from os import write

f=open("demo.txt", "r")
line1=f.readline()
print(line1)
lin2=f.readline()
#print(lin2)
f.close()

# r+ : Open for reading and writing.  The stream is positioned at the beginning of the file.
f=open("demo.txt","r+")
line3=f.write("70 DAYS: ")
f.close()

# W : Truncate file to zero length or create text file for writing. The stream is positioned at the beginning of the file
f=open("demo.txt","w")
line4=f.write("DSA,AI,SYSTEM DESIGN,PROJECTS")
print(line4)


#w+:   Open for reading and writing.  The file is created if it does not
#          exist, otherwise it is truncated.  The stream is positioned at
#               the beginning of the file.

m=open("masad.txt","w+")
m.write(" I want to learn full stack with python ")
#print(m.read())
m.close()

# a: Open for writing.  The file is created if it does not exist.  The
#         stream is positioned at the end of the file.  Subsequent writes
#         to the file will always end up at the then current end of file,
#         irrespective of any intervening fseek(3) or similar.

m=open("masad.txt","a")
m.write(" I will get the job")
m.close()

#a+ : open for reading and writing, create file automatically

#with syntax

with open("masad.txt", "a") as f:
    data= f.write(" by the next 70 days ")
    print(data)

#delete file
import  os
os.remove("masad.txt")























