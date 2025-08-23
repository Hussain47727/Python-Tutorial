  # LOOPS IN PYTHON 
 # Loops are used for squential traversal. For traversing list, string, tuple etc.


   # FOR LOOP

# HOW TO USE FOR LOOP / STRUCTURE OF FOR LOOP

veggies = ["potato", "brijal", "ladyfinger", "cucumber"]
  # using for loop we print the each element from the list
for el in veggies :  # el is varaible we can use any var like val, item etc and in is keyword
    print(el)

# another example using tuple

tuple = (1, 2, 3, 4, 5)
for val in tuple:
    print(val)

# Whenever we use for or while loop we can use (else) for optional to execute some work after ending if loop

str = "Israr Hussan"
for dig in str:
    print(dig)
else:
    print("All digits are printed")

       # LETS PRACTICE
# USING FOR LOOP
# PRINT THE ELEMENT OF GIVE LIST [1,4,9,16,34, 54, 98, 90, 45] USING A LOOP

list = [1,4,9,16,34, 54, 98, 90, 45]
for ele in list:
    print(ele)

# SEARCH FOR A NUMBER X (MEANS ANY NUMBER) IN THIS TUPLE (1,4,9,16,34, 54, 98, 90, 45) USING LOOP

nums = (1,4,9,16,34, 54, 98, 90, 45)
x = 34
idx = 0
for val in nums:
    if(val == x):
        print("number founded at idx", idx)
    idx += 1
