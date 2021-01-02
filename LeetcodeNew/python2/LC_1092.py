"""
https://leetcode.com/problems/shortest-common-supersequence/discuss/617594/Python-two-solutions%3A-from-slow-DP-to-fast-DP

"""

import functools

class SolutionDFS1:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        @functools.lru_cache(None)
        def dfs(i, j):
            print(i, j)
            if i == len(str1):
                return str2[j:]
            elif j == len(str2):
                return str1[i:]

            if str1[i] == str2[j]:
                res = str1[i] + dfs(i + 1, j + 1)
            else:
                ps1 = str1[i] + dfs(i + 1, j)
                ps2 = str2[j] + dfs(i, j + 1)
                if len(ps1) < len(ps2):
                    res = ps1
                else:
                    res = ps2

            return res

        return dfs(0, 0)


class SolutionDFS2:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memo = {}
        return self.dfs(str1, str2, 0, 0, memo)

    def dfs(self, str1, str2, i, j, memo):
        print(i, j)
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(str1):
            return str2[j:]
        elif j == len(str2):
            return str1[i:]

        if str1[i] == str2[j]:
            res = str1[i] + self.dfs(str1, str2, i + 1, j + 1, memo)
        else:
            ps1 = str1[i] + self.dfs(str1, str2, i + 1, j, memo)
            ps2 = str2[j] + self.dfs(str1, str2, i, j + 1, memo)
            if len(ps1) < len(ps2):
                res = ps1
            else:
                res = ps2
        memo[(i, j)] = res
        return memo[(i, j)]



class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0 for i in range( n +1)] for j in range( m +1)]

        for i in range(1, m+ 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j = m, n
        res = []
        while i > 0 or j > 0:
            if i == 0:
                res.append(str2[j - 1])
                j -= 1
            elif j == 0:
                res.append(str1[i - 1])
                i -= 1
            elif str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i][j - 1] == dp[i][j]:
                res.append(str2[j - 1])
                j -= 1
            elif dp[i - 1][j] == dp[i][j]:
                res.append(str1[i - 1])
                i -= 1

        return "".join(res[::-1])


str1 = "atdznrqfwlfbcqkezrltzyeqvqemikzgghxkzenhtapwrmrovwtpzzsyiwongllqmvptwammerobtgmkpowndejvbuwbporfyroknrjoekdgqqlgzxiisweeegxajqlradgcciavbpgqjzwtdetmtallzyukdztoxysggrqkliixnagwzmassthjecvfzmyonglocmvjnxkcwqqvgrzpsswnigjthtkuawirecfuzrbifgwolpnhcapzxwmfhvpfmqapdxgmddsdlhteugqoyepbztspgojbrmpjmwmhnldunskpvwprzrudbmtwdvgyghgprqcdgqjjbyfsujnnssfqvjhnvcotynidziswpzhkdszbblustoxwtlhkowpatbypvkmajumsxqqunlxxvfezayrolwezfzfyzmmneepwshpemynwzyunsxgjflnqmfghsvwpknqhclhrlmnrljwabwpxomwhuhffpfinhnairblcayygghzqmotwrywqayvvgohmujneqlzurxcpnwdipldofyvfdurbsoxdurlofkqnrjomszjimrxbqzyazakkizojwkuzcacnbdifesoiesmkbyffcxhqgqyhwyubtsrqarqagogrnaxuzyggknksrfdrmnoxrctntngdxxechxrsbyhtlbmzgmcqopyixdomhnmvnsafphpkdgndcscbwyhueytaeodlhlzczmpqqmnilliydwtxtpedbncvsqauopbvygqdtcwehffagxmyoalogetacehnbfxlqhklvxfzmrjqofaesvuzfczeuqegwpcmahhpzodsmpvrvkzxxtsdsxwixiraphjlqawxinlwfspdlscdswtgjpoiixbvmpzilxrnpdvigpccnngxmlzoentslzyjjpkxemyiemoluhqifyonbnizcjrlmuylezdkkztcphlmwhnkdguhelqzjgvjtrzofmtpuhifoqnokonhqtzxmimp"
str2 = "xjtuwbmvsdeogmnzorndhmjoqnqjnhmfueifqwleggctttilmfokpgotfykyzdhfafiervrsyuiseumzmymtvsdsowmovagekhevyqhifwevpepgmyhnagjtsciaecswebcuvxoavfgejqrxuvnhvkmolclecqsnsrjmxyokbkesaugbydfsupuqanetgunlqmundxvduqmzidatemaqmzzzfjpgmhyoktbdgpgbmjkhmfjtsxjqbfspedhzrxavhngtnuykpapwluameeqlutkyzyeffmqdsjyklmrxtioawcrvmsthbebdqqrpphncthosljfaeidboyekxezqtzlizqcvvxehrcskstshupglzgmbretpyehtavxegmbtznhpbczdjlzibnouxlxkeiedzoohoxhnhzqqaxdwetyudhyqvdhrggrszqeqkqqnunxqyyagyoptfkolieayokryidtctemtesuhbzczzvhlbbhnufjjocporuzuevofbuevuxhgexmckifntngaohfwqdakyobcooubdvypxjjxeugzdmapyamuwqtnqspsznyszhwqdqjxsmhdlkwkvlkdbjngvdmhvbllqqlcemkqxxdlldcfthjdqkyjrrjqqqpnmmelrwhtyugieuppqqtwychtpjmloxsckhzyitomjzypisxzztdwxhddvtvpleqdwamfnhhkszsfgfcdvakyqmmusdvihobdktesudmgmuaoovskvcapucntotdqxkrovzrtrrfvoczkfexwxujizcfiqflpbuuoyfuoovypstrtrxjuuecpjimbutnvqtiqvesaxrvzyxcwslttrgknbdcvvtkfqfzwudspeposxrfkkeqmdvlpazzjnywxjyaquirqpinaennweuobqvxnomuejansapnsrqivcateqngychblywxtdwntancarldwnloqyywrxrganyehkglbdeyshpodpmdchbcc"


a = SolutionDFS2()
print(a.shortestCommonSupersequence(str1, str2))


