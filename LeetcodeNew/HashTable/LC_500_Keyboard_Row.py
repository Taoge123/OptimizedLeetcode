
"""
Given a List of words, return the words that can be typed using letters of alphabet
on only one row's of American keyboard like the image below.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]


Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

"""
I have used set to check the word.
I firstly make every line a set of letter.
Then I check every word if this word set is the subset if any line set.
"""
class SolutionLee:
    def findWords(self, words):
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        ret = []
        for word in words:
            w = set(word.lower())
            if w <= line1 or w <= line2 or w <= line3:
                ret.append(word)
        return ret

    def findWords2(self, words):
        keyboards = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        ans = []
        for w in words:
            if any(set(w.lower()) <= set(r) for r in keyboards):
                ans.append(w)

        return ans

    def findWords3(words):
        return [word for row in [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')] for word in words if
                set(word.lower()) <= row]




