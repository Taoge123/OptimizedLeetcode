
class Solution:
    def rankTeams(self, votes) -> str:
        count = {val : [0] * len(votes[0]) for val in votes[0]}

        for vote in votes:
            for i, char in enumerate(vote):
                count[char][i] -= 1 # - as we need to sort in reverse
        count = sorted(count.items(), key=lambda k :(k[1], k[0]))
        res = ""
        for char, _ in count:
            res += char
        return res


class SolutionLee:
    def rankTeams(self, votes) -> str:
        n = len(votes[0])
        count = {val: [0] * n for val in votes[0]}

        for vote in votes:
            for i, val in enumerate(vote):
                count[val][i] -= 1

        return ''.join(sorted(votes[0], key=lambda v: count[v] + [v]))




