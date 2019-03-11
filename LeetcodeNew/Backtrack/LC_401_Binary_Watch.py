"""
Given a non-negative integer n which represents
the number of LEDs that are currently on,
return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

"""

import itertools

class Solution:
    def readBinaryWatch(self, num):
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]


"""
The code has O(1) time complexity, because all the possible watch combinations 
(valid or invalid) can't be more that 12 * 59.
Regarding space complexity, it's also O(1) cause the DFS will have depth of maximum n, 
which can't be more than 9 as per problem boundary.

"""


class Solution(object):
    def readBinaryWatch(self, n):

        def dfs(n, hours, mins, idx):
            if hours >= 12 or mins > 59: return
            if not n:
                res.append(str(hours) + ":" + "0" * (mins < 10) + str(mins))
                return
            for i in range(idx, 10):
                if i < 4:
                    dfs(n - 1, hours | (1 << i), mins, i + 1)
                else:
                    k = i - 4
                    dfs(n - 1, hours, mins | (1 << k), i + 1)

        res = []
        dfs(n, 0, 0, 0)
        return res


"""
Generate all possible combinations of num indexes in the range from 0 to 10. For example, 
one possible combination of 5 indexes is {0, 1, 4, 7, 8}, which is "3:25".
"""


class Solution2:
    def readBinaryWatch(self, num):
        watch = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        times = []
        for leds in itertools.combinations(range(len(watch)), num):
            h = sum(watch[i] for i in leds if i < 4)
            m = sum(watch[i] for i in leds if i >= 4)
            if h > 11 or m > 59: continue
            times.append("{}:{:02d}".format(h, m))
        return times


class Solution3(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        def backtrack(positions, remaining, outputs, start):
            if remaining == 0:
                outputs.append(positions[:])
            else:
                for i in range(start, len(positions)):
                    positions[i] = 1
                    backtrack(positions, remaining - 1, outputs, i + 1)
                    positions[i] = 0

        outputs = []
        leds = [0] * 10
        backtrack(leds, num, outputs, 0)
        outputs = map("".join, [map(str, x) for x in outputs])
        ans = []
        for led in outputs:
            hr = int(led[0:4], 2)
            minutes = int(led[4:10], 2)
            if hr <= 11 and minutes <= 59:
                ans.append("{}:{:02}".format(hr, minutes))
        return ans

