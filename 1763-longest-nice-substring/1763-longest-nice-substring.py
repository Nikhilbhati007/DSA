class Solution:
    def longestNiceSubstring(self, s):
        def solve(s):
            if len(s) < 2:
                return ""
            chars = set(s)
            for i in range(len(s)):
                ch = s[i]
                if ch.swapcase() not in chars:
                    left = solve(s[:i])
                    right = solve(s[i + 1:])

                    if len(left) >= len(right):
                        return left
                    else:
                        return right
            return s

        return solve(s)