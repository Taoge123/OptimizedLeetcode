
"""
https://leetcode.com/problems/implement-magic-dictionary/discuss/255330/Python-Basic-Trie

Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether
if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary,
as static/class variables are persisted across multiple test cases. Please see here for more details.
"""
"""
Instead of adding a flag self.isWord in the trie, here we use self.count to count how many words can reach the same ending character. 
Say we have 'aaa','aab' already built in the magic dict, then self.findWord('aab') should return True because when 'aa_' 
reaches its end in the trie, the count is 2.
"""

import collections

class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.count = 0


class MagicDictionary:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dict):
        for word in dict:
            self.addWord(word)
            for i, char in enumerate(word):
                self.addWord(word[:i] + '_' + word[i + 1:])

    def search(self, word: str) -> bool:
        original = self.findWord(word)
        changed = 0
        for i, char in enumerate(word):
            changed += self.findWord(word[:i] + '_' + word[i + 1:])
        return True if changed > original * len(word) else False

    def addWord(self, word):
        layer = self.trie
        for i, char in enumerate(word):
            layer = layer.children[char]
        layer.count += 1

    def findWord(self, word):
        layer = self.trie
        for i, char in enumerate(word):
            if char in layer.children:
                layer = layer.children[char]
            else:
                return 0
        return layer.count



"""
解题思路：
创建字典dmap<String, Set>

build操作：用下划线'_'替换word的每一个位置的字母，作为Key，被替换的字母作为Value，存入dmap

search操作：用下划线'_'替换word的每一个位置的字母，作为Key，在dmap中查找与被替换字母不同的值
"""
class MagicDictionary2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dmap = collections.defaultdict(set)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            for x in range(len(word)):
                key = word[:x] + '_' + word[x+1:]
                self.dmap[key].add(word[x])

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for x in range(len(word)):
            key = word[:x] + '_' + word[x+1:]
            values = self.dmap[key]
            if not values: continue
            if word[x] not in values or len(values) > 1:
                return True
        return False


class MagicDictionary3:

    def _candidate(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i + 1:]

    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.words = set(words)
        print
        self.words
        self.near = collections.Counter([word for word in words for word in self._candidate(word)])
        print
        self.near

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return any(
            self.near[cand] > 1 or self.near[cand] == 1 and word not in self.words for cand in self._candidate(word))




class MagicDictionary3:
    def _genneighbors(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i+1:]

    def buildDict(self, words):
        self.words = set(words)
        self.count = collections.Counter(nei for word in words
                                        for nei in self._genneighbors(word))

    def search(self, word):
        return any(self.count[nei] > 1 or
                   self.count[nei] == 1 and word not in self.words
                   for nei in self._genneighbors(word))


