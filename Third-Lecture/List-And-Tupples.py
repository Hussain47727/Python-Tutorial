# List and Tupples 
"""A built-in data type that stores set of values 
 it can store elements of different types (integer, float, string, etc)
"""


class Pet:
    def __init__(self, name1, age):
        self.name =name1
        self.age = age

#subclass
class Cat(Pet):
    def __init__(self, name1, age, breed):
        super().__init__(name1, age)
        self.breed =breed

    def bark(self):
        print("bark")

class Dog(Pet):
    def purr(self):
        print("purr purr")

