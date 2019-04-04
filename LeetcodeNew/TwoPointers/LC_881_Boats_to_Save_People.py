
"""
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
(It is guaranteed each person can be carried by a boat.)

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
Note:

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000
"""

#Greedy
class Solution1:
    def numRescueBoats(self, people, limit):
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans

"""
Sort people.
For the current heaviest person, we try to let him go with the lightest person.
As all people need to get on the boat.
If the sum of weight is over the limit, we have to let the heaviest go alone.
No one can take the same boat with him.

At the end of for loop, it may happend that i = j.
But it won't change the result so don't worry about it.

Time Complexity:
O(NlogN)
"""

class SolutionLee:
    def numRescueBoats(self, people, limit):
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
        return i


"""
Some food for thoughts: Why don't we try to match highest people[r] with possibly maximum people[l] 
instead of smallest people[l]? All these greedy solutions seem fishy, intiutively.
"""
class Solution2:
    def numRescueBoats(self, people, limit):
        people.sort()
        l, n = 0, len(people)
        for r in range(n - 1, -1, -1):
            if people[l] + people[r] <= limit:
                l += 1
            if l >= r: return n - r





