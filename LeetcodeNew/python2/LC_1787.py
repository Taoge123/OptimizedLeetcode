
"""
https://leetcode-cn.com/problems/make-the-xor-of-all-segments-equal-to-zero/solution/python-tan-xin-mei-ju-by-qubenhao-0g9f/
https://leetcode-cn.com/problems/make-the-xor-of-all-segments-equal-to-zero/solution/xsschao-de-ti-jie-jian-dan-yu-chu-li-xia-roqp/
https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/discuss/1097796/Python-3-Another-short-dp-7-lines-explained

[(x x i) x x]
set(i) = {A[i], A[i+k], A[i+2k], A[i+3k]....}

set(0) = {......}
set(1) = {......}
set(2) = {......}

O(k * 1024)

dp[i][d] : the minimum cost if uou make the XOR-sum of first i elements equal to d

for i in range(k):
    for d in range(1024):
        for v in range(1024):
            dp[i][d] = min(dp[i][d], dp[i-1][v^d] * cost(makes set(i) all v))

totalCount - count[i][v] = cost(makes set(i) all v)

"""

import functools
import collections

class Solution:
    def minChanges(self, nums, k: int) -> int:
        n = len(nums)
        count = collections.defaultdict(collections.Counter)
        for i in range(k):
            for j in range(i, n, k):
                count[i][nums[j]] += 1

        # 每组数的众数
        msv = [count[i].most_common(1)[0][1] for i in range(k)]
        # 每组全部变为同样的数的最小代价
        ans = n - sum(msv)

        # 每组数都是众数，要满足异或为0，需要统计每组数选哪个数达到最优解，或者牺牲哪组数
        @functools.lru_cache(None)
        def dfs(i, curr):
            if i == k and curr == 0:
                return 0
            elif i == k:
                return float("inf")
            # 牺牲这组数的额外代价,所有数都换为某个数，使得异或为0
            res = msv[i]
            # 变为这组数中的某个数
            for key in count[i].keys():
                res = min(res, dfs(i + 1, curr ^ key) - count[i][key] + msv[i])
            return res

        return ans + dfs(0, 0)



# nums = [3,4,5,2,1,7,3,4,7]
# k = 3
nums = [1,2,4,1,2,5,1,2,6]
k = 3
a = Solution()
print(a.minChanges(nums, k))



