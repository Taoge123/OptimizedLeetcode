
"""
You are given a circular array nums of positive and negative integers. If a number k at an index is positive, then move forward k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index and the cycle's length > 1. Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.


Example 1:

Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
Example 2:

Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.
Example 3:

Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.


Note:

-1000 ≤ nums[i] ≤ 1000
nums[i] ≠ 0
1 ≤ nums.length ≤ 5000

"""

"""
This solution does not use slow/fast pointer and achieve true O(n) time O(1) space.

Basic idea is to mark/change visited elements/indexes to prevent duplcate search and using extra space.

3 steps:

1. Change all initial values %= n (n is array length) so they are within [-n, n] range 
   but the "jump information" (the next index it is pointing to) is not changed;
2. Use every index as starting index and judge if there is a loop in this path. 
   Mark all visited elements in current path +n or -n depending on current direction. 
   In this way, the "jump information" is not changed but we know if it is already visited 
   or not in current path search. During the search, if we find a 0 or direction change, 
   terminate the search; or if we find a value which abs > n, we know it is already visited in current path 
   and we found a loop.
3. If we didn't find a loop in current path, mark all visited elements in current path as 0, 
   and 0 will be skipped in future search to prevent duplicate search.

In this way, each element is visited/changed constant times for the following cases: 1. initially %= n, 2. 
   used as termination point for a search, 3. mark as visited in current path, 4. mark as 0.

The condition in the orginal problem "there is no initial 0" can be deleted.
"""


class Solution1:
    def circularArrayLoop(self, nums):

        if not nums or len(nums) < 2:
            return False

        n = len(nums)
        for i in range(n):
            if type(nums[i]) != int:  # visited element
                continue
            if nums[i] % n == 0:  # self-loop
                continue

            direction = (nums[i] > 0)  # loop direction, cannot be changed midway

            mark = str(i)
            while (type(nums[i]) == int) and (direction ^ (nums[i] < 0)) and (nums[i] % n != 0):
                jump = nums[i]
                nums[i] = mark
                i = (i + jump) % n

            if nums[i] == mark:
                return True

        return False


"""
When we start a loop, as the problem description says, every item in the loop should have same sign, 
and when some loop have length more than len(nums) then it's indeed a circular loop, then we can avoid to have auxiliary storage
"""
class Solution2:
    def circularArrayLoop(self, nums: 'List[int]') -> 'bool':
        n = len(nums)
        for i, num in enumerate(nums):
            linkLength = 0
            j = i
            forward = nums[j] > 0
            while True:
                if (forward and nums[j] < 0) or (not forward and nums[j] > 0):
                    break
                nextj = (j + nums[j] + n) % n
                if nextj == j:
                    break
                j = nextj
                linkLength += 1
                if linkLength > n:
                    return True
        return False


"""
Start from every number, visit trough the loop process, if we can find a loop all positive or negative 
and the length of loop is bigger than n, then we find a loop.

Or we can just set all numbers in this failed "loop" path, marking we have already visited, 
and find the next non-zero number.
"""
class Solution3:
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        length = len(nums)

        # set all numbers to zero in the failed "loop" path
        def set_zero_loop(nums, i):
            while 1:
                newIdx = (nums[i] + i + length) % length
                if newNum * nums[i] > 0:
                    nums[i], i = 0, newIdx
                else:
                    break

        for i in range(length):
            if nums[i] != 0:
                cnt, tempI = 0, i
                while cnt < length:
                    newIdx = (nums[tempI] + tempI + length) % length
                    newNum = nums[newIdx]
                    # if only one number in the loop or differ in direction
                    if tempI == newIdx or newNum * nums[i] <= 0:
                        set_zero_loop(nums, i)
                        break
                    tempI = newIdx
                    cnt += 1
                if cnt == length:
                    return True

        return False

"""
by union-find: for each edge (i,j), we union them when both i and j are in the same direction; 
if there's a loop, there must be an edge(i, j) where j and i have already been connected.
"""
class Solution4:
    def circularArrayLoop(self, nums: 'List[int]') -> 'bool':
        n = len(nums)
        parent = dict((i, i) for i in range(n))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        for i, v in enumerate(nums):
            j = (i + v) % n
            if i != j and nums[j]*nums[i] > 0:
                ri, rj = find(i), find(j)
                if ri == rj:
                    return True
                parent[ri] = rj
        return False

