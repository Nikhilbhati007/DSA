class Solution(object):
    def checkStraightLine(self, coord):
        x1, y1 = coord[0]
        x2, y2 = coord[1]

        for x, y in coord:
            if (y - y1) * (x2 - x1) != (x - x1) * (y2 - y1):
                return False

        return True