"""
Design a Phone Directory which supports the following operations:

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
Example:

// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);
"""

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.available = set(range(maxNumbers))


    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        return self.available.pop() if self.available else -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number in self.available

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        self.available.add(number)

class PhoneDirectory2:

    def __init__(self, maxNumbers: int):
        self.next = 0
        self.max = maxNumbers
        self.released = set()


    def get(self) -> int:
        if self.next < self.max:
            self.next += 1
            return self.next - 1
        return self.released.pop() if self.released else -1

    def check(self, number: int) -> bool:
        return (number in self.released) or self.next <= number < self.max

    def release(self, number: int) -> None:
        if number < self.next:
            self.released.add(number)



# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)!
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
