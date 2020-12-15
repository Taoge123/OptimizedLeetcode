import heapq


class DinnerPlates:
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = []
        self.stacks = []

    def push(self, val):
        while self.heap and self.heap[0] < len(self.stacks) and len(self.stacks[self.heap[0]]) == self.capacity:
            heapq.heappop(self.heap)

        if not self.heap:
            heapq.heappush(self.heap, len(self.stacks))

        if self.heap[0] == len(self.stacks):
            self.stacks.append([])

        self.stacks[self.heap[0]].append(val)

    def pop(self):
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.heap, index)
            return self.stacks[index].pop()

        return -1






class DinnerPlates2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = [] # record the available stack, will use heap to quickly find the smallest available stack
        # if you are Java or C++ users, tree map is another good option.
        self.stacks = [] # record values of all stack of plates, its last nonempty stack are the rightmost position

    def push(self, val):
        # To push, we need to find the leftmost available position
        # first, let's remove any stacks on the left that are full
        # 1) self.q: if there is still available stack to insert plate
        # 2) self.q[0] < len(self.stacks): the leftmost available index self.q[0] is smaller than the current size of the stacks
        # 3) len(self.stacks[self.q[0]]) == self.c: the stack has reached full capacity
        while self.heap and self.heap[0] < len(self.stacks) and len(self.stacks[self.heap[0]]) == self.capacity:
            # we remove the filled stack from the queue of available stacks
            heapq.heappop(self.heap)

        # now we reach the leftmost available stack to insert

        # if the q is empty, meaning there are no more available stacks
        if not self.heap:
            # open up a new stack to insert
            heapq.heappush(self.heap, len(self.stacks))

        # for the newly added stack, add a new stack to self.stacks accordingly
        if self.heap[0] == len(self.stacks):
            self.stacks.append([])

        # append the value to the leftmost available stack
        self.stacks[self.heap[0]].append(val)

    def pop(self):
        # To pop, we need to find the rightmost nonempty stack
        # 1) stacks is not empty (self.stacks) and
        # 2) the last stack is empty
        while self.stacks and not self.stacks[-1]:
            # we throw away the last empty stack, because we can't pop from it
            self.stacks.pop()

        # now we reach the rightmost nonempty stack

        # we pop the plate from the last nonempty stack of self.stacks by using popAtStack function
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        # To pop from an stack of given index, we need to make sure that it is not empty
        # 1) the index for inserting is valid and，
        # 2) the stack of interest is not empty
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            # we add the index into the available stack
            heapq.heappush(self.heap, index)
            # take the top plate, pop it and return its value
            return self.stacks[index].pop()

        # otherwise, return -1 because we can't pop any plate
        return -1


