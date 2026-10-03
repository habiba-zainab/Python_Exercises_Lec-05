"""

=========================================================================
   LECTURE 05 - SET 03 :   LOOPS WITH COLLECTIONS
   Topics : Loops with Lists, Tuples, Dictionaries, Sets, Comprehensions
   Total Questions :  
=========================================================================

"""

# ==========================================================
# PART A:   Iterating Basic Collections
# ==========================================================

# Q1: Loop through tuple
#    Given: 
#          coordinates = (10, 20, 30, 40, 50)
#    Calculate sum and average
#    Find index of maximum value

print("\n--- Q1: Loop through Tuple ---")

coordinates = (10, 20, 30, 40, 50)
print("Coordinates: ", coordinates)

total_sum = 0
max_val = coordinates[0]
max_idx = 0

for idx, val in enumerate(coordinates) :
    total_sum += val
    if val > max_val :
        max_val = val
        max_idx = idx

avg_val = total_sum / len(coordinates) 

print("Sum: ", total_sum)
print("Average: ", avg_val)
print("Maximum: ", max_val, "at index", max_idx)

# ----------------------------------------------------------

# Q2: Loop through dictionary - keys, values, items
#    Given: 
#      student = {'name' : 'Katherine', 'age' : 20, 
#                  'grade' : 'A', 'gpa' : 3.8}
#    Print keys, values, and items seperately

print("\n--- Q2: Loop through Dictionary ---")

student = {'name' : 'Katherine', 'age' : 20, 'grade' : 'A', 'gpa' : 3.8}

print("Keys: ")
for key in student.keys() :
    print("-", key)

print("\nValues: ")
for value in student.values() :
    print("-", value) 

print("\nItems: ")
for key, value in student.items() :
    print(key + ":", value)

# ----------------------------------------------------------

# Q3: Loop through set 
#    Given:
#          unique_nums = {5, 2, 8, 1, 9, 3}
#    Find sum, max, min
#    Create sorted list from set

print("\n--- Q3: Lopp thorugh Set ---")

unique_nums = {5, 2, 8, 1, 9, 3}

print("Set: ", unique_nums)

total_set_sum = 0
set_max = None
set_min = None

for num in unique_nums :
    total_set_sum += num
    if set_max is None or num > set_max :
        set_max = num
    if set_min is None or num < set_min :
        set_min = num

print("Sum: ", total_set_sum)
print("Max: ", set_max)
print("Min: ", set_min)
print("Sorted: ", sorted(list(unique_nums)))

# ----------------------------------------------------------

# ==========================================================
# PART B:   Data Transformation (Comprehensions)
# ==========================================================

# Q4: Loop through list and modify
#    Given: 
#           numbers = [1, 2, 3, 4, 5]
#    Create new list with each number squared
#    Do with both loop and list comprehension

print("\n--- Q4: Loop & Modify List ---")

numbers = [1, 2, 3, 4, 5]

print("Original: ", numbers)

squared_loop = []
for num in numbers :
    squared_loop.append(num * num)
print("\nUsing loop: ")
print("Squared: ", squared_loop)

squared_comp = [num * num for num in numbers]
print("\nUsing comprehension: ")
print("Squared: ", squared_comp)

# ----------------------------------------------------------

# Q5: List comprrehension - filter even numbers
#    Given: 
#          numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    Create list of even numbers
#    Create list of squares of odd numbers
#    Use comprehension

print("\n--- Q5: List Comprehension ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original: ", numbers)

evens = [num for num in numbers if num % 2 == 0]
odd_squares = [num * num for num in numbers if num % 2 != 0]

print("Even numbers: ", evens)
print("Squares of odd: ", odd_squares)

# ----------------------------------------------------------

# ==========================================================
# PART C:   Zip & Nested Sequence Loops 
# ==========================================================