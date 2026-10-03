"""

===========================================================
   LECTURE 05 - SET 02 :        WHILE LOOPS
   Topics : While Loops - Basics, Conditions, Loop Control
   Total Questions :  09
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
# PART C:   Loop Control (break & continue)
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

print("\n--- Q7: while with continue ---")

num = 1
count = 0 

print("Odd numbers from 1 to 20: ")

while num <= 20 :
    if num % 2 == 0 :
        num += 1
        continue
    print(num, end=" ")
    count += 1
    num += 1
print()
print("\nTotal odd numbers: ", count)

# ----------------------------------------------------------

# ==========================================================
# PART D:   Input Checking & Digit Extraction  
# ==========================================================

# Q8:  Input validation loop
#    Keep asking for age until valid input
#    Valid:  between 1 and 120
#    (Use predefined inputs for practice)

print("\n--- Q8: Input Validation ---")

test_inputs = [0, 150, 25]
index = 0

print("Enter your age (1 - 120): ")

while index < len(test_inputs) :
    age = test_inputs[index]
    print("Input: ", age)
    if 1 <= age <= 120 :
        print("Valid age entered: ", age)
        break
    else: 
        print("Invalid! Age must be between 1 and 120.")
        print()
    index += 1

# ----------------------------------------------------------

# Q9: Digit sum calculator
#    Given a number, find sum of its digits
#    Use while loop to extract digits
#    Example: 12345 → 1 + 2 + 3 + 4 + 5 = 15

print("\n--- Q9: Digit Sum ---")

number = 12345
original = number
digit_sum = 0

print("Number: ", number)
print("\nExtracting digits: ")

while number > 0 :
    digit = number % 10
    digit_sum += digit
    print(str(number), "→", digit, "(sum: ", str(digit_sum) + ")")
    number = number // 10
print("\nSum of digits: ", digit_sum)

# ----------------------------------------------------------