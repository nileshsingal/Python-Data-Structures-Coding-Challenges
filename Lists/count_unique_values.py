#How to count unique values inside a list

#1
def count_unique_values(input_list):
    temp_list = []
    
    for i in input_list:
        if i not in temp_list:
            temp_list.append(i)
    return len(temp_list)


input_list = [1, 2, 2, 5, 8, 4, 4, 8]
print(count_unique_values(input_list))


#2
def count_unique_values(input_list):
    return len(set(input_list))

input_list = [1, 2, 2, 5, 8, 4, 4, 8]
print(count_unique_values(input_list))

#3
def count_unique_values(input_list):
    new_set = [x for i,x in enumerate(input_list) if x not in input_list[:i]]
    return len(new_set)

input_list = [1, 2, 2, 5, 8, 4, 4, 8]
print(count_unique_values(input_list))
