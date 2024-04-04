"""
This article focuses on one of the operations of getting the unique list from a list that contains a possible duplicated and finding its product. This operation has a large no. of applications and hence its knowledge is good to have. 
"""

def exclude_duplicate_from_list(lst):
    #return list(set(lst))
    result = []
    
    for i in lst:
        if i not in result:
            result.append(i)
    return result

def calculate_product(lst):
    prod = 1
    for i in lst:
        prod *= i
    return prod

def list_product_exclude_duplicate(lst):
    unique_list = exclude_duplicate_from_list(lst)
    product = calculate_product(unique_list)
    return product
    
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("Duplication removal list product : ", list_product_exclude_duplicate(test_list))
