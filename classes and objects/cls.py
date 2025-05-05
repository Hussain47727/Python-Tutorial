 #classes and objects 
#  Classes are the plueprint of creating objects

#now we create a class and object for student
#


#now for car 

class Car :
    color = "blue"
    price = 3000000

car1 = Car()
print(car1.price)

#__ init __ Fuction or constructor
# All classes have a fuction called __init__(), which is always
# execute when the class is being initiated

class Students :

    College_name = "Uswa public School And College"
    def __init__ (self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        print("another student..")
        print(Students.College_name)

s1 = Students("Ali", 20, 45)
print(s1.name, s1.age, s1.marks)
s2 = Students("Haider", 19, 34)
print(s1.name, s1.age, s1.marks)
s1 = Students("Ali", 20, 45)
print(s1.name, s1.age, s1.marks)

        

#Methods 
# Methods are the fuctions that belong  to objects.
