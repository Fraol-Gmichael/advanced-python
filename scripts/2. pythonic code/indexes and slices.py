numbers = (1, 1, 2, 3, 5, 8, 13, 21)

print('numbers[:3]: ', numbers[:3])
print('numbers[3:]: ', numbers[:3])
print('numbers[:]: ', numbers[:])
print('numbers[::]: ', numbers[::])
print(numbers[:]== numbers[::])
print(numbers[1:7:2])

interval = slice(1, 7, 2)

print(numbers[interval])
print(interval)