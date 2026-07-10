class Solution(object):
    def countPoints(self, rings):
        rods = {}

        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings[i + 1]

            if rod not in rods:
                rods[rod] = set()

            rods[rod].add(color)
        count = 0
        for rod in rods:
            if len(rods[rod]) == 3:
                count += 1
        return count