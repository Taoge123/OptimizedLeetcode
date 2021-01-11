

class SolutionBFS:
    def minimumJumps(self, forbidden, a: int, b: int, x: int) -> int:
        threshold = x + a + b + max(forbidden)
        forbidden = set(forbidden)
        step = 0
        queue = collections.deque()
        queue.append([0, False])
        visited = set()
        visited.add((0, False))

        while queue:
            size = len(queue)
            for _ in range(size):
                node, backward = queue.popleft()
                # print(node)
                if node == x:
                    return step

                newNode = node + a
                if newNode < threshold and newNode not in forbidden and (newNode, False) not in visited:
                    queue.append([newNode, False])
                    visited.add((newNode, False))

                newNode = node - b
                if newNode >= 0 and not backward and newNode not in forbidden and (newNode, True) not in visited:
                    queue.append([newNode, True])
                    visited.add((newNode, True))

            step += 1
        return -1
