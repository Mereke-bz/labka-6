from functools import reduce

def multiply(x, y):
    return x * y

def multiply_numbers(lst):
    return reduce(multiply, lst)

numbers = [2, 3, 4, 5]
result = multiply_numbers(numbers)
print("Number:", result)
