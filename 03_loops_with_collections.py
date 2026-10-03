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
