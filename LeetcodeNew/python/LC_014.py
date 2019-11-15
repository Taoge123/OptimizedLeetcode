class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''

        for i in range(len(strs[0])):
            for j in strs:
                if len(j) <= i or strs[0][i] != j[i]:
                    return strs[0][:i]

        return strs[0]

