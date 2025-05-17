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