class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-", "").upper()
        n = len(s)

        ans = ""

        first = n % k

        if first:
            ans += s[:first]

        i = first

        while i < n:
            if ans:
                ans += "-"
            ans += s[i:i+k]
            i += k

        return ans