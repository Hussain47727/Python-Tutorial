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


