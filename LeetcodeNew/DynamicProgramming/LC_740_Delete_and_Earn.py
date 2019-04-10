
"""
Similar to House Robbers

Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points.
After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation:
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.


Example 2:

Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation:
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.

Note:

The length of nums is at most 20000.
Each element nums[i] is an integer in the range [1, 10000].
"""

"""
This question can be reduced to the House Robbers question also on LeetCode. 
Please have a look at it if you haven't seen it before.

Observations:

- The order of nums does not matter.
- Once we decide that we want a num, we can add all the occurrences of num into the total.
We first transform the nums array into a points array that sums up the total number of points for that particular value. 
A value of x will be assigned to index x in points.

nums: [2, 2, 3, 3, 3, 4] (2 appears 2 times, 3 appears 3 times, 4 appears once)
points: [0, 0, 4, 9, 4] <- This is the gold in each house!

The condition that we cannot pick adjacent values is similar to the House Robber question that we cannot rob adjacent houses. 
Simply pass points into the rob function for a quick win 🌝!
"""
import collections


"""
Time: O(M+N)
Space: O(N)

M: the length of input array
N: the range of the value of each int element

public int deleteAndEarn(int[] nums) {
    int[] count = new int[10001];
    for(int n : nums){
        count[n] += n;
    }
    int[] dp = new int[10003];
    for(int i = 10000; i >= 0; i--) {
        dp[i] = Math.max(count[i] + dp[i + 2], dp[i + 1]);
    }
    return dp[0];
}
"""

"""
解题思路：
动态规划（Dynamic Programming）

dp[x]表示删除不大于x的所有数字的最大得分。

cnt[x]存储数字x的个数。
状态转移方程：

dp[x] = max(dp[x - 1], dp[x - 2] + cnt[x] * x)
"""
class Solution2:
    def deleteAndEarn(self, nums):
        cnt = collections.Counter(nums)
        maxn = max(nums + [0])
        dp = [0] * (maxn + 10)
        for x in range(1, maxn + 1):
            dp[x] = max(dp[x - 1], dp[x - 2] + cnt[x] * x)
        return dp[maxn]


"""
动态规划问题，对于nums中出现的最大的数n来说，有两种可能：

能挣到点数，那么最大的分数就是n×n出现的次数+最大值为n-2时的分数
不能挣到点数，那么最大值就是最大值为n-1的分数
因为nums的元素取值范围为[1,10000]所以可以用哈希表来保存每个数字出现了多少次。
"""
class Solution3:
    def deleteAndEarn(self, nums):
        numSum = [0]*10001
        dp = [0] * 10001
        for num in nums:
            numSum[num] += num
        for i in range(1, len(dp)):
            if i == 1:
                dp[i] = numSum[i]
            else:
                dp[i] = max(dp[i-1], dp[i-2]+numSum[i])
        return max(dp)

class Solution4:
    def deleteAndEarn(self, nums):
        points=[0]*1001
        # print(points)
        for num in nums:
            points[num]+=num
        prev,curr=0,0
        for point in points:
            prev,curr=curr,max(point+prev,curr)
        return curr


class SolutionHouseRob:
    def rob(self, nums):
        prev = curr = 0
        for value in nums:
            prev, curr = curr, max(prev + value, curr)
        return curr

    def deleteAndEarn(self, nums):
        points = [0] * 10001
        for num in nums:
            points[num] += num
        return self.rob(points)

"""
When rob is used directly, it is just 6 lines:
"""
class Solution1:
    def deleteAndEarn(self, nums):
        points, prev, curr = [0] * 10001, 0, 0
        for num in nums:
            points[num] += num
        for value in points:
            prev, curr = curr, max(prev + value, curr)
        return curr


"""
Suggested by @ManuelP, it can be further shortened into 4 lines if you use collections.Counter and modify the rob function:
"""
class Solution11:
    def deleteAndEarn(self, nums):
        points, prev, curr = collections.Counter(nums), 0, 0
        for value in range(10001):
            prev, curr = curr, max(prev + value * points[value], curr)
        return curr

class SolutionFast1:
    def deleteAndEarn(self, nums):
        histogram = collections.Counter(nums)
        value = valueBack1 = valueBack2 = 0
        prevElement = -9999
        for element,count in sorted(histogram.items()):
            if prevElement+1 == element:
                value = max(valueBack1, valueBack2+element*count)
            else:
                value = valueBack1 + element*count
            valueBack2 = valueBack1
            valueBack1 = value
            prevElement = element
        return value


