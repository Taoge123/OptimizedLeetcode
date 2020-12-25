
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        """
        Given n, this program generates an array of length n + 1
        according to the problem statement and returns the maximum
        of the array.

        :param n: last index (0 based) of generated array
        :type n: int
        :return: maximum value in generated array
        :rtype: int
        """

        """
        Base Case (n < 2):
        - The first two numbers in the array are 0 and 1.
        - The array formula does not start until index 2.
        - Return quickly with the answer if n is 0 or 1.
        """
        if n < 2:
            return n

        """
        General Case (n >= 2):
        - Generate array (nums) as follows:
          - For even k, nums[k] = nums[k/2]
          - For odd k, nums[k] = nums[(k-1)/2] + nums[(k+1)/2]
        - Return the maximum of nums.
        """
        nums = [0, 1]
        for k in range(2, n + 1):
            m = k // 2
            if k & 1 == 0:
                nums.append(nums[m])
            else:
                nums.append(nums[m] + nums[m + 1])
        return max(nums)


