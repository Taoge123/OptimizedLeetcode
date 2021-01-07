import collections

class Solution:
    def sequenceReconstruction(self, org, seqs) -> bool:

        values = {x for seq in seqs for x in seq}
        graph = collections.defaultdict(list)
        degree = {char: 0 for char in values}

        for seq in seqs:
            for i in range(len(seq) - 1):
                graph[seq[i]].append(seq[i + 1])
                degree[seq[i + 1]] += 1

        queue = collections.deque([i for i in degree if degree[i] == 0])
        res = []

        while queue:
            if len(queue) != 1:
                return False
            node = queue.popleft()
            res.append(node)
            for i in graph[node]:
                degree[i] -= 1
                if degree[i] == 0:
                    queue.append(i)
        return len(res) == len(values) and res == org


