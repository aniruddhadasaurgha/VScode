def setOrnot(number, n):
    if (number & (1 << n)):
        print(f"The {n}th bit is set.")
    else:
        print(f"The {n}th bit is not set.")
number = int(input("Enter a number: "))
n = int(input("Enter the bit position to check (0-indexed): "))
setOrnot(number, n)