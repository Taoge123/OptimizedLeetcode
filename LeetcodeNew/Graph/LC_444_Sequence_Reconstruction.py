"""
https://leetcode.com/problems/sequence-reconstruction/discuss/92574/Very-short-solution-with-explanation


Check whether the original sequence org can be uniquely reconstructed
from the sequences in seqs. The org sequence is a permutation of the integers
from 1 to n, with 1 ≤ n ≤ 104.
Reconstruction means building a shortest common supersequence of the sequences in seqs
(i.e., a shortest sequence so that all sequences in seqs are subsequences of it).
Determine whether there is only one sequence that can be reconstructed from seqs
and it is the org sequence.

Example 1:

Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].
Example 3:

Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true

"""

"""
s思路：
1. 这是一道两体问题，即：输入是两个对象，一个是org,一个是seqs，要求寻找两者之间的联系。
   首先，我们遍历seqs,把其某些特征保存下来，然后再遍历org，提取同样的特征，然后从前面的特征中查询即可！
2. 具体的做法：先将seq中每个数字前面的数字记录下来，保证supersequence中数字相对位置关系正确，
   而且都定义过的。比如：seqs=[[1,2],[1,3]]，１的前面没有，可以用０表示, 2的前面是１，３的前面是；
   然后遍历org,看是否所有的前后关系所形成的特征都能在之前记录的特征库中查询，例如：org=[1,2,3]，
   1前面没有，正确；２前面是１，也正确；３的前面是２，不正确，因为在上面的特征库里我们只记录了３的前面是１没有２，所以不正确！
3. 上面的方法还不完全正确，例如：seqs=[[1,4],[4,1]],org=[1,4].
   我们根据上文做法：１的前面有0,4，４的前面有1,0，而org里需要1前面有０，正确；４前面有１，正确。
   但显然这个org不是seqs的super sequence。因为，1在４前，又再４后。
   所以，除了检查org里前后相继的特征是否存在，还需要检查某个数前面所有的数是否都存在！
4. 这样检查就费劲了！例如：seqs=[[1,3],[2,3]],org=[1,2,3],3前面有{1,2}.所以在org遇到3,
   就判断前面{1,2}是否等于{1,2}。看来这个时候，需要我们反过来思考。根据3前面的数字1，
   查询org知道1的位置是０，而３前面的数字２对于的org中２的位置是１，所以，我们直接选位置最大的数即可，
   从而不用保存和比较３前面所有的数。这个方法可行的原因，是每次需判断3在org里的坐标是否比１、２在org的坐标大。
   这里利用了数据相对位置在seqs和org中永远保持不变

"""




"""

解法I 拓扑排序（Topological Sort）
将seqs中的各序列seq按照其中元素出现的先后顺序建立有向图g。

例如seqs中的某序列seq = [1, 2, 3]，对应有向图，顶点为1, 2, 3；边为(1, 2), (2, 3)。

利用数组indeg记录各顶点的入度（indegree），sucset记录各顶点的后继（边）。

然后对图g执行拓扑排序，将得到的排序结果与原始序列org作比对即可。


解法II “边检查法”
首先建立原始序列org中各元素到其下标的映射indices。

遍历seqs，记当前序列为seq，遍历seq；

记seq中相邻元素为pre, cur，若indices[pre] > indices[cur]，说明与org中各元素的前后关系产生矛盾，返回False

否则，将(pre, cur)加入边集edges。

最后遍历org，判断其中两两相邻元素构成的边是否都在edges中，若是返回True，否则返回False。
"""

"""
The basic is to get topological sort of seqs nodes, if it is unique and equal to org, then true, else False

Following is how to implement in details:

in each step,
if we have more than one node whose incoming nodes count is zero then org is not unique, return False

At last we check if the topological sort contain all nodes in the in seqs and equal to org
"""

import collections


