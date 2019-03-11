
"""
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:
The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to return the sum of all paths from the root towards the leaves.


Example 1:
Input: [113, 215, 221]
Output: 12
Explanation:
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
Example 2:
Input: [113, 221]
Output: 4
Explanation:
The tree that the list represents is:
    3
     \
      1

The path sum is (3 + 1) = 4.

"""

"""
Convert the given array into a tree using Node objects. 
Afterwards, for each path from root to leaf, we can add the sum of that path to our answer.

Algorithm

There are two steps, the tree construction, and the traversal.

In the tree construction, we have some depth, position, and value, 
and we want to know where the new node goes. With some effort, 
we can see the relevant condition for whether a node should be left or right is pos - 1 < 2**(depth - 2). 
For example, when depth = 4, the positions are 1, 2, 3, 4, 5, 6, 7, 8, and it's left when pos <= 4.

In the traversal, we perform a depth-first search from root to leaf, 
keeping track of the current sum along the path we have travelled. 
Every time we reach a leaf (node.left == null && node.right == null), 
we have to add that running sum to our answer.


这道题还是让我们求二叉树的路径之和，但是跟之前不同的是，树的存储方式比较特别，并没有专门的数结点，
而是使用一个三位数字来存的，百位数是该结点的深度，十位上是该结点在某一层中的位置，个位数是该结点的结点值。
为了求路径之和，我们肯定还是需要遍历树，但是由于没有树结点，所以我们可以用其他的数据结构代替。
比如我们可以将每个结点的位置信息和结点值分离开，然后建立两者之间的映射。
比如我们可以将百位数和十位数当作key，将个位数当作value，建立映射。
由于题目中说了数组是有序的，所以首元素就是根结点，然后我们进行先序遍历即可。
在递归函数中，我们先将深度和位置拆分出来，然后算出左右子结点的深度和位置的两位数，
我们还要维护一个变量cur，用来保存当前路径之和。如果当前结点的左右子结点不存在，
说明此时cur已经是一条完整的路径之和了，加到结果res中，直接返回。
否则就是对存在的左右子结点调用递归函数即可


为了便于查找方便，我们首先将每个节点映射到一个哈希表中，其中key是节点的位置，
value是节点的值。由于符合满二叉树的性质，所以我们很容易根据一个父结点的key找到它的两个左右子孩子所对应的节点。
这样这个问题就和其它的path sum问题没有区别了。


"""

class SolutionLee:
    def pathSum(self, nums):
        s = {}
        l = {}
        for i in nums[::-1]:
            a, b, c = i / 100, i / 10 % 10, i % 10
            l[a, b] = max(1, l.get((a + 1, b * 2 - 1), 0) + l.get((a + 1, b * 2), 0))
            s[a, b] = s.get((a + 1, b * 2 - 1), 0) + s.get((a + 1, b * 2), 0) + l[a, b] * c
        return s.get((1, 1), 0)



class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution:
    def pathSum(self, nums):
        self.ans = 0
        root = Node(nums[0] % 10)

        for x in nums[1:]:
            depth, pos, val = x/100, x/10 % 10, x % 10
            pos -= 1
            cur = root
            for d in range(depth - 2, -1, -1):
                if pos < 2**d:
                    cur.left = cur = cur.left or Node(val)
                else:
                    cur.right = cur = cur.right or Node(val)

                pos %= 2**d

        def dfs(node, running_sum = 0):
            if not node: return
            running_sum += node.val
            if not node.left and not node.right:
                self.ans += running_sum
            else:
                dfs(node.left, running_sum)
                dfs(node.right, running_sum)

        dfs(root)
        return self.ans


"""
Intuition and Algorithm

As in Approach #1, we will depth-first search on the tree. 
One time-saving idea is that we can use num / 10 = 10 * depth + pos 
as a unique identifier for that node. 
The left child of such a node would have identifier 10 * (depth + 1) + 2 * pos - 1, 
and the right child would be one greater.
"""


class Solution2:
    def pathSum(self, nums):
        self.ans = 0
        values = {x / 10: x % 10 for x in nums}
        def dfs(node, running_sum = 0):
            if node not in values: return
            running_sum += values[node]
            depth, pos = divmod(node, 10)
            left = (depth + 1) * 10 + 2 * pos - 1
            right = left + 1

            if left not in values and right not in values:
                self.ans += running_sum
            else:
                dfs(left, running_sum)
                dfs(right, running_sum)

        dfs(nums[0] / 10)
        return self.ans


class Solution3:
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dmap = {1 : 0}
        leaves = set([1])
        for num in nums:
            path, val = num / 10, num % 10
            lvl, seq = path / 10, path % 10
            parent = (lvl - 1) * 10 + (seq + 1) / 2
            dmap[path] = dmap[parent] + val
            leaves.add(path)
            if parent in leaves: leaves.remove(parent)
        return sum(dmap[v] for v in leaves)



class Solution4:
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total, nodes_map = 0, {}
        def num_to_tuple(num, i):
            # The node 113 becomes a tuple of (0, 0, 3).
            depth, pos, value = int(str(num)[0]) - 1, int(str(num)[1]) - 1, int(str(num)[2])
            if depth not in nodes_map:
                nodes_map[depth] = {}
            nodes_map[depth][pos] = i
            return (depth, pos, value)
        # Convert numbers to tuples.
        nodes = [num_to_tuple(num, i) for i, num in enumerate(nums)]
        path_sums = [0] * len(nodes)

        for index, node in enumerate(nodes):
            depth, pos, value = node
            path_sums[index] = value
            # Look up the dictionary for the node's parent.
            if depth - 1 in nodes_map and (pos // 2) in nodes_map[depth - 1]:
                # If node has a parent, add the parent's value to the path sum.
                path_sums[index] += path_sums[nodes_map[depth - 1][pos // 2]]
            # Look up the dictionary for the node's children.
            if not (depth + 1 in nodes_map and ((pos * 2) in nodes_map[depth + 1] or (pos * 2 + 1) in nodes_map[depth + 1])):
                # If there are no children, it is a leaf. Add the path sum to the total.
                total += path_sums[index]
        return total




