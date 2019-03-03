'''
/**
 * Approach: Build Tree Graph + BFS
 * 想要求到树某一个节点 distance 为 K 的所有点。
 * 很容易想到就是使用 BFS。根据要求，我们在遍历的时候应该
 * 将整棵树看作是一个 无向图 来进行比遍历。
 * 因此首先我们需要构建出这张图才行。
 *
 * 做法比较简单，使用 Map<Integer, List<Integer>> 即可。
 * 因为树中每一个节点的值都是唯一的，所以我们可以直接以节点值作为每个节点的标记（代表）
 * 来构建这张无向图。构造的过程其实就是一个递归遍历的过程。
 * 具体注意事项可以参考注释。
 * 总的来说就是：把一棵树转换成一个 无向图 然后进行 Graph Serach.属于比较常规的做法
 *
 * 时间复杂度：O(n)
 * 空间复杂度：O(n)
 *
 * 类似的问题：
 * Closest Leaf in a Binary Tree：
 *  https://github.com/cherryljr/LeetCode/blob/master/Closest%20Leaf%20in%20a%20Binary%20Tree.java
 *
 * 参考资料（存在第二种解法）：
 *  http://zxi.mytechroad.com/blog/tree/leetcode-863-all-nodes-distance-k-in-binary-tree/
'''

class Node:
    # A constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Recursive function to print all the nodes at distance k
# int the tree(or subtree) rooted with given root. See
def printkDistanceNodeDown(root, k):

    # Base Case
    if root is None or k< 0:
        return

        # If we reach a k distant node, print it
    if k == 0:
        print(root.data)
        return

        # Recur for left and right subtee
    printkDistanceNodeDown(root.left, k - 1)
    printkDistanceNodeDown(root.right, k - 1)


# Prints all nodes at distance k from a given target node
# The k distant nodes may be upward or downward. This function
# returns distance of root from target node, it returns -1
# if target node is not present in tree rooted with root
def printkDistanceNode(root, target, k):
    # Base Case 1 : IF tree is empty return -1
    if root is None:
        return -1

    # If target is same as root. Use the downward function
    # to print all nodes at distance k in subtree rooted with
    # target or root
    if root == target:
        printkDistanceNodeDown(root, k)
        return 0

        # Recur for left subtree
    dl = printkDistanceNode(root.left, target, k)

    # Check if target node was found in left subtree
    if dl != -1:

        # If root is at distance k from target, print root
        # Note: dl is distance of root's left child
        # from target
        if dl + 1 == k:
            print(root.data)

            # Else go to right subtreee and print all k-dl-2
        # distant nodes
        # Note: that the right child is 2 edges away from
        # left chlid
        else:
            printkDistanceNodeDown(root.right, k - dl - 2)

            # Add 1 to the distance and return value for
        # for parent calls
        return 1 + dl

        # MIRROR OF ABOVE CODE FOR RIGHT SUBTREE
    # Note that we reach here only when node was not found
    # in left subtree
    dr = printkDistanceNode(root.right, target, k)
    if dr != -1:
        if (dr + 1 == k):
            print(root.data)
        else:
            printkDistanceNodeDown(root.left, k - dr - 2)
        return 1 + dr

        # If target was neither present in left nor in right subtree
    return -1


# Driver program to test above function
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
target = root.left.right
printkDistanceNode(root, target, 2)











