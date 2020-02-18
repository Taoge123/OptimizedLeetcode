
"""
8. String to Integer (atoi)
"""
class Solution008:
    def myAtoi(self, s):

        ###better to do strip before sanity check (although 8ms slower):
        # ls = list(s.strip())
        if len(s) == 0:
            return 0
        ls = list(s.strip())
        if not ls:
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']:
            del ls[0]
        res, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            res = res * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))


"""
29. Divide Two Integers
"""
class Solution029:
    def divide(self, dividend: int, divisor: int) -> int:
        a, b = abs(dividend), abs(divisor)
        res = 0
        while a >= b:
            step, index = b, 1
            while a >= step:
                a -= step
                step += step
                res += index
                index += index

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = -res
        return min(max(res, -pow(2 ,31)), pow(2 ,31) - 1)


"""
151. Reverse Words in a String
"""
class Solution151:
    def reverseWords(self, s):
        print(list(reversed(s.split())))
        return ' '.join(reversed(s.split()))


class SolutionCaikehe151:
    def reverseWords(self, s):
        s = list(" ".join(s.split()))[::-1]
        i = 0
        while i < len(s):
            start = i
            while i < len(s) and not s[i].isspace():
                i += 1
            self.reverse(s, start, i-1)
            i += 1
        return "".join(s)

    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1; j -= 1


"""
220. Contains Duplicate III
"""

"""
解法II：“滑动窗口” + TreeSet
参考LeetCode Discuss：https://leetcode.com/discuss/38177/java-o-n-lg-k-solution

TreeSet数据结构（Java）使用红黑树实现，是平衡二叉树的一种。

该数据结构支持如下操作：

1. floor()方法返set中≤给定元素的最大元素；如果不存在这样的元素，则返回 null。

2. ceiling()方法返回set中≥给定元素的最小元素；如果不存在这样的元素，则返回 null。

Java代码：
public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if(k < 1 || t < 0)
            return false;
        TreeSet<Integer> set = new TreeSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            int n = nums[i];
            if(set.floor(n) != null && n <= t + set.floor(n) || 
                    set.ceiling(n) != null && set.ceiling(n) <= t + n)
                return true;
            set.add(n);
            if (i >= k)
                set.remove(nums[i - k]);
        }
        return false;
    }
}
"""
"""
题目大意：
给定一个整数数组，判断其中是否存在两个不同的下标i和j满足：| nums[i] - nums[j] | <= t 并且 | i - j | <= k

解题思路：
解法I：“滑动窗口” + 字典（桶）
如果： | nums[i] - nums[j] | <= t   式a

等价： | nums[i] / t - nums[j] / t | <= 1   式b

推出： | floor(nums[i] / t) - floor(nums[j] / t) | <= 1   式c

​等价： floor(nums[j] / t) ∈ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 式d
其中式b是式c的充分非必要条件，因为逆否命题与原命题等价，所以：

如果： floor(nums[j] / t) ∉ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 非d

推出： | nums[i] - nums[j] | > t   非a
因此只需要维护一个大小为k的窗口（字典）numDict，其中键为nums[i] / t，值为nums[i]。

遍历数组nums时，检查nums[i]与键集{floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}对应的值的差值即可。
"""
class Solution220:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:

        if t < 0:
            return False
        n = len(nums)
        table = {}
        bucket = t + 1
        for i in range(n):
            val = nums[i] // bucket
            if val in table:
                return True
            if val - 1 in table and abs(nums[i] - table[val - 1]) < bucket:
                return True
            if val + 1 in table and abs(nums[i] - table[val + 1]) < bucket:
                return True
            table[val] = nums[i]
            if i >= k:
                del table[nums[i - k] // bucket]
        return False





import collections
class Solution166:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = ""
        res += "-" if (numerator > 0) ^ (denominator > 0) else ""
        num, den = abs(numerator), abs(denominator)

        res += str(num // den)
        num %= den
        if num == 0:
            return res
        res += "."
        table = collections.defaultdict(int)
        table[num] = len(res)

        while num != 0:
            num *= 10
            res += str(num // den)
            num %= den

            if num in table:
                index = table[num]
                res = res[:index] + "(" + res[index:] + ")"
                break
            else:
                table[num] = len(res)
        return res




"""
468. Validate IP Address
"""


class Solution468:
    def validIPAddress(self, IP: str) -> str:
        if IP.count(".") == 3 and all(self.isIPv4(i) for i in IP.split(".")):
            return "IPv4"
        if IP.count(":") == 7 and all(self.isIPv6(i) for i in IP.split(":")):
            return "IPv6"

        return "Neither"

    def isIPv4(self, s):
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except:
            return False

    def isIPv6(self, s):
        if len(s) > 4:
            return False
        try:
            # print(int(s, 16), '---')
            return int(s, 16) >= 0 and s[0] != '-'
        except:
            return False


# s = "0201:0db8:85a3:0000:0000:8a2e:0370:7334"
# a = Solution468()
# for item in s.split(':'):
#     print(a.isIPv6(item))


"""
91. Decode Ways
"""

class Solution091:
    def numDecodings(self, s: str) -> int:
        if s == "":
            return 0
        n = len(s)
        dp = [0 for x in range(n +1)]
        dp[0] = 1

        for i in range(1, n + 1):
            if s[i -1] != '0':
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] >= "10" and s[i-2:i] <= "26":
                dp[i] += dp[i-2]

        return dp[-1]

s = "12"
a = Solution091()
print(a.numDecodings(s))

"""
163. Missing Ranges
"""

class Solution:
    def findMissingRanges(self, nums, lower, upper):
        res = []
        n = len(nums)
        pre = cur = lower - 1

        for i in range(n + 1):
            if i == n:
                cur = upper + 1
            else:
                cur = nums[i]
            if cur - pre >= 2:
                res.append(self.getRange(pre + 1, cur - 1))
            pre = cur
        return res

    def getRange(self, lower, upper):
        if lower == upper:
            return "{}".format(lower)
        else:
            return "{}->{}".format(lower, upper)






