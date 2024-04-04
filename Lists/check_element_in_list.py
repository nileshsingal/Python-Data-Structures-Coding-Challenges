"""
Check if element exists in list in Python.

Input: test_list = [1, 6, 3, 5, 3, 4]
            3  # Check if 3 exist or not.
Output: True
Explanation: The output is True because the element we are looking is exist in the list.
"""
#1
def check_element_in_list(lst, element):
    if element in lst:
        return True
    else:
        return False
        
test_list = [1, 6, 5, 3, 4]
search = 7

print(check_element_in_list(test_list, search))


#2.
def check_element_in_list(lst, element):
    return any(item == element for item in lst)
        
test_list = [1, 6, 5, 3, 4]
search = 7

print(check_element_in_list(test_list, search))
