"""
Python | Sort Python Dictionaries by Key or Value
There are two elements in a Python dictionary-keys and values. 
You can sort the dictionary by keys, values, or both. In this article, 
we will discuss the methods of sorting dictionaries by key or value using Python.
"""

def sort_dictionary(my_dict):
    keys = list(my_dict.keys())
    keys.sort()
    sorted_dict = {key: my_dict[key] for key in keys}
    return sorted_dict

my_dict = {'alice': 10, 'bob': 9, 'charlie': 15, 'david': 2, 'emma': 32}
print(sort_dictionary(my_dict))
