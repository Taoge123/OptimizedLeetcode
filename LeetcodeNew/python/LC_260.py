
import collections

"""
lowbit : an positive integer, the number formed by the lowest 1 and 0 afterward


00001010 -> 10
11101100 -> 100

011
101
----
110


"""


class Solutionbit:
    def singleNumber(self, nums):
        diff = 0
        for num in nums:
            diff ^= num

        diff &= -diff
        res = [0, 0]
        for num in nums:
            if num & diff == 0:
                res[0] ^= num
            else:
                res[1] ^= num

        return res



class Solution:
    def singleNumber(self, nums):
        res = []
        table = collections.Counter(nums)

        for num in table:
            if table[num] == 1:
                res.append(num)

        return res


class Solution2:
    def singleNumber(self, nums):

        visited = set()
        for num in nums:
            if num in visited:
                visited.remove(num)
            else:
                visited.add(num)
        return list(visited)






