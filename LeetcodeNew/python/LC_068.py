
"""
https://leetcode.com/problems/text-justification/discuss/24902/Java-easy-to-understand-broken-into-several-functions
https://leetcode.com/problems/text-justification/discuss/1324217/Python-version-of-the-nicely-broken-Java-code.

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
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

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

            path = []
            path.append(words[index])  # first word

            diff = last - index - 1  # 总共需要几个间隔

            if last == len(words) or diff == 0:  # 不需要多余空格
                for i in range(index + 1, last):
                    path.append(" ")
                    path.append(words[i])
                start = sum(len(i) for i in path)
                for i in range(start, maxWidth):  # last row --> 后面加空格
                    path.append(" ")

            else:
                spaces = (maxWidth - count) // diff  # 每个单词间的空格为多少
                r = (maxWidth - count) % diff
                for i in range(index + 1, last):
                    for k in range(spaces, 0, -1):
                        path.append(" ")

                    if r > 0:  # the empty slots on the left will be assigned more spaces than the slots on the right
                        path.append(" ")
                        r -= 1
                    path.append(" ")
                    path.append(words[i])

            res.append("".join(path))
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


















