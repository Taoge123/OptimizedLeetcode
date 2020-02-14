class ListNode:
    def __init__(self, x):
        self.val = x
        self.next, self.prev = None, None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val: int) -> None:
        pred = self.head
        succ = self.head.next

        self.size += 1
        node = ListNode(val)
        node.prev = pred
        node.next = succ
        pred.next = node
        succ.prev = node

    def addAtTail(self, val: int) -> None:
        succ = self.tail
        pred = self.tail.prev
        self.size += 1
        node = ListNode(val)
        node.prev = pred
        node.next = succ
        pred.next = node
        succ.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        # find predecessor and successor of the node to be added
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        # insertion itself
        self.size += 1
        node = ListNode(val)
        node.prev = pred
        node.next = succ
        pred.next = node
        succ.prev = node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        # find predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        # delete pred.next
        self.size -= 1
        pred.next = succ
        succ.prev = pred


class MyLinkedList2:
    def __init__(self):
        pass

    def get(self, index: int) -> int:
        pass

    def addAtHead(self, val: int) -> None:
        pass

    def addAtTail(self, val: int) -> None:
        pass

    def addAtIndex(self, index: int, val: int) -> None:
        pass

    def deleteAtIndex(self, index: int) -> None:
        pass







