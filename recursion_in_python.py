#print n to 1 in backward
def print_n(n):
    if n==0:
        return
    print(n)

    print_n(n-1)


print_n(5)

#returns n!

def factorial(n):
   if n==0 or n==1:
       return 1
   else:
       return n*factorial(n-1)



print(factorial(5))




#sum of first n natural numbers

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)

print(sum(10))



# print_list
def print_list(list, idx):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

print_list(["Masad", "Rasel","Roman","Afzal"], 0)





