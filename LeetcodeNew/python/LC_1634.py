
class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next

class Solution:
    def addPoly(self, p1: 'PolyNode', p2: 'PolyNode') -> 'PolyNode':
        head = node = PolyNode()

        while p1 and p2:
            if p1.power > p2.power:
                node.next = node = p1
                p1 = p1.next
            elif p1.power < p2.power:
                node.next = node = p2
                p2 = p2.next
            else:
                coef = p1.coefficient + p2.coefficient
                if coef:
                    node.next = node = PolyNode(coef, p1.power)
                p1 = p1.next
                p2 = p2.next

        node.next = p1 or p2
        return head.next




