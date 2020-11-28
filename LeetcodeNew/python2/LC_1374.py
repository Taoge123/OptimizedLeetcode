
class Solution:
    def generateTheString(self, n: int) -> str:
        if n < 1:
            return ''

        if n % 2 == 1:
            return n * 'a'
        else:
            return 'a' + ( n -1) * 'b'



