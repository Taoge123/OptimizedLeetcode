
"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""


class Solution:
    def oddEvenList(self, head):
        if head is None:
            return None

        odd = oddHead = head
        even = evenHead = head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = evenHead
        return oddHead


"""
    1  ->  2  ->  3  ->  4  ->  5  ->  6  ->  7  ->  8
   odd           odd           odd           odd
  oddHead       
          even          even          even          even
        evenHead

odd.next -> evenHead 
   1 -> 3 -> 5 -> 7 -> 2 -> 4 -> 6 -> 8
   
then we just return oddHead 
"""





