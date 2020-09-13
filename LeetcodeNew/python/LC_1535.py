"""
[X X X X] X X X X
本题模拟一个“打擂台”的机制。对于一个数A，如果它连续大于之后的K个数，那么它是winner。

如果数A在成为winner之前被数B压过，那么数A（以及被数A击败的数）是否要append到arr末尾来继续参与这场模拟呢？不需要。事实上没必要在考察完n个数之后继续模拟来找winner。因为我们在第一轮遍历这n个数的时候，必然会遇到一个全局的最大值Max，它之后的所有数（以及包括额外append到数组末尾的数）都不可能击败它。所以如果我们考察完n个数之后还没有确定winner，那么手头的最大值（就是全局最大值）就一定是winner，因为它一定会击败所有元素。

因此，我们只需要从头开始，模拟类似“打擂台”的机制，只要某个数连胜K场，就是winner。否则考察完n个数，手头的最大值（就是全局最大值）就是winner。

另外，如果K大于n的话，说明winner要击败所有元素（好几圈），那么同样说明winner一定就是全局最大值。

"""

import collections


class Solution:
    def getWinner(self, arr, k: int) -> int:
        curMax = arr[0]
        times = 0
        for i in range(1, len(arr)):
            if arr[i] > curMax:
                curMax = arr[i]
                times = 1
            else:
                times += 1

            if times == k:
                return curMax

        return curMax




class Solution2:
    def getWinner(self, arr, k: int) -> int:
        self.table = collections.defaultdict(int)
        n = len(arr)
        if k >= n:
            return max(arr)
        nums = collections.deque(arr)
        count = 0
        for i in range(n*2):
            num, val = self.compare(nums)
            count = max(count, val)
            if count >= k:
                print(self.table)
                return num

    def compare(self, nums):
        a = nums.popleft()
        b = nums.popleft()
        self.table[max(a, b)] += 1
        nums.appendleft(max(a, b))
        nums.append(min(a, b))
        return max(a, b), self.table[max(a, b)]

