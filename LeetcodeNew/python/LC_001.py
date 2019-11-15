class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_temp = dict()
        for index, value in enumerate(nums):
            if target - value in dict_temp:
                return [dict_temp[target - value], index]
            dict_temp[value] = index
