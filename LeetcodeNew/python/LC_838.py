
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = "L" + dominoes + "R"
        res = []
        i = 0
        for j in range(1, len(dominoes)):
            if dominoes[j] == ".":
                continue
            count = j - i - 1
            if i > 0:
                res.append(dominoes[i])
            if dominoes[i] == dominoes[j]:
                for k in range(count):
                    res.append(dominoes[i])

            elif dominoes[i] == "L" and dominoes[j] == "R":
                for k in range(count):
                    res.append(".")

            else:
                for k in range(count // 2):
                    res.append("R")
                if count % 2 == 1:
                    res.append(".")
                for k in range(count // 2):
                    res.append("L")
            i = j

        return "".join(res)



