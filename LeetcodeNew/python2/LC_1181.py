
class Solution:
    def beforeAndAfterPuzzles(self, phrases):

        n = len(phrases)

        for i in range(n):
            phrases[i] = phrases[i].split()

        res = set()
        for i in range(n):
            for j in range( i +1, n):

                if phrases[i][-1] == phrases[j][0]:
                    res.add(' '.join(phrases[i] + phrases[j][1:]))

                if phrases[i][0] == phrases[j][-1]:
                    res.add(' '.join(phrases[j] + phrases[i][1:]))

        return sorted(res)


