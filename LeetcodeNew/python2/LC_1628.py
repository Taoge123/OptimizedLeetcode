
import abc
from abc import ABC, abstractmethod
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


class NNode(Node):
    def __init__(self, val: str):
        self.val = val
        self.left = None
        self.right = None

    def evaluate(self) -> int:
        if self.val == '+':
            return self.left.evaluate() + self.right.evaluate()
        if self.val == '-':
            return self.left.evaluate() - self.right.evaluate()
        if self.val == '*':
            return self.left.evaluate() * self.right.evaluate()
        if self.val == '/':
            return self.left.evaluate() // self.right.evaluate()
        return int(self.val)



"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix) -> 'Node':
        stack = []
        for ch in postfix:
            if ch in ['+', '-', '*', '/']:
                right = stack.pop()
                left = stack.pop()
                node = NNode(ch)
                node.left = left
                node.right = right
                stack.append(node)
            else:
                stack.append(NNode(ch))
        return stack[0]


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""



