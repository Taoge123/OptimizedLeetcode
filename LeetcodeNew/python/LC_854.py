import collections


class SolutionTony:
    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0
        queue = collections.deque()
        queue.append(A)
        visited = set()
        visited.add(A)
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node == B:
                    return step

                #找出第一个不一样的char
                i = 0
                while node[i] == B[i]:
                    i += 1

                for j in range(i+1, len(B)):
                    #然后找出node后面和B[i]一样的去交换
                    if node[j] != B[i]:
                        continue

                    newNode = list(node)
                    newNode[i], newNode[j] = newNode[j], newNode[i]
                    newNode = "".join(newNode)
                    # if newNode == B:
                    #     return step + 1

                    if newNode in visited:
                        continue
                    queue.append(newNode)
                    visited.add(newNode)
            step += 1
        return -1




class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0
        queue = collections.deque()
        queue.append(A)
        visited = set()
        visited.add(A)
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                #找出第一个不一样的char
                i = 0
                while node[i] == B[i]:
                    i += 1

                for j in range(i+1, len(B)):
                    #然后找出node后面和B[i]一样的去交换
                    if node[j] != B[i]:
                        continue

                    newNode = list(node)
                    newNode[i], newNode[j] = newNode[j], newNode[i]
                    newNode = "".join(newNode)
                    if newNode == B:
                        return step + 1

                    if newNode in visited:
                        continue
                    queue.append(newNode)
                    visited.add(newNode)
            step += 1
        return -1






