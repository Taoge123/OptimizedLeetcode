
"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
"""
# def guess(num):

class Solution(object):

    def guessNumber(self, n):

        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1


class Solution2:
    def guessNumber(self, n):

        low = 0
        high = n
        while low <= high:
            mid = int((high + low) / 2)
            if guess(mid) == 1:
                low = mid + 1
            elif guess(mid) == -1:
                high = mid - 1
            else:
                break  # found the right number.
        return mid

class Solution3:
    def guessNumber(self, n):

        low  = 0
        high = n
        while True:
            mid = (low + high) // 2
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == -1:
                high = mid-1
            elif ans == 1:
                low = mid+1






