import collections


class Solution:
    def sortItems(self, n: int, m: int, group, beforeItems):
        Items = collections.defaultdict(set)
        nextGroupID = m

        for i in range(n):
            if group[i] == -1:
                group[i] = nextGroupID
                nextGroupID += 1
            Items[group[i]].add(i)

        # build table inside each group
        nxtTableItems = collections.defaultdict(set)
        inDegreeItems = collections.defaultdict(int)

        # build graph amoung groups
        nxtTableGroup = collections.defaultdict(set)
        inDegreeGroup = collections.defaultdict(int)

        for i in range(n):
            for j in beforeItems[i]:
                # 先考虑smae group
                if group[i] == group[j]:
                    nxtTableItems[j].add(i)
                    inDegreeItems[i] += 1
                else:
                    if group[i] not in nxtTableGroup[group[j]]:
                        nxtTableGroup[group[j]].add(group[i])
                        inDegreeGroup[group[i]] += 1

        # sort nodes inside of each group
        ItemsOrdered = collections.defaultdict(list)
        for groupId, val in Items.items():
            ItemsOrdered[groupId] = self.topoSort(Items[groupId], nxtTableItems, inDegreeItems)
            if len(ItemsOrdered[groupId]) != len(Items[groupId]):
                return []

        # sort group
        groups = set()
        for i in range(n):
            groups.add(group[i])

        groupOrdered = self.topoSort(groups, nxtTableGroup, inDegreeGroup)
        res = []
        for groupId in groupOrdered:
            # print(groupItemsOrdered[groupId])
            for node in ItemsOrdered[groupId]:
                res.append(node)
        return res


    def topoSort(self, nodes, nxtTable, inDegree):
        queue = collections.deque()
        res = []

        for node in nodes:
            if inDegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in nxtTable[node]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)

        if len(res) == len(nodes):
            return res
        return []







