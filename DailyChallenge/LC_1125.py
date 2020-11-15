import collections

class SolutionTonyBFS:
    def smallestSufficientTeam(self, req_skills, people):
        n = len(req_skills)
        N = (1 << n) - 1
        table = {}
        # map skill to binary
        for i, skill in enumerate(req_skills):
            table[skill] = 1 << i

        queue = collections.deque()
        queue.append([0, []])
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                state, path = queue.popleft()

                if state == N:
                    return path

                for i in range(len(people)):
                    nextState = state
                    for skill in people[i]:
                        nextState |= table[skill]

                    if nextState not in visited:
                        visited.add(nextState)
                        queue.append([nextState, path + [i]])
        return -1


