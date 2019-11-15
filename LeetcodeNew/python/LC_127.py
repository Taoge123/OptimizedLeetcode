import collections
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordList = set(wordList)
        visited = set()
        queue = collections.deque([(beginWord, 1)])
        lowercase = string.ascii_lowercase
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                for j in lowercase:
                    if j != word[i]:
                        newWord = word[:i] + j + word[ i +1:]
                        if newWord not in visited and newWord in wordList:
                            queue.append((newWord, dist + 1))
                            visited.add(newWord)




        return 0

