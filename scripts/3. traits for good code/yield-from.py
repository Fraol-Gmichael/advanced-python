def numbers_gen():
    # yield from list(range(50))
    for each in range(50):
        yield each

print(list(numbers_gen()))