"""
https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step

https://buptwc.com/2018/09/16/Leetcode-907-Sum-of-Subarray-Minimums/
https://www.cnblogs.com/grandyang/p/8887985.html
https://www.youtube.com/watch?v=Ax31nm1GWb4&t=358s

For some more similar problem, I suggest
828. Unique Letter String
891. Sum of Subsequence Widths
What can monotonous decrease stack do?
Some applications of monotone (increase/decrease) stack in leetcode:
Next Greater Element II (a very basic one)
Largest Rectangle in Histogram(almost the same as this problem)
Maximal Rectangle(please do this problem after you solve the above one)
Trapping Rain Water (challenge)
Remove Duplicate Letters(challenge)
Remove K Digits
Create Maximum Number
132 Pattern(challenge, instead of focusing on the elements in the stack, this problem focuses on the elements poped from the monotone stack)
sliding window maximum(challenge, monotone queue)
Max Chunks To Make Sorted II

"""
"""
order matters, unlike 花花酱 LeetCode 898. Bitwise ORs of Subarrays we can not sort the numbers in this problem.
e.g. sumSubarrayMins([3, 1, 2, 4]) !=sumSubarrayMins([1, 2, 3, 4]) since the first one will not have a subarray of [3,4].
For A[i], assuming there are L numbers that are greater than A[i] in range A[0] ~ A[i – 1],
and there are R numbers that are greater or equal than A[i] in the range of A[i+1] ~ A[n – 1].
Thus A[i] will be the min of (L + 1) * (R + 1) subsequences.
e.g. A = [3,1,2,4], A[1] = 1, L = 1, R = 2,
there are (1 + 1) * (2 + 1) = 6 subsequences are 1 is the min number.
[3,1], [3,1,2], [3,1,2,4], [1], [1,2], [1,2,4] 1 * 6 + 2 * 2 + 4 * 1 
"""
"""
How many times a number will appear in the results(Not thinking about minimum)
for a element A[i], it will represents (i + 1) * (len - i + 1) times.
i + 1 means the subarrays whose end point is A[i]
(len - i + 1) means the subarrays whose start point is A[i].
How to solve this question:
res = sum(A[i] * f[i], A[i] is the number and f[i] means the number of subarrays where A[i] is the minimum in the subarray.
f[i] = left[i] * right[i], where left[i] is the left subarray numbers where A[i] is the last element 
and A[i] is minimum in current array and right[i] is the minimum and first element in the subarray.
How to get left[i] and right[i]. Consider leetcode question 901.
We need to consider a corner case, two elements have the same value.
"""
"""
这道题给了一个数组，对于所有的子数组，找到最小值，并返回累加结果，并对一个超大数取余。
由于我们只关心子数组中的最小值，所以对于数组中的任意一个数字，需要知道其是多少个子数组的最小值。
就拿题目中的例子 [3,1,2,4] 来分析，开始遍历到3的时候，其本身就是一个子数组，最小值也是其本身，累加到结果 res 中，此时 res=3，
然后看下个数1，是小于3的，此时新产生了两个子数组 [1] 和 [3,1]，且最小值都是1，此时在结果中就累加了 2，此时 res=5。
接下来的数字是2，大于之前的1，此时会新产生三个子数组，其本身单独会产生一个子数组 [2]，可以先把这个2累加到结果 res 中，
然后就是 [1,2] 和 [3,1,2]，可以发现新产生的这两个子数组的最小值还是1，跟之前计算数字1的时候一样，可以直接将以1结尾的子数组最小值之和加起来，
那么以2结尾的子数组最小值之和就是 2+2=4，此时 res=9。对于最后一个数字4，其单独产生一个子数组 [4]，
还会再产生三个子数组 [3,1,2,4], [1,2,4], [2,4]，其并不会对子数组的最小值产生影响，
所以直接加上以2结尾的子数组最小值之和，总共就是 4+4=8，最终 res=17。

分析到这里，就知道我们其实关心的是以某个数字结尾时的子数组最小值之和，可以用一个一维数组 dp，
其中 dp[i] 表示以数字 A[i] 结尾的所有子数组最小值之和，将 dp[0] 初始化为 A[0]，结果 res 也初始化为 A[0]。
然后从第二个数字开始遍历，若大于等于前一个数字，则当前 dp[i] 赋值为 dp[i-1]+A[i]，前面的分析已经解释了，
当前数字 A[i] 组成了新的子数组，同时由于 A[i] 不会影响最小值，所以要把之前的最小值之和再加一遍。
假如小于前一个数字，就需要向前遍历，去找到第一个小于 A[i] 的位置j，假如j小于0，表示前面所有的数字都是小于 A[i] 的，
那么 A[i] 是前面 i+1 个以 A[i] 结尾的子数组的最小值，累加和为 (i+1) x A[i]，若j大于等于0，则需要分成两部分累加，
dp[j] + (i-j)xA[i]，这个也不难理解，前面有 i-j 个以 A[i] 为结尾的子数组的最小值是 A[i]，
而再前面的子数组的最小值就不是 A[i] 了，但是还是需要加上一遍其本身的最小值之和，
因为每个子数组末尾都加上 A[i] 均可以组成一个新的子数组，最终的结果 res 就是将 dp 数组累加起来即可，别忘了对超大数取余，



上面的方法虽然 work，但不是很高效，原因是在向前找第一个小于当前的数字，每次都要线性遍历一遍，造成了平方级的时间复杂度。
而找每个数字的前小数字或是后小数字，正是单调栈擅长的，可以参考博主之前的总结贴 LeetCode Monotonous Stack Summary 单调栈小结。
这里我们用一个单调栈来保存之前一个小的数字的位置，栈里先提前放一个 -1，作用会在之后讲解。
还是需要一个 dp 数组，跟上面的定义基本一样，但是为了避免数组越界，将长度初始化为 n+1，
其中 dp[i] 表示以数字 A[i-1] 结尾的所有子数组最小值之和。对数组进行遍历，当栈顶元素不是 -1 且 A[i] 小于等于栈顶元素，
则将栈顶元素移除。这样栈顶元素就是前面第一个比 A[i] 小的数字，此时 dp[i+1] 更新还是跟之前一样，分为两个部分，
由于知道了前面第一个小于 A[i] 的数字位置，用当前位置减去栈顶元素位置再乘以 A[i]，
就是以 A[i] 为结尾且最小值为 A[i] 的子数组的最小值之和，而栈顶元素之前的子数组就不受 A[i] 影响了，
直接将其 dp 值加上即可。将当前位置压入栈，并将 dp[i+1] 累加到结果 res，同时对超大值取余：


我们也可以对上面的解法进行空间上的优化，只用一个单调栈，用来记录当前数字之前的第一个小的数字的位置，然后遍历每个数字，
但是要多遍历一个数字，i从0遍历到n，当 i=n 时，cur 赋值为0，否则赋值为 A[i]。
然后判断若栈不为空，且 cur 小于栈顶元素，则取出栈顶元素位置 idx，由于是单调栈，
那么新的栈顶元素就是 A[idx] 前面第一个较小数的位置，由于此时栈可能为空，所以再去之前要判断一下，若为空，则返回 -1，
否则返回栈顶元素，用 idx 减去栈顶元素就是以 A[idx] 为结尾且最小值为 A[idx] 的子数组的个数，
然后用i减去 idx 就是以 A[idx] 为起始且最小值为 A[idx] 的子数组的个数，
然后 A[idx] x left x right 就是 A[idx] 这个数字当子数组的最小值之和，累加到结果 res 中并对超大数取余即可，
"""

