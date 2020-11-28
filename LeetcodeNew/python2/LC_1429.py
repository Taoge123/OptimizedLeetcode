
class FirstUnique:
    def __init__(self, nums):
        self.ban = set()
        self.unique = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        # return next(iter(self.once), -1)
        for v in self.unique:
            if self.unique[v]:
                return v
        return -1

    def add(self, value: int) -> None:
        if value in self.unique:
            self.ban.add(value)
            del self.unique[value]
        elif value not in self.ban:
            self.unique[value] = True






a = FirstUnique([2, 3, 5])
print(a.showFirstUnique())
print(a.add(5))
print(a.showFirstUnique())
print(a.add(2))
print(a.showFirstUnique())
print(a.add(3))


