def longest_consecutive_ones(n):
    b = bin(n)[2:]
    max_count = 0
    count = 0

    for bit in b:
        if bit == '1':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count

print(longest_consecutive_ones(56))  