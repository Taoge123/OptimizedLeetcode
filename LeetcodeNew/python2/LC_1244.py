import collections

class Leaderboard:
    def __init__(self):
        self.count = collections.Counter()

    def addScore(self, playerId, score):
        self.count[playerId] += score

    def top(self, K):
        return sum(v for i, v in self.count.most_common(K))

    def reset(self, playerId):
        self.count[playerId] = 0



