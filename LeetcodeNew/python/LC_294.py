"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:

Input: s = "++++"
Output: true
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
Follow up:
Derive your algorithm's runtime complexity.

"""



class Solution:
    def canWin(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i:i + 2] == "++":
                if not self.canWin(s[:i] + "--" + s[i + 2:]):
                    return True
        return False



class Solution2:
    def canWin(self, s: str) -> bool:
            self.memo={}
            return self.helper(s)

    def helper(self,s):
        if s in self.memo:
            return self.memo[s]

        for i in range(len(s)-1):
            if s[i]=='+' and s[i+1]=='+' and not self.helper(s[:i]+'--'+s[i+2:]):
                self.memo[s]=True
                return True
        self.memo[s]=False
        return False



s = "++++"
a = Solution()
print(a.canWin(s))

