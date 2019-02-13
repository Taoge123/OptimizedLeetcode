"""
The difficult parts are validating the two rules:

Row R and column C both contain exactly N black pixels.
For all rows that have a black pixel at column C, they should be exactly the same as row R
My solution:

Scan each row. If that row has N black pixels, put a string signature,
which is concatenation of each characters in that row, as key
and how many times we see that signature into a HashMap.
Also during scan each row, we record how many black pixels in each column
in an array colCount and will use it in step 2.
For input:
[['W', 'B', 'W', 'B', 'B', 'W'],
['W', 'B', 'W', 'B', 'B', 'W'],
['W', 'B', 'W', 'B', 'B', 'W'],
['W', 'W', 'B', 'W', 'B', 'B']]
We will get a HashMap:
{"WBWBBW": 3, "WWBWBB": 1}
and colCount array:
[0, 3, 1, 3, 4, 1]
Go through the HashMap and if the count of one signature is N,
those rows potentially contain black pixels we are looking for.
Then we validate each of those columns. For each column of them has N black pixels
(lookup in colCount array), we get N valid black pixels.
For above example, only the first signature "WBWBBW" has count == 3.
We validate 3 column 1, 3, 4 where char == 'B', and column 1 and 3 have 3 'B',
then answer is 2 * 3 = 6.
Time complexity analysis:
Because we only scan the matrix for one time, time complexity is O(m*n).
m = number of rows, n = number of columns.
"""

"""
Short Fast python solution based on @StefanPochmann solution.

The key insight is that if a valid column (satisfying rule2 and rule1) 
would contribute exactly N nodes. 
The problem then reduces to finding the number of valid columns.

The conditions for a valid column are:

col.count('B') == N <---- rule 1
first_row_with_B_intersecting_with_col.count('B') == N <---- rule 1
picture.count(first_row_with_B_intersecting_with_col) == N <---- rule 2

https://leetcode.com/problems/lonely-pixel-ii/discuss/137451/Python-100-O(m*n)-Solution-188ms

"""

class Solution:
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        count = 0
        #for each row in picture
        for row in zip(*picture):
            #check count of B
            if row.count('B') != N: continue
            # print(row)
            # print(row.index('B'))
            first_row = picture[row.index('B')]
            print(first_row)
            if first_row.count('B') != N: continue
            if picture.count(first_row) != N: continue
            count += 1
        return count * N


class Solution(object):
    def findBlackPixel(self, picture, N):
        row = [r.count('B') for r in picture]
        col = [c.count('B') for c in zip(*picture)]

        loneP = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] != 'B':
                    continue
                if row[i] == N and col[j] == N:
                    if all(picture[k] == picture[i] for k in range(len(picture)) \
                           if picture[k][j] == 'B'):
                        loneP += 1

        return loneP


a = Solution()
input = [['W', 'B', 'W', 'B', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'B', 'W'],
 ['W', 'W', 'B', 'W', 'B', 'W']]
N = 3
print(a.findBlackPixel(input, N))

