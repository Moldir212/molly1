from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map()
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

# filter()
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# reduce()
sum_all = reduce(lambda x, y: x + y, numbers)
print("Sum:", sum_all)

# базовые функции
print("Length:", len(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))




from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

#2
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

#3
total = reduce(lambda a, b: a + b, numbers)
print(f"Sum: {total}")

#4
odd_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))
print(odd_squares)

#5
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(f"Max: {maximum}")