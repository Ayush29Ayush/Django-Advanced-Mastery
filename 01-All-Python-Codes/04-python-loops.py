# for loop
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    if fruit == 'banana':
        continue  # Skip banana
    print(fruit)  # Output: apple cherry

# while loop
i = 0
while i < 5:
    print(i)  # Output: 0 1 2 3 4
    i += 1

# break statement
for num in range(1, 11):
    if num == 5:
        break  # Exit the loop when num == 5
    print(num)  # Output: 1 2 3 4

# continue statement
for letter in 'hello':
    if letter == 'l':
        continue  # Skip 'l'
    print(letter)  # Output: h e o

# pass statement
for item in []:
    pass  # No output

# combination of statements
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    if num == 5:
        break  # Exit when num == 5
    print(num)  # Output: 1 3
