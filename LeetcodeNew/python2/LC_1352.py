"""
本题看第一眼就知道解法是构造前缀乘积的数组，令pre[i]表示从nums[1]连续乘到nums[i]的积。假设当前已经有n个元素，
那么最后k个元素的乘积就是pre[n]/pre[n-k]。注意本题的约束条件里保证了前缀乘积数组不会溢出。

但是本题就这么简单吗？其实本题需要考察的是当年nums[i]=0的情况。我们发现一旦加入了0，那么会使得当前乃至之后的pre永远都是0，
于是在getProduct时的计算公式pre[n]/pre[n-k]的表达式就会有除数为0的风险。那么如何解决这个问题呢？

首先，如果从n往前数的k个数包括了0，那么最终答案就是返回0. 其次，如果这k个数不包括0的话，那么如何保证pre[n]/pre[n-k]一定合法呢？
我们可以认为把最近的0之前的数字都忽略掉，将整个pre数组从最近的0之后开始重新计数：也就是当nums[i]==1时，令pre[i]=1。

"""


class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]

    def add(self, num):
        if num == 0:
            self.nums = [1]
        else:
            self.nums.append(self.nums[-1] * num)

    def getProduct(self, k):
        if k >= len(self.nums):
            return 0
        return self.nums[-1] // self.nums[-k - 1]



