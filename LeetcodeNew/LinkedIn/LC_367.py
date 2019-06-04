

class Solution(object):
    def isPerfectSquare(self, num):
        b, e = 1, (num >> 1) + 1
        while b <= e:
            mid = (b + e) >> 1
            sq = mid * mid
            if sq == num:
                return True
            if sq > num:
                e = mid - 1
            else:
                b = mid + 1
        return False

def hcjdsb(num):
    l , r = 1,num
    while l<=r:
        mid = (l+r)//2
        if mid*mid == num:
            return True
        elif mid*mid < num:
            l = mid +1
        else:
            r = mid -1
    return False