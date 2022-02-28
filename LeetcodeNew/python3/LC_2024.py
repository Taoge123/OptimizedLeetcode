
import collections


class SolutionRika1:
    def countMaxOrSubsets(self, nums):
        # pick or not pick

        # step1: get max possible bitwise OR
        maxx = 0
        for num in nums:
            maxx = maxx | num

        # step2: get combination from nums and make the bitwise OR equal to max bit
        self.count = 0
        self.dfs(nums, maxx, 0, 0)
        return self.count

    def dfs(self, nums, target, pos, mask):
        if pos == len(nums):
            if mask == target:
                self.count += 1
            return

        self.dfs(nums, target, pos + 1, mask | nums[pos])
        self.dfs(nums, target, pos + 1, mask)



class SolutionRika2:
    def countMaxOrSubsets(self, nums):
        # similar to combination summ ---> combination OR == target
        maxx = 0
        for i in nums:
            maxx = maxx | i

        self.res = 0
        self.dfs(nums, maxx, 0, 0)
        return self.res

    def dfs(self, nums, maxx, mask, pos):
        if mask > maxx:
            return

        if mask == maxx:
            self.res += 1

        for i in range(pos, len(nums)):
            self.dfs(nums, maxx, mask | nums[i], i + 1)



class SolutionTony1:
    def countMaxOrSubsets(self, nums):

        table = collections.defaultdict(list)
        n = len(nums)

        def dfs(i, count, path, table):
            if i >= n:
                table[count].append(path[:])
                return

            temp = count
            new_count = count | nums[i]
            path.append(nums[i])
            dfs( i +1, new_count, path, table)
            count = temp
            path.pop()
            dfs( i +1, count, path, table)


        dfs(0, 0, [], table)
        res = 0
        for k, v in table.items():
            if len(v) > res:
                res = len(v)
        return res



class SolutionTony2:
    def countMaxOrSubsets(self, nums):

        table = collections.defaultdict(int)
        n = len(nums)

        def dfs(i, count, table):
            if i >= n:
                table[count] += 1
                return

            temp = count
            new_count = count | nums[i]

            dfs(i + 1, new_count, table)

            count = temp

            dfs(i + 1, count, table)

        dfs(0, 0, table)
        res = 0
        for k, v in table.items():
            if res < v:
                res = v

        return res







