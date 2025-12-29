n = 12
print(bin(n)[2:])
rightmost_set_bit = n & -n
print(rightmost_set_bit)
