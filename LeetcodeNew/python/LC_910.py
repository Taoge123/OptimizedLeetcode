
"""
910.Smallest-Range-II
首先要有一个直觉：我们将A排序之后，为了减少“贫富差距”，我们一定是将A的左边一部分元素都加上K，右边一部分元素都减去K。为什么左边那部分一定都是加上K，而不是加减交错呢？
比如说，a<b<c，如果我们决策是 a+K, b-K, c+K 的话，b和c之间的差距不仅没有减小反而被拉大了。
所以在最终的方案里，绝对不可能出现“加，减，加”交错操作的情况，唯一的方案就是：左边一部分加K，右边一部分减K。

那么如果确定这个分界线呢？其实并没有更优秀的办法，挨个尝试就行了。假设这个分界线在A[i]后面，也即是说A[0]～A[i]都是加K，A[i+1]～A[n-1]都是减K，
那么这个新数组B的最大值，其实可以从左右两部分分别的最大值得到，即MAX = max(A[i]+K, A.back()-K).同理，这个新数组B的最小值，其实可以从左右两部分分别的最小值得到，
即MIN = min(A[0]+K, A[i+1]-K)。而我们的答案就是在所有的diff=MAX-MIN中挑选最小的那个。

"""

"""

1 2 3 || 4 5 6 7 8 9 
+ + + || - - - - - -
每个点找出分割线，都试一次

"""


class Solution:
    def smallestRangeII(self, A, K: int) -> int:
        A = sorted(A)
        diff = A[-1] - A[0]
        for i in range(len(A) - 1):
            maxi = max(A[i] + K, A[-1] - K)
            mini = min(A[0] + K, A[i + 1] - K)
            diff = min(diff, maxi - mini)
        return diff






