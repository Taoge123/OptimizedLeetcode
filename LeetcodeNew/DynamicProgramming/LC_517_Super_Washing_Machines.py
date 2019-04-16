
"""
https://leetcode.com/problems/super-washing-machines/discuss/235584/Explanation-of-Java-O(n)-solution
https://leetcode.com/problems/super-washing-machines/discuss/99203/C%2B%2B-12-ms-O(n)-8-lines
https://www.cnblogs.com/grandyang/p/6648557.html



You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.

For each move, you could choose any m (1 ≤ m ≤ n) washing machines,
and pass one dress of each washing machine to one of its adjacent washing machines at the same time .

Given an integer array representing the number of dresses in each washing machine from left to right on the line,
you should find the minimum number of moves to make all the washing machines have the same number of dresses.
If it is not possible to do it, return -1.

Example1

Input: [1,0,5]

Output: 3

Explanation:
1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3
3rd move:    2     1 <-- 3    =>    2     2     2
Example2

Input: [0,3,0]

Output: 2

Explanation:
1st move:    0 <-- 3     0    =>    1     2     0
2nd move:    1     2 --> 0    =>    1     1     1
Example3

Input: [0,2,0]

Output: -1

Explanation:
It's impossible to make all the three washing machines have the same number of dresses.
Note:
The range of n is [1, 10000].
The range of dresses number in a super washing machine is [0, 1e5].
"""

"""
toLeft: the number of cloths moved to left from this machine
toRight: the number of cloths moved to right from this machine
toLeft and toRight may be negative but it's okay.
"""
class SolutionLee:
    def findMinMoves(self, machines):
        if sum(machines) % len(machines) == 0:
            target = sum(machines) / len(machines)
        else:
            return -1
        toLeft = 0
        res = 0
        for i in range(len(machines)):
            toRight = machines[i] - target - toLeft
            res = max(res, toLeft, toRight, toLeft + toRight)
            toLeft = -toRight
        return res


"""
Instead of using some DP methodology to solve the problem, 
I have a very intuitive way to approach the solution.

Think about the machine i, after we make all machines have the same dresses, 
how many dresses will be passed through machine i?
Let's denote the current sum of dresses of machines [0...i-1] as leftSums[i], 
and the current sum of dresses of machines [i+1...n-1] as rightSums[i].
Let's denote the expected sum of dresses of machines [0...i-1] as expLeft, 
which means after all dresses are equally distributed, the sum of address in machines [0...i-1] should be expLeft. 
The same logic applies to machines [i+1...n-1], denoted as expRight.

Then the above question should be clearly answered.
 If expLeft is larger than leftSums[i], that means no matter how you move the dresses, 
there will be at least expLeft - leftSums[i] dresses being moved to left of machine i, 
which means pass through machine i. For the right machines of machine i, the logic remains the same. 
So we could conclude that the minimum dresses passed through machine i will be:

left = expLeft > leftSums[i] ? expLeft - leftSums[i] : 0;
right = expRight > rightSums[i] ? expRight - rightSums[i] : 0;
total = left + right;
With this answer in mind, we could know that the minimum moves is the maximum dresses that pass through for each single machine, 
because for each dress, it will require at least one move. 
Hence the following solution. The code could be more concise, 
but I will leave it here for purpose of explanation.

If you have any doubts or suggestions for this solution, any comments are welcome.
"""
"""
First we check the sum of dresses in all machines. 
if that number cannot be divided by count of machines, there is no solution.

Otherwise, we can always transfer a dress from one machine to another, 
one at a time until every machines reach the same number, 
so there must be a solution. In this way, the total actions is sum of operations on every machine.

Since we can operate several machines at the same time, 
the minium number of moves is the maximum number of necessary operations on every machine.

For a single machine, necessary operations is to transfer dresses 
from one side to another until sum of both sides and itself reaches the average number. 
We can calculate (required dresses) - (contained dresses) of each side as L and R:

L > 0 && R > 0: both sides lacks dresses, and we can only export one dress from current machines at a time, 
so result is abs(L) + abs(R)
L < 0 && R < 0: both sides contains too many dresses, and we can import dresses from both sides at the same time, 
so result is max(abs(L), abs(R))
L < 0 && R > 0 or L >0 && R < 0: 
the side with a larger absolute value will import/export its extra dresses from/to current machine or other side, 
so result is max(abs(L), abs(R))

For example, [1, 0, 5], average is 2
for 1, L = 0 * 2 - 0 = 0, R = 2 * 2 - 5= -1, result = 1
for 0, L = 1 * 2 - 1= 1, R = 1 * 2 - 5 = -3, result = 3
for 5, L = 2 * 2 - 1= 3, R = 0 * 2 - 0= 0, result = 3
so minium moves is 3
"""

