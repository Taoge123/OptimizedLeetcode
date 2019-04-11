
"""
https://www.geeksforgeeks.org/partition-problem-dp-18/
https://blog.csdn.net/fuxuemingzhu/article/details/79787425

https://leetcode.com/problems/partition-equal-subset-sum/discuss/90643/Python-solution-with-detailed-explanation
https://leetcode.com/problems/partition-equal-subset-sum/discuss/90658/2-liner-in-Python.-Optimization-and-tricks-explained.

Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

"""

class Solution1:
    def canPartition(self, nums):

        possible_sums = {0}
        for n in nums:
            possible_sums.update({(v + n) for v in possible_sums})
        return (sum(nums) / 2.)  in possible_sums


class SolutionLee:
    def canPartition(self, nums):
        if sum(nums) & 1 == 0:
            target = sum(nums) >> 1
            cur = {0}
            for i in nums:
                cur |= {i + x for x in cur}
                if target in cur:
                    return True
        return False


"""
Seek whether there's a combination has the sum equal to half of total sum.
Simply return False if sum of the list is not even.
Target minus each element as Target for next recursion of the rest elements.

Base case:
Target < 0 (ignore)
Target == 0 (return True)

Recursive case:
Otherwise
"""
class Solution3:
    def canPartition(self, nums):
        nums.sort(reverse=True)
        def helper(start, target):         # Here path is not needed
            if target < 0: return
            elif target == 0: return True
            for i in range(start, len(nums)):
                if helper(i+1, target-nums[i]): return True
            return False

        return False if sum(nums)%2 else helper(0, sum(nums)/2)


"""
Algorithm

- If the sum of all elements is odd, then you cannot have 2 subsets with equal sum. So test this and return False.
- If the sum is even, then the problem produces to find a subset which is equal to a target sum.
- is_subset(i, target) = Can we form target using array[i,...N-1]?
- You can include nums[i] or exclude nums[i] and reduce the problem to the nums array starting from i+1.
- is_subset(i, target) = is_subset(i+1, target) or is_subset(i+1, target-nums[i])"""

from collections import defaultdict
class Solution4:
    def helper(self, i, array, target, cache):
        if target == 0:
            return True
        elif target < 0 or i == len(array):
            return False
        else:
            if i in cache and target in cache[i]:
                return cache[i][target]
            else:
                cache[i][target] = self.helper(i+1, array, target, cache)
                if target-array[i] >= 0:
                    cache[i][target] = cache[i][target] or self.helper(i+1, array, target-array[i], cache)
                return cache[i][target]

    def canPartition(self, nums):

        total = sum(nums)
        if total & 1:
            return False
        else:
            target = total // 2
        return self.helper(0, nums, target, defaultdict(dict))


class Solution5:
    def canPartition(self, nums):

        total = sum(nums)
        dp = [True] + [False] * (total / 2)
        for i in range(1, len(nums) + 1):
            for j in reversed(range(1, total / 2 + 1)):
                dp[j] = dp[j] or (j - nums[i - 1] >= 0 and dp[j - nums[i - 1]])
        return dp[-1] and not total % 2

"""
Faster/More efficient method. Less intuitive, 
relies on weird method of going through weights in reverse 
on the inner loop to avoid overwriting prior outer loop iteration's dp[j] calculations.
"""


class Solution6:
    # this is an application of knapsack problem, where w=sum(nums)/2
    def canPartition(self, nums):

        isum = sum(nums)

        # if weight not divisible by two, we cannot possibly have two equal sets
        if isum % 2 != 0:
            return False

        # isum is weight
        isum /= 2

        # dp init
        dp = [False for j in range(isum + 1)]
        dp[0] = True

        # j is weight bound, and i is arr pointer.
        # dp[j] :: for a weight j, can we partition into two equal sets with elements 0..i
        for i in range(len(nums)):
            # reversal neessary, because if we go in non-reversed order, we will overwrite
            # dp[] calculations from the previous iteration of outer loop. thus we go small to big to preserve previous iteration
            for j in reversed(range(1, isum + 1)):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]

        return dp[isum]


"""
Slightly less efficient, still same complexity at O(n^2)... 
More intuitive and straight forward in my opinion. This i my preferred solution.
"""


