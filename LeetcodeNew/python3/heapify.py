""""
https://www.bilibili.com/video/BV1Eb41147dK?from=search&seid=1450286583142562471
https://zhuanlan.zhihu.com/p/266665145

"""


class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        # write your code here
        n = len(A)
        # for i in range(n):
        #     self.siftUp(A, i)
        for i in range(n, -1, -1):
            self.siftDown(A, i)

        # last_node = n - 1
        # parent = (last_node - 1) // 2
        # for i in range(parent, -1, -1):
        #     self.siftDown(A, i)

    def siftDown(self, A, k):
        if 2 * k + 1 >= len(A):
            return

        left = 2 * k + 1
        right = 2 * k + 2

        next_idx = left
        # find the smaller node as next
        if right < len(A) and A[right] < A[left]:
            next_idx = right

        # if next node is already bigger, then no need to change
        if A[k] < A[next_idx]:
            return

        A[k], A[next_idx] = A[next_idx], A[k]
        self.siftDown(A, next_idx)

    def siftUp(self, A, k):

        if k <= 0:
            return

        parent = (k - 1) // 2
        if A[parent] < A[k]:
            return

        A[parent], A[k] = A[k], A[parent]
        self.siftUp(A, parent)


nums = []
m1, m2, m3 = float('-inf'), float('-inf'), float('-inf')
for num in nums:
    if num > m1:
        m3, m2, m1 = m2, m1, num
    elif num > m2:
        m3, m2 = m2, num
    elif num > m3:
        m3 = num





"""



Package_name/app_id
Addition:
    Matching Keyword
    Play App:
        Recall asset type
        Comment
Removal:
Removal Reason

Package_name/app_id
Play:
    Play App Addition:
        Play Matching Keyword
        Recall asset type
        Comment
    Play App Removal:
        Removal Reason

IOS:
    Addition:
        IOS Matching Keyword
        


"""
