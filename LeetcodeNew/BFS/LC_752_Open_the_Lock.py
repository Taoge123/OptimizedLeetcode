
"""
You have a lock in front of you with 4 circular wheels.
Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0',
or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends,
meaning if the lock displays any of these codes,
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1

"""


"""
Intuition

We can think of this problem as a shortest path problem on a graph: 
there are 10000 nodes (strings '0000' to '9999'), 
and there is an edge between two nodes if they differ in one digit, 
that digit differs by 1 (wrapping around, so '0' and '9' differ by 1), 
and if both nodes are not in deadends.

Algorithm

To solve a shortest path problem, we use a breadth-first search. 
The basic structure uses a Queue queue plus a Set seen that records if a node has ever been enqueued. 
This pushes all the work to the neighbors function - in our Python implementation, 
all the code after while queue: is template code, except for if node in dead: continue.

As for the neighbors function, for each position in the lock i = 0, 1, 2, 3, 
for each of the turns d = -1, 1, 
we determine the value of the lock after the i-th wheel has been turned in the direction d.

Care should be taken in our algorithm, as the graph does not have an edge unless both nodes are not in deadends. 
If our neighbors function checks only the target for being in deadends, 
we also need to check whether '0000' is in deadends at the beginning. 
In our implementation, we check at the visitor level so as to neatly handle this problem in all cases.

In Java, our implementation also inlines the neighbors function for convenience, 
and uses null inputs in the queue to represent a layer change. 
When the layer changes, we depth++ our global counter, 
and queue.peek() != null checks if there are still nodes enqueued.
"""

import collections


class Solution2:
    def getAdjs(self, s):
        for i in range(4):
            yield s[:i] + str((int(s[i]) + 1) % 10) + s[i+1:]
            yield s[:i] + str((int(s[i]) - 1) % 10) + s[i+1:]
    def openLock(self, deadends, target):
        memo = set(deadends)
        if target in memo:
            return -1
        queue = ["0000"]
        d = 0
        while queue:
            queueN = []
            for s in queue:
                if s in memo:
                    continue
                if s == target:
                    return d
                memo.add(s)
                for ss in self.getAdjs(s):
                    queueN.append(ss)
            queue = queueN
            d += 1
        return -1


class Solution:
    def openLock(self, deadends, target):
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1


class Solution3:
    def openLock(self, deadends, target):
        moved, q, cnt, move = set(deadends), ["0000"], 0, {str(i): [str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}
        if "0000" in moved:
            return -1
        while q:
            new = []
            cnt += 1
            for s in q:
                for i, c in enumerate(s):
                    for cur in (s[:i] + move[c][0] + s[i + 1:], s[:i] + move[c][1] + s[i + 1:]):
                        if cur not in moved:
                            if cur == target:
                                return cnt
                            new.append(cur)
                            moved.add(cur)
            q = new
        return -1







