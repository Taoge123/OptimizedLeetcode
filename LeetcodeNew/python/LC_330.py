
"""
这道题给我们一个有序的正数数组nums，又给了我们一个正整数n，问我们最少需要给nums加几个数字，使其能组成[1,n]之间的所有数字，
注意数组中的元素不能重复使用，否则的话只有要有1，就能组成所有的数字了。这道题我又不会了，
上网看到了史蒂芬大神的解法，膜拜啊，这里就全部按他的解法来讲吧。我们定义一个变量miss，
用来表示[0,n]之间最小的不能表示的值，那么初始化为1，为啥不为0呢，因为n=0没啥意义，直接返回0了。
那么此时我们能表示的范围是[0, miss)，表示此时我们能表示0到miss-1的数，如果此时的num <= miss，
那么我们可以把我们能表示数的范围扩大到[0, miss+num)，如果num>miss，那么此时我们需要添加一个数，
为了能最大限度的增加表示数范围，我们加上miss它本身，以此类推直至遍历完整个数组，我们可以得到结果。
下面我们来举个例子说明：

给定nums = [1, 2, 4, 11, 30], n = 50，我们需要让[0, 50]之间所有的数字都能被nums中的数字之和表示出来。

首先使用1, 2, 4可能表示出0到7之间的所有数，表示范围为[0, 8)，但我们不能表示8，因为下一个数字11太大了，
所以我们要在数组里加上一个8，此时能表示的范围是[0, 16)，那么我们需要插入16吗，答案是不需要，因为我们数组有1和4，
可以组成5，而下一个数字11，加一起能组成16，所以有了数组中的11，我们此时能表示的范围扩大到[0, 27)，
但我们没法表示27，因为30太大了，所以此时我们给数组中加入一个27，那么现在能表示的范围是[0, 54)，
已经满足要求了，我们总共添加了两个数8和27，所以返回2即可。


"""

"""
Initialize an empty list, keep adding new numbers from provided nums into this list, 
keep updating the coverage range of this list. 
If you do so, you only need to care about the effect of new number added each time.

Suppose 1~10 is already covered during this process, (by whatever combinations in the above list, 
doesn't matter), then for the next number added

If the next number is "11", you will have these new sums:
11, 11+1, 11+2, ..., 11+10, so your total coverage becomes 1~21, which is "2 x coverage + 1"
If the next numberis smaller than "11", for example "3", then the new coverage becomes: 10+3, 9+3, 8+3-> 1~13, which is "num + coverage"
If the next number is bigger than "11", for example "12", then number "11" is missing forever. 
There is no way to sum 11 by existing combinations. 
You have to manually patch "11" before being able to process the next number.
"""

class Solution:
    def minPatches(self, nums, n: int) -> int:

        covered, i = 0, 0
        res = 0
        while covered < n:
            num = nums[i] if i < len(nums) else float('inf')
            if num > covered + 1:
                covered = covered * 2 + 1
                res += 1
            else:
                covered += num
                i += 1
        return res


class Solution2:
    def minPatches(self, nums, n: int) -> int:

        i, res = 0, 0
        miss = 1

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                res += 1

        return res



