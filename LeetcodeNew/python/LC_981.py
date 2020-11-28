import collections
import bisect
from sortedcontainers import SortedSet


class TimeMapTony:
    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = SortedSet(key=lambda k: k[1])

        self.table[key].add((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        idx = self.table[key].bisect_right(("", timestamp))
        if idx:
            return self.table[key][idx - 1][0]
        else:
            return ""




class TimeMap:
    def __init__(self):
        self.table = collections.defaultdict(lambda: SortedSet(key=lambda x: x[1]))

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].add((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        idx = self.table[key].bisect_right(("", timestamp))
        if idx:
            return self.table[key][idx - 1][0]
        else:
            return ""




class TimeMapBinarySearch:
    def __init__(self):
        self.table = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.table[key].append((timestamp, value))

    def get(self, key, timestamp):
        A = self.table.get(key, None)
        if A is None: return ""
        i = bisect.bisect_left(A, (timestamp, chr(127)))
        return A[i - 1][1] if i else ""


a = TimeMapTony()
print(a.set("foo", "bar", 1))
print(a.get("foo", 1))
print(a.set("tony", "bar", 2))
print(a.get("foo", 1))
print(a.set("tony", "bar", 3))
print(a.get("foo", 1))
print(a.set("foo", "bar", 4))
print(a.get("foo", 1))
print(a.set("tony", "bar", 4))
print(a.get("foo", 1))
print(a.set("foo", "bar", 4))
print(a.get("tony", 1))
print(a.set("foo", "bar", 4))
print(a.get("foo", 1))
print(a.set("foo", "bar", 4))