"""
another alternative: walk along and use set to check directly
"""
class Solution5:
    def circularArrayLoop(self, nums: 'List[int]') -> 'bool':
        n, done = len(nums), set()
        for i in range(n):
            if i in done: continue
            j, cur = i, set()
            while j not in cur and j not in done and nums[i]*nums[j] > 0:
                cur.add(j)
                j = (j+nums[j]) % n
            if j in cur and nums[j] % n != 0:
                return True
            done = done.union(cur)
        return False

"""
解题思路：
深度优先搜索（DFS Depth First Search）

对nums中的各元素执行DFS，将搜索过的不满足要求的元素置为0，从而避免重复搜索。

当搜索深度depth ＞ 数组长度size时，说明一定有元素被访问了2次，从而推断数组中存在环，返回True。

数组遍历结束，返回False。

由于数组中每一个元素的平均访问次数为常数，因此算法的时间复杂度为O(n)。

例如nums = [7, -1, -2, -3, -1, -2, -3]，0号、3号元素被访问多次，但是各元素的访问次数之和是数组长度的常数倍。
"""

class Solution6:
    def circularArrayLoop(self, nums):

        size = len(nums)
        def dfs(idx, cnt):
            if cnt < size:
                nidx = (idx + nums[idx] + size) % size
                if nidx == idx or \
                  nums[nidx] * nums[idx] <= 0 or \
                  dfs(nidx, cnt + 1) == 0:
                    nums[idx] = 0
            return nums[idx]
        for idx in range(size):
            if nums[idx] and dfs(idx, 0):
                return True
        return False

"""
弄清楚了题意后来考虑如何做，由于从一个位置只能跳到一个别的位置，而不是像图那样一个点可以到多个位置，
所以这里我们就可以根据坐标建立一对一的映射，一旦某个达到的坐标已经有映射了，说明环存在，当然我们还需要进行一系列条件判断。
首先我们需要一个visited数组，来记录访问过的数字，然后我们遍历原数组，如果当前数字已经访问过了，直接跳过，
否则就以当前位置坐标为起始点开始查找，进行while循环，计算下一个位置，计算方法是当前位置坐标加上对应的数字，
由于是循环数组，所以结果可能会超出数组的长度，所以我们要对数组长度取余。
当然上面的数字也可能是负数，加完以后可能也是负数，所以在取余之前还得再补上一个n，使其变为正数。
此时我们判断，如果next和cur相等，说明此时是一个数字的循环，不符合题意，再有就是检查二者的方向，数字是正数表示forward，
若是负数表示backward，在一个loop中必须同正或同负，我们只要让二者相乘，如果结果是负数的话，说明方向不同，直接break掉。
此时如果next已经有映射了，说明我们找到了合法的loop，返回true，否则建立一个这样的映射，
将next位置在visited数组中标记true，继续循环
"""

"""
我们还可以简化上面的代码，可以不用visited数组，直接在nums中标记，由于题目中说了nums中不会有0，所以可以把访问过的位置标记为0。
然后计算next位置，通过cur加上i，再加上n之后，对n取余。如果next和i相等，直接跳过，因为这表示循环只有一个数字，不合题意。
然后开始循环，当cur和nums[next]的乘积为正时，说明此时是一个方向的，我们将cur赋值为nums[next]，将nums[next]赋值为0，
表示已经访问过，然后再计算新的next位置。直到循环被打破，若此时next和i相等，说明有大于1个数字的环存在，返回true。
最终for循环退出后，返回false
"""

"""
思路：Just think it as finding a loop in Linkedlist, except that loops with only 1 element do not count. 
Use a slow and fast pointer, slow pointer moves 1 step a time while fast pointer moves 2 steps a time. 
If there is a loop (fast == slow), we return true, else if we meet element with different directions, 
then the search fail, we set all elements along the way to 0. Because 0 is fail for sure 
so when later search meet 0 we know the search will fail.
"""


class Solution6:
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        def getIndex(i):
            return (i + nums[i]) % n

        for i in range(n):
            if not nums[i]: continue

            # slow/faster pointer
            j, k = i, getIndex(i)
            while (nums[k] * nums[i] > 0 and nums[getIndex(k)] * nums[i] > 0):  # check fast pointer is enough
                if j == k:
                    # check the loop has more than 1 element
                    if j == getIndex(j): break
                    return True

                j = getIndex(j)
                k = getIndex(getIndex(k))

            # if not return from while, set all elements along the way to 0
            j = i
            while nums[j] * nums[i] > 0:
                nums[j] = 0
                j = getIndex(j)

        return False


s = Solution()
print(s.circularArrayLoop([2, -1, 1, 2, 2]))
print(s.circularArrayLoop([-1, 2]))




