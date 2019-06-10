
"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.


Example:

Input: [2,1,5,6,2,3]
Output: 10
"""

"""
This idea is really beautiful. However I felt a bit confused when reading the explanation. 
After thinking for a while, here is my thought if it is helpful. 
For any bar x, if it's in a rectangle of which the height is also the height of x, 
we know that every bar in the rectangle must be no shorter than x. 
Then the issue is to find the left and right boundary where the bars are shorter than x. 
According to the code, when a bar is popped out from the stack, 
we know it must be higher than the bar at position i, so bar[i] must be the right boundary 
(exclusive) of the rectangle, and the previous bar in the stack is the first one that is shorter 
than the popped one so it must be the left boundary (also exclusive). Then we find the rectangle.
"""

class Solution1:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans


"""
The algorithm using stack actually is not quite intuitive. 
At least I won't think about using it at first time.

It is more natural to think about this way. Let left[i] to indicate how many bars to the left 
(including the bar at index i) are equal or higher than bar[i], 
right[i] is that to the right of bar[i], 
so the the square of the max rectangle containing bar[i] is simply height[i] * (left[i] + right[i] - 1)

Note, this algorithm runs O(n) not O(n^2)! The while loop in the for loop jumps forward or backward by the steps already calculated.

Because when he calculated the left[i], he started from the left side, 
and if height[i-1] >= height[i]: we just add the left[i-1] to the left[i] 
and so as to the index j, because left[i-1] means the number of rectangles that are higher or equal to the height[i-1] (and height[i-1] >= height[i]). 
In this way, he saved much time (although cost more space). 
And same way for the array right[i]. So, in general, I guess that he used more space to save time, 
but as for the running time, I couldn't agree that it is O(n) but I think it is close to it.

"""

class Solution2:
    def largestRectangleArea(self, height):
        n = len(height)
        # left[i], right[i] represent how many bars are >= than the current bar
        left = [1] * n
        right = [1] * n
        max_rect = 0

        # calculate left
        for i in range(0, n):
            j = i - 1
            while j >= 0:
                if height[j] >= height[i]:
                    left[i] += left[j]
                    j -= left[j]
                else:
                    break

        # calculate right
        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n:
                if height[j] >= height[i]:
                    right[i] += right[j]
                    j += right[j]
                else:
                    break

        for i in range(0, n):
            max_rect = max(max_rect, height[i] * (left[i] + right[i] - 1))

        return max_rect



class Solution3:
    # Helper function calculating how far each bar can be extended to the right.
    def calmax(self, height):
        stack = []
        n = len(height)
        rec = [0] * n
        for i in range(len(height)):
            while len(stack) > 0 and height[stack[-1]] > height[i]:
                top = stack.pop()
                rec[top] = i
            stack.append(i)
        for i in stack:
            rec[i] = n
        return rec
    def largestRectangleArea(self, height):
        # How far can each bar be extended to the right?
        rec1 = self.calmax(height)
        # How far can each bar be extended to the left?
        rec2 = self.calmax(height[::-1])[::-1]
        maxa = 0
        n = len(height)
        for i in range(n):
            # Add the left and right part together
            new = height[i] * (rec1[i] + rec2[i] - n)
            maxa = max(new, maxa)
        return maxa


"""
Solution with discussion https://discuss.leetcode.com/topic/77574/python-solution-with-detailed-explanation

Largest Rectangle in Histogram https://leetcode.com/problems/largest-rectangle-in-histogram/

http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
http://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/

For every bar ‘x’, we calculate the area with ‘x’ as the smallest bar in the rectangle.
If we calculate such area for every bar ‘x’ and find the maximum of all areas, our task is done.
How to calculate area with ‘x’ as smallest bar? We need to know index of the first smaller (smaller than ‘x’) bar 
on left of ‘x’ and index of first smaller bar on right of ‘x’. Let us call these indexes as ‘left index’ and ‘right index’ respectively.
We traverse all bars from left to right, maintain a stack of bars. Every bar is pushed to stack once.
A bar is popped from stack when a bar of smaller height is seen.
When a bar is popped, we calculate the area with the popped bar as smallest bar.
How do we get left and right indexes of the popped bar – the current index tells us the ‘right index’ 
and index of previous item in stack is the ‘left index’. Note index of previous item is important here.
Now using the above idea, we can make both an N^2 and NlgN algorithm.
For N^2 algorithm, no stack is requried. We scan at each step in left and right direction.
For NlgN algorithm, we find the minimum height m1. We then split at the minimum height.

"""


class Solution5:
    def largestRectangleArea(self, heights):
        max_area, st = 0, []
        for idx,x in enumerate(heights):
            if len(st) == 0:
                st.append(idx)
            elif x >= heights[st[-1]]:
                st.append(idx)
            else:
                while st and heights[st[-1]] > x:
                    # For min_height, the right index is idx and the left index is st[-1].
                    # Distance between them will be (right_index - left_index - 1). right & left index are not included in result.
                    # If the stack is empty, then no bar on left is smaller. So width of base is idx.
                    min_height = heights[st.pop()]
                    max_area = max(max_area, min_height*(idx-1-st[-1])) if st else max(max_area, min_height*idx)
                st.append(idx)
        while st:
            min_height = heights[st.pop()]
            max_area = max(max_area, min_height*(len(heights)-1-st[-1])) if st else max(max_area, min_height*len(heights))
        return max_area


