
"""
https://blog.csdn.net/fuxuemingzhu/article/details/79138621

Suppose Andy and Doris want to choose a restaurant for dinner,
and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum.
If there is a choice tie between answers, output all of them with no order requirement.
You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""

"""
Say the lists are A and B. Let Aindex[element] be the index of that element in A. 
For every index, value pair (j, v) in B, we have some candidate sum-of-indexes i + j,
where i = Aindex[v] if it exists. If the candidate sum is better, it becomes our new answer; 
if the candidate sums are the same, then we append to our answer.
"""
"""
思路
想要得到“最小索引和”那就免不了要遍历两个数组了。注意到只有值相等的元素才能够用来计算索引和，
所以我们只需要遍历其中一个数组，而把另一个数组当作Map（key为元素值，value为索引）来查表就可以了。
这样在遍历其中一个数组时，对于每个元素，只用在Map中找到相同元素，得到其在另一数组中的索引，
与自身的索引相加即为索引和；遍历完成得到的最小索引和即为最终结果。

这里还有一个剪枝的步骤，遍历每个元素时，我们会维护一个当前得到的最小索引和，
而如果仅当前元素的索引就已经比当前最小索引和大的话，也就没有继续遍历下去的意义了
（当前元素索引与Map得到的另一数组中的索引的和一定大于最小索引和）。
"""

class Solution1:
    def findRestaurant(self, A, B):
        Aindex = {u: i for i, u in enumerate(A)}
        best, ans = 1e9, []

        for j, v in enumerate(B):
            i = Aindex.get(v, 1e9)
            if i + j < best:
                best = i + j
                ans = [v]
            elif i + j == best:
                ans.append(v)
        return ans


class Solution2:
    def findRestaurant(self, list1, list2):
        if len(list1) > len(list2):
            return self.findRestaurant(list2, list1)

        d = {s: i for i, s in enumerate(list1)}

        minIdxSum = float('inf')
        res = []
        for i, s in enumerate(list2):
            if s in d:
                idxSum = d[s] + i
                if idxSum < minIdxSum:
                    minIdxSum = idxSum
                    del res[:]
                    res.append(s)
                elif idxSum == minIdxSum:
                    res.append(s)

        return res

from collections import defaultdict
class Solution3:
    def findRestaurant(self, list1, list2):
        C=list(set(list1)&set(list2))
        if len(C)==1:
            return C
        elif len(C)>1:
            index_name_dict=defaultdict(list)
            for name in C:
                index1=list1.index(name)
                index2=list2.index(name)
                index_sum=index1+index2
                index_name_dict[index_sum].append(name)
            return index_name_dict[min(index_name_dict.keys())]


class Solution4:
    def findRestaurant(self, list1, list2):
        dict1 = {v : i for i, v in enumerate(list1)}
        minSum = len(list1) + len(list2)
        ans = []
        for i, r in enumerate(list2):
            if r not in dict1:
                continue
            currSum = i + dict1[r]
            if currSum < minSum:
                ans = [r]
                minSum = currSum
            elif currSum == minSum:
                ans.append(r)
        return ans





