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
        