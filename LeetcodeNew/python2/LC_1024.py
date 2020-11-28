"""
https://www.youtube.com/watch?v=tEx3z4L7F-c
"""
"""

------------------------right
    --------
        --------
            ----------
                           --------------------
            
            
            
"""

class SolutionTony:
    def videoStitching(self, clips, T: int) -> int:
        clips = sorted(clips)
        right = 0
        idx = 0
        count = 0

        while idx < len(clips):
            if clips[idx][0] > right:
                return -1

            reach = right
            # clip起始点<=right, 继续考察
            while idx < len(clips) and clips[idx][0] <= right:
                reach = max(reach, clips[idx][1])
                idx += 1

            right = reach
            count += 1
            if reach >= T:
                return count
        return -1




class Solution:
    def videoStitching(self, clips, T: int) -> int:
        end = -1
        end2 = 0
        res = 0

        for i, j in sorted(clips):
            if end2 >= T or i > end2:
                break
            elif end < i <= end2:
                res += 1
                end = end2

            end2 = max(end2, j)
        return res if end2 >= T else -1



class Solution11:
    def videoStitching(self, clips, T: int) -> int:
        clips = sorted(clips)
        start, end = 0, 0
        count = 0
        idx = 0
        while start <= end:
            count += 1
            newstart, newend = end + 1, end
            while idx < len(clips) and start <= clips[idx][0] <= end:
                newend = max(newend, clips[idx][1])
                if newend >= T:
                    return count
                idx += 1
            start, end = newstart, newend
        return -1


"""
Sort clips first.
Then for each clip, update dp[clip[0]] ~ dp[clip[1]].

Time O(NlogN + NT), Space O(T)

Solution 3: DP
Loop on i form 0 to T,
loop on all clips,
If clip[0] <= i <= clip[1], we update dp[i]

Time O(NT), Space O(T)
"""

