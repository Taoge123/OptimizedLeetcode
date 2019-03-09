
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

"""
"""
Build a (int parent: list[int] children)hashMap and do a simple bfs.


"""

import collections

class Solution:
    def killProcess(self, pid, ppid, kill):
        dic = collections.defaultdict(list)
        for p, pp in zip(pid, ppid):
            dic[p].append(pp)

        queue = [kill]
        for i in queue:
            queue.extend(dic.get(i, []))
        return queue


class Solution2:
    def killProcess(self, pid, ppid, kill):
        dic, queue, res = collections.defaultdict(list), collections.deque([kill]), []
        for parent, child in zip(ppid, pid):
            dic[parent].append(child)
        while queue:
            parent = queue.popleft()
            res.append(parent)
            queue.extend(dic[parent])
        return res

class SolutioinDFS:
    def killProcess(self, pid, ppid, kill):
        dic, visited = collections.defaultdict(list), set()
        for parent, child in zip(ppid, pid):
            dic[parent].append(child)
        self.help(dic, kill, visited)
        return list(visited)

    def help(self, dic, kill, visited):
        visited.add(kill)
        for child in dic[kill]:
            if child not in visited:
                self.help(dic, child, visited)

                
