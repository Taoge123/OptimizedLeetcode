import collections


class Solution:
    def mostVisitedPattern(self, username, timestamp, website):

        events = [[u, t, w] for u, t, w in zip(username, timestamp, website)]
        events.sort()

        users = collections.defaultdict(list)

        for u, t, w in events:
            users[u].append(w)

        seq = collections.defaultdict(set)

        for u, w in users.items():
            if len(w) >= 3:
                for i in range(len(w) - 2):
                    for j in range(i + 1, len(w) - 1):
                        for k in range(j + 1, len(w)):
                            webs = (w[i], w[j], w[k])
                            seq[webs].add(u)

        res = sorted(seq.items(), key=lambda x: (-len(x[1]), x[0]))
        # print(seq)
        # print(res)
        return res[0][0]






