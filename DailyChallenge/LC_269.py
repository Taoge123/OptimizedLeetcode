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
