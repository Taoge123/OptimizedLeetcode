import collections

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = collections.Counter("balloon")
        count = collections.Counter(text)

        mini = float('inf')
        for k, val in balloon.items():
            mini = min(mini, count[k] // val)
        return mini


