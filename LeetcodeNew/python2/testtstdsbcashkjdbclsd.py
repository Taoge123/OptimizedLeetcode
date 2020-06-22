
"""
The given input is a graph that started as a tree with N nodes
(with distinct values 1, 2, ..., N), with one additional edge added.
The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

 The resulting graph is given as an array of edges. Each element of edges is a pair [u, v] with u < v,
 that represents an undirected edge connecting nodes u and v. Ex: [[1,2], [1,3], [2,3]]


 Return an edge that can be removed so that the resulting graph is a tree of N nodes.
 If there are multiple answers, return the answer that occurs last in the given array.


Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |  |
    4 - 3
n nodes,
n-1 edges

{1, 5, 2, 3, 4}
          1  1  1  1
parent = [1, 2, 3, 4, 5]


[1,2],   |  [4,3], | [2,3], [1,5], [1,4]


             2  3  5  3  5
parent = [0, 1, 2, 3, 4, 5]


1                  5
234               6789

s = ["\    " ," \   " ,"  \  "]

-------
|\    |
| \   |
|  \  |
-------

1
2
3
4


--------\
|       \
|       \
|       \
-------


"""
# import logging
#
# logging.warning()
# def find(i, parent):
#     if i == parent[i]:
#         return parent[i]
#     return find(parent[i], parent)
#
# def union(i, j, parent):
#     x = find(i, parent)
#     y = find(j, parent)
#     rank = []
#     if x == y:
#         return [i, j]
#     y = parent[x]
#     return False
#
# def search(edges, n):
#     parent = [i+1 for i in range(n+1)]
#     for u, v in edges:
#          pair = union(u, v, parent)
#          if pair:
#              return pair
#     return []
#
#
"""
12345

"""
import collections, heapq
# import copy
#
#
# class Solution:
#     def minDays(self, nums, m: int, k: int) -> int:
#         self.k = k
#         self.m = m
#         left = min(nums)
#         right = max(nums)
#         while left < right:
#             mid = (right - left) // 2 + left
#             if self.valid(nums, mid):
#                 right = mid
#             else:
#                 left = mid + 1
#
#         if left == max(nums):
#             if self.valid(nums, left):
#                 return left
#             else:
#                 return -1
#
#     def valid(self, nums, target):
#         count = 0
#         newNums = copy.deepcopy(nums)
#         for i, num in enumerate(nums):
#             newNums[i] = (num <= target)
#
#         i = 0
#         while i < len(newNums):
#             if newNums[i:i + self.k] == [True] * self.k:
#                 count += 1
#                 i = i + self.k
#             else:
#                 i += 1
#         return count >= self.m
#
#
#
#
# nums = [1,10,3,10,2]
#
# m = 3
# k = 1
# a = Solution()
# print(a.minDays(nums, m, k))



"""
0 - 32,000

read int interface getNumber(): -1 if you reach the end of the file
write int interface writeNumber(int num):

4 2 5 1 3 7 8 9

time complecity - log(n) * n
O(n) 32,000 * 8 bytes = 256k // 32 = 4k
buffer = [2, 4, 5]

n - operations
O(1)

32,000 - 1000 * 00000000000000
33 // 32 = # of element 

00000000000000 + 01000000000000 + 01000000000000 + 01000000000000
"""

def getNumber():
    continue

def writeNumber():
    continue


class Solution:
    def __init__(self):
        self.buffer = [0] * 1000

    def buildBuffer(self):
        while getNumber():
            num = getNumber()
            x = num >> 5
            bitmask = 0
            for i in range(5):
                if num & 1 == 1:
                    bitmask |= i << 1
                num <<= 1
            y = bitmask
            # y = (num << 27) >> 27
            self.buffer[x] |= 1 << y

        number = 0
        for num in self.buffer:
            if (num & 1) == 1:
                writeNumber(number)
            else:
                continue
            number += 1
            num >>= 1


"""
32
0000000000000001110

num = 64

32
x = 1
y = 1
[000000000000000000000000000111, 00000000000000000000000000000001, 00000000000000000000000000000000]

"""





"""
[[1,2,2,3,3,3,4], [1,2,5,6], [2,2,33,4,5], [1]]
len(self.num)

1 - 1

for num, count in minMap:
        core1 , core2, .... , core1000
[1,2,2,3,3,3,4], [1,2,5,6], [2,2,33,4,5]



"""







"""
userID - DaysInCompany    -     {UserID : min(DaysInCOmpany)} 
userID - DaysInCompany    -     {UserID : min(DaysInCOmpany)} - reduce(UserID : min(DaysInCopmany))

userID - DaysInCompany
userID - DaysInCompany

userID - DaysInCompany
userID - DaysInCompany

reduce(UserID : min(DaysInCopmany))

UserId - name - DaysInCOmpany

input : meetings - {start, end}
min
[8, 11] [9, 10] [10, 11]   [10, 11]
 
starts = [8, 9, 10, 10]

min(end)
res = 1

"""


"""       Node3
 Node   - Node1 - Node(1)
 newNode  newNode1       Node2   
           node1 - newNode1              newNode2
                         
                         
                         newNode1/neighos = [newNode2]
                         newNode2/neighos = [newNode1]

[node1] = newNode1

      1                   (1)
 
   2 3 4 5             (2) 

5 1 6 5


"""

import collections

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class GraphSearch:

    def deepcopy(self, nodes):
        self.res = []
        for node in nodes:
            self.deepcopyOneNode(node)
        return self.res

    def deepcopyOneNode(self, node):
        self.table = collections(list)
        newNode = self.dfs(node)
        return newNode

    def dfs(self, node):
        if node in self.table:
            return self.table[node]
        newNode = Node(node.val, [])
        self.table[node] = newNode
        self.resa.append(newNode)
        for nei in node.neighbors:
            newNode.neighbors.append(self.dfs(nei))
        return newNode


node = Node(1, [2,3,4,5])













