class ImmutableListNode:
    def printValue(self) -> None: # print the value of this node.
        pass
    def getNext(self) -> 'ImmutableListNode':
        pass

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if not head:
            return

        node = head.getNext()
        self.printLinkedListInReverse(node)
        head.printValue()

