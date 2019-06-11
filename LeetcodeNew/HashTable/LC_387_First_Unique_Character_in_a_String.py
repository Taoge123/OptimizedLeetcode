
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


"""

import collections

class Solution1:
    def firstUniqChar(self, s):
        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        index = 0
        for ch in s:
            if count[ch] == 1:
                return index
            else:
                index += 1
        return -1


"""
387. First Unique Character in a String
Two Pass
> 类型：Hash Table
> Time Complexity O(2N)
> Space Complexity O(N)
扫两边，第一遍存字典，第二遍查找，如果字典里面对应Counter为1，就返回。
这里有个可以改进的地方，如果我们的input长度特别的长，我们第二次的for loop就会比较浪费时间，所以我们可以对第二遍迭代进行优化。

"""

class Solution2:
    def firstUniqChar(self, s):
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1

        for i, char in enumerate(s):
            if dic[char] and dic[char] == 1:
                return i
        return -1


"""
One Pass
> 类型：Hash Table
> Time Complexity O(N * M)
> Space Complexity O(M)
Step 1 扫描s并存储字典
存字典时候，将value设成index，如果在存储的时候发现字典里面有重复，则将value设置成-1

Step 2 扫描字典，实施更新最小返回值。
我们迭代存储好了的字典，因为我们知道-1代表一定有重复，我们就pass掉这种情况，只要当前key对应的value不为负数，
就证明value是unique character相对应的index，我们在外围设置一个res记录最小的index值，
在对字典迭代的时候，实时比较+更新即可。
另外如果res从头到尾没有变过，则代表字典没有unique character，返回-1

"""

class Solution3:
    def firstUniqChar(self, s):
        dic = {}
        for i, char in enumerate(s):
            if char in dic:
                dic[char] = -1
            else:
                dic[char] = i

        res = float('inf')
        for key, val in dic.items():
            if val == -1: continue
            res = min(res, val)

        return res if res != float('inf') else -1





