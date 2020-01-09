
"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.






Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]


Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""


class Solution:
    def findWords(self, words):

        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        res = []
        for word in words:
            w = set(word.lower())
            if w <= line1 or w <= line2 or w <= line3:
                res.append(word)
        return res


words = ["Hello", "Alaska", "Dad", "Peace"]
a = Solution()
print(a.findWords(words))



