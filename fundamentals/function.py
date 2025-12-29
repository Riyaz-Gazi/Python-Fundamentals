"""
========================================
        PYTHON FUNCTIONS - NOTES
========================================
Author  : Riyaz
Purpose : Beginner to Intermediate Python
Topics  :
    - Function basics
    - Parameters & arguments
    - Default arguments
    - *args and **kwargs
    - Return vs print
    - Type hints
========================================
"""


# ---------------------------------------
# 1. BASIC FUNCTION
# ---------------------------------------
def greet():
    """Prints a simple greeting"""
    print("Hello from greet")


greet()


# ---------------------------------------
# 2. FUNCTION WITH PARAMETERS
# ---------------------------------------
def greet_user(name):
    """Greets a user by name"""
    print(f"Hello, {name}")


greet_user("Riyaz")


# ---------------------------------------
# 3. DEFAULT ARGUMENT
# ---------------------------------------
def greet_guest(name="Guest"):
    """Greets user, default is Guest"""
    print(f"Hello, {name}")


greet_guest("Riyaz")
greet_guest()


# ---------------------------------------
# 4. KEYWORD ARGUMENTS
# ---------------------------------------
def info(name, age):
    """Prints name and age"""
    print("Name:", name)
    print("Age:", age)


info(name="Riyaz", age=40)


# ---------------------------------------
# 5. *args (VARIABLE POSITIONAL ARGUMENTS)
# ---------------------------------------
def add_numbers(*args):
    """
    Accepts any number of arguments
    *args is stored as a tuple
    """
    print("Arguments:", args)
    return sum(args)


result = add_numbers(1, 2, 3, 4)
print("Sum:", result)


# ---------------------------------------
# 6. **kwargs (VARIABLE KEYWORD ARGUMENTS)
# ---------------------------------------
def user_details(**kwargs):
    """
    Accepts keyword arguments
    **kwargs is stored as a dictionary
    """
    print("User Details:", kwargs)


user_details(name="Riyaz", age=20, city="Kolkata")


# ---------------------------------------
# 7. *args AND **kwargs TOGETHER
# ---------------------------------------
def demo(*args, **kwargs):
    """Demonstrates args and kwargs together"""
    print("Args:", args)
    print("Kwargs:", kwargs)


demo(1, 2, 3, a=10, b=20)


# ---------------------------------------
# 8. CORRECT PARAMETER ORDER
# ---------------------------------------
def func(a, b, *args, **kwargs):
    """
    Correct order:
    positional -> *args -> **kwargs
    """
    print(a, b)
    print(args)
    print(kwargs)


func(1, 2, 3, 4, x=10, y=20)


# ---------------------------------------
# 9. RETURN VS PRINT
# ---------------------------------------
def add(a, b):
    """Returns the sum of two numbers"""
    return a + b


sum_result = add(5, 10)
print("Returned Value:", sum_result)


# ---------------------------------------
# 10. REAL-WORLD LOGGING EXAMPLE
# ---------------------------------------
def log(message, *args, **kwargs):
    """Logs message with extra data"""
    print("Message:", message)
    print("Extra Data:", args)
    print("Metadata:", kwargs)


log("Order created", 101, 102, user="Riyaz", status="SUCCESS")


# ---------------------------------------
# 11. TYPE HINTS & DEFAULT VALUES
# ---------------------------------------
def calculate_discount(price: float, discount: float = 0.1) -> float:
    """
    Calculates discounted price

    :param price: Original price
    :param discount: Discount percentage (default 10%)
    :return: Final price after discount
    """
    return price * (1 - discount)


discount_price_1 = calculate_discount(1000)
print("Discounted Price (10%):", discount_price_1)

discount_price_2 = calculate_discount(1000, 0.2)
print("Discounted Price (20%):", discount_price_2)


print("\n✅ Python Function Notes Completed Successfully")
