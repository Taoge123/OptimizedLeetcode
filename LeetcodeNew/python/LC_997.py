class Solution:
    def findJudge(self, N: int, trust) -> int:
        if len(trust) < N - 1:
            return -1

        indegree = [0] * (N + 1)
        outdegree = [0] * (N + 1)

        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for i in range(1, N + 1):
            if indegree[i] == N - 1 and outdegree[i] == 0:
                return i
        return -1




class Solution2:
    def findJudge(self, N: int, trust) -> int:
        if len(trust) < N - 1:
            return -1

        score = [0] * (N + 1)

        for a, b in trust:
            score[a] -= 1
            score[b] += 1

        for i, score in enumerate(score[1:], 1):
            if score == N - 1:
                return i
        return -1




