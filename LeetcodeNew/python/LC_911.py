import collections
import bisect

class TopVotedCandidate:
    def __init__(self, persons, times):
        count = collections.Counter()
        leader = 0

        self.winners = [-1] * len(times)
        self.times = times

        for i, person in enumerate(persons):
            count[person] += 1
            if count[person] >= count[leader]:
                leader = person

            self.winners[i] = leader

    def q(self, t: int) -> int:
        return self.winners[bisect.bisect(self.times, t) - 1]