class Solution5:
    def sequenceReconstruction(self, org, seqs):
        graph = collections.defaultdict(list)
        degree = collections.Counter()
        nodes = {x for seq in seqs for x in seq}
        for seq in seqs:
            for i in range(0, len(seq) - 1):
                s, e = seq[i], seq[i + 1]
                graph[s].append(e)
                degree[e] += 1
        ans = []
        starts = [k for k in nodes if degree[k] == 0]
        while len(starts) == 1:
            start, starts = starts[0], []
            ans.append(start)
            for node in graph[start]:
                degree[node] -= 1
                if degree[node] == 0:
                    starts.append(node)
        return len(set(ans)) == len(nodes) and ans == org



class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        adjacent = collections.defaultdict(list)
        incoming_nodes = collections.defaultdict(int)
        nodes = set()
        for arr in seqs:
            nodes |= set(arr)
            for i in range(len(arr)):
                if i == 0:
                    incoming_nodes[arr[i]] += 0
                if i < len(arr) - 1:
                    adjacent[arr[i]].append(arr[i + 1])
                    incoming_nodes[arr[i + 1]] += 1
        cur = [k for k in incoming_nodes if incoming_nodes[k] == 0]
        res = []
        while len(cur) == 1:
            cur_node = cur.pop()
            res.append(cur_node)
            for node in adjacent[cur_node]:
                incoming_nodes[node] -= 1
                if incoming_nodes[node] == 0:
                    cur.append(node)
        if len(cur) > 1:
            return False
        return len(res) == len(nodes) and res == org


"""
Topological Sort

Build the graph by finding each number's parents and children in seqs.

Then push the number with no parent into the answer, and delete the number from the graph. 
If the graph from the seqs can generate only one common supersequence, 
then every time there is only one node with no parent can be found.

At last, check if all nodes in seqs has been visited, and if the answer found equals to the org.
"""


class Solution2:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        children = collections.defaultdict(set)
        parents = collections.defaultdict(set)
        nodes = set()

        for s in seqs:
            for i in range(len(s)):
                nodes.add(s[i])
                if i > 0:
                    parents[s[i]].add(s[i - 1])
                if i < len(s) - 1:
                    children[s[i]].add(s[i + 1])

        potentil_parent = [n for n in nodes if not parents[n]]
        count = len(potentil_parent)
        ans = []

        while count == 1:
            cur_parent, count = potentil_parent.pop(), count - 1
            ans.append(cur_parent)
            nodes.remove(cur_parent)
            for n in children[cur_parent]:
                parents[n].remove(cur_parent)
                if not parents[n]:
                    potentil_parent.append(n)
                    count = count + 1

        return True if not nodes and ans == org else False


class Solution3:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        pairs = set()
        idxs = {}

        for i in range(len(org)):
            idxs[org[i]] = i

        for i in range(len(seqs)):
            s = seqs[i]
            for j in range(len(s)):
                if s[j] not in idxs:
                    return False
                if j > 0 and idxs[s[j - 1]] >= idxs[s[j]]:
                    return False
                pairs.add((s[j - 1], s[j]))

        if not pairs: return False
        for i in range(1, len(org)):
            if (org[i - 1], org[i]) not in pairs:
                return False
        return True



class Solution4:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if not org: # corner case 1
            return not seqs
        if not seqs: # corner case 2
            return not org
        out_edges=collections.defaultdict(set)
        nodes=set(org)
        for seq in seqs: # constructing edges for BFS topological sort
            n=len(seq)
            if n==1 and seq[0] not in nodes: # corner case 3
                return False
            for i in range(n-1):
                out_edges[seq[i]].add(seq[i+1])
        n=len(org)
        if n==1: # corner case 4
            for seq in seqs:
                if seq!=org:
                    return False
            return True

        for i in xrange(n-1): # BFS topological sort
            node=org[i]
            nxt=org[i+1]
            if node not in out_edges or nxt not in out_edges[node]:
                return False
            out_edges.pop(node)
        return not out_edges





