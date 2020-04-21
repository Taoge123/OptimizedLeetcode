"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""

import collections
import string


class SolutionBestOneWay:
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


# two-way bfs
class SolutionBestTwoWay:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)
        word_len = len(beginWord)

        # construct word comb dict
        table = collections.defaultdict(list)
        for word in wordSet:
            for i in range(word_len):
                table[word[:i] + '*' + word[i + 1:]].append(word)

        # bfs prep
        queue = collections.deque()
        queue.append(beginWord)
        queue.append(endWord)
        visited = {beginWord: 1, endWord: -1}

        # bfs
        while queue:
            n = queue.popleft()
            level = visited[n]
            for i in range(word_len):
                node = n[:i] + '*' + n[i + 1:]
                for word in table[node]:
                    if word not in visited:
                        visited[word] = level + 1 if level > 0 else level - 1
                        queue.append(word)
                    if (visited[word] > 0) ^ (level > 0):
                        return abs(visited[word] - level)

        return 0





class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
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




class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        queue = collections.deque([beginWord])
        another_queue = collections.deque([endWord])
        words, n, res = set(wordList), len(beginWord), 1
        if endWord not in words:
            return 0

        while queue:
            res += 1
            words -= set(queue)
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(n):
                    for char in string.ascii_lowercase:
                        next_word = word[:i] + char + word[i + 1:]
                        if next_word in words:
                            if next_word in another_queue:
                                return res
                            queue.append(next_word)
            if len(queue) > len(another_queue):
                queue, another_queue = another_queue, queue

        return 0



class SolutionTempt:

    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return 0

        def gen_nei_word(word):
            for i in range(len(word)):
                for char in string.ascii_lowercase:
                    if char != word[i]:
                        yield word[:i] + char + word[i + 1:]

        begins, ends, step, seen = {beginWord}, {endWord}, 1, {beginWord}
        while begins and ends:
            if len(begins) > len(ends):  # pick the smaller group for next BFS iteration
                begins, ends = ends, begins
            next_begins = set()
            for word in begins:
                for nei in gen_nei_word(word):
                    if nei in ends:
                        return step + 1
                    if nei in words and nei not in seen:
                        seen.add(nei)
                        next_begins.add(nei)
            begins, step = next_begins, step + 1
        return 0