"""
Intuition:
I guess this is a general intuition for most solution.
res = sum(A[i] * f(i))
where f(i) is the number of subarrays,
in which A[i] is the minimum.

To get f(i), we need to find out:
left[i], the length of strict bigger numbers on the left of A[i],
right[i], the length of bigger numbers on the right of A[i].

Then,
left[i] + 1 equals to
the number of subarray ending with A[i],
and A[i] is single minimum.

right[i] + 1 equals to
the number of subarray starting with A[i],
and A[i] is the first minimum.

Finally f(i) = (left[i] + 1) * (right[i] + 1)

For [3,1,2,4] as example:
left + 1 = [1,2,1,1]
right + 1 = [1,3,2,1]
f = [1,6,2,1]
res = 3 * 1 + 1 * 6 + 2 * 2 + 4 * 1 = 17


Explanation:
To calculate left[i] and right[i],
we use two increasing stacks.

It will be easy if you can refer to this problem and my post:
901. Online Stock Span
I copy some of my codes from this solution.

Complexity:
All elements will be pushed twice and popped at most twice
O(N) time, O(N) space


Improvement
1.Here I record (A[i], count) in the stack.
We can also only record index.
2. For left part and right part, the logic is same.
So for each, I used one stack and one pass.
This process can be optimized to one pass using one stack in total.

"""
"""
1 2 3 4

stack = 1, 1, 1, 1 

4 3 2 1




"""

