import math;

def printPowerSet(set,Setsize):

    PowerSetSize = int(math.pow(2, Setsize));

    outer = 0;
    inner = 0;
    for outer in range(0, PowerSetSize):
        for inner in range(0, Setsize):
            if((outer & (1 << inner)) > 0):
                print(set[inner], end = "");
        print();
size = int(input("Enter size of set: "));
set = [];
for i in range(0, size):
    n = int(input("Enter element: "));
    set.append(n);

printPowerSet(set, len(set));