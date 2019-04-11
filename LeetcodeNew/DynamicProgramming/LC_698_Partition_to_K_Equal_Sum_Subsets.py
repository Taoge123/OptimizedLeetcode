
"""
https://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/

Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
"""
"""

We can solve this problem recursively, we keep an array for sum of each partition 
and a boolean array to check whether an element is already taken into some partition or not.
First we need to check some base cases,
If K is 1, then we already have our answer, complete array is only subset with same sum.
If N < K, then it is not possible to divide array into subsets with equal sum, 
because we can’t divide the array into more than N parts.
If sum of array is not divisible by K, then it is not possible to divide the array. 
We will proceed only if k divides sum. Our goal reduces to divide array into K parts where sum of each part should be array_sum/K
In below code a recursive method is written which tries to add array element into some subset. 
If sum of this subset reaches required sum, we iterate for next part recursively, 
otherwise we backtrack for different set of elements. 
If number of subsets whose sum reaches the required sum is (K-1), 
we flag that it is possible to partition array into K parts with equal sum, 
because remaining elements already have a sum equal to required sum.
"""

class SolutionLee:
    def canPartitionKSubsets(self, A, k):
        if len(A) < k:
            return False
        ASum = sum(A)
        A.sort(reverse=True)
        if ASum % k != 0:
            return False
        target = [ASum / k] * k

        def dfs(pos):
            if pos == len(A): return True
            for i in range(k):
                if target[i] >= A[pos]:
                    target[i] -= A[pos]
                    if dfs(pos + 1):
                        return True
                    target[i] += A[pos]
            return False
        return dfs(0)


"""
Put n items into k bucket so each bucket has same total item value.
- For each bucket, try all possible content O(k*2^n) -- no good.
- For each item, try all possible destined bucket O(n^k) -- doable.

Utilizes "empty bucket" trick by @chengyuge925 from here.
Recursively checks whether element i fits either of subsets.

Surprisingly, removing of "empty bucket" trick makes it slowest python solution.
"""

"""
1, if sums[j] == 0: break

1. The key is, sums[j] == 0 means for all k > j, sum[k] == 0; 
   because this algorithm always fill the previous buckets before trying the next.
2. So if by putting nums[i] in this empty bucket can't solve the game, 
   putting nums[i] on other empty buckets can't solve the game either.
2, nums.sort(reverse=True)

   Always start from big numbers for this kind of problem, 
   just by doing it yourself for a few times you will find out that the big numbers are the easiest to place.
"""
class Solution1:
    def canPartitionKSubsets(self, nums, k):
        sums = [0] * k
        subsum = sum(nums) / k
        nums.sort(reverse=True)
        l = len(nums)

        def walk(i):
            if i == l:
                return len(set(sums)) == 1
                # return True
            for j in range(k):
                sums[j] += nums[i]
                if sums[j] <= subsum and walk(i + 1):
                    return True
                sums[j] -= nums[i]
                if sums[j] == 0:
                    break
            return False

        return walk(0)


class Solution11:
    def canPartitionKSubsets(self, nums, k):
        nums.sort(reverse=True) # Game Changer 1
        buck, kSum = [0] * k, sum(nums) // k
        def dfs(idx):
            if idx == len(nums): return len(set(buck)) == 1
            for i in range(k):
                buck[i] += nums[idx]
                if buck[i] <= kSum and dfs(idx + 1): return True
                buck[i] -= nums[idx]
                if buck[i] == 0: break # Game Changer 2
            return False
        return dfs(0)


class Solution2:
    def canPartitionKSubsets(self, nums, k):
        # trivial case one subset
        if k == 1: return True
        # trivial case, k must be k<=n
        n = len(nums)
        if k > n: return False
        # k*target = sum(nums)
        total = sum(nums)
        if total % k: return False

        target = total / k
        seen = [0] * n
        # speeds things up, as larger numbers are tried first if its not possible
        # to get k subsets we will know sooner
        nums.sort(reverse=True)

        def dfs(k, index, current_sum):
            # trivial, one group
            if k == 1: return True
            # found one group, need more k-1 groups
            if current_sum == target:
                return dfs(k - 1, 0, 0)
            # group can start with any number
            for i in range(index, n):
                # if we have not tried it before, and adding it
                # to current sum does not exceed target then
                if not seen[i] and current_sum + nums[i] <= target:
                    # we have seen it
                    seen[i] = 1
                    # recursively build group from i+1
                    if dfs(k, i + 1, current_sum + nums[i]):
                        return True
                    seen[i] = 0
            return False

        return dfs(k, 0, 0)


