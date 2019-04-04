
"""
https://buptwc.com/2018/10/15/Leetcode-923-3Sum-With-Multiplicity/
https://blog.csdn.net/fuxuemingzhu/article/details/83115850

Given an integer array A, and an integer target,
return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

Example 1:

Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.


Note:

3 <= A.length <= 3000
0 <= A[i] <= 100
0 <= target <= 300
"""

"""
Count the occurrence of each number.
using hashmap or array up to you.

Loop i on all numbers,
loop j on all numbers,
check if k = target - i - j is valid.

Add the number of this combination to result.
3 cases covers all possible combination:

i == j == k
i == j != k
i < k && j < k
Time Complexity:
3 <= A.length <= 3000, so N = 3000
But 0 <= A[i] <= 100
So my solution is O(N + 101 * 101)
"""
import collections
import itertools

class SolutionLee:
    def threeSumMulti(self, A, target):
        c = collections.Counter(A)
        res = 0
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k: res += c[i] * (c[i] - 1) * (c[i] - 2) / 6
            elif i == j != k: res += c[i] * (c[i] - 1) / 2 * c[k]
            elif k > i and k > j: res += c[i] * c[j] * c[k]
        return res % (10**9 + 7)


"""
因为我自己代码逻辑的问题，每次twoSum都用重新开空间，确实会有很大的重复计算，但是我想每次重开的空间d，
其实数量并不大，也就不到100，A的长度不超过3000，总空间也不会超过300000啊，感觉应该是能AC的。

然后我写了个O(1) space的解法，最后勉强能通过，我猜测可能是python本身语言特性的原因导致tle。

当然为了验证这个猜测，我也仿照discuss里面别人c++的思路来写python代码，但只要时间复杂度为O(n^2)并涉及到空间的都会TLE。

唯独这一种解法，在使用单纯的数组而非Counter()函数后，是勉强可以通过的，运行时间和我的解法差不多。
(所以我脑子还是不够灵性，像这样计算前面的twoSum就不用每次都重开数组了)
"""

# O(n^2) time, O(300) space 2744ms
class Solution2:
    def threeSumMulti(self, A, target):
        d = [0] * 300
        res = 0
        for i in range(len(A)):
            res += d[target-A[i]] if target-A[i] >=0 else 0
            res %= (10**9+7)
            for j in range(i):
                d[A[i] + A[j]] += 1
        return res % (10**9+7)

"""
解题方法
看到3sum直接就3sum走起啊！因为需要统计总共出现的次数，那么直接暴力肯定是不行的，需要我们先统计每个数字出现了多少次，
过会进行一个查找和组合。使用了set和list来保存去重的数字。

两重循环i, j，分别对应了第一二个数字，需要注意的是第二个数字和第一个数字相同，所以j从i开始向后遍历。
第三个数字等于target减去前两个数字，比较重要的一步是需要判断第三个数字要不比第二个数字小，而且第三个数字必须在set中，
因为第三个数字不能向前找，得向后找，而且可以等于第二个数字！

如果把上面的a, b, c全都找到了，那么底下的方法就很简单了，求一个组合数字！从counter里面知道每个数字出现了多少次，
判断一下，这三个数字是不是都不相等、有两个相等、三个全相等，这三种情况，然后就知道了总的数字组合会出现多少次。

最后最后，需要模一个数，就是因为忘了求模，导致又浪费了一次提交。。

时间复杂度是O(N^2)，空间复杂度是O(N)。
"""






