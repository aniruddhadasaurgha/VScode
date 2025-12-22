def isEvenOdd( n):
    if (n ^ 1 == n + 1):
        return True;
    else:
        return False;

number = int(input("Enter a number: "))
if isEvenOdd(number):
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")