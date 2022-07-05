
from sortedcontainers import SortedDict, SortedSet, SortedList


a = SortedList()

a.add(1)
a.add(2)
a.add(3)
a.add(3)
a.add(3)
a.add(4)
a.add(6)
a.add(5)
a.add(3)

print(a)
print(a.bisect_left(3))
print(a.bisect_right(3))




