 # DICTIONARY IN PYTHON

#Dictionaries are used to store data values in key : value pairs

#They are unordered, mutable(changeable) and don't allow duplicate keys

dic = {
    "name" : "israr Hussain",
    "age" : 12,
    "class" : "13 year",
    "subjects" : ["opps", "dld", "database", "linear algebra", "multivariable claclus"]
    }
print(dic)
print(type(dic))

 #Nested Dictionaries
# Nested Dictionaries are used to make nesting list in dictionaries.. for example
student ={
  "name" : "Rahus kumar",
  "subjects" : {     
    "phy" : 80,
    "che" : 30,
    "bio" : 90
  }
 }
 # How to print nested dic 
print(student["subjects"])
 # How to print specific item in nexted dic
print(student["subjects"]["bio"])