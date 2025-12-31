def powerof8(w):
    if w == 0:
        return False
    else:
        while (w % 8 == 0):
            w /= 8
        return (w == 1)
        
w = int(input("Enter a number: "))
if powerof8(w):
    print(w, " is a power of 8")
else:
    print(w, " is not a power of 8")