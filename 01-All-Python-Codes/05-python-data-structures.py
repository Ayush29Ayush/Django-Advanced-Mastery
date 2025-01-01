# Lists
fruits = ['apple', 'banana', 'cherry']
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Attributes and operations
print(len(fruits))  # Length
print(fruits.index('banana'))  # Index of element
fruits.append('date')  # Add element
fruits.remove('apple')  # Remove element
fruits.sort()  # Sort
print(fruits)  # Output: ['banana', 'cherry', 'date']

# 2D Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Attributes and operations
print(len(matrix))  # Number of rows
print(len(matrix[0]))  # Number of columns
row = matrix[1]  # Access row
element = matrix[1][2]  # Access element
matrix[0].append(10)  # Modify element
print(matrix)  # Output: [[1, 2, 3, 10], [4, 5, 6], [7, 8, 9]]

# Dictionaries
person = {'name': 'Alice', 'age': 30}
print(person)  # Output: {'name': 'Alice', 'age': 30}

# Attributes and operations
print(person.keys())  # Keys
print(person.values())  # Values
print(person.items())  # Items
person['city'] = 'New York'  # Add key-value pair
del person['age']  # Remove key
print(person)  # Output: {'name': 'Alice', 'city': 'New York'}

# Tuples
coordinates = (10, 20)
print(coordinates)  # Output: (10, 20)

# Attributes and operations
print(coordinates.count(10))  # Count occurrences of element
print(coordinates.index(10))  # Index of first occurrence
new_tuple = coordinates + (30,)  # Concatenate
print(new_tuple)  # Output: (10, 20, 30)

# Sets
numbers = {1, 2, 3, 3, 4}
print(numbers)  # Output: {1, 2, 3, 4}

# Attributes and operations
print(len(numbers))  # Number of elements
numbers.add(5)  # Add element
numbers.remove(2)  # Remove element
print(numbers)  # Output: {1, 3, 4, 5}
print(3 in numbers)  # Check membership

# Strings
word = "Hello, World!"
print(word)  # Output: Hello, World!

# Attributes and operations
print(word.upper())  # Convert to uppercase
print(word.lower())  # Convert to lowercase
print(word.count('l'))  # Count occurrences of character
print(word.startswith('H'))  # Check if string starts with
print(word.endswith('!'))  # Check if string ends with
print(word.replace('World', 'Python'))  # Replace substring