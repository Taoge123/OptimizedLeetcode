
"""

理解题意之后不难分析出，为了使查询总和最大，我们对于查询频次越高的元素，希望它的值越大越好。所以显然只要将查询频率从高到低排序，同时将数组元素也从高到低排序，然后相乘相加必然就是我们期待的答案。

那我们我们如何统计每个元素被查询的频次呢？这里需要注意一个问题。比若说查询一次区间是[1,10000]，说明这10000个元素都要被查询一次。然后再来一次[1,10000]，那么这10000个元素的查询频次是否还要再挨个增加一次呢？可以知道这样的效率是很低的。

“差分数组”是解决这类问题的常见方法。上述区间需要自增查询频次的元素虽然很多，但是它们的变化率或者导数却是很稀疏的。对于每一个区间[start,end]，我们只要记录在start时的查询频次比start-1多一次、在end+1时的查询频次比end少一次即可。区间中部的这些元素，相邻元素之间的查询频次其实都是一样的。于是，我们只要两次改动，就可以描述这次区间查询的频次的变化。

具体地，我们开辟数组diff，其中diff[i]表示第i个元素的查询频次要比第i-1个元素的查询频次多多少。于是对于每一个区间[start,end]，我们做diff[start]+=1，diff[end+1]-=1. 最终我们从前缀0开始，一路不停地累加diff[i]，就能得到freq[i]的值（即第i各元素的查询频次）。

举个例子。有两个查询区间[1,3]和[2,4]，

0  1  2  3  4  5
  +1       -1
     +1        -1
-----------------
0  1  2  2  1   0
显然最终得到的就是我们期望的每个元素的频率。


0 1 2 3 4 5 6
X X X X X X X
  + + +
+ +
      + + + +

X X X X X X X
1 2 1 2 1 1 1


-1 0 1 2 3 4 5 6
   X X X X X X X
   + + + + + + +

diff[i] : freq[i] - freq[i-1]
freq[i-1] + diff[i] = freq[i]

[1-3] [2-5]
0  1  2  3  4  5
  +1       -1
     +1        -1

---------------------
0  1  1  0  -1  -1  diff
0  1  2  2   1   0

"""



class Solution:
    def maxSumRangeQuery(self, nums, requests) -> int:
        n = len(nums)
        diff = [0] * ( n +1)
        for i, j in requests:
            diff[i] += 1
            diff[ j +1] -= 1

        freq = [0] * n
        pre = 0
        for i in range(n):
            pre += diff[i]
            freq[i] = pre
        freq.sort()
        nums.sort()

        res = 0
        mod = 10 ** 9 + 7
        for i in range(n):
            res = (res + freq[i] * nums[i]) % mod
        return res



class Solution11:
    def maxSumRangeQuery(self, nums, requests) -> int:
        n = len(nums)
        count = [0] * (n + 1)
        for i, j in requests:
            count[i] += 1
            count[j + 1] -= 1
        for i in range(1, n + 1):
            count[i] += count[i - 1]
        res = 0
        for v, c in zip(sorted(count[:-1]), sorted(nums)):
            res += v * c
        return res % (10 ** 9 + 7)

