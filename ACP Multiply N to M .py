
def multiply_one(n, x):
    return n * x


def multiply_range(N, M):
    results = []
    for i in range(N, M + 1):
        results.append(multiply_one(N, i))
    return results


N = 2
M = 5
output = multiply_range(N, M)
print(f"Multiplying {N} to {M}: {output}")
