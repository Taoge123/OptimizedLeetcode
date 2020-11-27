import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        res = 0
        visited = set()

        for ch, freq in count.items():
            while freq > 0 and freq in visited:
                freq -= 1
                res += 1
            visited.add(freq)
        return res




class Solution2:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        res = 0

        visited = set()

        for freq in sorted(count.values(), reverse=True):
            while freq in visited:
                freq -= 1
                res += 1
            if freq:
                visited.add(freq)

        return res


