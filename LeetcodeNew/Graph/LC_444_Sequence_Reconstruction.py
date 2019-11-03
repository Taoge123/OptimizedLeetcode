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


"""
Topological Sort

Build the graph by finding each number's parents and children in seqs.

Then push the number with no parent into the answer, and delete the number from the graph. 
If the graph from the seqs can generate only one common supersequence, 
then every time there is only one node with no parent can be found.

At last, check if all nodes in seqs has been visited, and if the answer found equals to the org.
"""

import collections

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:

        values = {x for seq in seqs for x in seq}
        graph = collections.defaultdict(list)
        degree = {char: 0 for char in values}

        for seq in seqs:
            for i in range(len(seq) - 1):
                graph[seq[i]].append(seq[i + 1])
                degree[seq[i + 1]] += 1

        queue = collections.deque([i for i in degree if degree[i] == 0])
        res = []

        while queue:
            if len(queue) != 1:
                return False
            node = queue.popleft()
            res.append(node)
            for i in graph[node]:
                degree[i] -= 1
                if degree[i] == 0:
                    queue.append(i)
        return len(res) == len(values) and res == org



