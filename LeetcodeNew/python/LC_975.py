"""
https://leetcode.com/problems/odd-even-jump/discuss/562946/Solution-Python-With-SortedDict-from-sortedcontainers-library-(default-included-in-leetcode)

We need to jump higher and lower alternately to the end.

Take [5,1,3,4,2] as example.

If we start at 2,
we can jump either higher first or lower first to the end,
because we are already at the end.
higher(2) = true
lower(2) = true

If we start at 4,
we can't jump higher, higher(4) = false
we can jump lower to 2, lower(4) = higher(2) = true

If we start at 3,
we can jump higher to 4, higher(3) = lower(4) = true
we can jump lower to 2, lower(3) = higher(2) = true

If we start at 1,
we can jump higher to 2, higher(1) = lower(2) = true
we can't jump lower, lower(1) = false

If we start at 5,
we can't jump higher, higher(5) = false
we can jump lower to 4, lower(5) = higher(4) = false


Complexity
Time O(NlogN)
Space O(N)
"""
"""
    public int oddEvenJumps(int[] A) {
        int n  = A.length, res = 1;
        boolean[] higher = new boolean[n], lower = new boolean[n];
        higher[n - 1] = lower[n - 1] = true;
        TreeMap<Integer, Integer> map = new TreeMap<>();
        map.put(A[n - 1], n - 1);
        for (int i = n - 2; i >= 0; --i) {
            Map.Entry<Integer, Integer> hi = map.ceilingEntry(A[i]), lo = map.floorEntry(A[i]);
            if (hi != null) higher[i] = lower[(int)hi.getValue()];
            if (lo != null) lower[i] = higher[(int)lo.getValue()];
            if (higher[i]) res++;
            map.put(A[i], i);
        }
        return res;

    private int sln2(int[] A){
        TreeMap<Integer,Integer> map = new TreeMap<>();
        int n = A.length;
        boolean[][] dp = new boolean[2][n];
        dp[0][n-1] = true;
        dp[1][n-1] = true;
        map.put(A[n-1], n-1);
        int res = 1;
        for(int i = n-2;i>=0;i--){
            Integer floorKey = map.floorKey(A[i]);
            Integer ceilingKey = map.ceilingKey(A[i]);
            
            if(ceilingKey!=null){
                dp[0][i] = dp[1][map.get(ceilingKey)];
            }
            if(floorKey!=null){
                dp[1][i] = dp[0][map.get(floorKey)];
            }
            
            res += dp[0][i]? 1: 0;
            map.put(A[i], i);
        }
        return res;
    }
    
"""

from sortedcontainers import SortedDict


class SolutionTree:
    def oddEvenJumps(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        n = len(nums)
        isOkEven = [False] * len(nums)
        isOkOdd = [False] * len(nums)
        isOkEven[n - 1] = True
        isOkOdd[n - 1] = True
        tree = SortedDict()
        tree[nums[n - 1]] = n - 1
        for i in range(n - 2, -1, -1):
            val = nums[i]
            if val in tree:
                isOkEven[i] = isOkOdd[tree[val]]
                isOkOdd[i] = isOkEven[tree[val]]
            else:
                smallestP = tree.bisect_left(val)
                largestP = tree.bisect_left(val) - 1
                isOkOdd[i] = True if smallestP != len(tree) and isOkEven[tree.peekitem(smallestP)[1]] else False
                isOkEven[i] = True if largestP != -1 and isOkOdd[tree.peekitem(largestP)[1]] else False
            tree[val] = i
        res = 0
        for e in isOkOdd:
            if e:
                res += 1
        return res


class Solution:
    def oddEvenJumps(self, A):
        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        stack = []
        for num, i in sorted([num, i] for i, num in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for num, i in sorted([-num, i] for i, num in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)



# Dynamic programming
class Solution2:
    def oddEvenJumps(self, A):
        N = len(A)
        nums = sorted(range(N), key=lambda i: A[i])
        oddnext = self.convert(nums, N)
        nums = sorted(range(N), key=lambda i: -A[i])
        evennext = self.convert(nums, N)

        odd = [False] * N
        even = [False] * N
        odd[N - 1] = even[N - 1] = True
        for i in range(N - 2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]
        return sum(odd)

    def convert(self, nums, N):
        res = [None] * N
        stack = []
        for num in nums:
            while stack and num > stack[-1]:
                res[stack.pop()] = num
            stack.append(num)
        return res


A = [10,13,12,14,15]
a = Solution()
print(a.oddEvenJumps(A))

