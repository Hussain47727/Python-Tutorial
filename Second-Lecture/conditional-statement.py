#conditioal statement
"""if-elif-else(syntex)
if(condition):
statement1
elif(condition):
statement2
else:
statement N
"""
age = int(input('enter the number'))
if(age >= 19):
    print("can vote and apply for licences")
elif(age < 19):
    print("you are not able to vote")
else:
    print("enter correct please")

#practice questions
# 1.. Write a programe to check if a number entered by the user is odd or even.

num = int(input("Enter the number"))
if(num % 2 == 0):
    print(num,"is an even number")
elif(num % 2 != 0):
    print(num, "is an odd number")

# 2. WAP to find the greatest of 3 numbers entered by the user.
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the Third number"))

if(a > b and b > c):
    print(a, "is greater number")
elif(b > a and b > c):
    print(b, "is greater number")
elif(c > a and c > b):
    print(c, "is greatest number")
