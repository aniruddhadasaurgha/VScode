def circuit(A, B, C):
    X = A and B
    Y = B or C
    Z = B and C
    W = Y and Z
    Q = X or W
    return Q
def simplified(A, B, C):
    return B and (A or C)
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            if circuit(A, B, C) != simplified(A, B, C):
                print("Mismatch at:", A, B, C)
            else:
                print(f"A={A}, B={B}, C={C} => Output: {circuit(A, B, C)}")
print("All outputs match between the original and simplified circuits.")


