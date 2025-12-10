def myfunction(n):
    
    for i in range(0, n+1):
        print("First loop")

    j = 1
    while j <= n+1:
        print("Second loop", j)
        j = j * 2


for i in range(0, 100):
    print("Third loop")



def time_complexity():
    
    first_loop = "O(n)"

    
    second_loop = "O(log n)"

    
    third_loop = "O(1)"

    total = "O(n)"

    print("\nTime Complexity Results:")
    print("First loop:", first_loop)
    print("Second loop:", second_loop)
    print("Third loop:", third_loop)
    print("Total Time Complexity:", total)

time_complexity()




