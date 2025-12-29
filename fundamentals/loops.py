"""
loops.py

This module demonstrates the usage of Python loops:
- while loop
- for loop
- break, continue, pass statements
- forward and reverse iteration

Author: Riyaz
Purpose: Beginner-friendly explanation of looping concepts
"""

# --------------------------------------------------
# 1. Infinite loop with controlled exit using break
# --------------------------------------------------

count = 0
while True:
    count += 1
    print("Hello")
    if count == 5:
        break  # exits the infinite loop

# --------------------------------------------------
# 2. Print numbers from 1 to 5 using while loop
# --------------------------------------------------

i = 1
while i <= 5:
    print(i)
    i += 1  # increment to avoid infinite loop

# --------------------------------------------------
# 3. Print numbers from 5 to 1 using while loop
# --------------------------------------------------

i = 5
while i >= 1:
    print(i)
    i -= 1  # decrement

# --------------------------------------------------
# 4. Iterate over a list using while loop (forward)
# --------------------------------------------------

numbers = [1, 4, 9, 16, 25]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# --------------------------------------------------
# 5. Iterate over a list using while loop (reverse)
# --------------------------------------------------

i = len(numbers) - 1
while i >= 0:
    print(numbers[i])
    i -= 1

# --------------------------------------------------
# 6. break and continue example
# --------------------------------------------------

i = 1
while i <= 5:
    if i == 2:
        i += 1
        continue  # skip printing when i == 2

    print("num", i)

    if i == 4:
        break  # stop loop completely

    i += 1

# --------------------------------------------------
# 7. for loop with list (recommended approach)
# --------------------------------------------------

items = [1, 2, 3]
for item in items:
    print(item)

# --------------------------------------------------
# 8. for loop using range()
# --------------------------------------------------

# Prints 0 to 4
for i in range(5):
    print(i)

# Prints 1 to 4
for i in range(1, 5):
    print(i)

# Prints odd numbers: 1, 3
for i in range(1, 5, 2):
    print(i)

# Prints values from 100 to 10 with step -10
for i in range(100, 0, -10):
    print(i)

# --------------------------------------------------
# 9. pass statement example
# --------------------------------------------------

for i in range(5):
    pass  # placeholder, loop does nothing for now

print("Working")
