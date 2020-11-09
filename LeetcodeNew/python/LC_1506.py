
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def findRoot(self, tree) -> 'Node':
        summ = 0
        for node in tree:
            summ += node.val - sum(child.val for child in node.children)

        for node in tree:
            if node.val == summ:
                return node
        return None


class Solution2:
    def findRoot(self, tree) -> 'Node':
        res = 0
        for node in tree:
            res ^= node.val
            for child in node.children:
                res ^= child.val

        for node in tree:
            if res == node.val:
                return node



class Solution3:
    def findRoot(self, tree) -> 'Node':
        children = set()
        parents = list()

        for node in tree:
            parents.append(node)
            children |= set(node.children)

        for node in parents:
            if node not in children:
                return node



