"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []

"""


import collections


class Solution:
    def generatePalindromes(self, s: str):

        res = []
        n = len(s)
        counter = collections.Counter(s)
        odd = [key for key, value in counter.items() if value % 2]
        if len(odd) > 1:
            return []
        elif len(odd) == 1:
            counter[odd[0]] -= 1
            self.dfs(n, counter, odd[0], res)
        else:
            self.dfs(n, counter, "", res)
        return res

    def dfs(self, n, counter, path, res):
        if len(path) == n:
            res.append(path)
            return

        for k, v in counter.items():
            if v > 0:
                counter[k] -= 2
                self.dfs(n, counter, k + path + k, res)
                counter[k] += 2



class SolutionRika:
    def generatePalindromes(self, s: str):

        count = collections.defaultdict(int)
        for ch in s:
            count[ch] += 1

        odds = 0
        self.odd_char = ""
        for k, v in count.items():
            if v % 2 == 1:
                odds += 1
                self.odd_char = k

            if odds > 1:
                return []
        res = []
        self.dfs(s, count, '', res)

        return res

    def dfs(self, s, count, path, res):

        if len(path) == len(s) // 2:
            res.append(path + self.odd_char + path[::-1])
            return res

        for ch, v in count.items():
            if v >= 2:
                count[ch] -= 2
                self.dfs(s, count, path + ch, res)
                count[ch] += 2