import random

class Node:
    def __init__(self, val=-1, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down


class Skiplist:
    def __init__(self):
        self.head = Node()

    def search(self, target: int) -> bool:
        node = self.head
        while node:
            # move to the right in the current level
            while node.right and node.right.val < target:
                node = node.right

            if node.right and node.right.val == target:
                return True

            # move to the next level
            node = node.down
        return False

    def add(self, num: int) -> None:
        nodes = []
        node = self.head

        while node:
            while node.right and node.right.val < num:
                node = node.right
            nodes.append(node)
            node = node.down

        insert = True
        down = None
        while insert and nodes:
            node = nodes.pop()
            node.right = Node(num, node.right, down)
            down = node.right
            insert = (random.getrandbits(1) == 0)

        # create a new level with a dymmy head
        # right = None
        # down = current head
        if insert:
            self.head = Node(-1, None, self.head)

    def erase(self, num: int) -> bool:
        node = self.head
        found = False
        while node:
            # move to the right in the current level
            while node.right and node.right.val < num:
                node = node.right
            # find the target node
            if node.right and node.right.val == num:
                # delete by skipping
                node.right = node.right.right
                found = True
            # move to the next level
            node = node.down
        return found




