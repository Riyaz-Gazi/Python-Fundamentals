"""
========================================
        PYTHON DICTIONARY & SET
========================================
File    : dictionary_and_set.py
Author  : Riyaz
Purpose : Learn Dictionary & Set in Python
========================================
"""

# ---------------------------------------
# 1. DICTIONARY (Mutable, Key-Value Pair)
# ---------------------------------------
print("\n--- Dictionary Basics ---")

student = {
    "name": "Riyaz",
    "cgpa": 7.8,
    "marks": [23, 23, 45, 64],
    "is_adult": True,
    12: 23.4
}

print("Dictionary :", student)
print("Marks      :", student["marks"])

# Update value
student["name"] = "Rahul"
print("Updated Name :", student)

# Add new key
student["surname"] = "Gazi"
print("After Adding Key :", student)

# ---------------------------------------
# 2. EMPTY DICTIONARY
# ---------------------------------------
print("\n--- Empty Dictionary ---")

null_dict = {}
print("Empty Dict :", null_dict)

null_dict["name"] = "Mehak"
print("After Insert :", null_dict)

# ---------------------------------------
# 3. NESTED DICTIONARY
# ---------------------------------------
print("\n--- Nested Dictionary ---")

nested_dict = {
    "name": "Riyaz",
    "cgpa": 7.8,
    "score": {
        "math_score": 23.4,
        "english_score": 29.4
    }
}

print("Math Score    :", nested_dict["score"]["math_score"])
print("English Score :", nested_dict["score"]["english_score"])

# ---------------------------------------
# 4. DICTIONARY METHODS
# ---------------------------------------
print("\n--- Dictionary Methods ---")

print("Keys   :", list(nested_dict.keys()))
print("Values :", list(nested_dict.values()))
print("Items  :", list(nested_dict.items()))
print("Length :", len(nested_dict))

print("Get name :", nested_dict.get("name"))  # Safe access

# Update multiple values
nested_dict.update({"name": "Mehak", "age": 23})
print("After Update :", nested_dict)

# ---------------------------------------
# 5. SET (Unordered, Unique Elements)
# ---------------------------------------
print("\n--- Set Basics ---")

nums = {1, 2, 3, 4, "Hello"}
print("Set :", nums)

nums1 = {1, 2, 2, 2, 1, "Hello"}
print("Duplicate Removed :", nums1)

print("Length :", len(nums))

# ---------------------------------------
# 6. EMPTY SET & SET METHODS
# ---------------------------------------
print("\n--- Set Methods ---")

null_set = set()
print("Empty Set :", null_set)

null_set.add(1)
null_set.add("Hello")
null_set.add(3)
null_set.add(2)
print("After Add :", null_set)

null_set.remove(1)
print("After Remove :", null_set)

null_set.pop()
print("After Pop :", null_set)

null_set.clear()
print("After Clear :", null_set)

# ---------------------------------------
# 7. SET OPERATIONS
# ---------------------------------------
print("\n--- Set Operations ---")

set1 = {1, 2, 3, 4, 5, 6}
set2 = {2, 3, 4, 7, 8, 9}

union = set1.union(set2)
intersection = set1.intersection(set2)

print("Union        :", union)
print("Intersection :", intersection)
print("Set1         :", set1)
print("Set2         :", set2)

# ---------------------------------------
# END OF FILE
# ---------------------------------------
print("\n=== End of Dictionary & Set ===")
