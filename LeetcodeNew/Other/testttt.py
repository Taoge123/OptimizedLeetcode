#
# class Solution:
#     def maxEvents(self, events) -> int:
#         events = sorted(events)
#         res = 1
#         visited = set()
#         visited.add(events[0][0])
#         for i in range(1, len(events)):
#             if events[i - 1][1] >= events[i][0] and (events[i - 1][1] not in visited or events[i][0] not in visited):
#                 res += 1
#                 visited.add(events[i - 1][1])
#
#         return res
#
#
#
#
# events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
# a = Solution()
# print(a.maxEvents(events))
#
import collections

class Solution:
    def isPossible(self, target) -> bool:
        nums = [1] * len(target)
        queue = collections.deque()
        queue.append(nums)
        visited = set()
        visited.add(tuple(nums))

        while queue:
            node = queue.popleft()
            print(node)
            if max(node) > max(target):
                continue
            if collections.Counter(node) == collections.Counter(target):
                return True
            summ = sum(node)
            if summ > max(target):
                continue
            for i in range(len(nums)):
                temp = node[i]
                node[i] = summ
                print(sorted(tuple(node)))
                if set(sorted(tuple(node))) not in visited:
                    visited.add(tuple(sorted(node[:])))
                    queue.append(node[:])
                node[i] = temp
        return False

target = [1,1384,1,1,10,2767,379,1,217,1]
# target = [8,5]
a = Solution()
print(a.isPossible(target))




