import collections

class Solution:
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        index = collections.deque(range(n))
        res = [None] * n

        for card in sorted(deck):
            res[index.popleft()] = card
            if index:
                index.append(index.popleft())
        return res



class Solution2:
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        index = collections.deque(range(n))
        res = [None] * n

        for card in sorted(deck):
            res[index.popleft()] = card
            if index:
                temp = index.popleft()
                index.append(temp)
        return res


deck = [17,13,11,2,3,5,7]
a = Solution2()
print(a.deckRevealedIncreasing(deck))

