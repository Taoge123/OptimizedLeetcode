"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
"""

"""
Explanation
Initial the result res to include the case of empty string "".
res include all possible combinations we find during we iterate the input.

Itearte the the input strings,
but skip the word that have duplicate characters.
The examples is kind of misleading,
but the input string can have duplicate characters,
no need to considerate these strings.

For each string,
we check if it's conflit with the combination that we found.
If they have intersection of characters, we skip it.
If not, we append this new combination to result.

return the maximum length from all combinations.

"""


class Solution:
    def maxLength(self, arr) -> int:

        dp = [set()]
        for string in arr:
            # if string contains duplicated
            if len(set(string)) < len(string):
                continue
            string = set(string)
            for char in dp[:]:
                if string & char:
                    continue
                dp.append(string | char)

        return max(len(s) for s in dp)



class Solution2:
    def __init__(self):
        self.res = 0

    def maxLength(self, arr) -> int:
        self.backtrack([], 0, arr)
        return self.res

    def backtrack(self, path, pos, arr):
        self.res = max(self.res, len("".join(path)))
        for i in range(pos, len(arr)):
            path.append(arr[i])
            temp = "".join(path)
            if len(set(temp)) == len(temp):
                self.backtrack(path, i + 1, arr)
            path.pop()


class SolutionBest:
    def maxLength(self, arr) -> int:

        new = []
        for num in arr:
            num = list(num)
            if len(num) == len(set(num)):
                new.append(num)

        arr = [[ord(char) - ord('a') for char in num] for num in new]
        dp = {0: 0}

        for num in arr:
            for k in list(dp.keys()):
                # Check if characters in arr[i] dont exists in used[j]
                if all(not (k & (1 << char)) for char in num):
                    # Updated used[j] to make used[i]
                    used = k
                    for char in num:
                        used |= (1 << char)

                    # Recursive equation mentioned above
                    dp[used] = max(dp[k] + len(num), dp.get(used, 0))
        return max(dp.values())


arr = ["ab","cd","ef"]
a = Solution()
print(a.maxLength(arr))




