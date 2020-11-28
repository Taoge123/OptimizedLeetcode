"""
Intuition
Let chopper help explain.

Starting at the origin and face north (0,1),
after one sequence of instructions,

if chopper return to the origin, he is obvious in an circle.
if chopper finishes with face not towards north,
it will get back to the initial status in another one or three sequences.

Explanation
(x,y) is the location of chopper.
d[i] is the direction he is facing.
i = (i + 1) % 4 will turn right
i = (i + 3) % 4 will turn left
Check the final status after instructions.


Complexity
Time O(N)
Space O(1)

"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        x, y = 0, 0
        dx, dy = 0, 1
        for ins in instructions:
            if ins == 'R':
                dx, dy = dy, -dx

            if ins == 'L':
                dx, dy = -dy, dx

            if ins == 'G':
                x += dx
                y += dy

        return (x, y) == (0, 0) or (dx, dy) != (0, 1)



