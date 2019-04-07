
"""
Given an integer array, return the k-th smallest distance among all the pairs.
The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

"""

# Efficient Solution: uses binary search and bisect_right - refer to it here
import bisect

class Solution:
    def countPairsLTE(self, array, value):
        ans = 0
        for i in range(len(array)):
            ans += bisect.bisect_right(array, array[i] + value, lo=i) - i - 1
        return ans

    def smallestDistancePair(self, nums, k):

        nums.sort()
        low, high = min([abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1)]), abs(nums[0] - nums[~0])
        while low < high:
            mid = (low + high) / 2
            if self.countPairsLTE(nums, mid) < k:
                low = mid + 1
            else:
                high = mid
        return low




class Solution2:
    def smallestDistancePair(self, nums, k):

        nums.sort()
        lo = 0
        high = nums[-1] - nums[0]
        print(nums)
        while lo <= high:
            mid = (lo + high) // 2
            count = 0
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and abs(nums[j] - nums[i]) <= mid:
                    j += 1
                count += (j - i - 1)
            if count<k:
                lo = mid + 1
            else:
                high = mid - 1
        return lo


"""
RT: O(N lg N + M lg N)

O(N log N) for the initial sort of nums +
possible() does 2N passes, i.e. O(N), and we call it lg M times, where M is the max distance possible, 
i.e. max num - min num. Therefore O(N * lg M)

Spc: O(1)
"""

class Solution3:
    def smallestDistancePair(nums, k):
        # Return: Is there k or more pairs with distance <= guess? i.e. are
        # there enough?
        def possible(guess_dist):
            i = count = 0
            j = 1
            # Notice that we never decrement j or i.
            while i < len(nums):
                # If the distance calculated from j-i is less than the guess,
                # increase the window on `j` side.
                while (j < len(nums)) and ((nums[j] - nums[i]) <= guess_dist):
                    j += 1
                # Count all places between j and i
                count += j - i - 1
                i += 1
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]

        while lo < hi:
            mid = (lo + hi) // 2
            # If `mid` produced `k` or more results we know it's the upper bound.
            if possible(mid):
                # We don't set to `mid - 1` because we found a number of distances
                # bigger than *or equal* to `k`. If this `mid` ends up being
                # actually equal to `k` then it's a correct guess, so let's leave it within
                # the guess space.
                hi = mid
            # If `mid` did not produce enouh results, let's increase  the guess
            # space and try a higher number.
            else:
                lo = mid + 1

        # `lo` ends up being an actual distance in the input, because
        # the binary search mechanism waits until the exact lo/hi combo where
        # 2nd to last `mid` did not produce enough results (k or more), but
        # the last `mid` did.
        return lo

# Walkthrough example.Input = [2, 4, 5, 8, 9].k = 5
"""
lo: 0, hi: 7, mid: 3  # mid is 3, let's count how many distances are 3 or less
count: 5, k: 5, possible? yes  # There are 5 distances <= our guess '3'
hi (7) becomes mid (3)   # OK so 3 is the upper bound, why guess higher than '3'?
                         # No point as it might add more distances than we want
lo: 0, hi: 3, mid: 1
count: 2, k: 5, possible? no  # Only 2 distances are less than our new guess '1'
                              # This means our guess is bad: it's too low.
                              # Guess higher, by setting the guess space higher by
                              # moving `lo` to one higher than our guess.
lo (0) becomes mid+1 (2)
lo: 2, hi: 3, mid: 2
count: 3, k: 5, possible? no  # New guess is still too low
lo (2) becomes mid+1 (3)
lo is the answer: 3  # Notice we had guessed '3' before: at the start, but now
                     # we narrowed it down to a point where `mid` as a guess
     # is too low, but mid+1 is perfect. mid+1 happens to be `hi` that was set
     # in the very first step: it was waiting for `lo` to reach it.
"""






