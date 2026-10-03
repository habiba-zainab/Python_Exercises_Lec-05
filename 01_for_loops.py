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
