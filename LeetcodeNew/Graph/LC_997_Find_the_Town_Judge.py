"""
In a town, there are N people labelled from 1 to N.
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b]
representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

"""
"""
Intuition:
Consider trust as a graph, all pairs are directed edge.
The point with in-degree - out-degree = N - 1 become the judge.

Explanation:
Count the degree, and check at the end.

Time Complexity:
Time O(T + N), space O(N)
"""

class Solution:
    def findJudge(self, N, trust):
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1



"""
Keep track of the cumulative score of each person: if person a trusts person b, we decrement a's score and increment b's score.
The judge is the only person that ends up with a score of N-1.

I initialize the trusted list with N+1 items to make indexing easier, since the villagers are named 1 thorugh N.

Time complexity O(N + T): T=len(trust). We iterate through the trust list once 
and through all villagers once, so the time complexity is linear in these. 
This is equivalent to |Vertices| + |Edges| in graph terms, 
if we consider each person as a vertex and each trust relationship as a directed edge.

Space complexity O(N): We create a trusted list with a size of N+1 to store the cumulative scores.

"""

class Solution:
    def findJudge(self, N, trust):
        trusts = [0] * (N + 1)
        for a, b in trust:
            trusts[a] -= 1
            trusts[b] += 1
        return ([i for i, t in enumerate(trusts) if i and t == N - 1] + [-1])[0]





