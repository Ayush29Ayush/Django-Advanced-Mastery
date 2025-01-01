# if statement
x = 15
if x > 10:
    print("x is greater than 10")  # Output: x is greater than 10

# elif statement
y = 4
if y > 5:
    print("y is greater than 5")
elif y == 5:
    print("y equals 5")
elif y < 5:
    print("y is less than 5")  # Output: y is less than 5

# else statement
z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")  # Output: z is zero

# Nested if statement
a = 3
if a > 0:
    if a % 2 == 0:
        print("a is even and positive")
    else:
        print("a is odd and positive")  # Output: a is odd and positive

# Multiple conditions with and/or
b = 10
if b > 5 and b < 15:
    print("b is between 5 and 15")  # Output: b is between 5 and 15
elif b > 15 or b < 5:
    print("b is less than 5 or greater than 15")
