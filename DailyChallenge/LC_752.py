import collections


class Solution:
    def openLock(self, deadends, target: str) -> int:

        queue = collections.deque()
        queue.append('0000')
        visited = set()
        visited.add('0000')

        deadends = set(deadends)
        step = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node == target:
                    return step
                if node in deadends:
                    continue

                for i in range(len(node)):
                    num = int(node[i])
                    for dx in [-1, 1]:
                        newNum = (num + dx) % 10
                        newNode = node[:i] + str(newNum) + node[i + 1:]
                        if newNode not in visited:
                            queue.append(newNode)
                            visited.add(newNode)

            step += 1

        return -1
