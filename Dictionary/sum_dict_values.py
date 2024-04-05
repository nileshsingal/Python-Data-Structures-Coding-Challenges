"""
Python program to find the sum of all items in a dictionary
Given a dictionary in Python, write a Python program to find the sum of all items in the dictionary.

Examples: 

Input : {‘a’: 100, ‘b’:200, ‘c’:300}
Output : 600

Input : {‘x’: 25, ‘y’:18, ‘z’:45}
Output : 88
"""

def sum_dict_values(my_dict):
    values = list(my_dict.values())
    return sum(values)
    
my_dict = {'a': 100, 'b':200, 'c':300}
print(sum_dict_values(my_dict))


#2
def sum_dict_values(my_dict):
    value_list = []
    
    for i in my_dict:
        value_list.append(my_dict[i])
    return sum(value_list)

my_dict = {'a': 100, 'b':200, 'c':300}
print(sum_dict_values(my_dict))


#3
def sum_dict_values(my_dict):
    value_sum = 0
    for i in my_dict.values():
        value_sum += i
    return value_sum

my_dict = {'a': 100, 'b':200, 'c':300}
print(sum_dict_values(my_dict))