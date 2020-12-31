class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        if p in q.children:
            return root

        dummy = Node()   # Create a dummy node to address the edge case when p is the root
        dummy.children.append(root)

        p_parent = self.dfs(dummy, p) # Find p's parent (guaranteed to exist now because of the dummy node)
        q_in_p = self.dfs(p, q) # Check if q is in p's subtree

        p_index = p_parent.children.index(p) # Get p's original index in p's parent
        p_parent.children.pop \
            (p_index) # Remove p from p's parent. Again, guaranteed to succeed because of the dummy node

        q.children.append(p) # Add p to q's children
        if q_in_p:
            q_in_p.children.remove(q) # if q is in p's subtree, we need to disconnect q from its parent
            p_parent.children.insert(p_index, q)  # Then we need to put q in p's original position in p's parent

        return dummy.children[0]


    def dfs(self, node, tar):
        if tar in node.children: return node
        for x in node.children:
            res = self.dfs(x, tar)
            if res: return res
        return None




