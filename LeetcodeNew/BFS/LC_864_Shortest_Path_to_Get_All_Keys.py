
"""
We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall,
"@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.
We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.
We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of th
e first K letters of the English alphabet in the grid.
This means that there is exactly one key for each lock, and one lock for each key;
and also that the letters used to represent the keys
and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.



Example 1:

Input: ["@.a.#","###.#","b.A.B"]
Output: 8
Example 2:

Input: ["@..aA","..B#.","....b"]
Output: 6


Note:

1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.


"""

"""
题目大意： 求最短路径拿到所有钥匙
解题思路：求最短路径可以bfs求得，关键是如何标记状态避免重复访问，一般bfs或dfs就简单标记访问过和没访问过的状态，但是这道题要考虑此时已有钥匙的状态，也就是当你为了拿一把钥匙而走到死胡同，此时就要回走，因为你比之前多了把钥匙，所以状态不一样，可以回走。我们怎么标记状态呢，我们用位来标记有几把钥匙的状态，然后dfs和bfs都可以求最短路径，但bfs简单一点，开销也没那么大，dfs还要递归，不断求最小值。

迷宫遍历 + 最少步数 = BFS
注意 状态的表示即可，这里我使用了三维数组表示状态(x坐标，y坐标，身上携带的钥匙串)
内存开销是 地图大小*钥匙串 = 31 * 31 * (1<<6) a-f 6把钥匙

☝️一个技巧：使用 位运算 异或判断 身上钥匙串是否有对应的钥匙，比较方便



"""







