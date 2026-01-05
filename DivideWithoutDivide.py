def divide(ourDividend, ourDivisor):
    sign = (-1 if (ourDividend < 0) ^ (ourDivisor < 0) else 1)
    dividend = abs(ourDividend)
    divisor = abs(ourDivisor)
    quotient = 0
    temp = 0
    for i in range(31, -1, -1):
        if (temp + (divisor << i) <= dividend):
            temp += divisor << i
            quotient |= 1 << i
    if sign == -1:
        quotient = -quotient
    return quotient
a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))
print("The result of", a, "/", b, "is:", divide(a, b))