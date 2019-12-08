
"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores,
who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.
"""


class Solution:
    def findRelativeRanks(self, nums):

        if not nums:
            return []

        newNums = sorted(nums, reverse=True)
        table = {}
        l = len(newNums)
        table[newNums[0]] = "Gold Medal"
        if l > 1:
            table[newNums[1]] = "Silver Medal"
        if l > 2:
            table[newNums[2]] = "Bronze Medal"

        for i in range(3, l):
            table[newNums[i]] = str(i + 1)

        res = [table[num] for num in nums]
        return res

















