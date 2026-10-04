"""

===========================================================
   LECTURE 05 - SET 04 :   NESTED LOOPS PATTERNS
   Topics :     Nested Loops, Pattern Printing
   Total Questions :  06
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

print("\n--- Q3: Centered Pyramid ---")

height = 5

for i in range(height) :
    for j in range(height - i - 1) :
        print(" ", end=" ")
    for k in range(2 * i + 1) :
        print("*", end=" ")
    print()

# ----------------------------------------------------------

# Q4: Diamond pattern
#    Print diamond shape 
#    Middle row has 9 stars

print("\n--- Q4: Diamond Pattern ---")

height = 5

for i in range(height) :
    for j in range(height - i - 1) :
        print(" ", end=" ")
    for k in range(2 * i + 1) :
        print("*", end=" ")
    print()

for i in range(height - 2, -1, -1) :
    for j in range(height - i - 1) :
        print(" ", end=" ")
    for k in range(2 * i + 1) :
        print("*", end=" ")
    print()

# ----------------------------------------------------------

# ==========================================================
# PART C:   Mathematical Number Patterns
# ==========================================================

# Q5: Number Pyramid
#    Print numbers in pyramid form
#    Rows = 5

print("\n--- Q5: Number Pyramid ---")

rows = 5

for i in range(1, rows + 1) :
    for j in range(1, i + 1) :
        print(j, end=" ")
    print()

# ----------------------------------------------------------

# Q6: Floyd's triangle
#    Print Floyd's triangle with numbers
#    Rows = 5

print("\n--- Q6: Floyd's Triangle ---")

rows = 5
num = 1

for i in range(1, rows + 1) :
    for j in range(1, i + 1) :
        print(num, end=" ")
        num += 1
    print()

# ----------------------------------------------------------