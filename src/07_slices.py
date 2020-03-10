"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1:2][0])

# Output the second-to-last element: 9
# print(a[-2:-1][0])
print(a[-2:-3:-1][0])

# Output the last three elements in the array: [7, 9, 6]
print(a[-3:])

# Output the two middle elements in the array: [1, 7]
ary_len = len(a)
half_ary_len = int(ary_len/2)
print(a[half_ary_len-1:(half_ary_len+1)])

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[0:-1])
# [ 2,  4,  1,  7,  9,  6] This is the original list
#   0,  1,  2,  3,  4,  5  The forward index for the list
#  -6, -5, -4, -3, -2, -1  The backward index for the list
# so the first element's name is: 0 or -6, but 0 is the name of first element no matter the size of the list
# the last element's name is 5 or -1, but -1 is the name of the last element no matter the size of the list
# so from 1st to 2nd from last no matter the size of the list is: 0:-1:1


# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[8-1:12])
