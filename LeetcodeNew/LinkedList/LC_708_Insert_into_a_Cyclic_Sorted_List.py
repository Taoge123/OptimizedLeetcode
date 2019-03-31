
"""
Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the reference to that single node. Otherwise, you should return the original given node.

The following example may help you understand the problem better:

In the figure above, there is a cyclic sorted list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list.

The new node should insert between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.
"""

"""
这道题让我们在循环有序的链表中插入结点，要求插入结点后，链表仍保持有序且循环。
题目中强调了corner case的情况，就是当链表为空时，我们插入结点即要生成一个新的循环有序链表，
那么我们可以先处理这个特殊情况，比较简单，就是新建一个结点，然后将next指针指向自己即可。
好，下面来看给定的链表不为空的情况，最常见的情况就是要插入的结点值在两个有序结点值[a, b]之间，
那么只要满足 a <= insertVal <= b 即可。
由于是循环有序的链表，结点值不会一直上升，到某一个结点的时候，是最大值，
但是下一个结点就是最小值了，就是题目中的例子，结点4到结点1的时候，就是下降了。
那么在这个拐点的时候，插入值insertVal就会有两种特殊的情况，其大于等于最大值，
或者小于等于最小值，比如插入值是5，或者0的时候，这两种情况都插入在结点4之后，可以放一起处理。
而若其小于最大值，或者大于最小值，就是上面那种一般的情况，不会在这里处理，
所以我们只要检测如果属于上面的两种情况之一，就break掉循环，进行插入结点处理即可"""

"""
Can someone tell me what is it mean?

if prev == head:
 break
"""
"""
It takes care of an edge case where all the values in the circular list are the same.

Example:
1-1-1-1 insertval: 2

When the code hits

if prev == head:
 break
It means its already traversed the whole list without finding nodes that satisfy the conditions:

if prev.val <= val <= cur.val:
    break
elif prev.val > cur.val and (val<cur.val or val>prev.
    break
Without it, the algorithm would loop indefinitely.
"""

"""
Find insert position, only 2 cases
1st: prev.val <= x<=cur.val
2nd: x is the max value or min value in the new list, 
here when prev.val > cur.val, then prev is max, cur is min in the origin list. 
1-2-3-4-5-1, prev is 5, cur is 1,
"""

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head, val):
        node = Node(val, head)
        if not head:
            return node
        prev, cur = head, head.next
        while 1:
            if prev.val <= val <= cur.val:
                break
            elif prev.val > cur.val and (val<cur.val or val>prev.val):
                break
            prev, cur = prev.next, cur.next
            if prev == head:
                break
        prev.next = node
        node.next = cur
        return head

"""
insert at the end; insert in the middle; insert before head (e.g. all the values are equal in the original list)
"""
class Solution2:
    def insert(self, head, insertVal):

        new_node = Node(insertVal, head)

        if not head:
            return new_node

        node = head
        while True:
            if node.next.val < node.val and (insertVal <= node.next.val or insertVal >= node.val):
                break
            elif node.val <= insertVal <= node.next.val:
                break
            elif node.next == head:
                break
            node = node.next

        new_node.next = node.next
        node.next = new_node
        return head


#Geeksforgeeks
"""
Algorithm:
Allocate memory for the newly inserted node and put data in the newly allocated node. 
Let the pointer to the new node be new_node. After memory allocation, 
following are the three cases that need to be handled.

1) Linked List is empty:  
    a) since new_node is the only node in CLL, make a self loop.      
          new_node->next = new_node;  
    b) change the head pointer to point to new node.
          *head_ref = new_node;

2) New node is to be inserted just before the head node:    
  (a) Find out the last node using a loop.
         while(current->next != *head_ref)
            current = current->next;
  (b) Change the next of last node. 
         current->next = new_node;
  (c) Change next of new node to point to head.
         new_node->next = *head_ref;
  (d) change the head pointer to point to new node.
         *head_ref = new_node;

3) New node is to be inserted somewhere after the head: 
   (a) Locate the node after which new node is to be inserted.
         while ( current->next!= *head_ref && 
             current->next->data data)
         {   current = current->next;   }
   (b) Make next of new_node as next of the located pointer
         new_node->next = current->next;
   (c) Change the next of the located pointer
         current->next = new_node; 
"""


# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        # Utility function to print the linked LinkedList

    def printList(self):
        temp = self.head
        print(temp.data)
        temp = temp.next
        while (temp != self.head):
            print(temp.data)
            temp = temp.next

    """ function to insert a new_node in a list in sorted way. 
       Note that this function expects a pointer to head node 
       as this can modify the head of the input linked list """

    def sortedInsert(self, new_node):

        current = self.head

        # Case 1 of the above algo
        if current is None:
            new_node.next = new_node
            self.head = new_node

            # Case 2 of the above algo
        elif (current.data >= new_node.data):

            # If value is smaller than head's value then we
            # need to change next of last node
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

            # Case 3 of the above algo
        else:

            # Locate the node before the point of insertion
            while (current.next != self.head and
                   current.next.data < new_node.data):
                current = current.next

            new_node.next = current.next
            current.next = new_node

        # Driver program to test the above function


# llist = LinkedList()
arr = [12, 56, 2, 11, 1, 90]

list_size = len(arr)

# start with empty linked list
start = LinkedList()

# Create linked list from the array arr[]
# Created linked list will be 1->2->11->12->56->90
for i in range(list_size):
    temp = Node(arr[i])
    start.sortedInsert(temp)

start.printList()



