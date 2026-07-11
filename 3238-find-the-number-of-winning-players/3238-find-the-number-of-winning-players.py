class Solution(object):
    def winningPlayerCount(self, n, pick):
        freq = {}

        # Count occurrences of each (player, color)
        for player, color in pick:
            freq[(player, color)] = freq.get((player, color), 0) + 1

        winners = set()

        # Check if any color count is greater than player index
        for (player, color), cnt in freq.items():
            if cnt > player:
                winners.add(player)

        return len(winners)