class Solution(object):
    def dividePlayers(self, skill):
        n = len(skill)
        total = sum(skill)
        no_team = n // 2

        if total % no_team != 0:
            return -1

        req_sum = total // no_team
        skill.sort()

        chemistry = 0
        left = 0
        right = n - 1

        while left < right:
            if skill[left] + skill[right] != req_sum:
                return -1

            chemistry += skill[left] * skill[right]

            left += 1
            right -= 1

        return chemistry