# Encapsulaion
# hiding the data from the outside and get access only using key (method)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 🔐 Private variable (note: __)
    def get_balance(self):
        return self.__balance

account1 = BankAccount(20000)
print(account1.get_balance())

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("invalid")

p1 = Person("israr", 19)
print(p1.get_name())

p1.set_age(25)
print(p1.get_age())

  # a short practice proble
class Pet:
    def __init__(self, name1, age1):
        self.name1 = name1
        self.age1 = age1
class Dog(Pet):
    def __init__(self, name1, age1, breed):
        super().__init__(name1, age1)
        self.breed = breed
    def bark(self):
        print('bark bark')
class Cat(Pet):
    def pur(self):
        print('pur pur')

spotify = Dog("spotify", 3, "Golden retriver")
cutie = Cat('Cutie', 4)

spotify.bark()
cutie.pur()
        
