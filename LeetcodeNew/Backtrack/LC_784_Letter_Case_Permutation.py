
class Solution:
    def letterCasePermutation(self, S):
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i + j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i + ch for i in res]
        return res

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = list(S)
        solutions = ['']
        while S:
            last = S.pop()
            if last.isalpha():
                solutions = [last.lower() + x for x in solutions] + [last.upper() + x for x in solutions]
            else:
                solutions = [last + x for x in solutions]
        return solutions


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return [""]
        index = -1
        for i in range(len(S)):
            if S[i].isalpha():
                index = i
                break
        if index == -1:
            return [S]
        else:
            tmp = self.letterCasePermutation(S[index+1:])
            res = []
            for s in tmp:
                res.append(S[:index]+S[index].lower()+s)
                res.append(S[:index]+S[index].upper()+s)
            return res


class Solution4:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        def helper(s, p):
            if s == "":
                res.append(p)
                return
            if s[0].isdigit():
                helper(s[1:], p+s[0])
            else:
                helper(s[1:], p+s[0].upper())
                helper(s[1:], p+s[0].lower())
        helper(S, "")
        return res


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = []

        def recursion(i, str):
            if i == len(S):
                result.append(str)
                return

            if S[i].isdigit():
                recursion(i + 1, str + S[i])
            else:
                recursion(i + 1, str + S[i].lower())
                recursion(i + 1, str + S[i].upper())

        recursion(0, "")
        return result


"""
Lets look at the recursive calls, we will track character 
and string formed due to that character:

Input = "1a2"
iteration 1: char = "1", string="1"
	iteration 2: char = "a", string="1a"
		iteration 3: char = "2", string="1a2" ##########Add to list
	iteration 2: char = "A", string="1A"
		iteration 3: char = "2", string="1A2" ##########Add to list
return none
"""


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        l = []
        def permute(s, l, ns):
            """
            Returns: None
            Input:
            s : String formed till now
            l: list of all accepted strings
            ns: Original String - characters seen till now
	        """
            if ns =="":
                l.append(s)
            else:
                char = ns[0]
                ns = ns[1:]
                if char.isdigit():
                    permute(s+char, l, ns)
                else:
                    permute(s+char.lower(), l ,ns)
                    permute(s+char.upper(), l, ns)
        permute("", l, S)
        return (l)



class Solution5:
    def letterCasePermutation(self, S):
        def changeCase(ch):
            return ch.upper() if ch.islower() else ch.lower()

        def backtrack(res, S, start):
            res.append(S)
            for i in range(start, len(S)):
                if S[i].isnumeric():
                    continue
                S = S[:i] + changeCase(S[i]) + S[i + 1:]
                backtrack(res, S, i + 1)
                S = S[:i] + changeCase(S[i]) + S[i + 1:]

        res = []
        backtrack(res, S, 0)
        return res




