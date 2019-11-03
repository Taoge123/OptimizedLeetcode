
"""
Example 1:
Input:
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation:
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.
Note:
The given kill id is guaranteed to be one of the given PIDs.
n >= 1.

"""
"""
Build a (int parent: list[int] children)hashMap and do a simple bfs.


"""

import collections

class Solution:
    import collections

    class Solution:
        def killProcess(self, pid, ppid, kill: int):
            graph = collections.defaultdict(list)
            for i, j in zip(ppid, pid):
                graph[i].append(j)

            res = []
            self.helper(graph, kill, res)
            return res

        def helper(self, graph, kill, res):
            res.append(kill)
            for i in graph[kill]:
                self.helper(graph, i, res)


