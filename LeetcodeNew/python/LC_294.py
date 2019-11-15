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


