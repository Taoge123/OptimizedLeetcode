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

