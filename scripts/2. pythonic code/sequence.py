class Items:
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, key):
        return self._values.__getitem__(key)
    


items = Items(1, 2, 3, 4, 5, 6)
print(items[2])
print(len(items))