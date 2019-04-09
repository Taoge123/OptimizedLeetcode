
"""
You are given a series of video clips from a sporting event that lasted T seconds.
These video clips can be overlapping with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0]
and ends at time clips[i][1].  We can cut these clips into segments freely:
for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event ([0, T]).
If the task is impossible, return -1.



Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation:
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
Example 2:

Input: clips = [[0,1],[1,2]], T = 5
Output: -1
Explanation:
We can't cover [0,5] with only [0,1] and [0,2].
Example 3:

Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
Output: 3
Explanation:
We can take clips [0,4], [4,7], and [6,9].
Example 4:

Input: clips = [[0,4],[2,8]], T = 5
Output: 2
Explanation:
Notice you can have extra video after the event ends.


Note:

1 <= clips.length <= 100
0 <= clips[i][0], clips[i][1] <= 100
0 <= T <= 100
"""
"""
public int videoStitching(int[][] clips, int T) {
        Arrays.sort(clips, (a, b) -> a[0] - b[0]);
        int res = 0, end = -1, end2 = 0;
        for (int[] clip: clips) {
            int i = clip[0], j = clip[1];
            if (end2 >= T || i > end2) {
                // end2 >= T: We find the result
                // i > end2: There is a gap between the curr clip and the next clip
                break;
            } else if (end < i && i <= end2) {
                res++;
                end = end2;
            }
            end2 = Math.max(end2, j);
        }
        return end2 >= T ? res : -1;
    }
"""
class SolutionLee:
    def videoStitching(self, clips, T):
        end, end2, res = -1, 0, 0
        for i, j in sorted(clips):
            if end2 >= T or i > end2:
                break
            elif end < i <= end2:
                res, end = res + 1, end2
            end2 = max(end2, j)
        return res if end2 >= T else -1


class SolutionGreedy:
    def videoStitching(self, clips, T):
        d = {}
        for [s, e] in clips:
            if s in d:
                d[s] = max(e, d[s])
            else:
                d[s] = e
        ans = 1
        if 0 not in d:
            return -1
        start, next_start = 0, d[0]
        while start <= next_start < T:
            temp_max = 0
            for i in range(start + 1, next_start + 1):
                if i in d:
                    temp_max = max(temp_max, d[i])
            if temp_max <= next_start:
                return -1
            else:
                start = next_start
                next_start = temp_max
                ans += 1
        return ans


"""
1. We can sort the videos according to their end time. 
   So the last video's start time is equal or larger than T, 
   the last video will not be included. That is DP[i][j] = DP[i][j - 1]
2. If the last video's start time is smaller than T, We need to look at it's end time. 
   If it's end time is larger than T, we will make a new time clips[i - 1][1] (endtime) 
   as new T if we include the last video. Otherwise we just ignore the last video. 
   That is DP[i][j] = min(DP[i - 1][j], DP[i - 1][clips[i - 1][1]] + 1)
3. If the last video's end time is smaller than T, there is no way we can get the time span [0, T] covered, 
   since the clips are sorted by their ending times. So DP[i][j] = inf
   """


class Solution2:
    def videoStitching(self, clips, T):
        '''
        DP[i][T] = DP[i - 1][T] if T <= clips[i - 1][0]
        else
        DP[i][T] = DP[i - 1][clips[i - 1][0]] + 1 or DP[i - 1][T] whichever is smaller

        '''
        clips = sorted(clips, key=lambda x: x[::-1])
        n = len(clips)
        inf = float('inf')
        DP = [[inf for j in range(T + 1)] for i in range(n + 1)]

        DP[0][0] = 0

        for i in range(1, n + 1):
            DP[i][0] = 0
        for j in range(1, T + 1):
            DP[0][j] = inf

        for i in range(1, n + 1):
            for j in range(1, T + 1):
                if clips[i - 1][0] >= j:
                    DP[i][j] = DP[i - 1][j]
                else:
                    if j <= clips[i - 1][1]:  # now only need to cover to clips[i - 1][0] if clips[i] is included
                        DP[i][j] = min(DP[i - 1][clips[i - 1][0]] + 1, DP[i - 1][j])
                    else:  #
                        DP[i][j] = inf
        return DP[n][T] if DP[n][T] < inf else -1


class Solution3:
    def videoStitching(self, clips, T):
        dp = [T + 1] * (T + 1)
        dp[0] = 0

        for i in range(T + 1):
            for clip in clips:
                if i >= clip[0] and i <= clip[1]:
                    dp[i] = min(dp[i], dp[clip[0]] + 1)
            if dp[i] == T + 1:
                return -1
        return dp[-1]










