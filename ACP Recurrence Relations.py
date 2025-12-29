def T1(n):
    if n <= 0:
        return 1          
    return T1(n//2) + T1(n//3) + n



def T2(n):
    if n <= 1:
        return 1          
    return T2(n-1) + T2(n-2) + n
print(T1(12))
print(T2(5))
