
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




