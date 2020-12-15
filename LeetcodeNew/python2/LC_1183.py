"""
https://www.youtube.com/watch?v=FjIao84fqLg

https://leetcode.com/problems/maximum-number-of-ones/discuss/377317/Python-folding-submatrix-detailed-explanation
https://leetcode.com/problems/maximum-number-of-ones/discuss/376911/PythonC%2B%2B-Solution-with-explanation


Don't check whether there are too many "1"s in a submatrix, this is too hard to implement.
Instead, only look at the top left submatrix, try to set all points in it to "1", and find out how much benifit each "1" can make.
Since you are only allowed to have "maxOnes" number of "1"s in a submatrix, you don't actually set them all to "1",
instead you choose only those with best "benifit" to set to "1".
"Benifit" here means, if I set this position in the top left submatrix, then how many more "1" I can get in other folded submatrix.
If the big matrix can exactly fit all submatrix folded from top left submatrix,
then all points should have the same folding benifits, just randomly pick any "maxOnes" number of points will work.
But if not, then those at top left side will have more folding benifits than those on the bottom right side.
The final result will be the sum of all "benifits" from the choosen points in the top left submatrix

"""


"""
Devide the whole area into many sideLength*sideLength mini areas.

"""
import heapq

class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        dp = [[0] * sideLength for _ in range(sideLength)]

        for i in range(width):
            for j in range(height):
                dp[i % sideLength][j % sideLength] += 1

        heap = []
        for i in range(sideLength):
            for j in range(sideLength):
                heapq.heappush(heap, -dp[i][j])

        res = 0
        for i in range(maxOnes):
            res -= heapq.heappop(heap)

        return res




class Solution2:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        res=[]
        for i in range(sideLength):
            for j in range(sideLength):
                xFolds = (width-i-1) // sideLength+1
                yFolds = (height-j-1) // sideLength+1
                res.append(xFolds * yFolds)
        res.sort(reverse=True)
        return sum(res[:maxOnes])



width = 3
height = 3
sideLength = 2
maxOnes = 1

a = Solution()
print(a.maximumNumberOfOnes(width, height, sideLength, maxOnes))





