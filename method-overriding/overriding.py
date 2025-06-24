#  # overriding 

# class Animal:
#     def speak(self):
#         print("Animal is speaking")
# class Cat(Animal):
#     def speak(self):
#         print("cat is meouw")
# class Dog(Animal):
#     def speak(self):
#         print("dog are barking")

class Shape:
    def calculate_area(self):
        print('area is not defined')

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.widht = width
    def calculate_area(self):
        area = self.length * self.widht
        print('area of rectangle:', area)
    
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        print('area of circle :', area)
    
s = Shape()
s.calculate_area()

r = Rectangle(2,4)
r.calculate_area()
c = Circle(5)
c.calculate_area()