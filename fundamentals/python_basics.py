"""
========================================
        PYTHON BASICS - ONE FILE
========================================
Author  : Riyaz
Purpose : Beginner-friendly Python notes
========================================
"""

# ---------------------------------------
# 1. PRINTING OUTPUT
# ---------------------------------------
print("\n--- Printing Output ---")
print("Hello World")
print(23)

# ---------------------------------------
# 2. VARIABLES & DATA TYPES
# ---------------------------------------
print("\n--- Variables & Data Types ---")
name = "Riyaz"
age = 29
price = 23.44

age2 = age

print("Name :", name)
print("Age  :", age)
print("Age2 :", age2)

# ---------------------------------------
# 3. TYPE CHECKING
# ---------------------------------------
print("\n--- Type Checking ---")
print("Type of name  :", type(name))
print("Type of age   :", type(age))
print("Type of price :", type(price))

# ---------------------------------------
# 4. BOOLEAN & NONE TYPE
# ---------------------------------------
print("\n--- Boolean & None ---")
old = False
value = None

print("Old value type   :", type(old))
print("None value type  :", type(value))

# ---------------------------------------
# 5. ARITHMETIC OPERATORS
# ---------------------------------------
print("\n--- Arithmetic Operators ---")
a = 3
b = 2

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Modulus        :", a % b)
print("Floor Division :", a // b)
print("Power          :", a ** b)

# ---------------------------------------
# 6. RELATIONAL OPERATORS
# ---------------------------------------
print("\n--- Relational Operators ---")
a = 2
b = 3

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# ---------------------------------------
# 7. ASSIGNMENT OPERATORS
# ---------------------------------------
print("\n--- Assignment Operators ---")
a = 2
b = 3

a += b
print("a += b :", a)

# ---------------------------------------
# 8. LOGICAL OPERATORS
# ---------------------------------------
print("\n--- Logical Operators ---")
val1 = True
val2 = False

print("NOT False :", not False)
print("NOT True  :", not True)
print("AND       :", val1 and val2)
print("OR        :", val1 or val2)

# ---------------------------------------
# 9. TYPE CONVERSION (AUTOMATIC)
# ---------------------------------------
print("\n--- Type Conversion (Automatic) ---")
a = 1
b = 2.0

print("Sum :", a + b)

# ---------------------------------------
# 10. TYPE CASTING (MANUAL)
# ---------------------------------------
print("\n--- Type Casting (Manual) ---")
a = 1
b = "2"

c = int(b)
print("Sum after casting :", a + c)

a = 3.12
a = str(a)
print("Type after casting :", type(a))

# ---------------------------------------
# 11. USER INPUT
# ---------------------------------------
print("\n--- User Input ---")
a = int(input("Enter the value of a: "))
print("You entered :", a)

# ---------------------------------------
# END OF FILE
# ---------------------------------------
print("\n=== End of Python Basics ===")
