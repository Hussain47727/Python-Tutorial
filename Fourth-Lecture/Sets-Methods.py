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
