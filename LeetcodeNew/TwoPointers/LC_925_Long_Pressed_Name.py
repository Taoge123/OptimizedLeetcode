
"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
"""

"""
这个题目是对两个字符串进行操作，很容易想到双指针，如果name[i]和typed[j]相等，
那么就都往下走一步，当不相等时，由于长按，如果typed[j] == typed[j-1]，可以让j++。 
最后i要等于name.length。
"""
class SolutionLee:
    def isLongPressedName(self, name, typed):
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)


class Solution1:
    def isLongPressedName(self, name, typed):
        i, j = 0, 0
        L1, L2 = len(name), len(typed)
        while i < L1 and j < L2:
            if name[i] == typed[j]:
                i, j = i + 1, j + 1
            elif typed[j] == typed[j - 1]:
                j = j + 1
            else:
                return False
        return True if i == L1 else False

"""
The idea is to iterate through the typed string, because it's longer, 
checking against a particular location in name as you go. 
There are only a couple of possibilities:

There is a match (name[i] == typed[j]). In this case you want to increment both pointers.
There isn't a match and (given by else condition to case 1) 
there also isn't a match to the previous character in name (not name[i-1] == typed[j]), 
in which case it's clear the strings don't meet the condition.
Note you also have to be careful with the pointer i in to name, 
because it starts off not large enough to index name at i-1, 
and it can keep growing so long as there are matches. 
So ensure it's greater than zero before entering the second condition, 
and cap it at len(name) for the cases like ['vtkgn', 'vttkgnn']: 
i ends up being 5 at the end there while j keeps running along the extra 'n's, 
so we fall in to the second condition and check name[i-1] against typed[j].

If we violate both conditions, we know the things don't match, so we can return False immediately. 
If we meet both conditions for the duration of typed, 
then we only have to make sure we've also gotten entirely through the name 
so we catch cases like ['pyplrz', 'ppyypllr'].
"""

class Solution2:
    def isLongPressedName(self, name, typed):
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif not i > 0 and name[i-1] == typed[j]:
                return False
        return i == len(name)



class Solution3:
    def isLongPressedName(self, name, typed):
        j = 0
        for c in name:
            if j == len(typed):
                return False

            # If mismatch...
            if typed[j] != c:
                # If it's the first char of the block, ans is False.
                if (j == 0) or (typed[j-1] != typed[j]):
                    return False

                # Discard all similar chars.
                cur = typed[j]
                while j < len(typed) and typed[j] == cur:
                    j += 1

                # If next isn't a match, ans is False.
                if j == len(typed) or typed[j] != c:
                    return False

            j += 1

        return True




