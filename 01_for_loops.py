"""

===========================================================
   LECTURE 05 - SET 01 :        FOR LOOPS
   Topics : For Loops - Basics, range(), enumerate(), zip()
   Total Questions :  
============================================================

"""

# ==========================================================
# PART A:   Basic For Loops & Iterations
# ==========================================================

# Q1: Basic for loop - iterate through list
#    Given: 
#          fruits = ['orange', 'litchi', 'papaya', 'kiwi']
#    Print each fruit on a new line
#    Also print with numbering (1. orange, 2. litchi, etc.)

print("\n--- Q1: Basic For Loop ---")

fruits = ['orange', 'litchi', 'papaya', 'kiwi']

print("Fruits: ")
for fruit in fruits:
    print(fruit)

print("\nNumbered: ")
for i in range(len(fruits)) :
    print(str(i + 1) + ".", fruits[i])

# ----------------------------------------------------------

# Q2: Sum and average using for loop 
#    Given: 
#         numbers = [12, 45, 23, 67, 34, 89, 11, 56]
#    Calculate:
#    - Sum of all numbers
#    - Average
#    - Count of numbers
#    Use loop (don't use sum() function initially)

print("\n--- Q2: Sum & Average ---")

numbers = [12, 45, 23, 67, 34, 89, 11, 56]
print("Numbers: ", numbers)

total = 0
count = 0
for num in numbers:
    total += num
    count += 1

print("Sum: ", total)
print("Count: ", count)
print("Average: ", total / count)

# ----------------------------------------------------------

# Q3: Find max and min using loop
#    Given: 
#          scores = [78, 92, 85, 88, 76, 95, 89]
#    Find maximum and minimum without using max() or min()
#    Track with iterations found the max / min

print("\n--- Q3: Max & Min ---")

scores = [78, 92, 85, 88, 76, 95, 89]
print("Scores: ", scores)

maximum = scores[0]
max_index = 0
minimum = scores[0]
min_index = 0

for i in range(len(scores)) :
    if scores[i] > maximum :
        maximum = scores[i]
        max_index = i
    if scores[i] < minimum :
        minimum = scores[i]
        min_index = i

print("Maximum: ", maximum, "(found at index", str(max_index) + ")")
print("Minimum: ", minimum, "(found at index", str(min_index) + ")")

# ----------------------------------------------------------

# ==========================================================
# PART B:   range() Function
# ==========================================================

# Q4: Multiplication table generator 
#    Generate multiplication table for a given number
#    Input:   number = 7, range = 10
#    Format output nicely

