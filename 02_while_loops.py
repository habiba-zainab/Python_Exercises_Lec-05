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

print("\n--- Q3: Factorial ---")

n = 5
result = n
current = n
print("Calculating", str(n) + "!")

while current >= 1 :
    print(str(result), "×", current, "=", result * current)
    result = result * current
    current -= 1

print()
print(str(n) + "! =", result)

# ----------------------------------------------------------

# ==========================================================
# PART B:   Practical While Applications
# ==========================================================

# Q4: Number guessing game (simplified)
#    Secret number = 7
#    User has 5 attempts
#    Give hints (higher / lower)
#    (Use predefined guesses for practice)

print("\n--- Q4: Number Guessing ---")

secret = 7
guesses = [5, 8, 7]
attempt = 0

print("Guess the number (1 - 10): ")

while attempt < len(guesses) :
    guess = guesses[attempt]
    attempt += 1
    print("Attempt " + str(attempt) + ":", guess)
    if guess == secret :
        print("Correct! You won in", attempt, "attempts!")
        break
    elif guess < secret :
        print("Too low!")
    else: 
        print("Too high!")

# ----------------------------------------------------------

# Q5:  Fibonacci sequence
#    Generate first N Fibonacci numbers
#    N = 10 
#    Show sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

print("\n--- Q5: Fibonacci Sequence ---")

n = 10 
a = 0
b = 1
count = 0
print("First", n, "Fibonacci numbers: ")

while count < n :
    print(a, end=", " if count < n - 1 else "")
    next_val = a + b
    a = bb = next_val
    count += 1
print()

# ----------------------------------------------------------

# ==========================================================
# PART C:      Loop Control
# ==========================================================

# Q6:  while with break - find first divisible
#    Given a number, 
#            find first number divisible by both 3 and 5
#    Start from 1
#    Break when found

print("\n--- Q6: while with break ---")

num = 1

print("Finding first number divisible by both 3 and 5: ")

while True :
    if num % 3 == 0 and num % 5 == 0 :
        print("Checking: ", num, "✓")
        print("\nFound: ", num)
        break
    else: 
        print("Checking: ", num, "✗")
        num += 1

# ----------------------------------------------------------

# Q7:  while with continue - skip even numbers
#    Print odd numbers from 1 to 20
#    Use continue to skip even numbers
