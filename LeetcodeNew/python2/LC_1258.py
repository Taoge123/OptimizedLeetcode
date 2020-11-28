import collections

class Solution:
    def generateSentences(self, synonyms, text: str):
        graph = collections.defaultdict(dict)
        queue = collections.deque()
        res = set()
        queue.append(text)

        for k, v in synonyms:
            graph[k][v] = 1
            graph[v][k] = 1

        while queue:
            node = queue.popleft()
            res.add(node)
            words = node.split()
            for i, word in enumerate(words):
                if word in graph:
                    for nei in graph[word]:
                        newWord = ' '.join(words[:i] + [nei] + words[i + 1:])
                        if newWord not in res:
                            queue.append(newWord)

        return sorted(list(res))




