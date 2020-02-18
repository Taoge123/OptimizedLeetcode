"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

"""

"""
题目大意：
给定一个整数数组，判断其中是否存在两个不同的下标i和j满足：| nums[i] - nums[j] | <= t 并且 | i - j | <= k

解题思路：
解法I：“滑动窗口” + 字典（桶）
如果： | nums[i] - nums[j] | <= t   式a

等价： | nums[i] / t - nums[j] / t | <= 1   式b

推出： | floor(nums[i] / t) - floor(nums[j] / t) | <= 1   式c

​等价： floor(nums[j] / t) ∈ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 式d
其中式b是式c的充分非必要条件，因为逆否命题与原命题等价，所以：

如果： floor(nums[j] / t) ∉ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 非d

推出： | nums[i] - nums[j] | > t   非a
因此只需要维护一个大小为k的窗口（字典）numDict，其中键为nums[i] / t，值为nums[i]。

遍历数组nums时，检查nums[i]与键集{floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}对应的值的差值即可。
"""

import collections

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):

        if k < 1 or t < 0:
            return False

        table = collections.OrderedDict()
        for num in nums:
            key = num if not t else num // t
            for lastNum in (table.get(key - 1), table.get(key), table.get(key + 1)):
                if lastNum is not None and abs(num - lastNum) <= t:
                    return True
            if len(table) == k:
                table.popitem(False)

            table[key] = num

        return False


class Solution2:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 0 or t < 0:
            return False
        window = collections.OrderedDict()
        for num in nums:
            # Make sure window size
            #last=False means pop the First one
            if len(window) > k:
                window.popitem(False)

            bucket = num if not t else num // t
            # At most 2t items.
            for val in (window.get(bucket - 1), window.get(bucket), window.get(bucket + 1)):
                if val is not None and abs(num - val) <= t:
                    return True
            window[bucket] = num
        return False


class Solution3:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:

        if t < 0:
            return False
        n = len(nums)
        table = {}
        bucket = t + 1
        for i in range(n):
            val = nums[i] // bucket
            if val in table:
                return True
            if val - 1 in table and abs(nums[i] - table[val - 1]) < bucket:
                return True
            if val + 1 in table and abs(nums[i] - table[val + 1]) < bucket:
                return True
            table[val] = nums[i]
            if i >= k:
                del table[nums[i - k] // bucket]
        return False


"""
解法II：“滑动窗口” + TreeSet
参考LeetCode Discuss：https://leetcode.com/discuss/38177/java-o-n-lg-k-solution

TreeSet数据结构（Java）使用红黑树实现，是平衡二叉树的一种。

该数据结构支持如下操作：

1. floor()方法返set中≤给定元素的最大元素；如果不存在这样的元素，则返回 null。

2. ceiling()方法返回set中≥给定元素的最小元素；如果不存在这样的元素，则返回 null。

Java代码：
public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if(k < 1 || t < 0)
            return false;
        TreeSet<Integer> set = new TreeSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            int n = nums[i];
            if(set.floor(n) != null && n <= t + set.floor(n) || 
                    set.ceiling(n) != null && set.ceiling(n) <= t + n)
                return true;
            set.add(n);
            if (i >= k)
                set.remove(nums[i - k]);
        }
        return false;
    }
}
"""


