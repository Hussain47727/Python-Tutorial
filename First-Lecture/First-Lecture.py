#check version
import sys

print(sys.version)

# write first programe print hello world
print("hello world")
print("my name is israr Hussain")
print("hello world", "my name is israr Hussain")

# variable .... how to store value in a variable and also check the
# the data type

first = "Hello world"
name = "my name is israr Hussain"
age = 20
price = 3.33
old = False
a = None
print(first, name, "and iam ", age, "years old")
print(type(first))
print(type(age))
print(type(price))
print(type(old))
print(type(a))


  # Data Types 
  #.... 1-- integers (numbers like +1, -1, 204 etc)
  #.... 2-- string (a code we write in single code, double code or may be thipple code like ("hello world")) 
  #....3 -- float  (in float data type are always in decimal like 3.003, 89.38)
  #.... 4 --Bollean (in bollean there are just two values its may be true or false)
  #.... 5 -- None (in none varable there are no any value stored)

  #Keywords 
  # Keywords are reserved words in python (like and , false, true, for etc)


 # Print Sum
price1 = 10
price2 = 20
TotalPrice = price1 + price2
print(TotalPrice)

#print subtract
diff3 = 10
diff4 = 20
Tdiff = diff3 - diff4
print(Tdiff)

"""Types of operator
The operators are symbol to perform a certain operation between operands
there are many types of operators
1... Arithmatic operators(+,-,*,/,%,**)
2...Relational/Comparision Operators(==,!=,>,<,>=,<=)
3...Assignment Operators (=, +=, -=, *=, /=, %=, **=)
4...Logical Operator( not, and , or)  
"""

#1... Arithmatic operators(+,-,*,/,%,**)
a = 4
b = 2
print(a + b)
print(a -b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

#2...Relational/Comparision Operators(==,!=,>,<,>=,<=)
a = 20
b = 30

print(a == b)  #F
print(a != b)  #T
print(a > b)  #F
print(a < b)  #T
print(a >= b) #F
print(a <= b) #T

#3...Assignment Operators (+=,-=,*=,/=,%=)
num = 10
num += 10
num -= 10
num *= 10
num /= 10
num %= 10
print(num)

#Logical Operator( not, and , or)
"""There are three types of ligical operator 
  the first one is AND OPERATOR
  the second one is OR OPERATOR
  the third one is NOT OPERATOR
  """

  #Types of conversion
  #automatic conversion
  #casting conversion


  #input in python
  #input () statement is used to accept values (using keyboard) from users
 
name = input("enter you name :")
age = int(input("Enter your age :"))
marks = input("Enter your marks :")

print("you name is ", name , "you are ", 20, 
      "years old and you get", marks, "in physics")

#LETS PRACTICE 
#write a progrmae to input  2 numbers and print their sum.

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

print("The sum of ",num1, "and ", num2, "=", num1 + num2)

#Write a progrme to input side of a square and print its area

square = int(input("Enter side of a square"))
print('The areq of a square is ', square * square)

#write a programe to input 2 floating points numbers and print their average

n1 = float(input('Enter the first floating number :'))
n2 = float(input("Enter the second floating number :"))
average = (n1 + n2)/2
print("The average of ", n1, "and", n2, "is =", average)

#Write a progrmae to input 2 int numbers , a and b. Print True if a is greater than or equal to b. if not print False 
n1 = int(input('Enter the  number :'))
n2 = int(input("Enter the  number :"))

print(n1 >= n2)


            #THE END


 