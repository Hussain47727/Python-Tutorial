 # BREAK AND CONTINUE 

#  1.. BREAK : used to terminate the loop when encountered.

i = 1
while i <= 5:
    print(i)
    if( i == 3):
        break
    i += 1
print('end of loop ')

# 2.. CONTINUE : Terminate execution in the current iteration and continue of
# the loop with the next iteration

j = 1 
while j <= 5:
    if(j == 2):
        j += 1
        continue
    print(j)
    j += 1
print('j loop ending')

even = 1
while even <= 10:
    if(even % 2 == 0):
        even += 1
        continue
    print(even)
    even += 1
        
