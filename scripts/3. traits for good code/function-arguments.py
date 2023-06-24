def f(first, second, third):
    print(first)
    print(second)
    print(third)


nums = [1, 2, 3]
f(*nums)

first, *rest = [1, 2, 3, 4, 5, 6]

print(first)
print(rest)

first, *middle, last = [1, 2, 3, 4, 5, 6]
print(first)
print(middle)
print(last)
