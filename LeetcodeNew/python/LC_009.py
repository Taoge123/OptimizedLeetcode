class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        ans = 0
        absolute = abs(x)

        while absolute:
            ans = ans * 10 + absolute % 10
            absolute //= 10

        return x == ans