"""
Let me use an example to briefly explain this. For example, your machines[] is [0,0,11,5]. 
So your total is 16 and the target value for each machine is 4. Convert the machines array to a kind of gain/lose array, we get: [-4,-4,7,1]. 
Now what we want to do is go from the first one and try to make all of them 0.
To make the 1st machines 0, you need to give all its "load" to the 2nd machines.
So we get: [0,-8,7,1]
then: [0,0,-1,1]
lastly: [0,0,0,0], done.
You don't have to worry about the details about how these machines give load to each other. 
In this process, the least steps we need to eventually finish this process is determined by the peak of abs(cnt) 
and the max of "gain/lose" array. In this case, the peak of abs(cnt) is 8 and the max of gain/lose array is 7. So the result is 8.

Some other example:
machines: [0,3,0]; gain/lose array: [-1,2,-1]; max = 2, cnt = 0, -1, 1, 0, its abs peak is 1. So result is 2.
machines: [1,0,5]; gain/lose array: [-1,-2,3]; max = 3, cnt = 0, -1, -3, 0, its abs peak is 3. So result is 3.

public class Solution {
    public int findMinMoves(int[] machines) {
        int total = 0; 
        for(int i: machines) total+=i;
        if(total%machines.length!=0) return -1;
        int avg = total/machines.length, cnt = 0, max = 0;
        for(int load: machines){
            cnt += load-avg; //load-avg is "gain/lose"
            max = Math.max(Math.max(max, Math.abs(cnt)), load-avg);
        }
        return max;
    }
}

"""

"""
- For each machines, the number of moves it conducts is the number of dresses it sends out.
- Start scanning from left
    - if it has >target dresses, send the surplus to right
    - if it has <targer dresses, let its right neighbor send the deficit to it 
      (regardless of how many dresses this neighbor has at the momnet)
    - Don't worry about the aggregated surplus or deficit, it eventually will be taken care by later machines.

"""
class Solution1:
    def findMinMoves(self, machines: 'List[int]') -> 'int':
        N = len(machines)
        D = sum(machines)
        if D % N != 0:
            return -1

        target = D // N
        ans = 0
        send_out = [0] * N
        for i in range(N - 1):
            if machines[i] > target:
                send_out[i] += machines[i] - target
            elif machines[i] < target:
                send_out[i + 1] = target - machines[i]
            machines[i + 1] += machines[i] - target
            ans = max(ans, send_out[i], send_out[i + 1])
        return ans


"""
1.sumneed:record the number of dress needed until i, the step must be larger than abs(sumneed). Because each machine at each step can get at most one dress from one direction.
2.When the number of dress in current machine is larger than ave, it must be offloaded. Each step can only offload one dress.
3.The maximum step is max(1,2).
"""
class Solution2:
    def findMinMoves(self, machines):

        tot = sum(machines)
        L = len(machines)
        if tot%L!=0:
            return -1
        ave = tot//L
        sumneed = 0
        res = 0
        for m in machines:
            sumneed += m-ave
            res = max(res,abs(sumneed),m-ave)
        return res


