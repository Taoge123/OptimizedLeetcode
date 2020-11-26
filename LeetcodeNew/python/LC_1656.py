
class OrderedStream:
    def __init__(self, n: int):
        self.values = {}
        self.pointer = 1

    def insert(self, id: int, value: str):
        self.values[id] = value
        res = []
        while self.pointer in self.values:
            # print(self.values)
            res.append(self.values.pop(self.pointer))
            self.pointer += 1
        return res


