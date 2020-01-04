"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".


Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.


Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.


Note:

All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
"""



class Solution:
    def compress(self, chars):

        left = 0 # start replacing from left
        i = 0 # iterator
        while i < len(chars): #iterate through array
            char = chars[i] # current character
            count = 1 # current characters count
            while i+1 < len(chars) and char == chars[i+1]: # the last char
                count += 1 # increase current chars count
                i += 1  # increment pointer/iterator
            chars[left] = char # replace the character at poisition with current char
            if count > 1: # only replace if current char is seen more than once
                chars[left+1:left + 1 + len(str(count))] = str(count) # left to there = count = repeat count of current char
                left += len(str(count)) # if count > 10, replace it as "1", "0" so "there" value changes
            left += 1 # if no repetitions, move on to the next char
            i += 1 # incrementing the iterator
        return left



class Solution2:
    def compress(self, chars):

        pre = chars[0]
        count = 0
        pos = 0
        for char in chars:
            if pre == char:
                count += 1
            else:
                chars[pos] = pre
                pos += 1
                if count > 1:
                    count = str(count)
                    for i in range(len(count)):
                        chars[pos] = count[i]
                        pos += 1
                count = 1
                pre = char
        chars[pos] = pre
        pos += 1
        if count > 1:
            count = str(count)
            for i in range(len(count)):
                chars[pos] = count[i]
                pos += 1
        return pos



chars = ["a","a","b","b","c","c","c"]
a = Solution()
print(a.compress(chars))





