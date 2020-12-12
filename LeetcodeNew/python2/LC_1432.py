class Solution:
    def maxDiff(self, num: int) -> int:

        num_string = str(num)

        def change(src: str, dest: str, s: str):

            return int(s.replace(src, dest))

        # -----------------------------------------------------------

        # digit replacement for maximum number

        maxi = num
        for char in num_string:
            if char < '9':
                maxi = change(char, '9', num_string)
                break

        # -----------------------------------------------------------

        # digit replacement for minimum number
        mini = num
        if num_string[0] > '1':
            # leading digit cannot be zero
            mini = change(num_string[0], '1', num_string)

        else:
            for char in num_string[1:]:
                if char > '1':
                    mini = change(char, '0', num_string)
                    break

        return maxi - mini



