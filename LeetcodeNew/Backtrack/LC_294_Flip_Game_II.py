"""
You are playing the following Flip Game with your friend:
Given a string that contains only these two characters: + and -,
you and your friend take turns to flip two consecutive "++" into "--".
The game ends when a person can no longer make a move
and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:

Input: s = "++++"
Output: true
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".

"""

class Solution:
    def canWin(self, s):

        poss = self.getposs(s, False)
        return poss

    def getposs(self, s, poss):

        for i in range(len(s) - 1):
            if s[i:i + 2] != '++':
                continue
            else:
                poss = poss or not self.getposs(s[:i] + '--' + s[i + 2:], poss)
        return poss


class Solution2:
    def canWin(self, s):
        for i in range(len(s) - 1):
            if s[i:i + 2] == "++":
                if not self.canWin(s[:i] + "--" + s[i + 2:]):
                    return True
        return False



class Solution3:
    def __init__(self):
        self.result = {}

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s in self.result:
            return self.result[s]

        for i in range(len(s) - 1):
            if s[i:i + 2] == "++":
                if not self.canWin(s[:i] + "--" + s[i + 2:]):
                    ##just these two line to cache!!!! Done!
                    self.result[s[:i] + "--" + s[i + 2:]] = False
                    self.result[s] = True
                    return True
        return False



