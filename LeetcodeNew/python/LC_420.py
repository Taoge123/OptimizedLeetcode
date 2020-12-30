"""
https://leetcode.com/problems/strong-password-checker/discuss/788493/Clear-and-short-Python-explanation-%2B-commented-code
"""


class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        """
        Missing/length reqs are easy by themselves.
        For repeating sequences, we need to find number of ADDITIONAL replaces.
        We can insert (ideal for len(s) < 6) to disrupt missing (+ reduce one replace).
        We can delete (ideal for len(s) > 20) 1-3 characters to reduce one replace.
        We can replace as last resort.

        Excellent explainer: https://leetcode.com/problems/strong-password-checker/discuss/478197/Explanation-of-How-To-Approach-This-Problem
        """
        # Requirement 2
        req_missing = 3
        req_missing -= any(c.islower() for c in s)
        req_missing -= any(c.isupper() for c in s)
        req_missing -= any(c.isdigit() for c in s)

        # Requirement 3
        repeat_replace = 0
        mod0 = mod1 = 0
        i = 2
        while i < len(s):
            if s[i] == s[ i -1] == s[ i -2]:    # start of repeating sequence
                curr = 2  # track length of current repeating sequence
                while i < len(s) and s[ i -1] == s[i]:
                    curr += 1
                    i += 1
                repeat_replace += curr // 3 # {# of raw replacements needed}
                # We can reduce replaces, by using strategic deletes
                mod0 += int(cur r % 3= =0)      # mod0 -> mod2 costs 1 delete to save one replace
                mod1 += int(cur r % 3= =1)      # mod1 -> mod2 costs 2 deletes to save one replace
                # mod2 -> mod2 costs 3 deletes to save one replace
            else:
                i += 1

        # Requirement 1
        res = max(0, len(s ) -20)                     # {# deletes} + {# inserts} + {# replaces}
        if len(s) > 20:
            deletes = len(s ) -20                     # need to delete, then replace
            repeat_replace -= min(deletes, mod0)    # delete mod0 -> mod2 == save one replace
            deletes = max(0, deletes - mod0)
            repeat_replace -= min(deletes, mod 1 *2 )/ /2   # delete mod1 -> mod2 == save one replace
            deletes = max(0, deletes - mod 1 *2)
            repeat_replace -= deletes // 3                  # use remaining deletes to mod2 -> mod2
        res += max( 6 -len(s), req_missing, repeat_replace)   # can insert or replace with missing chars, so they're interchangeable here

        return res

