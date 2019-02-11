"""
Take aabbbcc as an example

counter would be {"a":2, "b":3, "c":2}

After preprocess: baseStr = "abc", mid = "b"
(if there is no char happens odd times, mid = "")

Then use backtracking to find all the permutation of baseStr,

the valid palindrome would be "permuStr + mid + reverseOfPermuStr"
"""

import collections

class Solution:
    def generatePalindromes(self, s):
        counter = collections.Counter(s)
        odds = filter(lambda x: x % 2, counter.values())
        if len(odds) > 1:
            return []
        baseStr, mid = self.preProcess(counter)
        return self.backTracking(baseStr, 0, mid, [baseStr + mid + baseStr[::-1]])

    def preProcess(self, counter):
        baseStr = mid = ""
        for char in counter:
            if counter[char] % 2:
                mid = char
            baseStr += char * (counter[char] / 2)
        return baseStr, mid

    def backTracking(self, s, idx, mid, ans):
        if idx == len(s) - 1:
            return ans
        for i in range(idx, len(s)):
            if i >= 1 and s[i] == s[i - 1] == s[idx]:
                continue  # no need to go deeper if swap would be the same
            # Swap s[idx] with s[i]
            if i != idx:
                permu = s[:idx] + s[i] + s[idx + 1:i] + s[idx] + s[i + 1:]
                ans.append(permu + mid + permu[::-1])
            else:
                permu = s
            self.backTracking(permu, idx + 1, mid, ans)
        return ans





class Solution2:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        # Same as 'Permutations I'. Add char to charlist if there is a double.
        chardict = {}
        charlist = []
        for c in sorted(s):
            if c not in chardict:
                chardict[c] = 1
            else:
                charlist.append(c)
                chardict.pop(c, None)

        if len(chardict) > 1: return []  # Same as 'Permutations I'. Return if not palindrome.
        mid = list(chardict.keys())[0] if len(chardict) == 1 else ""  # Get mid char.

        outlist = []
        visited = [0] * len(charlist)
        self.helper(visited, charlist, mid, "", outlist)  # Generate permutations via backtracking
        return outlist

    def helper(self, visited, charlist, mid, current, outlist):
        if len(current) == len(charlist):
            outlist.append(current + mid + current[::-1])
            return

        for i in range(len(charlist)):
            if i > 0 and visited[i - 1] == 0 and charlist[i] == charlist[i - 1]: continue
            if visited[i] == 0:
                visited[i] = 1
                self.helper(visited, charlist, mid, current + charlist[i], outlist)
                visited[i] = 0

        return




class Solution:

    def generatePalindromes(self, s):
        kv = collections.Counter(s)
        mid = [k for k, v in kv.iteritems() if v % 2]
        if len(mid) > 1:
            return []
        mid = '' if mid == [] else mid[0]
        half = ''.join([k * (v / 2) for k, v in kv.iteritems()])
        half = [c for c in half]

        def backtrack(end, tmp):
            if len(tmp) == end:
                cur = ''.join(tmp)
                ans.append(cur + mid + cur[::-1])
            else:
                for i in range(end):
                    if visited[i] or (i > 0 and half[i] == half[i - 1] and not visited[i - 1]):
                        continue
                    visited[i] = True
                    tmp.append(half[i])
                    backtrack(end, tmp)
                    visited[i] = False
                    tmp.pop()

        ans = []
        visited = [False] * len(half)
        backtrack(len(half), [])
        return ans

