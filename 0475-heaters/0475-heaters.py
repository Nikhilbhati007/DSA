class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()

        j = 0
        ans = 0

        for house in houses:
            while (j + 1 < len(heaters) and
                   abs(heaters[j + 1] - house) <= abs(heaters[j] - house)):
                j += 1

            ans = max(ans, abs(heaters[j] - house))

        return ans