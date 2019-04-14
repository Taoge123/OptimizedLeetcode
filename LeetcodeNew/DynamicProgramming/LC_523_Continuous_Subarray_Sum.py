
"""
Similar to
continuous subarray sum equals k
https://buptwc.com/2018/07/10/Leetcode-523-Continuous-Subarray-Sum/

Given a list of non-negative numbers and a target integer k,
write a function to check if the array has a continuous subarray of size at least 2
that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""

"""
If k == 0, then search for any consecutive pair of 0s.
Else, we will keep track of indices of the cumulative sum (or prefix sum) mod by k in a dictionary. 
We will return True if we've seen a cumulative sum % k at least 2 indices before.
This means that there is a subarray that has a sum(subarray) % k == 0 
and that subarray contains at least 2 elements.
"""
class Solution1:
    def checkSubarraySum(self, nums, k):
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in xrange(len(nums) - 1))
        mods, cum_sum_mod_k = {0: -1}, 0
        for i, n in enumerate(nums):
            cum_sum_mod_k = (cum_sum_mod_k + n) % k
            if cum_sum_mod_k in mods and i - mods[cum_sum_mod_k] > 1:
                return True
            if cum_sum_mod_k not in mods:
                mods[cum_sum_mod_k] = i
        return False


"""
if k == 0
If there are two continuous zeros in nums, return True
Time O(n).

if n >= 2k and k > 0
There will be at least three numbers in sum with the same remainder divided by k. So I can return True without any extra calculation.
Time O(1).

if n < 2k and k > 0
If I can find two numbers in sum with the same remainder divided by k and the distance of them is greater than or equal to 2， return True.
Time O(n) <= O(k).

k < 0
same as k > 0.
"""


class Solution2:
    def checkSubarraySum(self, nums, k):

        if k == 0:
            # if two continuous zeros in nums, return True
            # time O(n)
            for i in range(0, len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        k = abs(k)
        if len(nums) >= k * 2:
            return True

        # if n >= 2k: return True
        # if n < 2k:  time O(n) is O(k)

        sum = [0]
        for x in nums:
            sum.append((sum[-1] + x) % k)

        Dict = {}
        for i in range(0, len(sum)):
            if Dict.has_key(sum[i]):
                if i - Dict[sum[i]] > 1:
                    return True
            else:
                Dict[sum[i]] = i

        return False


"""
题目大意：
求数组nums中是否存在k的整数倍，并且长度至少为2的连续子段和。

注意：

数组长度不超过10,000。
可以假设所有数字的和范围在32位带符号整数之内。
解题思路：
遍历数组nums，求前i项和total；对k取模，记模值为m

利用map[m]记录模为m的前i项和的最小下标，初始令map[0] = -1

若map[m] + 1 < i，则返回True
"""

class Solution3:
    def checkSubarraySum(self, nums, k):

        map = {0 : -1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            m = total % k if k else total
            if m not in map:
                map[m] = i
            elif map[m] + 1 < i:
                return True
        return False


"""
我的思路：
这道题是求给定的一个序列中是否存在一个连续子序列，满足子序列元素之和为k的倍数。
最简单的办法，当然是暴力破解，通过二重循环，第一个重循环枚举每一个起点位置，
第二重循环遍历以当前起点位置开始，各个长度的连续子序列，一旦找到和为K的倍数就直接返回true，
如果一直都没找到就直接返回false，唯一需要注意的地方是几个特殊的测试用例，如nums = [1, 2], 
k = 0和nums = [0,0], k = 0。所以下面实现代码中的判断的条件才会略显复杂，时间复杂度是O(n2n2)，空间复杂度是O(1)。 
当然这道题可以用动态规划的思路去做，但是实现的时会发现时间复杂度接近O(n2n2)，
而空间复杂度比暴力破解更糟糕，会是O(nn)，所以就不贴出来我自己实现的动态规划的代码，如果有更好的动态规划的实现方式欢迎评论告知
"""

"""
参考思路：
在讨论里有个大神给出了时间复杂度是O(nn)的解法，他的思路非常巧妙，用了数学上的知识，下面给出他的解法的原理： 
假设: 
a[i]+a[i+1]+...+a[j]=n1k+q;
a[i]+a[i+1]+...+a[j]=n1k+q;

