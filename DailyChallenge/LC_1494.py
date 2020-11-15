import collections

class SolutionBFS:
    def minNumberOfSemesters(self, n: int, dependencies, k: int) -> int:
        # table[i] 代表要完成 第i课，一定要完成的课程
        table = collections.defaultdict(int)
        for u, v in dependencies:
            table[u] |= (1 << v)

        queue = collections.deque()
        queue.append([0, 0])
        visited = set()
        visited.add(0)
        while queue:
            state, step = queue.popleft()
            # 因为没有第0 门课，所以是-2
            if state == (1 << (n + 1)) - 2:
                return step
            nextState = state
            for i in range(1, n + 1):
                # 完成了node之后，i课程可以完成
                if state & table[i] == table[i]:
                    nextState |= (1 << i)
            # 完成了node的课程，可以在下一天完成的课程
            diff = nextState ^ state
            # 如果下一天完成的课程<=k个，就全完成
            if bin(diff).count("1") <= k and state + diff not in visited:
                visited.add(state + diff)
                queue.append((state + diff, step + 1))
            else:
                # 如果多于k个，就选其中的k个来完成
                while diff:
                    if bin(diff).count('1') == k and state + diff not in visited:
                        visited.add(state + diff)
                        queue.append((state + diff, step + 1))
                    # 相当于找nextState ^ state的子集
                    diff = (diff - 1) & (nextState ^ state)



