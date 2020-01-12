

"""
Given a list of strings, you could concatenate these strings together into a loop,
where for each string you could choose to reverse it or not. Among all the possible loops, you need to find the lexicographically biggest string after cutting the loop, which will make the looped string into a regular one.

Specifically, to find the lexicographically biggest string, you need to experience two phases:

Concatenate all the strings into a loop, where you can reverse some strings or not and connect them in the same order as given.
Cut and make one breakpoint in any place of the loop, which will make the looped string into a regular one starting from the character at the cutpoint.
And your job is to find the lexicographically biggest one among all the possible regular strings.

Example:
Input: "abc", "xyz"
Output: "zyxcba"
Explanation: You can get the looped string "-abcxyz-", "-abczyx-", "-cbaxyz-", "-cbazyx-",
where '-' represents the looped status.
The answer string came from the fourth looped one,
where you could cut from the middle character 'a' and get "zyxcba".
Note:
The input strings will only contain lowercase letters.
The total length of all the strings will not over 1,000.

"""


class Solution:
    def splitLoopedString(self, strs) -> str:
        arr = [max(word, word[::-1]) for word in strs]
        res = ''
        for i, word in enumerate(arr):
            for s in [word, word[::-1]]:
                for j in range(len(s)):
                    cur = s[j:] + ''.join(arr[i + 1:] + arr[:i]) + s[:j]
                    # print(cur)
                    res = max(res, cur)
        return res



strs = ["abc", "xyz", "opq"]
a = Solution()
print(a.splitLoopedString(strs))


"""
cbazyx
bazyxc
azyxcb
abczyx
bczyxa
czyxab
zyxcba
yxcbaz
xcbazy
xyzcba
yzcbax
zcbaxy
zyxcba
"""
"""
cbazyxqpo
bazyxqpoc
azyxqpocb
abczyxqpo
bczyxqpoa
czyxqpoab
zyxqpocba
yxqpocbaz
xqpocbazy
xyzqpocba
yzqpocbax
zqpocbaxy
qpocbazyx
pocbazyxq
ocbazyxqp
opqcbazyx
pqcbazyxo
qcbazyxop
zyxqpocba
"""
