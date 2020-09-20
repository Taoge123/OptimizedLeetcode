
import collections

class MapSum:
    def __init__(self):
        self.table = collections.defaultdict(int)
        self.words = collections.defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        diff = val - self.table[key]
        self.table[key] = val
        prefix = ""
        for c in key:
            prefix += c
            self.words[prefix] = self.words[prefix] + diff

    def sum(self, prefix: str) -> int:
        return self.words[prefix]




