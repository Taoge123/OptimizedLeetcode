
class Solution:
    def grayCode(self, n):
        results = [0]
        for i in range(n):
            for x in reversed(results):
                print(x, pow(2, i), list(reversed(results)))
                results.append(x + pow(2, i))

        return results