"""
往后找找next smaller or equal element
往前找找next smaller
12 [35555355553] 21
    -
12 3[5555355553] 21
    -
12 355553[55553] 21
          -


"""


class Solution:
    def sumSubarrayMins(self, A) -> int:
        n = len(A)
        prevSmaller, nextSmaller = [-1] * n, [n] * n

        stack = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                nextSmaller[stack.pop()] = i
            stack.append(i)

        stack = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            if stack:
                prevSmaller[i] = stack[-1]
            stack.append(i)

        res = 0
        mod = 10 ** 9 + 7

        for i in range(n):
            res += (i - prevSmaller[i]) * A[i] * (nextSmaller[i] - i)
            res %= mod
        return res


"""
1234543
54321
123345

"""
class SolutionLee:
    def sumSubarrayMins(self, A):
        n = len(A)
        mod = 10 ** 9 + 7
        stack1, stack2 = [], []
        left, right = [0] * n, [0] * n
        # the number of subarray ending with A[i]
        # left[i], the length of strict bigger numbers on the left of A[i]
        for i in range(n):
            count = 1
            #新来的num > 前面，说明没有大于的, count = 1 ex: 1234 - 1111
            while stack1 and A[i] < stack1[-1][0]:
                count += stack1.pop()[1]
            left[i] = count
            stack1.append([A[i], count])

        # the number of subarray starting with A[i]
        # right[i], the length of bigger numbers on the right of A[i]
        # 新来的num < 后面，说明没有大于的, count = 1    ex: 4321 - 1111
        for i in range(n)[::-1]:
            count = 1
            while stack2 and A[i] <= stack2[-1][0]:
                count += stack2.pop()[1]
            right[i] = count
            stack2.append([A[i], count])

        return sum(a * l * r for a, l, r in zip(A, left, right)) % mod


class Solution2:
    def sumSubarrayMins(self, nums):
        mod = (10 ** 9) + 7

        left = self.leftSmall(nums)
        right = self.rightSmall(nums)

        return sum(a * l * r for a, l, r in zip(nums, left, right)) % mod

    """
    For each element, get the previous least element (to it's left)
    """

    def leftSmall(self, nums):
        n = len(nums)
        left, stack = [-1] * n, []

        for i in range(n):
            # To maintain stack as a monotonically increasing stack
            while stack and nums[i] < nums[stack[-1]]:
                stack.pop()
            # We have popped everything that is > than curr nums[i], stack top is the least for nums[i]
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        for i in range(n):
            left[i] = i + 1 if left[i] == -1 else i - left[i]

        return left

    """
    For each element, get the next least element (to it's right)
    """

    def rightSmall(self, nums):
        n = len(nums)
        right, stack = [-1] * n, []

        for i in range(n):
            # To maintain stack as a monotonically increasing stack
            while stack and nums[i] < nums[stack[-1]]:
                # When curr nums[i] is smaller to the nums in stack.
                right[stack.pop()] = i
            stack.append(i)

        for i in range(n):
            right[i] = n - i if right[i] == -1 else right[i] - i

        return right


class Solution1:
    def sumSubarrayMins(self, A):
        mod = 10 ** 9 + 7
        left = [-1] * len(A)
        right = [len(A)] * len(A)
        # 计算left数组
        stack = [0]
        for i in range(1, len(A)):
            if A[i] > A[stack[-1]]:
                left[i] = stack[-1]
            else:
                while stack and A[i] <= A[stack[-1]]:
                    stack.pop()
                if not stack:
                    left[i] = -1
                else:
                    left[i] = stack[-1]
            stack.append(i)
        # 计算right数组
        stack = [len(A) - 1]
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[stack[-1]]:
                right[i] = stack[-1]
            else:
                while stack and A[i] < A[stack[-1]]:
                    stack.pop()
                if not stack:
                    right[i] = len(A)
                else:
                    right[i] = stack[-1]
            stack.append(i)

        res = 0
        for i in range(len(A)):
            res += A[i] * (i - left[i]) * (right[i] - i)
        return res % mod



"""
A     =  [3, 1, 2, 2, 2, 4, 4, 5]
left  =  [1, 2, 1, 1, 1, 1, 1, 1]
right =  [1, 7, 6, 5, 4, 3, 2, 1]
"""
A = [3,1,2,2,2,4,4,5]
a = SolutionLee()
print(a.sumSubarrayMins(A))









