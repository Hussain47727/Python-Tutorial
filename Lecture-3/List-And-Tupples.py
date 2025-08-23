# List and Tupples 
"""A built-in data type that stores set of values 
 it can store elements of different types (integer, float, string, etc)

 in other languages we use array to store a lot of data in varaible in the
 same way in python we use list
"""
# for example
marks1 = 12
marks2 = 45
marks3 = 55
marks4 = 45

#instead of the above we can use 
marks = [12, 45, 55, 45]
print(marks)
# Type of list
print(type(marks))
#we can find any index
print(marks[0])
print(marks[1])

#lengt of list
print(len(marks))

# Here is a small difference between array and list 
# In arrays we can store only same type of elements like int, string etc but
# But in list we can store any type of element

student = ["israr", 33, "Nagar"]
print(student)

#List are mutable mean (we can change data or element whenever we want)
#For example in the above student variable we remove "nagar" into 12

student[2] = "12"
print(student)




