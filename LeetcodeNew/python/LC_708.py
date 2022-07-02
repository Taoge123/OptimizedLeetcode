
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode

        prev, curr = head, head.next
        toInsert = False

        while True:
            if prev.val <= insertVal <= curr.val:
                # Case #1.
                toInsert = True
            elif prev.val > curr.val:
                # Case #2. where we locate the tail element
                # 'prev' points to the tail, i.e. the largest element!
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                prev.next = Node(insertVal, curr)
                # mission accomplished
                return head

            prev, curr = curr, curr.next
            # loop condition
            if prev == head:
                break
        # Case #3.
        # did not insert the node in the loop
        prev.next = Node(insertVal, curr)
        return head


class SolutionTest:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head

            return head
        elif head.next == head:
            head.next = Node(insertVal)
            head.next.next = head
            # print(head.next.val)
            return head

        dummy = Node(float('inf'))
        dummy.next = head
        node = dummy.next

        while node:
            nxt = node.next
            if node.val <= insertVal <= nxt.val:
                newNode = Node(insertVal)
                node.next = newNode
                newNode.next = nxt
                node = node.next
                return head
            node = node.next
        return head


head = Node(3)
head.next = Node(4)
head.next.next = Node(1)
head.next.next.next = head


a = SolutionTest()
print(a.insert(head, 2))


