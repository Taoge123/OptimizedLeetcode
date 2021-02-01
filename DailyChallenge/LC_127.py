

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        n = len(beginWord)
        wordList = set(wordList)

        # construct word comb dict
        table = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                table[word[:i] + '*' + word[i + 1:]].append(word)

        # bfs prep
        queue = collections.deque()
        queue.append(beginWord)
        visited = set()
        level = 0

        # bfs
        while queue:
            size = len(queue)
            level += 1
            for _ in range(size):
                node = queue.popleft()
                for i in range(n):
                    newNode = node[:i] + '*' + node[i + 1:]
                    for word in table[newNode]:
                        if endWord == word:
                            return level + 1
                        if word not in visited:
                            visited.add(word)
                            queue.append(word)
        return 0

    