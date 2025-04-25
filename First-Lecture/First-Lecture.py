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