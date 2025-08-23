# There are some basic method or fuction related to funtion we discuss below

List = [2, 1, 3]
print(List)

# 1.List append 
# by using list append we can add an element in the end of list.. for example we add 4
List.append(4)
print(List)

# 2.List sort
# By using list sort we arrange the element in order like acending to decending
# First we print in ascending

print(List.sort())
print(List)

# now in decending
print(List.sort(reverse=True))
print(List)

# 3. List.reverse
# List.reverse is basically used to reverse all the list 
print(List.reverse())
print(List)

# 4. List.insert
# it is similar to list.append but it insert element in a particular index

List.insert(2, "ahmad")
print(List)

# 5. List.remove
# this method is use to remove any element from the list

List.remove(3)
print(List)

# 6. List.pop 
# this is similar to list.remove but its use to remove a particular index

List.pop(2)
print(List)


