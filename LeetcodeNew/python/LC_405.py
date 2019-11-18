



class Solution:
    def toHex(self, num: int) -> str:
        if not num:
            return '0'
        mp = '0123456789abcdef'  # like a map
        ans = ''
        for i in range(8):
            n = num & 15       # this means num & 1111b
            c = mp[n]          # get the hex char
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')  # strip leading zeroes



