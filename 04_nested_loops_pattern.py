"""

===========================================================
   LECTURE 05 - SET 04 :   NESTED LOOPS PATTERNS
   Topics :     Nested Loops, Pattern Printing
   Total Questions :  
============================================================

"""

# ==========================================================
# PART A:   Basic Geometric Patterns
# ==========================================================

# Q1: Rectangle of stars
#    Print rectangle of stars
#    Rows = 4,  Columns = 6

print("\n--- Q1: Rectangle ---")

rows = 4
columns = 6

for i in range(rows) :
    for j in range(columns) :
        print("*", end=" ")
    print()

# ----------------------------------------------------------