# Python program to interchange first and last elements in a list
# Given a list, write a Python program to swap first and last element of the list.

# Examples: 

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

#1st approach
def swap_list(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

#2nd approach
def swap_list(lst):
    start, *middle, end = lst
    lst = [end, *middle, start]
    return lst


print(swap_list([12, 35, 9, 56, 24]))

