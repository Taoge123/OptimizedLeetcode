import collections


class SolutionTony:
    def openLock(self, deadends, target: str) -> int:
        deadends = set(deadends)
        queue = collections.deque()
        queue.append(('0000'))
        visited = set('0000')
        step = -1
        while queue:
            size = len(queue)
            step += 1
            for _ in range(size):
                node = queue.popleft()
                if node in deadends:
                    continue
                if node == target:
                    return step

                for i in range(len(node)):
                    num = int(node[i])
                    for dx in (-1, 1):
                        newNum = (num + dx) % 10
                        newNode = node[:i] + str(newNum) + node[i + 1:]
                        if newNode not in visited:
                            queue.append(newNode)
                            visited.add(newNode)
        return -1



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
                # print(node[:i] + str(y) + node[i+1:])
                yield node[:i] + str(y) + node[i+1:]




deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
a = SolutionTest()
print(a.openLock(deadends, target))






