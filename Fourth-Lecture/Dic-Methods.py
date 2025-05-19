 # METHODS IN DICTIONARY
# There are many types of methods but here we discuss some basic and importand methods

# my.Dict.keys()
# This method returns all the key from the dictionary.. for example

student = {
    "name" : "israr",
    "age" : 45,
    "class" : "third year"
}
print(student)
print((student.keys()))

# myDic.values()
# This method returns all the values from the dictionary... for example

print(student.values())
print(list(student.values()))

# myDic.items()
# This method ruturn all (key : values) pairs as tuple

print(student.items())
print(list(student.items()))

# myDic.get("key")
# This method return the key according to value

print(student.get("name"))

# myDic.update("new key")
# This method is used to add a new pair in dictionary

print(student.update({"gender" : "male"}))
print(student)