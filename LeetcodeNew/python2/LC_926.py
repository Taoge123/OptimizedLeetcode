"""
818. Race Car

https://leetcode.com/problems/race-car/
"""

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        if not S:
            return 0

        ones = 0
        flip = 0

        for ch in S:
            if ch == '0':
                if ones != 0:
                    flip += 1
                else:
                    continue
            else:
                ones += 1

            # flip = min(flip, ones)
            if flip > ones:
                flip = ones

        return flip



"""
left[i] : number of min flips -> s[0] ~ s[i] all 0
right[i] : number of min flips -> s[i] ~ s[n-1] all 1

res = min(left[i-1] + right[i], left[n-1], right[0])

if s[i] == '1':
    left[i] = left[i-1] + 1

if s[i] == '0':
    right[i] = right[i+1] + 1

"""



class SolutionDP:
    def minFlipsMonoIncr(self, S: str) -> int:
        dp0 = [0] # cnts to make S[:i+1] valid and ending with '0' after flip
        dp1 = [0] # cnts to make S[:i+1] valid and ending with '1' after flip

        for c in S:
            if c is '0':
                dp0.append(dp0[-1])
                dp1.append(min(dp0[-2], dp1[-1]) + 1)
            elif c is '1':
                dp0.append(dp0[-1] + 1)
                dp1.append(min(dp0[-2], dp1[-1]))

        return min(dp0[-1], dp1[-1])