"""
Below explanation is inspired by 
https://leetcode.com/problems/super-washing-machines/discuss/235584/Explanation-of-Java-O(n)-solution and I add my understanding as well.

Take @darewreck54's example,
1 <-1 <- 4 <- 8  1 [2,1,4,7,1]
2 <-1 <- 4 <- 7   1 [3,1,4,6,1]
3     1 <- 4 <- 6  1 [3,2,4,5,1]
3     2 <- 4     5->1 [3,3,3,4,2]
3     3     3     4->2 [3,3,3,3,3]

I can conclude that for each node, its absolute accumulated defict to the average decides how many dress 
(=how many move) will flow THRU it. 
For example, the accumulated defict（ or Running Balance) are [-2, -4, -3, 2, 0], 
the physical meaning is that for node 1, totally 2 dresses need to flow through it (see how many left arrow "<-" in above for node 1? it's 2); 
for node 2, totally 4 dresses (sign indicates flow direction BTW). 
The minimal number of move for a node is the max of absolute Runnning Balance IF there is only 1 direction.
However, in above example, I have 2 directions (see the last node, 
it accept 2 address from its left node). 
Therefore, I need to compare max absolute Runnning Balance with (max dress - average dress). 
Refer to @darewreck54's post for why (max dress - average dress) can be a possible answer :)
"""

