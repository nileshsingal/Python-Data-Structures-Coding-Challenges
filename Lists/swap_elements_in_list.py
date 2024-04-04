"""
Python Program to Swap Two Elements in a List
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 

Examples:  

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
"""
#1
def swap_elements_in_list(lst, pos1, pos2):
    lst[pos1-1], lst[pos2-1] = lst[pos2-1], lst[pos1-1]
    return lst

lst = [23, 65, 19, 90]
pos1, pos2  = 1, 3
print(swap_elements_in_list(lst, pos1, pos2))

#2
def swap_positions(lst, pos1, pos2):
    for i,value in enumerate(lst):
        if i==pos1:
            pos1_value = value
        if i==pos2:
            pos2_value = value
    lst[pos1] = pos2_value
    lst[pos2] = pos1_value
    
    return lst

lst = [23, 65, 19, 90]
pos1, pos2  = 1, 3
print(swap_positions(lst, pos1-1, pos2-1))

