
"""
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""
class Solution1:
    def firstBadVersion(self, n):

        r = n-1
        l = 0
        while(l<=r):
            mid = l + (r-l)/2
            if isBadVersion(mid)==False:
                l = mid+1
            else:
                r = mid-1
        return l


class Solution2:
    def firstBadVersion(self, n):
        lo = 1
        hi = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo


class Solution3:
    def firstBadVersion(self, n):

        head, tail = 1, n
        if isBadVersion(1):
            return 1
        while head < tail-1:
            middle = (tail + head) // 2
            if isBadVersion(middle):
                tail = middle
            else:
                head = middle
        return tail