"""
The key idea is pretty straightforward, adding numbers until the sum equals to target.
Thinking it as pouring water to multiple buckets, fill the first then deal with the others.

Some key points:

1. Instead of filling in k buckets, we can reduce k when sum == target <- keep track only one sum each time
2. We don't need to verify till k==0, since we always check that total%k == 0. 
   That means if we already fill in k-1 buckets perfectly, the last one will be also filled
3. We need -
 - A list to keep recorders on used value (by index, due to the duplication in the nums)
 - An index to help us to keep add values after the current value until we filled the bucket (== target)
4. Everytime we need to check and add value from the very beginning of the list, 
   due to the current index may make us skip certain values. DFS(k-1, 0, 0)
   For example,
   [3,3,2,2] target =5
   If we start from the first 3, we will end up using the first 2 to fill the buckets. Then current index = 2
   If we use DFS (k-1,index,0) then we will start at index=3 (the second 2) to fill the next buckets, 
   while skipping the second 3 unexpected.

5. Sorting numbers will help a lot, since larger numbers are easier to fit in
"""


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 0: return False

        n = len(nums)
        if k > n: return False

        total = sum(nums)


        if total % k: return False

        sub_sum = total / k
        nums.sort(reverse=True)
        visited = [0] * n


        def DFS(k, index, curr_sum):
            if k == 1:
                return True
            if curr_sum == sub_sum:
                return DFS(k - 1, 0, 0)
            for i in range(index, n):
                if not visited[i] and nums[i] + curr_sum <= sub_sum:
                    visited[i] = 1
                    if DFS(k, i + 1, curr_sum + nums[i]):
                        return True
                    visited[i] = 0
            return False


        return DFS(k, 0, 0)


"""
回溯法
这是一个套题，和416. Partition Equal Subset Sum，473. Matchsticks to Square基本一致的代码，
上面的两个题分别是求平分成2份和4份。这个是任意的k份。所以改成了k组数字记录的div，最后看是否能够正好进行平分。

直接使用回溯法即可，这个回溯的要求是恰好把nums的所有数字用过一遍，使得目标数组中恰好有k个相同数字。
当所有的数字恰好用完的时候，就是我们平分的时候，即可返回true。题目给出的数字范围只到16，所以本算法时间复杂度是O(N!)，仍然能通过。

这里要证明，为什么只需要判断恰好用完即可返回true。因为我们所有数字的和是确定的，
即sum(target) = div * k = sum(nums)。如果我们在每个位置放数字的时候，
保证了放置的数字<=该位置的数字，即保证了在最终状态的target[i]>=0。此时有sum(target) >= 0。
又已知所有数字恰好用完，所以恰好有sum(target) = 0。故，当所有数字恰好用完时，target的每个位置都是0.
"""


class Solution3:
    def canPartitionKSubsets(self, nums, k):

        if not nums or len(nums) < k: return False
        _sum = sum(nums)
        div, mod = divmod(_sum, k)
        if _sum % k or max(nums) > _sum / k: return False
        nums.sort(reverse=True)
        target = [div] * k
        return self.dfs(nums, k, 0, target)

    def dfs(self, nums, k, index, target):
        if index == len(nums): return True
        num = nums[index]
        for i in range(k):
            if target[i] >= num:
                target[i] -= num
                if self.dfs(nums, k, index + 1, target): return True
                target[i] += num
        return False


"""
另外一种Python解法定义的dfs()函数的意义是使用nums[ind:]能不能构成k个和分别为self.target的数字，
因为这种做法会反复遍历nums，而不像上面这种做法只用遍历一次，所以这个做法需要用visited数组，
表示nums[i]数字是否已经使用过。"""

class Solution4:
    def canPartitionKSubsets(self, nums, k):

        if k == 1: return True
        self.n = len(nums)
        if self.n < k: return False
        total = sum(nums)
        if total % k: return False
        self.target = total / k
        visited = [0] * self.n
        nums.sort(reverse = True)
        def dfs(k, ind, sum, cnt):
            if k == 1: return True
            if sum == self.target and cnt > 0:
                return dfs(k - 1, 0, 0, 0)
            for i in range(ind, self.n):
                if not visited[i] and sum + nums[i] <= self.target:
                    visited[i] = 1
                    if dfs(k, i + 1, sum + nums[i], cnt + 1):
                        return True
                    visited[i] = 0
            return False
        return dfs(k, 0, 0, 0)


class Solution5:
    def canPartitionKSubsets(self, nums, k):

        dmap = {}
        def solve(nums, target, k):
            if k == 1: return sum(nums) == target
            key = (tuple(nums), k)
            if key in dmap: return dmap[key]
            size = len(nums)
            ans = False
            for x in range(1 << size):
                sums = 0
                rest = []
                for y in range(size):
                    if (x >> y) & 1:  sums += nums[y]
                    else: rest.append(nums[y])
                if sums == target and solve(rest, target, k - 1):
                    ans = True
                    break
            dmap[key] = ans
            return ans
        sums = sum(nums)
        if sums % k: return False
        return solve(sorted(nums), sums / k, k)