class Solution7:
    # this is an application of knapsack problem, where w=sum(nums)/2
    def canPartition(self, nums):

        isum = sum(nums)

        # if weight not divisible by two, we cannot possibly have two equal sets
        if isum % 2 != 0:
            return False

        # isum is weight
        isum /= 2

        # dp init
        dp = [[False for j in range(isum + 1)] for i in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            for j in range(isum + 1):
                if i == 0 and j == 0:  # base case, nothing to select with, and 0 weight
                    dp[i][j] = True
                elif i == 0:  # i == 0 signifies base case where we select nothing, we can never achieve any non-zero goal
                    dp[i][j] = False
                elif j == 0:  # we can always achieve weight goal of 0, just select nothing.
                    dp[i][j] = True
                else:  # dp transition step
                    if j >= nums[
                        i - 1]:  # do a weight bounds check, then check both possibilities of both including and excluding the current element nums[i - 1]
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                    else:
                        dp[i][j] = dp[i - 1][j]

        return dp[len(nums)][isum]

"""
To make the code short, here are some tricks:

divmod is used.
More importantly, dp array should be reversed, where dp[0] stores the value 
for sum target, dp[1] stores the value for target-1...dp[values] stores the value for 0
That's why we return dp[0] in the end.
"""

class Solution8:
    def canPartition(self, nums):
        target = sum(nums)
        if target % 2:
            return False
        target //= 2
        dp = [True] + [False]*target
        for n in nums:
            for s in range(target, n-1, -1):
                dp[s] = dp[s] or dp[s-n]
        return dp[-1]


"""
问题分析：
这个题目给的标签是动态规划，看了一下大神们做的，大多数用的深度优先搜索。在这里就介绍一种简单的方法。
思路：求出这些数字中的所有可能的和，放到字典中，然后判断平分值是否在这个字典中，即可。
"""
class Solution9:
    def canPartition(self, nums):
        sums = sum(nums)
        if sums % 2 == 1: return False  # 能否被2整除
        all_sum = {0}  # 用于存放所有可能的和
        for n in nums:  # 计算出所有可能的和
            all_sum.update({(v + n) for v in all_sum})
        return (sum(nums) / 2.) in all_sum  # 1/2总和， 是否存在

"""
解题思路：
动态规划（Dynamic Programming）

利用数组dp[i]记录和为i的子数组是否存在，初始令dp[0] = 1

for num in nums:
    for i in range(sum(nums) - num + 1):
        if dp[i]: dp[i + num] = 1
"""
class Solution99:
    def canPartition(self, nums):

        sums = sum(nums)
        if sums & 1: return False
        nset = set([0])
        for n in nums:
            for m in nset.copy():
                nset.add(m + n)
        return sums / 2 in nset

"""
题目大意 给定一个数组，求能不能把数组分成两部分使得两个子数组的和相等

解题思路：直接brute force解，数组的每个元素都取二进制0或者1来表示有没有选取，这样时间复杂度太高。会超时

动态规划：dp[i][j]表示能否用数组前i个元素的到和j。退一步就是能否用前i-1个元素得到和 j - num_i 。
所以如果 dp[i-1][j - num_i] 成立，那么dp[i][j]也成立。最后就是检查dp[n-1][sum/2]是不是成立。
所以如果数组的和为基数的话，那么肯定无解。
"""
class Solution10:
    def canPartition(self, nums):
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        dp = [0 for _ in range(s + 1)]
        dp[0] = 1
        for num in nums:
            for i in range(s, -1, -1):
                if dp[i]:
                    dp[i+num] = 1
            if dp[s/2]:
                return True
        return False


"""
Following are the two main steps to solve this problem:
1) Calculate sum of the array. If sum is odd, there can not be two subsets with equal sum, so return false.
2) If sum of array elements is even, calculate sum/2 and find a subset of array with sum equal to sum/2.

The first step is simple. The second step is crucial, it can be solved either using recursion or Dynamic Programming.

Recursive Solution
Following is the recursive property of the second step mentioned above.

Let isSubsetSum(arr, n, sum/2) be the function that returns true if 
there is a subset of arr[0..n-1] with sum equal to sum/2

The isSubsetSum problem can be divided into two subproblems
 a) isSubsetSum() without considering last element 
    (reducing n to n-1)
 b) isSubsetSum considering the last element 
    (reducing sum/2 by arr[n-1] and n to n-1)
If any of the above the above subproblems return true, then return true. 
isSubsetSum (arr, n, sum/2) = isSubsetSum (arr, n-1, sum/2) ||
                              isSubsetSum (arr, n-1, sum/2 - arr[n-1])

"""


def isSubsetSum(arr, n, sum):
    # Base Cases
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    # If last element is greater than sum, then
    # ignore it
    if arr[n - 1] > sum:
        return isSubsetSum(arr, n - 1, sum)

    ''' else, check if sum can be obtained by any of  
    the following 
    (a) including the last element 
    (b) excluding the last element'''

    return isSubsetSum(arr, n - 1, sum) or isSubsetSum(arr, n - 1, sum - arr[n - 1])


# Returns true if arr[] can be partitioned in two
# subsets of equal sum, otherwise false
def findPartion(arr, n):
    # Calculate sum of the elements in array
    sum = 0
    for i in range(0, n):
        sum += arr[i]
        # If sum is odd, there cannot be two subsets
    # with equal sum
    if sum % 2 != 0:
        return False
        # Find if there is subset with sum equal to
    # half of total sum
    return isSubsetSum(arr, n, sum // 2)


# Driver program to test above function
arr = [3, 1, 5, 9, 12]
n = len(arr)
if findPartion(arr, n) == True:
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")

"""
Time Complexity: O(2^n) In worst case, this solution tries two possibilities (whether to include or exclude) for every element.
"""

"""
Dynamic Programming Solution
The problem can be solved using dynamic programming when the sum of the elements is not too big. 
We can create a 2D array part[][] of size (sum/2)*(n+1). 
And we can construct the solution in bottom up manner such that every filled entry has following property

part[i][j] = true if a subset of {arr[0], arr[1], ..arr[j-1]} has sum 
             equal to i, otherwise false
"""


def findPartition(arr, n):
    sum = 0
    i, j = 0, 0

    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]

    if sum % 2 != 0:
        return False

    part = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]

    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True

    # intialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False

    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):

        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]

            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])

    return part[sum // 2][n]


# Driver Code
arr = [3, 1, 1, 2, 2, 1]
n = len(arr)
if findPartition(arr, n) == True:
    print("Can be divided into two",
          "subsets of equal sum")
else:
    print("Can not be divided into ",
          "two subsets of equal sum")


'''------------------------------------------------------------------------------------------'''
"""
DFS
首先要判断所有数字的和是不是偶数，然后我们使用一个长度为2的数组进行保存我们要平分得到的target，
这么做是我们可以通过使用-，+两种操作来跳过一些数字。同样是dfs，这里的dfs操作允许跳过某些位置去向下寻找，
只要找到一个满足条件的就可以停止。而subsets的题不可以这么做，因为我们要找到所有的可能的答案。因此可以看做是两套模板。
"""


class Solution111:
    def canPartition(self, nums):

        _sum = sum(nums)
        div, mod = divmod(_sum, 2)
        if mod or max(nums) > div: return False
        nums.sort(reverse=True)
        target = [div] * 2
        return self.dfs(nums, 0, target)

    def dfs(self, nums, index, target):
        for i in range(2):
            if target[i] >= nums[index]:
                target[i] -= nums[index]
                if target[i] == 0 or self.dfs(nums, index + 1, target): return True
                target[i] += nums[index]


"""
动态规划
这个题其实是个0-1背包问题。所以可以使用动态规划求解。

求和是必须的，目标target等于和的一半。如果和不是偶数的话则一定不可能由数组构成出来，直接返回false.

首先定义dp数组为dp[i][j]，其意义是使用前i个数字的和能不能构成整数j。
我们需要把每个位置都进行遍历，同时也要对0~target之间的所有正整数进行遍历。
很显然，状态转移的方程是，遍历到i位置时能不能构成target = 前面的数字的和能够成target || 前面的数字能构成target - nums[i]。
这两个状态分别是选不选取nums[i]的两种情况，如果有一种情况成立即可。
"""
"""
状态转移方程如下：

dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i]]
1
这个题的技巧和难点就在于，需要把数组的每个数字的和当做dp的一个状态，这个是很少见的，其实题目给的有提示：
数组的每个数都是整数，并且数字不会超过200，数组长度不超过100，这些说明了数字的和不会太大不会太多。
"""
"""
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        const int N = nums.size();
        int target = sum >> 1;
        if (sum % 2 != 0) return false;
        //dp[i][j] means whether we can sum to j using first i numbers.
        vector<vector<bool>> dp(N + 1, vector<bool>(sum + 1, false));
        // every number can build number 0.
        for (int i = 0; i <= N; ++i) {
            dp[i][0] = true;
        }
        // but for position 0, it can build number nothing.
        for (int j = 1; j <= target; ++j) {
            dp[0][j] = false;
        }
        // anyway, position 0 can build number 0.
        dp[0][0] = true;
        for (int i = 1; i <= N; ++i) {
            for (int j = 0; j <= target; ++j) {
                if (j >= nums[i - 1])
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i - 1]];
                else
                    dp[i][j] = dp[i - 1][j];
            }
        }
        return dp[N][target];
    }
};
"""
"""
从上面的代码中可以看出，每个位置的状态只与其前面位置的状态有关，所以可以做状态压缩节约空间复杂度。

只使用一维dp数组，dp[j]表示从数组中任意取数字的和能不能构成j。状态转移方程就是忽略掉二维数组的第一个维度即可，即：

dp[j] = dp[j] || dp[j - nums[i]]
1

还要说一下，为什么需要从后向前更新dp，这是因为每个位置依赖与前面的一个位置加上nums[i]，
如果我们从前向后更新的话，那么dp[i - 2]会影响dp[i - 1]，然后dp[i - 1]接着影响dp[i]，
即同样的一个nums[i]被反复使用了多次，结果肯定是不正确的。但是从后向前更新就没有问题了。

那么结合上面的分析，可以写出如下代码：

"""
"""
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        const int N = nums.size();
        if (sum % 2 != 0) return false;
        int target = sum >> 1;
        vector<bool> dp(sum + 1, false);
        dp[0] = true;
        for (int num : nums) {
            for (int j = target; j >= num; --j) {
                dp[j] = dp[j] || dp[j - num];
            }
        }
        return dp[target];
    }
};
"""




