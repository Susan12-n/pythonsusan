# python lists 
# a list is an ordered collection of items 
# we use square brackets 
# we separate the items inside the square brackets with a comma (,)

lab1=["susan","teddy","keanche","rose","banana","seth","peter","faith","vincent","samuel"]
print(lab1)

# print the size of the list 

print(len(lab1))


# accessing each item in the list 
# NB:we access each item using the index 
# we start counting from  zero index 

print(lab1[0])
print(lab1[1])
print(lab1[2])
print(lab1[3])
print(lab1[4])
print(lab1[5])
print(lab1[6])
print(lab1[7])
print(lab1[8])
print(lab1[9])




# append items in the list 
# add stephen in the list 

lab1.append("stephen")

print(lab1)

# insert jonson at index 3 
lab1.insert(2,"jonson")
print(lab1)

# print items from number four and above 
print(lab1[4:])

# print items from four and below 
# NB-there is a minus one 
print(lab1[4-1:])
#  slicing 
# print items from index 2 to 5 
print(lab1[2:5])
# NB-does not include the last index 
