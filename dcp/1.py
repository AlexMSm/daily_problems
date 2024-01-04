# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


list = [10, 15, 3, 7, 10, 14]
k = 17

x = 0
for i in list:
    for j in list[x:]:
        if (i + j) == k:
            print(i, j)
    x+=1

