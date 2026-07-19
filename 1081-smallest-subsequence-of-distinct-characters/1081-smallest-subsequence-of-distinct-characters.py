class Solution(object):
    def smallestSubsequence(self, s):
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        l = []
        visited = set()

        for i in range(len(s)):
            ch = s[i]

            if ch in visited:
                continue

            while l and l[-1] > ch and last[l[-1]] > i:
                visited.remove(l.pop())

            l.append(ch)
            visited.add(ch)

        ans = ""
        for ch in l:
            ans += ch

        return ans