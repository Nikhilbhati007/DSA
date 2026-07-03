class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()
            x = stones[-1]
            y = stones[-2]

            stones.remove(x)
            stones.remove(y)

            if x != y:
                stones.append(x - y)

        return stones[0] if stones else 0