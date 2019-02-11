#Use dictionary to store patterns, and backtrack when mismatch happens.


class Solution:
    def wordPatternMatch(self, pattern, str):
        return self.dfs(pattern, str, {})

    def dfs(self, pattern, str, dict):
        if len(pattern) == 0 and len(str) > 0:
            return False
        if len(pattern) == len(str) == 0:
            return True
        for end in range(1, len(str) - len(pattern) + 2):  # +2 because it is the "end of an end"
            if pattern[0] not in dict and str[:end] not in dict.values():
                dict[pattern[0]] = str[:end]
                if self.dfs(pattern[1:], str[end:], dict):
                    return True
                del dict[pattern[0]]
            elif pattern[0] in dict and dict[pattern[0]] == str[:end]:
                if self.dfs(pattern[1:], str[end:], dict):
                    return True
        return False



class Solution2:
    def wordPatternMatch(self, pattern, str):
        d = dict()
        return self.dfs(pattern, str, 0, '', d)

    def dfs(self, pattern, str, index, cur, d):
        # index is the current index of the pattern we are checking
        # cur stores the combination of new words formed by following pattern rules
        # d is a dict to store the previous letter to string correspondence
        if index >= len(pattern):
            return cur == str
        if pattern[index] in d:
            if str.startswith(cur + d[pattern[index]]):
                return self.dfs(pattern, str, index + 1, cur + d[pattern[index]], d)
        else:
            for i in range(len(cur), len(str)):
                if str[len(cur):i + 1] not in d.values():
                    d[pattern[index]] = str[len(cur):i + 1]
                    if self.dfs(pattern, str, index + 1, cur + str[len(cur):i + 1], d) == True:
                        return True
                    del d[pattern[index]]
            return False




