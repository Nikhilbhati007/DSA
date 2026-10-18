class Solution(object):
    def appealSum(self, s):
        n = len(s)
        ans = 0
        last = {}  # CHANGE: Store the last occurrence of each character
        curr = 0   # CHANGE: Track the appeal of substrings ending at the current index

        for i in range(n):
            ch = s[i]

            # CHANGE: Add the contribution of the current character
            curr += i - last.get(ch, -1)

            # CHANGE: Update the last occurrence
            last[ch] = i

            # CHANGE: Add the appeal of all substrings ending at index i
            ans += curr

        return ans