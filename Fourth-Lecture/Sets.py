 # Sets 
# Sets is the collection of unordered items.
# Each element is the set must be unique and immutable.

# syntex : variable name = {}

collection = {1, 2, 2, 2, 3, 4, 5, "hello", "world"}
print(collection)
print(type(collection))

# repeated elements stored only once, so it resolved to {1, 2}
# for example if we have a set {1, 2, 2} it will print {1 ,2} only not 2 times 2

empty = set() # empty set : syntex
print(empty)
print(type(empty))