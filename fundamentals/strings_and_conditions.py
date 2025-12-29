"""
strings_and_conditions.py

This script demonstrates:
1. String creation and operations
2. String concatenation and slicing
3. Conditional statements (if-elif-else)

Author  : Riyaz
Purpose : Beginner-friendly Python examples
"""

# --------------------------------------------------
# 1. STRING OPERATIONS
# --------------------------------------------------

# Creating a string with a newline character
str1 = "Hello World.\nThis is Python"
print(str1)

# String concatenation
str2 = "Hello "
str3 = "World"
result = str2 + str3
print(result)

# String slicing
print(result[0:3])   # Characters from index 0 to 2
print(result[3:])    # Characters from index 3 till end


# --------------------------------------------------
# 2. CONDITIONAL STATEMENTS
# --------------------------------------------------

# Example 1: Age classification
age = 23

if age >= 18:
    print("You are an adult")
elif 10 <= age < 18:
    print("You are a teenager")
else:
    print("Senior citizen")


# --------------------------------------------------
# 3. GRADING SYSTEM USING INPUT
# --------------------------------------------------

marks = int(input("Enter your marks: "))

if marks >= 60:
    print("Grade A")
elif marks >= 40:
    print("Grade B")
else:
    print("Grade C")
