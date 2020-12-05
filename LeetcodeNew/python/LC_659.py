


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

"""
3 X 4 X X 5 X [6 X X 7 X 8]

1 1 2 2 3 3 4

"""


class Solution:
    def isPossible(self, nums) -> bool:
        # {ending number : how many seqs}
        seq = collections.Counter()
        # {number : how many of key unchecked}
        count = collections.Counter(nums)

        for num in nums:
            if count[num] == 0:
                continue

            # 可以抱大腿
            if seq[num - 1] > 0:
                # 以num-1为结尾的少一个, num结尾的多一个
                seq[num - 1] -= 1
                seq[num] += 1
                count[num] -= 1

            else:
                if count[num + 1] == 0 or count[num + 2] == 0:
                    return False
                count[num] -= 1
                count[num + 1] -= 1
                count[num + 2] -= 1
                seq[num + 2] += 1

        return True




class SolutionLee:
    def isPossible(self, nums):
        freq = collections.Counter(nums)
        need = collections.Counter()
        for i in nums:
            if not freq[i]:
                continue
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


nums = [1,2,3,3,4,4,5,5]
a = SolutionLee()
print(a.isPossible(nums))
