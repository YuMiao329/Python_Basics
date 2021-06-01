# map() = applies a function to each item in a iterable (list, tuple, etc.)
#
# map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)
to_dollars = lambda data: (data[0], data[1] / 0.82)

# map will fill in first argument as the function and second as the variable
store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store_euros))

for i in store_euros:
    print(i)
# ('shirt', 16.4)
# ('pants', 20.5)
# ('jacket', 41.0)
# ('socks', 8.2)

for i in store_dollars:
    print(i)
# ('shirt', 20.0)
# ('pants', 25.0)
# ('jacket', 50.0)
# ('socks', 10.0)
