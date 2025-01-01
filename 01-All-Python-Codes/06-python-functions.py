
#! 1. Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

#! 2. Lambda functions
square = lambda x: x ** 2
print(square(5))  # Output: 25

#! 3. Recursive functions
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120

#! 4. Default arguments
def greet_with_default(name="Guest"):
    return f"Welcome, {name}!"

print(greet_with_default())  # Output: Welcome, Guest!
print(greet_with_default("Bob"))  # Output: Welcome, Bob!

#! 5. Keyword arguments
def describe_person(name, age, city=None):
    if city:
        return f"{name} is {age} years old and lives in {city}."
    else:
        return f"{name} is {age} years old."

print(describe_person("Charlie", 30, "New York"))  # Output: Charlie is 30 years old and lives in New York.
print(describe_person("David", 25))  # Output: David is 25 years old.

#! 6. args and kwargs
def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_args(1, 2, 3, name="Alice", age=30)  
# Output:
# Positional arguments: (1, 2, 3) #! The positional arguments will be stored in a tuple
# Keyword arguments: {'name': 'Alice', 'age': 30}

#! 7. Scope in Python
x = 10

def modify_x():
    global x  # Use global keyword to modify variable from outer scope
    x = 20
    print("Inside function:", x)

modify_x()
print("Outside function:", x)  # Output:
# Inside function: 20
# Outside function: 20

def nested_function():
    y = 30
    def inner_function():
        nonlocal y  # Use nonlocal keyword to modify variable from enclosing scope
        y += 10
    inner_function()
    return y

result = nested_function()
print(result)  # Output: 40