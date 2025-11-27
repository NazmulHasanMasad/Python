# set - collection of unique values and they are unordered and immutable
 #no duplicate values


nums={1,2,3, "Hello", "Nazmul"}
print(nums)
print(type(nums))

#empty set

number= set()
print(type(number))


#methods of set
nums.add(5)
print(nums)

nums.remove("Nazmul")
print(nums)

nums.pop()
print(nums)



nums2={5,6,7,8,9, "Hello"}

print(nums.union(nums2))
print(nums.intersection(nums2))



