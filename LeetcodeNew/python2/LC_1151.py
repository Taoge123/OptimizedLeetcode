
"""

Find the total number of one's in the array ==> K
K will be the size of the sliding windows, as long as 'end - start +1' is bigger than K,
we need to shrink the window
Have the counter for '1's in the array, find the max value of the count (maxCount) in sliding window for each iteration.
Total number of one - maxCount ==> Min. Swaps

"""


class Solution:
    def minSwaps(self, data) -> int:
        ones = sum(data)
        count = maxi = 0
        left = 0
        # while right < len(data):
        for right in range(len(data)):
            # updating the number of 1's by adding the new element
            count += data[right]
            right += 1
            # maintain the length of the window to ones
            if right - left > ones:
                # updating the number of 1's by removing the oldest element
                count -= data[left]
                left += 1
            # record the maximum number of 1's in the window
            maxi = max(maxi, count)
        return ones - maxi


