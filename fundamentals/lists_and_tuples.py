"""
========================================
        PYTHON LISTS & TUPLES
========================================
Author  : Riyaz
Purpose : Learn List & Tuple in Python
========================================
"""

# ---------------------------------------
# 1. LIST (Mutable)
# ---------------------------------------
print("\n--- List Basics ---")

marks = [23, 35.5, 99.5, 88.9]
print("Marks List :", marks)
print("Type        :", type(marks))
print("First Value :", marks[0])
print("Length      :", len(marks))

# Mixed data types in list
student = ["Karan", 89, "Kolkata"]
print("\nStudent List :", student)

# Modify list element (mutable)
student[2] = "Delhi"
print("Updated Student List :", student)

# ---------------------------------------
# 2. LIST SLICING
# ---------------------------------------
print("\n--- List Slicing ---")
print("marks[0:3]  :", marks[0:3])
print("marks[3:]   :", marks[3:])
print("marks[-3:]  :", marks[-3:])

# ---------------------------------------
# 3. LIST METHODS
# ---------------------------------------
print("\n--- List Methods ---")

numbers = [2, 1, 3]
print("Original List :", numbers)

numbers.append(4)
print("After append  :", numbers)

numbers.sort()
print("After sort    :", numbers)

numbers.sort(reverse=True)
print("Reverse sort  :", numbers)

numbers.reverse()
print("After reverse :", numbers)

numbers.insert(2, 34)
print("After insert  :", numbers)

numbers.remove(34)
print("After remove  :", numbers)

numbers.pop(1)
print("After pop     :", numbers)

# ---------------------------------------
# 4. TUPLE (Immutable)
# ---------------------------------------
print("\n--- Tuple Basics ---")

tup = (2, 1, 3)
print("Tuple        :", tup)
print("First Value  :", tup[0])

# Empty tuple
tup1 = ()
print("Empty Tuple  :", tup1)
print("Type         :", type(tup1))

# Single element tuple
tup2 = (1,)
print("Single Tuple :", tup2)

# ---------------------------------------
# 5. TUPLE SLICING & METHODS
# ---------------------------------------
print("\n--- Tuple Operations ---")
print("tup[0:1] :", tup[0:1])
print("tup[1:]  :", tup[1:])

# Tuple methods
print("Index of 1 :", tup.index(1))
print("Count of 2 :", tup.count(2))

# ---------------------------------------
# END OF FILE
# ---------------------------------------
print("\n=== End of Lists & Tuples ===")
