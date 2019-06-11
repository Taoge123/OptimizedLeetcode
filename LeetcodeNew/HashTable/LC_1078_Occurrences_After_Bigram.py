
"""
Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.



Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]


Note:

1 <= text.length <= 1000
text consists of space separated words, where each word consists of lowercase English letters.
1 <= first.length, second.length <= 10
first and second consist of lowercase English letters.
"""
class Solution1:
    def findOcurrences(self, text, first, second):
        words = text.split()
        res = []
        if len(words) < 3:
            return res
        for i in range(len(words) - 2):
            if words[i] == first and words[i+1] == second:
                res.append(words[i+2])
        return res


"""
2 steps solution:

split the sentence into words
match the words with first and second, make sure second is not the last word of the sentence
"""
class Solution:
    def findOcurrences(self, text, first, second):
        l= list(text.strip().split())
        a=[]
        for i in range(0,len(l)-1):
            if l[i]==first and l[i+1]==second and i+2 < len(l):
                a.append(l[i+2])
        return(a)



