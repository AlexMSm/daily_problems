# Given an array of integers, return a new array such that each element at index i 
# of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. 

# If our input was [3, 2, 1], 
# the expected output would be [2, 3, 6].

list = [1, 2, 3, 4, 5]
x = 0
length = len(list) - 1
index_list = [x for x in range(0, length)]
new_list = []

for i in list:
    num = 1
    for j in index_list:
        if j != x:
            num *= list[i]
    new_list[x] = num
    x += 1

print(new_list)