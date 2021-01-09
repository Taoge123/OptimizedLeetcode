class Solution:
    def longestPrefix(self, s: str) -> str:
        left, right = 0, 0
        power = 1
        idx = 0
        mod = 10 ** 9
        nums = [ord(s[i]) - ord('a') for i in range(len(s))]

        for i in range(len(s) - 1):

            left = (left * 26 + nums[i]) % mod
            right = (right + power * nums[-i - 1]) % mod
            power = power * 26 % mod
            if left == right:
                idx = i + 1

        return s[0:idx]



class SolutionSame:
    def longestPrefix(self, s: str) -> str:
        left, right = 0, 0
        power = 1
        idx = 0
        mod = 10 ** 9
        nums = [ord(s[i]) - ord('a') for i in range(len(s))]

        i, j = 0, len(s) - 1
        while j > 0:

            left = (left * 26 + nums[i]) % mod
            right = (right + power * nums[j]) % mod
            power = power * 26 % mod
            if left == right:
                idx = i + 1

            i += 1
            j -= 1

        return s[0:idx]



class SolutionRolling2:
    def longestPrefix(self, s):
        res = 0
        left, right = 0, 0
        base = 128
        mod = 10 ** 9 + 7

        for i in range(len(s) - 1):
            left = (left * base + ord(s[i])) % mod
            right = (right + pow(base, i, mod) * ord(s[-i - 1])) % mod

            if left == right:
                res = i + 1

        return s[:res]



class SolutionKMP:
    def longestPrefix(self, s: str) -> str:
        table = self.LPS(s)
        last = table[-1]
        return s[:last]

    def LPS(self, pattern):
        M = len(pattern)
        lps = [0] * M
        i, j = 1, 0
        while i < M:
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps






class SolutionLee:
    def longestPrefix(self, s):
        # res stores the index of the end of the prefix, used for output the result
        # l stores the hash key for prefix
        # r stores the hash key for suffix
        # mod is used to make sure that the hash value doesn't get too big, you can choose another mod value if you want.
        res = 0
        left, right = 0, 0
        mod = 10 ** 9 + 7

        # now we start from the beginning and the end of the string
        # note you shouldn't search the whole string! because the longest prefix and suffix is the string itself
        for i in range(len(s) - 1):

            # based on an idea that is similar to prefix sum, we calculate the prefix hash in O(1) time.
            # specifically, we multiply the current prefix by 128 (which is the length of ASCII, but you can use another value as well)
            # then add in the ASCII value of the upcoming letter
            left = (left * 128 + ord(s[i])) % mod

            # similarly, we can calculate the suffix hash in O(1) time.
            # Specifically, we get the ith letter from the end using s[~i], note ~i is -i-1
            # we find the pow(128, i, mod) and multiply by the letter's ASCII value
            # Actually, if we don't care about the beautifulness of the code, you can have a variable to keep track of pow(128, i, mod) as you increase i
            right = (right + pow(128, i, mod) * ord(s[-i - 1])) % mod

            # we check if the prefix and suffix agrees, if yes, we find yet another longer prefix, so we record the index
            if left == right:
                res = i + 1

        # after we finish searching the string, output the prefix
        return s[:res]




