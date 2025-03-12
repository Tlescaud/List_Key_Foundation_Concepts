#EXERCISE 1 - remove duplicates

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage
original_list = [1, 2, 2, 3, 4, 3, 5, 1]
new_list = remove_duplicates(original_list)
print(new_list)  # Output: [1, 2, 3, 4, 5]


#EXCERCISE 2 - rotate list

def rotate_list(lst, k):
    # Ensure k is within the bounds of the list length
    k = k % len(lst)

    # Rotate the list by slicing
    return lst[-k:] + lst[:-k]


# Example usage
original_list = [1, 2, 3, 4, 5, 6, 7]
rotated_list = rotate_list(original_list, 3)
print(rotated_list)  # Output: [5, 6, 7, 1, 2, 3, 4]

# EXERCISE 3 - flatten a nested list

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # Recursively flatten the sublist
        else:
            flat_list.append(item)
    return flat_list

# Example usage
nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
flat_list = flatten(nested_list)
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

'''Recursion: The function flatten uses recursion to handle nested lists. 

If an item in the list is itself a list, the function calls itself to flatten that sublist and extends the flat_list
 
with the flattened sublist.

Base Case: If the item is not a list, it is added directly to the flat_list.

This approach ensures that all nested lists are flattened, regardless of their depth.'''

# EXERCISE 4 - find second largest number in a list


def second_largest(lst):
    # Remove duplicates by converting the list to a set
    unique_lst = list(set(lst))

    # If there are fewer than 2 unique numbers, return None
    if len(unique_lst) < 2:
        return None

    # Sort the unique list in descending order
    unique_lst.sort(reverse=True)

    # The second largest number is the second element in the sorted list
    return unique_lst[1]


# Example usage
numbers = [4, 2, 7, 3, 7, 5, 9, 4]
result = second_largest(numbers)
print(result)  # Output: 7

'''Remove Duplicates: Convert the list to a set to remove duplicates, then convert it back to a list.

Check Length: If there are fewer than two unique numbers, return None, as there is no second-largest number.

Sort: Sort the unique list in descending order.

Return Second Largest: Return the second element in the sorted list, which is the second-largest number.

This function ensures that the second-largest number is found even if there are duplicates in the original list.'''

# EXERCISE 5 - USE Python functions to interleave two list and append any remaining elements from the longer list

def interleave_lists(lst1, lst2):
    interleaved_list = []
    # Get the length of the shorter list
    min_length = min(len(lst1), len(lst2))

    # Interleave elements from both lists
    for i in range(min_length):
        interleaved_list.append(lst1[i])
        interleaved_list.append(lst2[i])

    # Append remaining elements from the longer list, if any
    if len(lst1) > len(lst2):
        interleaved_list.extend(lst1[min_length:])
    else:
        interleaved_list.extend(lst2[min_length:])

    return interleaved_list


# Example usage
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']
interleaved = interleave_lists(list1, list2)
print(interleaved)  # Output: [1, 'a', 2, 'b', 3, 'c', 'd', 'e']

'''Interleaving Elements: The function first interleaves elements from both lists up to the length of the shorter list.

Appending Remaining Elements: After interleaving, it appends any remaining elements from the longer list to the result.

Example Usage: In the example, the lists [1, 2, 3] and ['a', 'b', 'c', 'd', 'e'] are interleaved, resulting in [1, 'a', 2, 'b', 3, 'c', 'd', 'e'].

This function ensures that elements from both lists are interleaved, and any extra elements from the longer list are appended at the end.'''