如果存在一个n 
n>j且a[i]+a[i+1]+...+a[j]+...+a[n]=n2k+q;
n>j且a[i]+a[i+1]+...+a[j]+...+a[n]=n2k+q;

那么 
a[j+1]+...+a[n]=(n2−n1)k
a[j+1]+...+a[n]=(n2−n1)k

因此利用这一结果，可以从序列第一个元素开始遍历，不断累加上当前的元素，并求出当前和除以k后的余数，用一个映射记录该余数出现时的下标，如果同一个余数出现了两次，
并且两次出现的下标之差大于1，那么就表示在这两个坐标之间的元素之和是k的倍数，因此就可以返回true，否则最后返回false。 
需要注意的两个地方： 
1. k可能取0，所以只有当k不为0时才对当前的和求余，同时针对于nums = [0, 0], k = 0的情况，需要添加一个初始映射(0, -1)来确保结果的正确。 
2. 下标之差至少为2才算是正确的情况，因为题目要求子序列长度至少为2，以上面的例子就是n至少等于j+2。 
具体实现见下面参考代码。
"""

"""
Since we are interested in quantities of the form A[L] + A[L+1] + ... + A[R], 
let's use a standard technique of keeping a prefix sum P[i] = sum(A[:i]), 
so that we can quickly query A[L] + A[L+1] + ... + A[R] = P[R+1] - P[L].

Now, we would like to know if P[R+1] - P[L] = 0 (mod k) is solvable with 0 <= L < R < len(A). 
This means: For any 0 <= L < len(A), we would like to know if there is some L + 2 <= X < len(A) with P[X] = P[L].

This can be solved in linear time: at decreasing time i, 
we've now seen in total all elements in P[i+2:], and we want to know if P[i] is something we've seen before. 
If we have, then indeed P[i] = P[j] for j >= i + 2 as desired.

