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




class Solution2:
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
                # print(node[:i] + str(y) + node[i+1:])
                yield node[:i] + str(y) + node[i+1:]




deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
a = Solution()
print(a.openLock(deadends, target))






