"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores,
who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and
"Bronze Medal".
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


class Solution2:
    def findRelativeRanks(self, nums):
        nums = sorted(nums, reverse=True)  # store results in descending order
        place = 1  # start counting places
        for score in nums:  # iterate from first to last place
            if place > 3:  # after podium
                nums[nums.index(score)] = str(place)  # find index of score and replace it with its place as string
            elif place == 1:
                nums[nums.index(score)] = "Gold Medal"  # for the first place give gold medal and analogically for the whole podium
            elif place == 2:
                nums[nums.index(score)] = "Silver Medal"
            elif place == 3:
                nums[nums.index(score)] = "Bronze Medal"
            place += 1  # in the end before checking next result go to the next place

        return nums


nums = [5, 4, 3, 2, 1]
a = Solution2()
print(a.findRelativeRanks(nums))
