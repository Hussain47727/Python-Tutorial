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
# class Pet:
#     def __init__(self, name, age, price):
#         self.name = name
#         self.age = age
#         self.price = price

    # def display_info(self):
    #     print(f"Name: {self.name}, Age: {self.age}, Price: ${self.price}")

class Dog(Pet):
    def __init__(self, name, age, price, breed):
        super().__init__(name, age, price)
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

class Cat(Pet):
    def __init__(self, name, age, price, color):
        super().__init__(name, age, price)
        self.color = color

    def meow(self):
        print("Meow! Meow!")

# Create objects
dog = Dog("Rex", 2, 300, "Labrador")
cat = Cat("Misty", 1, 200, "White")

# Test
dog.display_info()  # Output: Name: Rex, Age: 2, Price: $300
cat.display_info()  # Output: Name: Misty, Age: 1, Price: $200

dog.bark()  # Output: Woof! Woof!
cat.meow()  # Output: Meow! Meow!
