
"""
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.


Example:

MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4

Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.

"""

import collections


class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = collections.deque([])
        self.remain = k


    def enQueue(self, value: int) -> bool:
        if self.remain < 1:
            return False
        else:
            self.queue.append(value)
            self.remain -= 1
            return True


    def deQueue(self) -> bool:
        if not self.queue:
            return False
        else:
            self.queue.popleft()
            self.remain += 1
            return True


    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        else:
            return -1


    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        else:
            return -1


    def isEmpty(self) -> bool:
        if not self.queue:
            return True
        else:
            return False


    def isFull(self) -> bool:
        if self.remain == 0:
            return True
        else:
            return False


class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None



class MyCircularQueue2:
    def __init__(self, k):
        self.size = k
        self.curSize = 0
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def enQueue(self, value):
        if self.curSize < self.size:
            node = Node(value)
            node.pre = self.tail.pre
            node.next = self.tail
            node.pre.next = node.next.pre = node
            self.curSize += 1
            return True
        return False

    def deQueue(self):
        if self.curSize > 0:
            node = self.head.next
            node.pre.next = node.next
            node.next.pre = node.pre
            self.curSize -= 1
            return True
        return False

    def Front(self):
        return self.head.next.val

    def Rear(self):
        return self.tail.pre.val

    def isEmpty(self):
        return self.curSize == 0

    def isFull(self):
        return self.curSize == self.size



