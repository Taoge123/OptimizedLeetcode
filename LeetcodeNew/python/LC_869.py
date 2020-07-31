import collections


class SolutionTony:
    def reorderedPowerOf2(self, N: int) -> bool:
        print(2**30)
        visited = set()
        for i in range(30):
            visited.add("".join(sorted(str(pow(2, i)))))

        if "".join(sorted(str(N))) in visited:
            return True
        return False



class Solution:
    def reorderedPowerOf2(self, N):
        c = collections.Counter(str(N))
        return any(c == collections.Counter(str(1 << i)) for i in range(30))