Of course, there is the pesky "mod k" part. When k is zero, 
the modulus should be ignored, otherwise we should consider values of P modulo abs(k).
"""

class Solution4:
    def checkSubarraySum(self, A, k):
        P = [0]  # P[i] = sum(A[:i]), mod abs(k) if k != 0
        for x in A:
            v = P[-1] + x
            if k: v %= abs(k)
            P.append(v)

        seen = set()
        for i in xrange(len(P) - 3, -1, -1):
            seen.add(P[i + 2])
            if P[i] in seen:
                return True
        return False


"""
Idea: if sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. 
So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i. 
Once some later sum(nums[:i']) % k == sum(nums[:i]) % k and i' - i > 1, we return True.

Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n)
"""
class Solution5:
    def checkSubarraySum(self, nums, k):

        dic = {0:-1}
        summ = 0
        for i, n in enumerate(nums):
            if k != 0:
                summ = (summ + n) % k
            else:
                summ += n
            if summ not in dic:
                dic[summ] = i
            else:
                if i - dic[summ] >= 2:
                    return True
        return False


"""
For the case when k == 0 , we simply look for 2 consecutive occurences of 0 in nums.
When k != 0, we try to find 2 indices i and j, such that (sum(nums[0:j]) - sum(nums[0:i])) % k == 0. 
This can in turn be implemented by maintaining a running sum rs 
and storing rs % k in a hashset to check for a future occurence of the same number.
"""
class Solution6:
    def checkSubarraySum(self, nums, k):
        if k == 0:
            for i in range(0, len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False
        seen = {0, nums[0] % k}
        rs = nums[0]
        for i in range(1, len(nums)):
            rs = (rs + nums[i]) % k
            if rs in seen:
                return True
            seen.add(rs)
        return False


"""
Similar to the problem of continuous subarray sum equals k, 
use a hashmap to speedup the lookup, but the difference is that now the key should be the remainder
(cummulative sum mod k), so when we find the same key/remainder in hashmap, 
we find a subarray sum of n*k.
Time complexity is O(n).
Space complexity is O(min(k, n)).
"""

class Solution7:
    def checkSubarraySum(self, nums, k):

        if 0 == k:
            return len(nums) >= 2 and any(i == 0 and j == 0 for i, j in zip(nums, nums[1:]))

        sums = 0
        map = {0:-1}
        for i in range(len(nums)):
            sums += nums[i]
            rem = sums % k
            if rem in map:
                if i - map[rem] >= 2:
                    return True
            else:
                map[rem] = i
        return False

"""
Step 1: check array length, needs to be greater than 1
Step 2: if k == 0, return true if two consecutive items are 0
Step 3: Use presum and dictionary to record already appeard sums(%k). If the newly added sum (%k) is in the dic, it tells the newly added slice of array meets the criteria.
For example, if presum = 3, k =5, we have presume%k = 3 (add to dictionary), so if you added two more numbers 4, and 1, the presume will becomes 8, 8 %5 = 3, and 3 is already in dictionary, so we know the newly added two numbers must be divsible by k(5)
Step 4: care for the two corner cases:
a: what if the newly added value is the same as k: for example (1,3,5) k = 5, so we need to exclude this situation: nums[i] != k
b: what if the first two values are the same as k: for example (1,1), k=1, so we can include this situation by adding nums[0] == nums[1] == k
Either a or b can happen, so we use or in between
"""
class Solution8:
    def checkSubarraySum(self, nums, k):
        if len(nums) <= 1:
            return False
        if k == 0:
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1] == 0:
                    return True
                return False
        presum, dic = 0, {0:1}
        for i in range(len(nums)):
            presum += nums[i]
            if presum % k in dic and (nums[0] == nums[1] == k or nums[i]!=k):
                return True
            else:
                dic[presum%k] = 1
        return False


"""
分析：

这道题和560题解法一样，强烈建议先看那道题，具体见https://leetcode.com/problems/subarray-sum-equals-k/solution/
当我们分析数组中连续的若干数之和时，很容易想到先用一个数组sm[i]记录sum(nums[:i])，那么则有sm[j] - sm[i] = sum(nums[i:j])
但是如果依次遍历时间复杂度为O(n^2)，在这里肯定超时，所以我们得想个简单的办法，这也就是这类型题的经典思想，前缀和处理
我们先来考虑一个简单的情况，即是否存在连续的子数组的和为k，我们应该怎么做呢？
假设存在i,j满足sum(nums[i:j]) = k，那么则应有sm[j] - sm[i] = k，也就是如果我们找到i,j满足这个式子就可以说明存在…！
那当我们遍历sm数组时，将遍历的数依次存进集合，遍历至sm[j]时，我们如果发现sm[j]-k，即sm[i]是存在于集合中的，那么我们就可以确定,确实存在sum(nums[i:j]) = k
回到我们这道题上，假设确实存在i,j(j-i>=2)满足sum(nums[i:j]) = n * k，即sm[j] - sm[i] = n * k，
此时用上面的方法是不可行的，因为n*k是个不确定的数，我们无法判断其是否在集合内，
但我们只用作一个小小的变换————对上式两边同时模k，上式变为sm[j]%k - sm[i]%k = 0，
此时就和4中情况是等价的，唯独是集合中存储的数从sm[i]变成了sm[i]%k
思路：

因为j-i>=2，所以更新集合的时候应当推迟一步，即分析完sm[i]之后才将sm[i-1]%k加入集合之中
注意k = 0的情况，因为模0操作是不被允许的，所以需要单独处理
"""
class Solution9:
    def checkSubarraySum(self, nums, k):

        if k == 0: return '00' in ''.join(map(str,nums))
        # 初始化集合和前缀和数组
        s = set([0])
        sm = [nums[0]] * len(nums)
        for i in range(1,len(nums)):
            sm[i] = sm[i-1] + nums[i]
            if sm[i] % k in s:
                return True
            # 分析完之后再更新集合
            s.add(sm[i-1]%k)
        return False




