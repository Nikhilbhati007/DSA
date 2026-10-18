class Solution(object):
    def uniqueLetterString(self, s):
        n = len(s)

        # CHANGE: Store the previous two occurrence positions of each character
        prev = {}
        ans = 0

        for i in range(n):
            ch = s[i]

            # CHANGE: Get the previous two occurrences of the character
            p1, p2 = prev.get(ch, (-1, -1))

            # CHANGE: Calculate this character's contribution
            ans += (i - p1) * (p1 - p2)

            # CHANGE: Update the last two occurrence positions
            prev[ch] = (i, p1)

        # CHANGE: Count contributions from each character's final occurrence
        for ch, (p1, p2) in prev.items():
            ans += (n - p1) * (p1 - p2)

        return ans