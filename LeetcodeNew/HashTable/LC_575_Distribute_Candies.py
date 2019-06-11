
"""
Given an integer array with even length, where different numbers in this array represent different kinds of candies.
Each number means one candy of the corresponding kind. You need to distribute these candies equally in number
to brother and sister. Return the maximum number of kinds of candies the sister could gain.
Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.
Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.
Note:

The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].
"""

"""
There are len(set(candies)) unique candies, and the sister picks only len(candies) / 2 of them, so she can't have more than this amount.

For example, if there are 5 unique candies, then if she is picking 4 candies, 
she will take 4 unique ones. If she is picking 7 candies, then she will only take 5 unique ones.

"""
def distributeCandies(self, candies):
    return min(len(candies) / 2, len(set(candies)))


"""
解法一
思路
这题换一个表达方式就是：一个数组，划分为元素个数相等的两份，使得其中一份中元素的值尽可能不相同。

这里一个关键点在于“不同值的个数”和“子数组长度”的关系。例如[1, 2, 3, 4]的“不同值的个数”是4，“子数组长度”是2，
很显然无论如何划分都是最优解（如[1, 2]），即2；再例如[1, 1, 2, 2, 2, 2]的“不同值的个数”是2，“子数组长度”是3，
最优的划分是[1, 1, 2]或[1, 2, 2]，即2。

这样答案就呼之欲出了：“不同值的个数” > “子数组长度” ? “子数组长度” : “不同值的个数”。

"""

class Solution2:
    def distributeCandies(self, candies):

        nums = set(candies)
        num_nums = len(nums)
        target_num = len(candies) // 2
        return target_num if num_nums >= target_num else num_nums



