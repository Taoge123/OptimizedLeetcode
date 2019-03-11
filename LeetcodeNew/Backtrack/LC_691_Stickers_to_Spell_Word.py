"""

We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters
from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

Example 1:

Input:

["with", "example", "science"], "thehat"
Output:

3
Explanation:

We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input:

["notice", "possible"], "basicbasic"
Output:

-1
Explanation:

We can't form the target "basicbasic" from cutting letters from the given stickers.

"""



import collections


class Solution:
    def minStickers(self, stickers, target):
        cnt, res, n = collections.Counter(target), [float("inf")], len(target)
        def dfs(dic, used, i):
            if i == n: res[0] = min(res[0], used)
            elif dic[target[i]] >= cnt[target[i]]: dfs(dic, used, i + 1)
            elif used < res[0] - 1:
                for sticker in stickers:
                    if target[i] in sticker:
                        for s in sticker: dic[s] += 1
                        dfs(dic, used + 1, i + 1)
                        for s in sticker: dic[s] -= 1
        dfs(collections.defaultdict(int), 0, 0)
        return res[0] < float("inf") and res[0] or -1






