"""

https://leetcode.com/problems/race-car/discuss/124326/Summary-of-the-BFS-and-DP-solutions-with-intuitive-explanation

Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following:
if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input:
target = 3
Output: 2
Explanation:
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.
Example 2:
Input:
target = 6
Output: 5
Explanation:
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.

Note:

1 <= target <= 10000.
"""

"""
For the input 5, we can reach with only 7 steps: AARARAA. Because we can step back.

Let's say n is the length of target in binary and we have 2 ^ (n - 1) <= target < 2 ^ n
We have 2 strategies here:
1. Go pass our target , stop and turn back
We take n instructions of A.
1 + 2 + 4 + ... + 2 ^ (n-1) = 2 ^ n - 1
Then we turn back by one R instruction.
In the end, we get closer by n + 1 instructions.

2. Go as far as possible before pass target, stop and turn back
We take N - 1 instruction of A and one R.
Then we take m instructions of A, where m < n
"""

"""
Consider two general cases for number i with bit_length n.

i==2^n-1, this case, n is the best way
2^(n-1)-1<i<2^n-1, there are two ways to arrive at i:
Use n A to arrive at 2^n-1 first, then use R to change the direction, 
by here there are n+1 operations (n A and one R), then the remaining is same as dp[2^n-1-i]
Use n-1 A to arrive at 2^(n-1)-1 first, then R to change the direction, 
use m A to go backward, then use R to change the direction again to move forward, 
by here there are n-1+2+m=n+m+1 operations (n-1 A, two R, m A) , 
current position is 2^(n-1)-1-(2^m-1)=2^(n-1)-2^m, the remaining operations is same as dp[i-(2^(n-1)-1)+(2^m-1)]=dp[i-2^(n-1)+2^m)].
Why dp in this way?

I first think the dp way should be:

dp[i] = min(n+1+dp[2**n-1-i], n-1+2+dp[i-2**(n-1)+1])
But it's wrong, look at the (n-1) A case, we do A for (n-1) times, then do two R, then the situation is the same as dp[i-2**(n-1)+1]. 
This can be larger than the actual min operations since, there may be redundant R operations, 
we can combine RR operation with the remaining (2**(n-1)-1) to i path. 
So we use m to go backward between the two R operations and count the remaining (2^(n-1)-2^m) to i path to include the combining situation.

For example:

target = 5

The right answer should be AARARAA, positions: 0, 1, 3, 3, 2, 2, 3, 5
But if we use the above formula, the answer is AA (0->3) RR (make speed at 1 again) AARA (3->5)

We can move the last A to the middle of RR, so that we save an operation. That's where the combine can happen.
So we do dp by adding m A between the RR and add the # operations for remaining distance.
"""

import heapq
import collections

class SolutionLee:
    def __init__(self):
        self.dp = {0: 0}


    def racecar(self, t):
        if t in self.dp:
            return self.dp[t]
        n = t.bit_length()
        if 2 ** n - 1 == t:
            self.dp[t] = n
        else:
            self.dp[t] = self.racecar(2 ** n - 1 - t) + n + 1
            for m in range(n - 1):
                self.dp[t] = min(self.dp[t], self.racecar(t - 2 ** (n - 1) + 2 ** m) + n + m + 1)
        return self.dp[t]


# BFS
class Solution2:
    def racecar(self, target):
        q, cnt, used = [(0, 1)], 0, {(0, 1)}
        while q:
            new = []
            for pos, speed in q:
                if pos == target:
                    return cnt
                elif pos > 20000 or -20000 > pos:
                    continue
                if (pos + speed, speed * 2) not in used:
                    new.append((pos + speed, speed * 2))
                    used.add((pos + speed, speed * 2))
                if speed > 0 and (pos, -1) not in used:
                    new.append((pos, -1))
                    used.add((pos, -1))
                elif speed < 0 and (pos, 1) not in used:
                    new.append((pos, 1))
                    used.add((pos, 1))
            q = new
            cnt += 1


class Solution3:
    def racecar(self, target):
        target *= -1
        q, used = [(0, 0, -1)], {(0, -1)}
        while q:
            cnt, pos, speed = heapq.heappop(q)
            if pos == target:
                return cnt
            elif pos > 20000 or -20000 > pos:
                continue
            if (pos + speed, speed * 2) not in used:
                heapq.heappush(q, (cnt + 1, pos + speed, speed * 2))
                used.add((pos + speed, speed * 2))
            if speed < 0 and (pos, 1) not in used:
                heapq.heappush(q, (cnt + 1, pos, 1))
                used.add((pos, 1))
            elif speed > 0 and (pos, -1) not in used:
                heapq.heappush(q, (cnt + 1, pos, -1))
                used.add((pos, -1))


class Solution4:
    def racecar(self, target: int) -> int:
        que = collections.deque([(0, 1)])
        visited = set([(0, 1)])
        steps = 0
        while que:
            for _ in range(len(que)):
                pos, speed = que.popleft()
                if pos == target:
                    return steps
                if not (pos+speed, speed*2) in visited:
                    que.append((pos+speed, speed*2))
                    visited.add((pos+speed, speed*2))
                if not (pos, -1 if speed > 0 else 1) in visited:
                    que.append((pos, -1 if speed > 0 else 1))
                    visited.add((pos, -1 if speed > 0 else 1))
            steps += 1

