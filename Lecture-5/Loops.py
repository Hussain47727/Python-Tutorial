 #  LOOPS IN PYTHON
 # Loops are used to repeat instructions.


# WHILE LOOP 
count = 1

while count <= 5 :
    print("print", count)
    count += 1

print(count)

reverse = 5

while reverse >= 1:
    print(reverse)
    reverse -= 1
print(reverse)

   # PRACTICE QUESTIONS
# 1.. PRINT NUMBERS FROM 1 TO 100.

n = 1

while n <= 100:
    print(n)
    n += 1


# 2.. PRINT NUMBERS FROM 100 TO 1.

i = 100

while i >= 1:
    print(i)
    i -= 1


# 3.. PRINT THE MULTIPLICATION TABLE  OF A NUMBER N

# lets print a table of 3
 
# table = int(input("Enter the number you want to print the table"))
table = 3
i = 1

while i <= 10:
    print(table * i)
    i += 1

# 4..PRINT THE ELEMENTS OF THE FOLLOWING LIST USING LOOP

nums = []

idx = 0

while idx < len(nums):
    print(nums[idx])
    idx += 1

# 5..SEARCH FOR A NUMBER X IN THIS TUPLE USING LOOP:
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

search = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

 # here we will search for 25

index = 0

x = 25

while index < len(search):
    if(search[index] == x):
        print(x, "is found at index", index)
    index += 1
