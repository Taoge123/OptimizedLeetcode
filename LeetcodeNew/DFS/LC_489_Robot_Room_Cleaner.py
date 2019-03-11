"""
interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Example:

Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.

"""



"""
When we come to a new cell, we turn left. 
If we try to go and turn right 3 times, 
we have covered everything in front of us and we should backtrack. 
If we can go to a direction, since we are facing backward for backtracking, 
we should turn left instead of right (if we didn't go, 
we would still face the direction, not its reverse). 
Also, when we are done with a cell, we should come back from it. 
Here is a minimalist code to solve the problem.
"""

DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # facing up, turning right as index increases


def dfs(robot, coord, dindex, visited):
    visited.add(coord)
    robot.clean()
    last_move = True
    for di in [3, 0, 1, 2]:
        robot.turnLeft() if last_move else robot.turnRight()
        d = DIRS[(dindex + di) % 4]
        new_c = (coord[0] + d[0], coord[1] + d[1])

        if new_c not in visited and robot.move():
            dfs(robot, new_c, (dindex + di) % 4, visited)
            robot.move()  # come back
            last_move = True
        else:
            last_move = False


class Solution5:
    def cleanRoom(self, robot):
        DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # facing up, turning right as index increases
        visited = set()

        def dfs(robot, coord, dindex):
            visited.add(coord)
            robot.clean()
            last_move = True

            for di in [3, 0, 1, 2]:
                if last_move:  # 固定先左后右
                    robot.turnLeft()
                else:
                    robot.turnRight()
                d = DIRS[(dindex + di) % 4]  # 調整方向
                new_c = (coord[0] + d[0], coord[1] + d[1])  # 下一步的位置

                if new_c not in visited and robot.move():  # 看一看可不可以前進
                    dfs(robot, new_c, (dindex + di) % 4)  # 前進
                    robot.move()  # come back                #精華，有前進就必須有相應的後退!!!原路返回
                    last_move = True  # 下一步繼續嘗試向左轉
                else:  # 某個點訪問過了或者不可訪問
                    last_move = False  # 下一步向右轉

        dfs(robot, (0, 0), 0)

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        dfs(robot, (0, 0), 0, set())


# left, up, right, down
DIR = ((0, -1), (-1, 0), (0, 1), (1, 0))


class Solution6:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # assume we start at (0, 0) the origin
        self.dfs(robot, (0, 0), set(), 1)

    def dfs(self, robot, curr_pos, visited, facing_direction):
        robot.clean()
        visited.add(curr_pos)

        for i in range(4):
            robot.turnLeft()
            # for i in [0, 3], i+1 means how many times we have turned left
            # (facing_direction - (i + 1)) % 4 therefore, is our new facing direction
            new_direction = (facing_direction - i - 1) % 4
            new_pos = (curr_pos[0] + DIR[new_direction][0], curr_pos[1] + DIR[new_direction][1])
            if new_pos not in visited and robot.move():
                self.dfs(robot=robot,
                         curr_pos=new_pos,
                         visited=visited,
                         facing_direction=new_direction)
                # turn around
                robot.turnLeft()
                robot.turnLeft()
                # move back
                robot.move()
                # face the previous direction, such that we can continue turning left
                robot.turnLeft()
                robot.turnLeft()











