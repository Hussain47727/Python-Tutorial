 # SETS METHOD
 # The methods or function which we use in sets are discuss below

 # 1.. set.add(el) add an element

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("hi there")
collection.add(("israr", "yawer", "hasnain"))
print(collection)

# 2.. set.remove 
# To remove element from the list
collection.remove(2)
print(collection)

# 3..set.clear
# To clear the set

collection.clear()
print(len(collection))

# 4.. set.pop
# To removes a random values
students = {"ali", "asghar", "abbas", "mujtaba"}
print(students.pop())
print(students.pop())

# 5.. set.union(set2)
# combines both set values and return new
set1 = {1, 2, 3, 4}
set2 = {4,5,6}
print(set1.union(set2))

# 6.. set.intersection(set2)
# Combine common values and return new
print(set1.intersection(set2))

     # SMALL PROBLEMS
# 1. Store following words meaning in a python dictionary
# table : "a piece of furniture", "list of facts and figure"
# cat : " a small animal "

dic = {
    'table' : ("a piece of furniture", "list of facts and figur"),
    'cat': 'a small animal'
}
print(dic)
print(type(dic))

# 2. You are given a list of students. Assume one classroom is required for 1 subject
# How many classrooms are needed by all the students.
# "python", "java", "c++", "javascript"
# "JAVA", "python", "java", "c"