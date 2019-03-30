
"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/159067/Python-Recursive-Solution-%2B-Analysis

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.



Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL

"""
"""
The Idea
We will process the list "depth first" (i.e. to the lowest child), redirecting parent nodes next pointers to their children, and saving the previous values of their next pointers in a Stack to be reattached once the bottom-most non-parent node has no siblings.

The algorithm
Pseudocode
    Initialize a current reference to the head of the list and an empty stack
    If our current reference is a Node, then see if it has a child.
    
        (case 1) If it does have a child, then push its next reference (if it has one) to the top of the Stack. 
        Then, reset the next reference of the current reference and the current's child reference appropriately. 
        After this operation, the current reference should have lost a child reference, 
        but have their next reference pointing to the former child.
        
        (case 2) If it does not have a child, then, if it lacks a next reference 
        and there are references left in the Stack, 
        then reassign its next reference and the current top of the Stack appropriately. After this operation, the next reference of the current reference should be the top of the Stack, and the top of the Stack's previous reference should be the current reference.
    
    Advance the current reference forward to its next reference.
    Repeat 2 and 3 until the current reference is None.
"""

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution1:
    def flatten(self, head):
        # Initialize the current reference and stack of saved next pointers
        curr, tempStack = head, [];
        while curr:
            if curr.child:
                # If the current node is a parent
                if curr.next:
                    # Save the current node's old next pointer for future reattachment
                    tempStack.append(curr.next);
                # Current <-> Current.child
                #   \-> None
                curr.next, curr.child.prev, curr.child = curr.child, curr, None;
            if not curr.next and len(tempStack):
                # If the current node is a child without a next pointer
                temp = tempStack.pop();
                # Current <-> Temp
                temp.prev, curr.next = curr, temp;
            curr = curr.next;
        return head;

class Solution2:
    def flatten(self, head):
        if not head:
            return

        dummy = Node(0, None, head, None)
        stack = []
        stack.append(head)
        prev = dummy

        while stack:
            root = stack.pop()

            root.prev = prev
            prev.next = root

            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root

        dummy.next.prev = None
        return dummy.next


"""
This question can be modelled as a simple DFS traversal question,where we must make sure we visit child before next. 
We also make use of a sentinel so that we avoid boilerplate code of checking if prev is not None.
"""

class Solution3:
    def flatten(self, head):
        if not head:
            return head

        prev = Node(0, None, head, None)
        stack = [head]
        while stack:
            curr = stack.pop()
            prev.next, curr.prev = curr, prev
            stack.append(curr.next) if curr.next else None
            stack.append(curr.child) if curr.child else None
            curr.child = None
            prev = curr

        head.prev = None  # get rid of sentinel
        return head





