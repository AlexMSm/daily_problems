# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

integers = [3, 4, -1, 1]

new_list = []

for i in range(len(integers)):
    for j in range(i + 1, len(integers)):
        if integers[i] > integers[j]:
            # Swap the elements
            integers[i], integers[j] = integers[j], integers[i]



