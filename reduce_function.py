# reduce () = apply a function to an iterable and reduce it to a single
#             cumulative value. It performs function on first two elements and repeats
#             process until 1 value remains

# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y: x + y, letters)
#string concatenation
print(word)  # HELLO

factorial = [5, 4, 3, 2, 1]
#if only single value, it will return a single value
result = functools.reduce(lambda x, y: x * y, factorial)
#number multiplication
print(result)  # 120
