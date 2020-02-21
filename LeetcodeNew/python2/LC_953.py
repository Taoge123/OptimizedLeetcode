
class Solution:
    def isAlienSorted(self, words, order: str) -> bool:

        table = {char :i for i, char in enumerate(order)}

        words = [[table[char] for char in word] for word in words]

        return all(w1 < w2 for w1, w2 in zip(words, words[1:]))


