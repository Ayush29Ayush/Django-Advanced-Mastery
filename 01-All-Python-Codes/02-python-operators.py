# Arithmetic Operators
a = 5
b = 2
print(f"Arithmetic: {a} + {b} = {a + b}")  # Output: Arithmetic: 5 + 2 = 7
print(f"{a} - {b} = {a - b}")  # Output: 5 - 2 = 3
print(f"{a} * {b} = {a * b}")  # Output: 5 * 2 = 10
print(f"{a} / {b} = {a / b}")  # Output: 5 / 2 = 2.5
print(f"{a} // {b} = {a // b}")  # Output: 5 // 2 = 2
print(f"{a} % {b} = {a % b}")  # Output: 5 % 2 = 1

# Assignment Operators
c = 10
d = 3
print(f"Assignment: c += d = {c += d}")  # Output: Assignment: c += d = 13
print(f"c -= d = {c -= d}")  # Output: c -= d = 10
print(f"c *= d = {c *= d}")  # Output: c *= d = 30
print(f"c /= d = {c /= d}")  # Output: c /= d = 10.0
print(f"c //= d = {c //= d}")  # Output: c //= d = 3
print(f"c %= d = {c %= d}")  # Output: c %= d = 1

# Comparison Operators
e = 5
f = 3
print(f"Comparison: {e} == {f} = {e == f}")  # Output: Comparison: 5 == 3 = False
print(f"{e} != {f} = {e != f}")  # Output: 5 != 3 = True
print(f"{e} > {f} = {e > f}")  # Output: 5 > 3 = True
print(f"{e} < {f} = {e < f}")  # Output: 5 < 3 = False
print(f"{e} >= {f} = {e >= f}")  # Output: 5 >= 3 = True
print(f"{e} <= {f} = {e <= f}")  # Output: 5 <= 3 = False

# Logical Operators
g = True
h = False
print(f"Logical: {g} and {h} = {g and h}")  # Output: Logical: True and False = False
print(f"{g} or {h} = {g or h}")  # Output: True or False = True
print(f"Not {g} = {not g}")  # Output: Not True = False

# Identity Operators
i = [1, 2, 3]
j = [1, 2, 3]
k = [1, 2, 4]
print(f"Identity: {i is j} = {i is j}")  # Output: Identity: [1, 2, 3] is [1, 2, 3] = False
print(f"{i is k} = {i is not k}")  # Output: [1, 2, 3] is not [1, 2, 4] = True

# Membership Operators
m = "Hello"
n = "world"
print(f"Membership: 'w' in '{m}' = {'w' in m}")  # Output: Membership: 'w' in 'Hello' = False
print("'o' not in '{m}' = {'o' not in m}")  # Output: 'o' not in 'Hello' = True

# Bitwise Operators
o = 5
p = 3
print(f"Bitwise AND: {o & p} = {o & p}")  # Output: Bitwise AND: 1 = 1
print(f"Bitwise OR: {o | p} = {o | p}")  # Output: Bitwise OR: 5 = 5
print(f"Bitwise XOR: {o ^ p} = {o ^ p}")  # Output: Bitwise XOR: 4 = 4
print(f"Bitwise NOT: ~{o} = {~o}")  # Output: Bitwise NOT: -6 = -6

# Special Operators
def square(x):
    return x ** 2

print("Special: square(5) = ", square(5))  # Output: Special: square(5) = 25
