#string
"""Today in this lecture we will learn about strings
string is a datatype that store a squence of characters
string is stored in the quots maybe its single, doulbe or thripple
"""
str1 = 'This is single string'
str2 = "This is single string" 
str3 = "'This is single string'"

    # How we purform different operation in string.. Basic operations
    # 1. concatination
    # "hello" + "world" = "helloworld"

    # length of str
print(len(str1))

    #slicing
"""accessing part of a string : str[starting_ind : ending_ind]
were ending index is not included"""

str = "iamhussainisrar"
print(str[3:10])

# Practice
# Write a programe to input user first name and prints its length

userName = input("Enter your name ")
print(len(userName))

# Write a progrmae to find the occurance of $ in the string 

st1 = "hi $iam israr $hussain and i get 400$ salary in five year"
print(st1.count("$"))



