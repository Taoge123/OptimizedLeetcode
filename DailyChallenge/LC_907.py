

class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)
        mod = 10 ** 9 + 7
        stack1, stack2 = [], []
        left, right = [0] * n, [0] * n
        # the number of subarray ending with A[i]
        # left[i], the length of strict bigger numbers on the left of A[i]
        for i in range(n):
            count = 1
            # 新来的num > 前面，说明没有大于的, count = 1 ex: 1234 - 1111
            while stack1 and arr[i] < stack1[-1][0]:
                count += stack1.pop()[1]
            left[i] = count
            stack1.append([arr[i], count])

        # the number of subarray starting with A[i]
        # right[i], the length of bigger numbers on the right of A[i]
        # 新来的num < 后面，说明没有大于的, count = 1    ex: 4321 - 1111
        for i in range(n)[::-1]:
            count = 1
            while stack2 and arr[i] <= stack2[-1][0]:
                count += stack2.pop()[1]
            right[i] = count
            stack2.append([arr[i], count])

        return sum(num * l * r for num, l, r in zip(arr, left, right)) % mod



