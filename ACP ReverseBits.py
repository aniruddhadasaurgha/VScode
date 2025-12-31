num = int(input("Enter a number :"))
bin_number = bin(num)[2:]
print(bin_number)
new_bin = bin_number[::-1]
print(new_bin)
print(int(new_bin, 2))
print("Here is the decimal form of the reversed bit.")