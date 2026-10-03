"""

===========================================================
   LECTURE 05 - SET 02 :        WHILE LOOPS
   Topics : While Loops - Basics, Conditions, Loop Control
   Total Questions :  
============================================================

"""

# ==========================================================
# PART A:   Basic While Loops
# ==========================================================

# Q1: Basic while loop - count from 1 to 10
#    Use while loop to print numbers 1 to 10
#    Also print sum of these numbers

print("\n--- Q1: Basic While Loop ---")

count = 1 
total = 0
print("Counting from 1 to 10: ")

while count <= 10 :
    print(count, end=" ")
    total += count
    count += 1

print()
print("Sum: ", total)

# ----------------------------------------------------------

# Q2: while loop with countdown
#    Create countdown from 10 to 1
#    Print "Blast off!" at the end

print("\n--- Q2: Countdown ---")

count = 10 
print("Countdown: ")

while count >= 1 :
    print(count)
    count -= 1
    print("Blast off!")

# ----------------------------------------------------------

# Q3: Factorial using while loop
#    Calculate fatorial of a number
#    Show step-by-step calculation
#    Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

