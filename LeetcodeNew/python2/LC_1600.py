import collections

class ThroneInheritance_DFS:

    def __init__(self, kingName: str):
        self.children = collections.defaultdict(list)
        self.death_ = set()
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.death_.add(name)

    def getInheritanceOrder(self):
        res = []
        def dfs(node):
            if node not in self.death_:
                res.append(node)

            for nei in self.children[node]:
                dfs(nei)

        dfs(self.kingName)
        return res



class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = collections.defaultdict(list)
        self.deaths = set()
        self.king = kingName


    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)


    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self):
        res = []
        self.inorder(self.king, res)
        return res

    def inorder(self, root, res):
        if root not in self.deaths:
            res.append(root)
        childs = self.graph[root]
        for child in childs:
            self.inorder(child, res)

