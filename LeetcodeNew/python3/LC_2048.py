
import bisect
import itertools


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # permuation
        # get # of digits of n
        # n <= 10**6 --> pick it from (1- 6) for num_to_be_used

        graph = [1,
                 22,
                 122, 333,
                 1333, 4444,
                 14444, 22333, 55555,
                 155555, 122333, 224444, 666666,
                 1224444  # 7-digit largest possible
                 ]

        # all possible
        nums = []
        for num in graph:
            nums.extend(self.get_permutations(str(num)))

        nums.sort()
        return nums[bisect.bisect_right(nums, n)]

    def get_permutations(self, s):
        res = set()
        for path in itertools.permutations(s):
            res.add(''.join(path))
        return [int(x) for x in res]


