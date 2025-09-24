a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))
print("Before swapping: a =", a, ", b =", b, ", c =", c)
temp = a
a = b
b = c
c = temp
print("After swapping: a =", a, ", b =", b, ", c =", c)