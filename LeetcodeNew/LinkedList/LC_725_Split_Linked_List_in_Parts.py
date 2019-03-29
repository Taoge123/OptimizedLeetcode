
"""
http://www.cnblogs.com/grandyang/p/7878548.html

Given a (singly) linked list with head node root,
write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible:
no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list,
and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3,
and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
Example 2:
Input:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1,
and earlier parts are a larger size than the later parts.
"""
"""
This question can be split into two parts:

1. Count the length of the linked list
2. Determine the length of nodes in each chunk
3. Splitting the linked list up
At the end of step 2, res will look something like this, for a list of length 10 and k of 3: [4, 4, 3].

Step 3 iterates through res using the values in res 
and replaces the value at each index with each chunk's head node. 
We have to keep a reference to prev in order to slice up the chunks nicely by setting prev.next = None.

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root, k):
        # Count the length of the linked list
        curr, length = root, 0
        while curr:
            curr, length = curr.next, length + 1
        # Determine the length of each chunk
        chunk_size, longer_chunks = length // k, length % k
        res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)
        # Split up the list
        prev, curr = None, root
        for index, num in enumerate(res):
            if prev:
                prev.next = None
            res[index] = curr
            for i in range(num):
                prev, curr = curr, curr.next
        return res


class Solution2:
    def splitListToParts(self, root, k):
        length = 0
        curr = root
        while curr:
            length += 1
            curr = curr.next

        len_mean = length // k
        len_over = length % k

        parts = []
        prev = ListNode(0)
        curr = root
        for _ in range(k):
            if curr:
                parts.append(curr)
                len_part = len_mean + 1 if len_over > 0 else len_mean
                len_over -= 1
                for _ in range(len_part):
                    prev, curr = curr, curr.next
                prev.next = None  # cut here
            else:
                parts.append(None)
        return parts



class Solution3:
    def splitListToParts(self, root, k):
        cur = root
        for N in range(1001):
            if not cur: break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = cur
            for j in range(width + (i < remainder) - 1):
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans








