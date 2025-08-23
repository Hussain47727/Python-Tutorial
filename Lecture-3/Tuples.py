 # Tuples
# A built-in data type that lets us create immutable sequences of values.
# A tuple is basically same as list but there is bit difference list is mutable
# and tuple is immutable.

tup = (2, 3, 5, 6)
print(tup)
print(type(tup))
print([1])

 # Methods in Tuple
 # Tuple.index(el) .. Returns index of first occurrence
print(tup.index(2))
 # Tuple.count(el) .. Counts total occurrences
print(tup.count(2))

# probles
# Q1.. WAP to ask the user to enter names of their 3 favorite movies and store them in a list

movie1 = input("please enter the first movie name")
movie2 = input("please enter the second movie name")
movie3 = input("please enter the third movie name")

list = [movie1, movie2, movie3]
print(list)

      # OR

# movies = []
# m1 = input('enter 1st : ')
# m2 = input('enter 2nd : ')
# m3 = input('enter 3rd : ')

# movies.append(m1)
# movies.append(m2)
# movies.append(m3)

# print(movies)

# Q2.. WAP to check if a list contains a palindrom of elements. (Hint: use copy() method)
 
list1 = [1,2,3,3,1]

list_copy = list1.copy()
list_copy.reverse()

if(list1 == list_copy):
    print("List is palindrom")
else:
    print("not palindrom")

print(list1)

# Q3.. WAP to count the number of students with the "A" grade in the following tuple

grade = ("c", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

# Q4 store the above values in a list  and sort them from "A" to "D"

sort = ["c", "D", "A", "A", "B", "B", "A"]
sort.sort()
print(sort)
 

    #   THE END