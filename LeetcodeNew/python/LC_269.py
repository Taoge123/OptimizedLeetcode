"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""



import collections

class Solution:
    def alienOrder(self, words) -> str:
        graph = collections.defaultdict(set)
        degree = {char: 0 for word in words for char in word}
        for i, word1 in enumerate(words[:-1]):
            word2 = words[i + 1]
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    continue
                if c2 not in graph[c1]:
                    degree[c2] += 1
                graph[c1].add(c2)
                break
        res = ''
        queue = collections.deque([char for char in degree if not degree[char]])
        while queue:
            char = queue.popleft()
            res += char
            for nei in graph[char]:
                degree[nei] -= 1
                if not degree[nei]:
                    queue.append(nei)
        return res if len(res) == len(degree) else ''



class SolutionDFS:  # 比较每个word的同index上的char，如果前面相同，比较不同的那位。不同的时候 --> word1[i]:word2[i]
    def alienOrder(self, words) -> str:

        graph = collections.defaultdict(set)
        visited = {char: 0 for word in words for char in word}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            diff = False
            for j in range(min(len(word1), len(word2))):
                c1, c2 = word1[j], word2[j]
                if c1 != c2:
                    graph[c1].add(c2)
                    diff = True
                    break
            # return False when, for example, word1="z", word2="zx"
            if not diff and len(word1) > len(word2):
                return ""

        self.res = []
        for node in visited:
            if visited[node] == 0:
                if not self.dfs(graph, node, visited):
                    return ''
        return "".join(self.res)[::-1]

    def dfs(self, graph, node, visited):
        if visited[node] == -1:  # visited --> check has cycle
            return False
        if visited[node] == 1:  # backtrack --> finished check --> no cycle
            return True

        visited[node] = -1
        for nei in graph[node]:
            if not self.dfs(graph, nei, visited):
                return False
        visited[node] = 1  # backtracking --> no cycle
        self.res.append(node)
        return True



words =  ["wrt",
          "wrf",
          "er",
          "ett",
          "rftt"]

a = Solution()
print(a.alienOrder(words))


