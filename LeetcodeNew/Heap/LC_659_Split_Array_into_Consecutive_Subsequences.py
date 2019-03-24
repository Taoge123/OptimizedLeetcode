
"""
https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106549/Python-8-liner-O(nlgn)-2-greedy-approaches-with-explanation
https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/129877/Python-O(n)-Time-O(1)-Space-solution-beat-100-the-only-solution-you-need-to-read.
https://blog.csdn.net/fuxuemingzhu/article/details/82185011
https://blog.csdn.net/sunday0904/article/details/78174122

You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3
3, 4, 5
Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3, 4, 5
3, 4, 5
Example 3:
Input: [1,2,3,4,4,5]
Output: False
"""

"""
I used a greedy algorithm.
leftis a hashmap, left[i] counts the number of i that I haven't placed yet.
endis a hashmap, end[i] counts the number of consecutive subsequences that ends at number i
Then I tried to split the nums one by one.
If I could neither add a number to the end of a existing consecutive subsequence 
nor find two following number in the left, I returned False
"""

"""
这道题就用贪婪解法就可以了，我们使用两个哈希表map，第一个map用来建立数字和其出现次数之间的映射freq，
第二个用来建立可以加在某个连续子序列后的数字及其可以出现的次数之间的映射need。对于第二个map，
举个例子来说，就是假如有个连，[1,2,3]，那么后面可以加上4，所以就建立4的映射。这样我们首先遍历一遍数组，
统计每个数字出现的频率，然后我们开始遍历数组，对于每个遍历到的数字，首先看其当前出现的次数，如果为0，则继续循环；
如果need中存在这个数字的非0映射，那么表示当前的数字可以加到某个连的末尾，我们将当前数字的映射值自减1，
然后将下一个连续数字的映射值加1，因为当[1,2,3]连上4后变成[1,2,3,4]之后，就可以连上5了；
如果不能连到其他子序列后面，我们来看其是否可以成为新的子序列的起点，可以通过看后面两个数字的映射值是否大于0，
都大于0的话，说明可以组成3连儿，于是将后面两个数字的映射值都自减1，还有由于组成了3连儿，
在need中将末尾的下一位数字的映射值自增1；如果上面情况都不满足，说明该数字是单牌，只能划单儿，
直接返回false。最后别忘了将当前数字的freq映射值自减1。退出for循环后返回true，
"""

import collections
import heapq

class SolutionLee:
    def isPossible(self, nums):
        freq = collections.Counter(nums)
        need = collections.Counter()
        for i in nums:
            if not freq[i]: continue
            freq[i] -= 1
            # If next_nums contains the number, it is directly appendable to a sequence.
            # We "append" it to the sequence by incrementing the next number by 1.
            if need[i - 1] > 0:
                need[i - 1] -= 1
                need[i] += 1
            # If the number + 1 and the number + 2 are both still in the occurrences hashmap,
            # We can create a new subsequence of length 3 and add the next number to next_nums.
            elif freq[i + 1] and freq[i + 2]:
                freq[i + 1] -= 1
                freq[i + 2] -= 1
                need[i + 2] += 1
            else:
                return False
        return True

"""
把一个升序的数组，分割成几个连续的递增的整数序列。如果能分割，
且分割后的每个序列的长度都至少为3，那么认为成功，否则失败。

这就是所谓的扑克牌算法，必须全部弄成“顺子”。一个“顺子”至少3张连续的牌。
方法是使用优先级队列，优先把当前的牌放入到更短的“顺子”里（贪心）
"""
"""
首先判断以（num-1）为结尾的序列是否存在，

如果存在，获取长度最小值len并出栈，创建以num为结尾的数组，并设置长度为len + 1，推入优先队列；

如果不存在，创建新的序列，以num为结尾，并且长度为1，推入优先队列，
创建新的键值对（num，currentPriorityQueue）推入map中。

1，2，3，3，4，4，5，5

num last            len     current         map
1   null->(0,[ ])   0       (1, [1])    (0,[ ] ) (1, [1])
2   (1, [1])        1       (2, [2])    (0,[ ] ) (1, [ ])(2, [2])
3   (2, [2])        2       (3, [3])    (0,[ ] ) (1, [ ])(2, [ ])(3, [3])
3   (2, [ ])        0       (3, [1])    (0,[ ] ) (1, [ ])(2, [ ])(3, [3])(3, [1])
4   (3, [1])        1       (4, [2])    (0,[ ] ) (1, [ ])(2, [ ])(3, [3])(3, [ ])(4, [2])
4   (3, [3])        3       (4, [4])    (0,[ ] ) (1, [ ])(2, [ ])(3, [ ])(3, [ ])(4, [2])(4, [4])
5   (4, [2])        2       (5, [3])    (0,[ ] ) (1, [ ])(2, [ ])(3, [ ])(3, [ ])(4, [ ])(4, [4])(5, [3])
5   (4, [4])        4       (5, [5])    (0,[ ] ) (1, [ ])(2, [ ])(3, [ ])(3, [ ])(4, [ ])(4, [ ])(5, [3])(5, [5])


"""


class Solution2:
    def isPossible(self, nums):

        saved = collections.defaultdict(list)
        for num in nums:
            last = saved[num - 1]
            _len = 0 if (not last) else heapq.heappop(last)
            current = saved[num]
            heapq.heappush(current, _len + 1)
        for values in saved.values():
            for v in values:
                if v < 3:
                    return False
        return True


"""
Lastly, General approach

Use a dictionary seqs, that maps keys to a collection (array/heap/priority queue). 
The key represents the ending value of the sequence 
and the collection stores lengths of sequences seen so far that end at the key.

As we iterate through the array, if there is an existing sequence in seqs that ends at num - 1, 
we can remove the sequence with the smallest length from seqs[num - 1] 
and create a new sequence at seqs[num] with length + 1. 
We choose the smallest length as we try to have as many sequences as possible that have at least length 3. 
If there is no existing sequence ending at num - 1, we create a new sequence at seqs[num] of length 1.

At the end of the iteration, return False if any of the sequences in seqs have a length < 3.

For the input [1,2,3,3,4,5], the ending dict will look like { 3: [3], 5: [3] }, 
indicating there is one sequence ending with 3 of length 3 and one sequence ending with 5 of length 3.

For the input [2,2,3,3,4,4,5,5], the ending dict will look like { 5: [4, 4] }, 
indicating there are two sequences ending with 5, both of length 4.

For the input [1,2,3,4,4,5], the ending dict will look like { 4: [4], 5: [2] }, 
indicating there is one sequence ending with 4 of length 4 and one sequence ending with 5 of length 2. 
This should return False since there is a sequence that is shorter then length 3.
"""
class SolutionL1:
    def isPossible(self, nums):
        # Time: O(n.lgn)
        # Space: O(n)
        seqs = {num: [] for num in nums}
        for num in nums:
            shortest_seq = 0
            if num - 1 in seqs and len(seqs[num - 1]):
                shortest_seq = heapq.heappop(seqs[num - 1])
            heapq.heappush(seqs[num], shortest_seq + 1)
        return len([None for seq_lengths in seqs.values() if len(seq_lengths) and seq_lengths[0] < 3]) == 0




nums = [1,2,3,3,4,4,5,5]
a = Solution2()
print(a.isPossible(nums))





