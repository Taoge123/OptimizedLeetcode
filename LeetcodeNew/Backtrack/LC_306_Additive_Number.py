"""
Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199.
             1 + 99 = 100, 99 + 100 = 199



The idea is quite straightforward:

Choose the first number A, it can be the leftmost 1 up to i digits.
i<=(L-1)/2 because the third number should be at least as long as the first number

Choose the second number B, it can be the leftmost 1 up to j digits
excluding the first number. the limit for j is a little bit tricky,
because we don't know whether A or B is longer.
The remaining string (with length L-j) after excluding A and B
should have a length of at least max(length A, length B),
where length A = i and length B = j-i, thus L-j >= max(j-i, i)

Calls the recursive checker function and returns true if passes the checker function,
or continue to the next choice of B (A) until there is no more choice for B or A,
in which case returns a false.

"""
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # Idea: find the first 2 strings and then continue to check the remaining strings
        L = len(num)
        # 1st number is num[0:i], 2nd number is num[i:j]
        for i in range(1, L/ 2 + 1):
            if num[0] == '0' and i >= 2: break
            for j in range(i + 1, min(L - i, (L + i) / 2) + 1):
                if num[i] == '0' and j - i >= 2: break  # means starting with "0", e.g., "03"
                num1 = num[0:i]
                num2 = num[i:j]
                remain = num[j:]
                if self.isAdditive(num1, num2, remain):
                    return True

        return False

    def isAdditive(self, num1, num2, remain):
        if remain == "":  # means checked whole string
            return True
        total = str(int(num1) + int(num2))
        if remain.startswith(total):
            return self.isAdditive(num2, total, remain[len(total):])
        else:
            return False



"""
1. Store the previous 2 numbers
2. Once you've reached level 2, it means 2 numbers are before you
3. Continue only if those 2 previous numbers == currennt number, 
or if we have not reached level 2 yet
4. if first character of current number is 0, and the length is greater than 1, 
then just continue without recursing. So it will allow 0, but not 01, 001, etc.

5. return True if and only if we reached the end of the string and we have at least 3 numbers

6. Once we have found a solution, no need to check anything else, 
just return True all the way back up the tree
"""


class Solution:
    def isAdditiveNumber(self, num):

        def recurse(end, level, prev, prev2):
            if level > 2 and end == len(num):
                return True
            for index in range(end + 1, len(num) + 1):
                if num[end:index][0] == '0' and len(num[end:index]) > 1: continue
                curr = int(num[end:index])
                if level <= 1 or (level > 1 and prev + prev2 == curr):
                    if recurse(index, level + 1, curr, prev): return True
            return False

        return recurse(0, 0, 0, 0) 

