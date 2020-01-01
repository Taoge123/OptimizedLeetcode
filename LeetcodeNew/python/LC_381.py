
"""
Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
"""


import collections, random

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.index = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.index[val].add(len(self.nums) - 1)
        return len(self.index[val]) == 1

    def remove(self, val: int) -> bool:
        if self.index[val]:
            idx=self.index[val].pop()
            temp_val=self.nums[-1]
            self.nums[idx]=temp_val
            self.index[temp_val].add(idx)
            self.index[temp_val].discard(len(self.nums)-1)
            self.nums.pop(-1)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)



a = RandomizedCollection()
print(a.insert(2))
print(a.insert(2))
print(a.insert(2))
print(a.insert(2))
print(a.insert(3))
print(a.remove(2))
print(a.remove(2))
print(a.insert(5))


