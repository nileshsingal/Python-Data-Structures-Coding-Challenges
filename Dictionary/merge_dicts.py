"""
Python | Merging two Dictionaries
In Python, a dictionary is a data structure that contains the element in the key-value pair in which keys are used to access the values in the dictionary. 
Python has some inbuilt dictionaries like defaultdict. 
In this article, we will see various ways to merge two dictionaries.
"""

#Using Update
def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1
    

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print(merge_dicts(dict1, dict2))


#Using unpacking operator
def merge_dicts(dict1, dict2):
    res = {**dict1, **dict2}
    return res

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print(merge_dicts(dict1, dict2))

#Merge Dictionaries Using | 
#we are using | operator to merge two dictionaries.
def merge_dicts(dict1, dict2):
    res = dict1 | dict2
    return res

dict1 = {'x': 10, 'y': 8} 
dict2 = {'a': 6, 'b': 4} 
print(merge_dicts(dict1, dict2))


#Using For loop
def merge_dicts(dict1, dict2):
    for key in dict2.keys():
        dict1[key] = dict2[key]
    return dict1

dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
print(merge_dicts(dict1, dict2))


#Using dict constructor
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
print(merge_dicts(dict1, dict2))


"""
This method uses the dict() constructor with the union operator (|) to merge two dictionaries. 
The union operator combines the keys and values of the two dictionaries, 
and any common keys in the two dictionaries take the value from the second dictionary.
"""

def merge_dicts(dict1, dict2):
    result = dict(dict1.items() | dict2.items())
    return result

dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
print(merge_dicts(dict1, dict2))
