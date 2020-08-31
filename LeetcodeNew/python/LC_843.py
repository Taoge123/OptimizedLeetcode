"""
此题的原理很简单：我们任取一个word，调用API查看它与secret的匹配度k。于是我们可知，任何与word匹配度不是k的单词，肯定都不会是secret，于是就可以从candidate中删除。

一旦我们取到某个word，与secret的匹配度是6，那么就是答案。

相似度==3 -> 相似度不为3的都排除
"""


import random

class Master:
    def guess(self, word: str) -> int:
        pass

class Solution:
    def findSecretWord(self, wordlist, master: 'Master') -> None:
        random.shuffle(wordlist)
        for i in range(10):
            guess = random.choice(wordlist)
            x = master.guess(guess)
            wordlist = [w for w in wordlist if self.match(guess, w) == x]

    def match(self, word1, word2):
        return sum(i == j for i, j in zip(word1, word2))


