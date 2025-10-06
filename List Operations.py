list = ["Fish", "Cat", "Dog", 2, 24.0, True, 10^8, "Hello"]
print(list)
print(list[-7])
print(list[1])
print(list[3:6])
list.append("Jet")
print(list)
list.remove(2)
print(list)
list.pop(6)
print(list)
sliced_list = list[2:5]
print(sliced_list)

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(prime_numbers)
slice_of_primes = prime_numbers[3:8]
print(slice_of_primes)
prime_numbers.reverse()
print(prime_numbers)
prime_numbers.sort()
print(prime_numbers)