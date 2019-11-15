
class Solution:
    def isPalindrome(self, s):

        i = 0
        j = len(s) - 1

        while i < j:

            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j = j - 1

            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True

