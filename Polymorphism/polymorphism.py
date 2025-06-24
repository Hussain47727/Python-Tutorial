# POLYMORPHISM
# Polymorphism means many forms -- we use same method name but different
# classes and behaviours 

# class cat :
#     def speak(self):
#         print('meauw')
# class Dog :
#     def speak(self):
#         print('Dogs are barking')
# class Cow :
#     def speak(self) :
#         print('cows are mewos')

# animals = [cat(), Dog(), Cow()]

# for  animal  in  animals:
#     animal.speak()

# SHORT PROBLEM

class Payment:
    def make_payment(self):
        print('payment method not defined')
class CreditCard(Payment):
    def make_payment(self):
        print('payment made using credit card')
class Paypal(Payment):
    def make_payment(self):
        print('payment made using paypal')

methods = [(CreditCard()), (Paypal())]
for method in methods:
    method.make_payment()