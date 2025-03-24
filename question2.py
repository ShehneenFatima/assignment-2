#2. Write a Python program to multiplies all the items in a list.
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage
numbers = [2, 3, 4, 5]
print("Product of list elements:", multiply_list(numbers))
#3. Write a Python program to get the smallest number from a list.
def find_smallest_number(numbers):
    return min(numbers)  # Using the built-in min() function

# Example usage
numbers = [5, 2, 8, 1, 9, 3]
print("Smallest number in the list:", find_smallest_number(numbers))

#4. Write a Python program to remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))  # Convert list to set to remove duplicates, then back to list

# Example usage
numbers = [1, 2, 3, 4, 2, 3, 5, 6, 1]
print("List after removing duplicates:", remove_duplicates(numbers))

#5. Write a Python program to clone or copy a list.
def clone_list(lst):
    return lst.copy()  # Creates a shallow copy

# Example usage
original_list = [1, 2, 3, 4, 5]
cloned_list = clone_list(original_list)
print("Original List:", original_list)
print("Cloned List:", cloned_list)

#6. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : [&#39;Red&#39;, &#39;Green&#39;, &#39;White&#39;, &#39;Black&#39;, &#39;Pink&#39;, &#39;Yellow&#39;]
#Expected Output : [&#39;Green&#39;, &#39;White&#39;, &#39;Black&#39;]
def remove_specified_elements(lst):
    indices_to_remove = {0, 4, 5}  # Use a set for faster lookup
    return [lst[i] for i in range(len(lst)) if i not in indices_to_remove]

# Sample List
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
filtered_colors = remove_specified_elements(colors)

print("List after removal:", filtered_colors)

