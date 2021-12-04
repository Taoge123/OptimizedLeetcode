
"""
https://www.youtube.com/watch?v=5tlOmRvNCfw&feature=youtu.be
https://www.youtube.com/watch?v=5Kr1PWAgEx8&t=413s

for object in objects:
    for capacity ...:
        dp[capacity] = dp[capacity - c[i]] + val[i]
        dp[capacity+c[i]] += dp[capacity] + val[i]
skillset = [01000, 01110, 00000, 11111]

for people[i]:
    for skillset:
        new_skillset = skillset + skills[i]
        dp[new_skillset] = min(new_skillset, dp[skillset] + 1)

dp[skill_set] is a sufficient team to cover the skill_set.
For each people,
update his_skill with all current combinations of skill_set in dp.

"""

import collections
import functools


"""
[ - 001111 - 11011
2
3
4
5]

[00101, 0100101, 0101001, 01001]

[00111][11011][]]


"""


class SolutionTony2:
    def smallestSufficientTeam(self, req_skills, people):
        # convert req_skills to bit mask --> record the position of each skill
        req = {}
        for i, skill in enumerate(req_skills):
            req[skill] = i

        # convert skills of each people to bit mask, save it in a list
        m, n = len(req_skills), len(people)
        people2skills = [0] * n

        for i, p in enumerate(people):
            for skill in p:
                if skill in req:
                    people2skills[i] = people2skills[i] | (1 << req[skill])

        # convert results that fullfill all req_skills to bit mask
        fullmask = (1 << m) - 1

        @functools.lru_cache(None)
        def dfs(mask):
            # base case
            if mask == fullmask:
                return []
            # for loop the list to see if nextskill(with this person's skills) has new skills, if has --> add this person
            # res => a list of people
            res = [0] * (len(people2skills) + 1)
            for i, skill_mask in enumerate(people2skills):
                nxt_mask = skill_mask | mask
                if nxt_mask != mask:
                    # 比人数少
                    # if len(res) > len(dfs(nxt_mask)):
                    #     res = dfs(nxt_mask) + [i]
                    res = min(res, dfs(nxt_mask) + [i], key=len)
            return res
        return dfs(0)



class SolutionTony:
    def smallestSufficientTeam(self, req_skills, people):

        m, n = len(req_skills), len(people)
        table = {v: i for i, v in enumerate(req_skills)}
        p2s = [0] * n

        for i, p in enumerate(people):
            for skill in p:
                if skill in table:
                    p2s[i] |= (1 << table[skill])

        full_mask = (1 << m) - 1
        @functools.lru_cache(None)
        def dfs(i, mask):
            if i >= n:
                if mask == full_mask:
                    return []
                else:
                    return [0] * (n + 1)
            res = [0] * (n + 1)
            take = dfs(i+1, mask | p2s[i]) + [i]
            no_take = dfs(i+1, mask)
            res = min(res, take, no_take, key=len)
            return res

        return dfs(0, 0)



class Solution:
    def smallestSufficientTeam(self, req_skills, people):

        m, n = len(req_skills), len(people)

        table = {v: i for i, v in enumerate(req_skills)}

        people2skills = [0] * n

        for i, p in enumerate(people):
            for skill in p:
                if skill in table:
                    people2skills[i] |= (1 << table[skill])

        full_mask = (1 << m) - 1

        @functools.lru_cache(None)
        def dfs(mask):
            if mask == full_mask:
                return []

            res = [0] * (n + 1)
            for i, skill_mask in enumerate(people2skills):
                nxt_mask = mask | skill_mask
                if nxt_mask != mask:
                    if len(dfs(nxt_mask)) < len(res):
                        res = [i] + dfs(nxt_mask)
                    else:
                        return res
                    # res = min(res, [i] + dfs(nxt_mask), key = len)
            return res

        return dfs(0)




class Solution:
    def smallestSufficientTeam(self, target, people):
        n, m = len(target), len(people)
        #convert skills into numbers
        skill2num = {val: i for i, val in enumerate(target)}
        dp = {0: []}
        for i, skills in enumerate(people):
            his_skill = 0
            # convert all this person's skills into numbers then into bit masks
            for skill in skills:
                if skill in skill2num:
                    his_skill |= 1 << skill2num[skill]
            # if he has no skills
            if his_skill == 0:
                continue

            if his_skill in dp and len(dp[his_skill]) == 1:
                continue

            for skill, team in list(dp.items()):
                newSkill = skill | his_skill
                if newSkill == skill:
                    continue
                if newSkill not in dp or len(dp[newSkill]) > len(team) + 1:
                    dp[newSkill] = team + [i]
        return dp[(1 << n) - 1]




class SolutionBFS:
    def smallestSufficientTeam(self, req_skills, people):
        n = len(req_skills)
        N = (1 << n) - 1
        table = {}
        # map skill to binary
        for i, skill in enumerate(req_skills):
            table[skill] = 1 << i

        queue = collections.deque()
        queue.append([0, []])
        visited = set()
        while queue:
            nextQueue = collections.deque()
            size = len(queue)
            for _ in range(size):
                state, path = queue.popleft()
                for i in range(len(people)):
                    nextState = state
                    for skill in people[i]:
                        nextState |= table[skill]

                    if nextState == N:
                        return path + [i]

                    if nextState not in visited:
                        visited.add(nextState)
                        nextQueue.append([nextState, path + [i]])
            queue = nextQueue
        return -1


class SolutionTonyBFS:
    def smallestSufficientTeam(self, req_skills, people):
        n = len(req_skills)
        N = (1 << n) - 1
        table = {}
        # map skill to binary
        for i, skill in enumerate(req_skills):
            table[skill] = 1 << i

        queue = collections.deque()
        queue.append([0, []])
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                state, path = queue.popleft()

                if state == N:
                    return path

                for i in range(len(people)):
                    nextState = state
                    for skill in people[i]:
                        nextState |= table[skill]

                    if nextState not in visited:
                        visited.add(nextState)
                        queue.append([nextState, path + [i]])
        return -1


