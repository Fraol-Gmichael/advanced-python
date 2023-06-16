from collections import UserList

class GoodList(UserList):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        
        value =  f"[{prefix}] {value}"
        
        return value
        
class BadList(list):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        
        value =  f"[{prefix}] {value}"
        
        return value
bl = BadList((0, 1, 2, 3, 4, 5))
# "".join(bl)
gl = GoodList((0, 1, 2, 3, 4, 5))
print(" ".join(gl))

