class Solution(object):
    def smallestPalindrome(self, s):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        left = []
        mid = ""

        for i in range(26):
            left.extend(chr(i + ord('a')) for _ in range(freq[i] // 2))
            if freq[i] % 2:
                mid = chr(i + ord('a'))

        left = "".join(left)
        return left + mid + left[::-1]
        