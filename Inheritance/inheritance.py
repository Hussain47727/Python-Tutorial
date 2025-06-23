# # inheritance mean use parant class features into child class

# class Animal:
#     def speak(self):
#         print("Animal is speaking")
        

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# d = Dog()
# d.speak()   # Inherited method
# d.bark() 

# # short exampel
# class vehical:
#     def __init__(self, brand):
#         self.brand = brand
#     def show_brand(self):
#         print('brand : toyota')

# class car(vehical):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model
#     def show_model(self):
#         print("model : corolla")
    

# car1 = car("Toyota", "Corolla")
# car1.show_brand()
# car1.show_model()

class Vehical :
    def __init__(self, brand):
        self.brand = brand
    def show_brand(self):
        print('brand :', self.brand)

class Car(Vehical):
    def __init__(self, brand, price):
        super().__init__(brand)
        self.price = price
    def show_price(self):
        print("price :", self.price)

car1 =Car('toyota', 3000)
car1.show_brand()
car1.show_price()

        