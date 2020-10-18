import collections

class Solution:
    def isNStraightHand(self, hand, W: int) -> bool:

        count = collections.Counter(hand)
        while count:
            mini = min(count.keys())
            for k in range(mini, mini + W):
                val = count[k]
                if not val:
                    return False
                if val == 1:
                    del count[k]
                else:
                    count[k] -= 1
        return True



class SolutionQueue:
    def isNStraightHand(self, hand, W: int) -> bool:
        count = collections.Counter(hand)
        queue = collections.deque()

        for num in count.keys():
            if num - 1 not in count:
                queue.append(num)

        while queue:
            start = queue.popleft()
            for i in range(start, start + W):
                if i not in count:
                    return False
                if count[i] > 1:
                    count[i] -= 1
                    if i - 1 not in count:
                        queue.append(i)
                else:
                    del count[i]

            if start + W - 1 not in count and start + W in count:
                queue.append(start + W)

        return True

