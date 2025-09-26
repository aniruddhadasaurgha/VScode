n = int(input("Enter a number: "))
num = n
sum = 0
order = len(str(n).replace('.', ''))
while n > 0:
    digit = n % 10
    sum += digit ** order
    n //= 10
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")