"""
这道题题给了我们一堆工藤新一，噢不，是滚筒洗衣机。我们有许多洗衣机，每个洗衣机里的衣服数不同，
每个洗衣机每次只允许向相邻的洗衣机转移一件衣服，问要多少次才能使所有洗衣机的衣服数相等。
注意这里的一次移动是说所有洗衣机都可以移动一件衣服到其相邻的洗衣机。
这道题的代码量其实不多，难点是在于解题思路，难的是对问题的等价转换等。
博主也没有做出这道题，博主想到了要先验证衣服总数是否能整除洗衣机的数量，
然后计算出每个洗衣机最终应该放的衣服数，返回跟初始状态衣服数之差的最大值，但这种解法是不对的，
无法通过这个test case [0, 0, 11, 5]，最终每个洗衣机会留4件衣服，我想的那方法会返回7，
然后正确答案是8。想想也是，如果这么是这么简单的思路，这题怎么会标记为Hard呢，
还是图样图森破啊。这里直接参照大神Chidong的帖子来做，我们就用上面那个例子，有四个洗衣机，
装的衣服数为[0, 0, 11, 5]，最终的状态会变为[4, 4, 4, 4]，那么我们将二者做差，
得到[-4, -4, 7, 1]，这里负数表示当前洗衣机还需要的衣服数，正数表示当前洗衣机多余的衣服数。
我们要做的是要将这个差值数组每一项都变为0，对于第一个洗衣机来说，需要四件衣服可以从第二个洗衣机获得，
那么就可以把-4移给二号洗衣机，那么差值数组变为[0, -8, 7, 1]，此时二号洗衣机需要八件衣服，
那么至少需要移动8次。然后二号洗衣机把这八件衣服从三号洗衣机处获得，
那么差值数组变为[0, 0, -1, 1]，此时三号洗衣机还缺1件，就从四号洗衣机处获得，
此时差值数组成功变为了[0, 0, 0, 0]，成功。
那么移动的最大次数就是差值数组中出现的绝对值最大的数字，8次
"""
"""
问题分析：这是状态转移问题，每个洗衣机在同一时间只能向相邻洗衣机传递一件衣服，
则合法的转移操作是在从左向右的+1、-1变化必须成对出现，例如：-1，0，+1，+1，0，0，0，-1，
而这种-1，-1，0，0，+1，-1，0，+1，+1，+1是不合法的转移操作。
而对于k个所有合法操作进行累加和，必然是需要转移的每个洗衣机与最终平衡洗衣机衣服数目的差值。
对于合法操作的特点：从左向右进行累加，最大值必然是1，所以对于所有k个合法操作累加之后的合法操作同样进行从左向右累加，
最大值必然是k，即转移操作的次数。由于每个合法操作的最大值出现的位置不同，
从左向右累加和必须和当前洗衣机本身需要转移的衣服数目进行比较。
"""
"""
思路：

我们首先计算所有洗衣机里面的衣服总和，如果衣服总和不能被洗衣机个数整除，那么就不存在解决方案。
否则，我们总是可以找到移动方案使得所有洗衣机最终的衣服个数相同，最差方案无非是每次只选择一个洗衣机，只移动一件衣服。在这种情况下，
移动次数就是所有洗衣机的移动次数之和。

然而更好的消息是：我们每次可以同时移动几个洗衣机里面的衣服。因此最小移动次数就变成了每个洗衣机的必要移动次数的最大值。
对于单个洗衣机而言，必要移动次数就是将衣服从它的一侧移动到另外一侧（这里的一侧还同时包含它自身），
直到它两边的洗衣机加上它本身的衣服件数都达到了平均值。对于每个洗衣机，
其必要移动次数取决于左侧必要移动次数L和右侧必要移动次数R，具体定义就是(所需衣服) - (已有衣服)。
根据L和R的正负，具体可以分为三种情况：

1）L > 0 && R > 0：说明两侧都缺衣服，所以我们必须从当前洗衣机一件一件地向两侧匀衣服，
所以必要移动次数是：abs(L) + abs(R)；

2）L < 0 && R < 0：说明两侧都有多余衣服，但是好消息是我们可以从两边同时向这台洗衣机匀衣服，
所以必要移动次数是：max(abs(L), abs(R))；

3）L < 0 && R > 0或者L > 0 && R < 0：有多余衣服的一侧需要向缺衣服的一侧匀衣服，
所以必要移动次数仍然是：max(abs(L), abs(R))。

例如对于题目中给出的例子[1, 0, 5]，平均每个洗衣机里面应该拥有2件衣服，那么：

对于第1台洗衣机, L = 0 * 2 - 0 = 0, R = 2 * 2 - 5= -1, result = 1；

对于第2台洗衣机, L = 1 * 2 - 1= 1, R = 1 * 2 - 5 = -3, result = 3；

对于第3台洗衣机, L = 2 * 2 - 1= 3, R = 0 * 2 - 0= 0, result = 3。

因此，最小必要移动次数就是3。很巧妙有木有？

"""
"""
题意很简单，我们就用上面那个例子，有四个洗衣机，装的衣服数为[0, 0, 11, 5]，最终的状态会变为[4, 4, 4, 4]，
那么我们将二者做差，得到[-4, -4, 7, 1]，这里负数表示当前洗衣机还需要的衣服数，
正数表示当前洗衣机多余的衣服数。我们要做的是要将这个差值数组每一项都变为0，对于第一个洗衣机来说，
需要四件衣服可以从第二个洗衣机获得，那么就可以把-4移给二号洗衣机，
那么差值数组变为[0, -8, 7, 1]，此时二号洗衣机需要八件衣服，那么至少需要移动8次。
然后二号洗衣机把这八件衣服从三号洗衣机处获得，那么差值数组变为[0, 0, -1, 1]，
此时三号洗衣机还缺1件，就从四号洗衣机处获得，此时差值数组成功变为了[0, 0, 0, 0]，成功。
那么移动的最大次数就是差值数组中出现的绝对值最大的数字，8次，
"""
class Solution3:
    def findMinMoves(self, machines):

        n, total = len(machines), sum(machines)
        if total % n != 0:
            return -1
        ave = total/n
        diff = [machines[i]-ave for i in xrange(n)]
        result, tmp = 0, 0
        for i in xrange(n):
            tmp += diff[i]
            result = max(result, abs(tmp), diff[i])
        return result


"""
下列解法均摘自LeetCode Discuss，暂时无法证明解法的正确性

解法I 参考：https://discuss.leetcode.com/topic/79938/very-short-easy-java-o-n-solution

"""
class Solution4:
    def findMinMoves(self, machines):

        if sum(machines) % len(machines):
            return -1
        avg = sum(machines) / len(machines)
        ans = total = 0
        for m in machines:
            total += m - avg
            ans = max(ans, abs(total), m - avg)
        return ans

"""
解法II 参考：https://discuss.leetcode.com/topic/79923/c-16ms-o-n-solution
"""
class Solution5:
    def findMinMoves(self, machines):

        total = sum(machines)
        size = len(machines)
        if total % size:
            return -1
        avg = total / size
        sums = [0] * size
        last = 0
        for i, m in enumerate(machines):
            last += m
            sums[i] = last
        ans = 0
        for i, m in enumerate(sums):
            left = i * avg - m + machines[i]
            right = (size - i - 1) * avg - sums[size - 1] + m
            if left > 0 and right > 0:
                ans = max(ans, left + right)
            else:
                ans = max(ans, abs(left), abs(right))
        return ans

