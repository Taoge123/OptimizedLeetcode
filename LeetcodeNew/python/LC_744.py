


class Solution:
    def nextGreatestLetter(self, letters, target: 'str') -> 'str':
        lo, hi = 0, len(letters)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if letters[mid] > target:
                hi = mid -1
            elif letters[mid] <= target:
                lo = mid + 1
        return letters[lo % len(letters)]




