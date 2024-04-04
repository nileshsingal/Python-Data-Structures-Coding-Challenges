#You are given a list of elements. Write a Python function to test if all elements in the list fall within a specified range.

#1
def test_list_elements_in_range(arr, start, end):
    for i in arr:
        if i < start or i > end:
            return False
    return True

test_list = [4, 5, 6, 7, 3, 9]
i, j = 3, 10

print(test_list_elements_in_range(test_list, i, j))


#2
def test_list_elements_in_range(arr, start, end):
    return all(element >= start and element <= end for element in arr)

test_list = [4, 5, 6, 7, 3, 9]
i, j = 3, 10

print(test_list_elements_in_range(test_list, i, j))   
     