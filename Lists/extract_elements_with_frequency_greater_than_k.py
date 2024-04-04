"""
Extract elements with Frequency greater than K
Given a List, extract all elements whose frequency is greater than K.

Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
Output : [4, 3] 
Explanation : Both elements occur 4 times. 

Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2 
Output : [4, 3, 6] 
Explanation : Occur 4, 3, and 3 times respectively.
"""

def count(arr, element):
    total_count = 0
    for i in arr:
        if i == element:
            total_count += 1
    return total_count

def extract_elements_with_frequency_greater_then_k(arr, k):
    temp_list = []
    for i in arr:
        if count(arr,i) > k and i not in temp_list:
            temp_list.append(i)
    return temp_list

test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3
print(extract_elements_with_frequency_greater_then_k(test_list, k))
