
"""

Given a picture consisting of black and white pixels,
and a positive integer N, find the number of black pixels located
at some specific row R and column C that align with all the following rules:

Row R and column C both contain exactly N black pixels.
For all rows that have a black pixel at column C, they should be exactly the same as row R
The picture is represented by a 2D char array consisting of 'B' and 'W',
which means black and white pixels respectively.

Example:
Input:
[['W', 'B', 'W', 'B', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'B', 'W'],
 ['W', 'W', 'B', 'W', 'B', 'W']]

N = 3
Output: 6
Explanation: All the bold 'B' are the black pixels we need (all 'B's at column 1 and 3).
        0    1    2    3    4    5         column index
0    [['W', 'B', 'W', 'B', 'B', 'W'],
1     ['W', 'B', 'W', 'B', 'B', 'W'],
2     ['W', 'B', 'W', 'B', 'B', 'W'],
3     ['W', 'W', 'B', 'W', 'B', 'W']]
row index

Take 'B' at row R = 0 and column C = 1 as an example:
Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels.
Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row 2. They are exactly the same as row R = 0.



这道题是之前那道Lonely Pixel I的拓展，我开始以为这次要考虑到对角线的情况，
可是这次题目却完全换了一种玩法。给了一个整数N，说对于均含有N个个黑像素的某行某列，
如果该列中所有的黑像素所在的行都相同的话，该列的所有黑像素均为孤独的像素，
让我们统计所有的这样的孤独的像素的个数。那么跟之前那题类似，
我们还是要统计每一行每一列的黑像素的个数，而且由于条件二中要比较各行之间是否相等，
如果一个字符一个字符的比较写起来比较麻烦，我们可以用个trick，把每行的字符连起来，
形成一个字符串，然后直接比较两个字符串是否相等会简单很多。然后我们遍历每一行和每一列，
如果某行和某列的黑像素刚好均为N，我们遍历该列的所有黑像素，如果其所在行均相等，
则说明该列的所有黑像素均为孤独的像素，将个数加入结果res中，然后将该行的黑像素统计个数清零，
以免重复运算，这样我们就可以求出所有的孤独的像素了

------------------------------------------------------------------------------------------
利用数组rows，cols分别记录某行、某列'B'像素的个数。
然后利用字典sdict统计每一行像素出现的个数。
最后遍历一次picture即可。

------------------------------------------------------------------------------------------
思路：
给了一个整数N，说对于均含有N个黑像素的某行某列，如果该列中所有的黑像素所在的行都相同的话，
该列的所有黑像素均为孤独的像素，让我们统计所有的这样的孤独的像素的个数。
那么跟之前那题类似，我们还是要统计每一行每一列的黑像素的个数，而且由于条件二中要比较各行之间是否相等，
如果一个字符一个字符的比较写起来比较麻烦，我们可以用个trick，把每行的字符连起来，形成一个字符串，
然后直接比较两个字符串是否相等会简单很多(用hashmap(string, count))。然后我们遍历每一行和每一列，
如果某行和某列的黑像素刚好均为N，我们遍历该列的所有黑像素，如果其所在行均相等，
则说明该列的所有黑像素均为孤独的像素，将个数加入结果res中，然后将该行的黑像素统计个数清零，
以免重复运算，这样我们就可以求出所有的孤独的像素了，


"""



import collections

class Solution:
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        w, h = len(picture), len(picture[0])
        rows, cols = [0] * w, [0] * h
        for x in range(w):
            for y in range(h):
                if picture[x][y] == 'B':
                    rows[x] += 1
                    cols[y] += 1

        dic = collections.defaultdict(int)
        for row in picture:
            dic[''.join(row)] += 1

        ans = 0
        for x in range(w):
            row = ''.join(picture[x])
            #Check for constrsint two whether N rows are identical
            if dic[row] != N:
                continue
            for y in range(h):
                if picture[x][y] == 'B':
                    #Samw as lonely pixel 1, we need to make sure the row and column will be the same
                    if rows[x] == N and cols[y] == N:
                        ans += 1
        return ans


























