import collections

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

