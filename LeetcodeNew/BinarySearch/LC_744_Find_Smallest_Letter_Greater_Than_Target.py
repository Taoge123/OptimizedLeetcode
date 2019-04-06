
"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""
import bisect

"""
Since the input is sorted, you can use binary search, or simply linear scan and it will still be accepted.
"""
class Solution1:
    def nextGreatestLetter(self, letters, target):
        for letter in letters:
            if letter > target:
                return letter
        return letters[0] # If not found


class Solution2:
    def nextGreatestLetter(self, letters, target):
        pos = bisect.bisect_right(letters, target)
        return letters[0] if pos == len(letters) else letters[pos]

"""
The letters[l % len(letters)] is really just a shortcut for the case where there's a wraparound 
for the next smallest letter larger than target. 
Like [c, f, g] with target h, solution is c, so with this binary search approach, 
we'd evaluate g last, and see that it's <= target, leading us to l = r = len(letters). 
You could also have done, return letters[l] if l < len(letters) else letters[0], 
but it would be same thing as (l % len(letters)).
"""
class Solution3:
    def nextGreatestLetter(self, letters, target):
        lo, hi = 0, len(letters)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if letters[mid] > target:
                hi = mid -1
            elif letters[mid] <= target:
                lo = mid + 1
        return letters[lo % len(letters)]


"""
Python - classic upper_bound / bisect_right algo
"""

class Solution4:
    def nextGreatestLetter(self, letters, target):
        lo, hi = 0, len(letters)
        while lo < hi:
            mid = lo + hi >> 1
            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return letters[lo % len(letters)]




class StandardBisect:
    #move high
    def bisect_right(self, a, x, lo=0, hi=None):

        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(a)
        while lo < hi:
            mid = (lo+hi)//2
            if x < a[mid]:
                hi = mid
            else:
                lo = mid+1
        return lo


    def bisect_left(self, a, x, lo=0, hi=None):
        # move low
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(a)
        while lo < hi:
            mid = (lo+hi)//2
            if a[mid] < x:
                lo = mid+1
            else:
                hi = mid
        return lo




