import collections

class Solution:
    def countStudents(self, students, sandwiches) -> int:
        count = collections.Counter(students)
        n = len(students)

        i = 0
        while i < n and count[sandwiches[i]]:
            count[sandwiches[i]] -= 1
            i += 1

        return n - i


