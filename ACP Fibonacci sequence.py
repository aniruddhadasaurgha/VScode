def Fibonacci(n):
    if n == 0:
        return n

    if n == 1:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
r = int(input("Enter range: "))

for i in range(r):
    print(Fibonacci(i))