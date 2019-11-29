"""
Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)
"""

import collections

class SnakeGame:
    def __init__(self, width: int, height: int, food):
        # E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        self.snake = collections.deque([[0 ,0]])    # snake head is at the front
        self.width = width
        self.height = height
        self.food = collections.deque(food)
        self.direct = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def move(self, direction: str) -> int:
        newHead = [self.snake[0][0 ] +self.direct[direction][0], self.snake[0][1 ] +self.direct[direction][1]]
        # notice that the newHead can be equal to self.snake[-1]
        if (newHead[0] < 0 or newHead[0] >= self.height) or (newHead[1] < 0 or newHead[1] >= self.width) \
                or (newHead in self.snake and newHead != self.snake[-1]): return -1

        if self.food and self.food[0] == newHead:  # eat food
            self.snake.appendleft(newHead)   # just make the food be part of snake
            self.food.popleft()   # delete the food that's already eaten
        else:    # not eating food: append head and delete tail
            self.snake.appendleft(newHead)
            self.snake.pop()

        return len(self.snake) -1




# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
