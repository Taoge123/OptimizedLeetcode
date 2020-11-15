
class SolutionTony:
    def shortestSuperstring(self, A):
        def getDistance(s1, s2):
            # suffix of s1 and prefix of s2
            for i in range(1, len(s1)):
                if s2.startswith(s1[i:]):
                    return len(s1) - i
            return 0

        n = len(A)
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                overlap[i][j] = getDistance(A[i], A[j])
                overlap[j][i] = getDistance(A[j], A[i])

        # distance = [[0 for i in range(n)] for _ in range(1 << n)]
        distance = collections.defaultdict(int)
        queue = collections.deque()
        for i in range(n):
            queue.append([i, 1 << i, [i], 0])
        # queue = collections.deque([(i, 1 << i, [i], 0) for i in range(n)])
        maxi = -1  # 记录最大的repeat_len
        final_path = []  # 记录对应的path
        while queue:
            node, state, path, dis = queue.popleft()
            if dis < distance[(state, node)]:
                continue
            if state == (1 << n) - 1 and dis > maxi:
                final_path = path
                maxi = dis
                continue
            for i in range(n):
                newState = state | (1 << i)
                # case1: 不能走回头路，因为每个结点只能遍历一次
                # case2: 如果走当前这条路能够获得更大的重复长度，才继续考虑

                if newState != state and distance[(state, node)] + overlap[node][i] >= distance[(newState, i)]:
                    distance[(newState, i)] = distance[(state, node)] + overlap[node][i]
                    queue.append((i, newState, path + [i], distance[(newState, i)]))

        res = A[final_path[0]]
        for i in range(1, len(final_path)):
            res += A[final_path[i]][overlap[final_path[i - 1]][final_path[i]]:]
        return res

