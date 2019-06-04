
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums ) % k! =0:
            return False
        use d =[0 ] *len(nums)
        nums.sort(reverse=True)
        if (sum(nums ) /k ) <nums[0]:
            return False
        for i in range(len(nums)):
            if used[i ]= =0:
                if not self.helper(nums ,i ,used ,sum(nums ) / k -nums[i]):
                    return False
        return True

    def helper(self ,nums ,index ,used ,subsum):
        if subsu m= =0:
            used[index ] =1
            return True
        used[index ] =1
        for i in range(inde x +1 ,len(nums)):
            if nums[i ]< =subsum and used[i ]= =0:
                if self.helper(nums ,i ,used ,subsu m -nums[i]):
                    return True
                else:
                    used[i ] =0
        return False


def canPartitionKSubsets(nums, k):
	target, m = divmod(sum(nums), k)
	if m: return False
	dp, n = [0]*k, len(nums)
	nums.sort(reverse=True)
	def dfs(i):
		if i == n:
			return len(set(dp)) == 1
		for j in range(k):
			dp[j] += nums[i]
			if dp[j] <= target and dfs(i+1):
				return True
			dp[j] -= nums[i]
			if not dp[j]: break
		return False
	return nums[0] <= target and dfs(0)




