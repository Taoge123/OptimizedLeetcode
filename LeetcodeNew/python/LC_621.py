
import collections

class Solution:
    def leastInterval(self, tasks, n):
        counter = collections.Counter(tasks)
        freq = sorted(counter.values())

        maxi = freq[-1] - 1
        freq.pop()

        idle = maxi * n
        for f in reversed(freq):
            idle -= min(f, maxi)

        if idle > 0:
            return len(tasks) + idle
        else:
            return len(tasks)

        # return len(tasks) + idle if idle > 0 else len(tasks)



