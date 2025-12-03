def  OnTime(n):
    iteration = 0
    for i in range(1, n + 1):
        iteration += 1 
        print("When n is ",n,"Iterations = ", iteration)
OnTime(5)
OnTime(10)
OnTime(15)
print("\n With every 'n'the time taken and iterations will increase ")