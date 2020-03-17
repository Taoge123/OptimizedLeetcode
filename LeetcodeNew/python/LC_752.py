import collections


class Solution:
    def openLock(self, deadends, target: str) -> int:
        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        visited = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in dead:
                continue
            for nei in self.neibhbors(node):
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, depth + 1))

        return -1


    def neibhbors(self, node):
        for i in range(4):
            x = int(node[i])
            for d in (-1, 1):
                y = (x + d) % 10
                # print(node[:i] + str(y) + node[ i +1:])
                yield node[:i] + str(y) + node[ i +1:]



a = Solution()
print(a.neibhbors('0000'))






