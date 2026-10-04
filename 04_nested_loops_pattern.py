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

# Q2: Right-angled triangle
#    Print right-angled triangle
#    Height = 5

print("\n--- Q2: Right-angled Triangle ---")

height = 5

for i in range(1, height + 1) :
    for j in range(i) :
        print("*", end=" ")
    print()

# ----------------------------------------------------------

# ==========================================================
# PART B:   Centered Symmetric Patterns
# ==========================================================

# Q3: Pyramid of stars (centered)
#    Print centered pyramid
#    Height = 5
