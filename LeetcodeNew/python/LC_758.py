
class Solution:
    def boldWords(self, words, S: str) -> str:
        n = len(S)
        isBold = [False] * n

        for word in words:
            index = S.find(word)

            while index != -1:
                for i in range(index, index + len(word)):
                    isBold[i] = True
                index = S.find(word, index + 1)
        res = []
        if isBold[0]:
            res.append("<b>")

        for i in range(len(isBold)):
            res.append(S[i])
            if i == len(isBold) - 1:
                if isBold[i]:
                    res.append("</b>")
                break
            if isBold[i] and not isBold[i + 1]:
                res.append("</b>")
            if not isBold[i] and isBold[i + 1]:
                res.append("<b>")

        return "".join(res)




