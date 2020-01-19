
"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""


class Solution:
    def fullJustify(self, words, maxWidth: int):

        res = []
        index = 0

        while index < len(words):
            count = len(words[index])
            last = index + 1
            while last < len(words):
                if len(words[last]) + count + 1 > maxWidth:
                    break
                count += 1 + len(words[last])
                last += 1

            builder = []
            builder.append(words[index])
            diff = last - index - 1
            if last == len(words) or diff == 0:
                for i in range(index + 1, last):
                    builder.append(" ")
                    builder.append(words[i])
                start = sum(len(i) for i in builder)
                for i in range(start, maxWidth):
                    builder.append(" ")

            else:
                spaces = (maxWidth - count) // diff
                r = (maxWidth - count) % diff
                for i in range(index + 1, last):
                    for k in range(spaces, 0, -1):
                        builder.append(" ")

                    if r > 0:
                        builder.append(" ")
                        r -= 1
                    builder.append(" ")
                    builder.append(words[i])

            res.append("".join(builder))
            index = last

        return res


class Solution2:
    def fullJustify(self, words, maxWidth):
        res, cur = [], []
        numOfLetter = 0
        for word in words:
            if numOfLetter + len(word) + len(cur) > maxWidth:
                for i in range(maxWidth - numOfLetter):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, numOfLetter = [], 0
            cur += [word]
            numOfLetter += len(word)
        return res + [' '.join(cur).ljust(maxWidth)]



words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

a = Solution()
print(a.fullJustify(words, maxWidth))


















