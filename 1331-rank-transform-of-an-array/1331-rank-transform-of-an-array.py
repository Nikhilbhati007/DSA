class Solution(object):
    def arrayRankTransform(self, arr):
        n = len(arr)
        ans = [0] * n

        # Store original array
        original = arr[:]

        # Sort a copy
        arr.sort()

        rank = 1
        freq = {}

        # Assign ranks to unique elements
        for i in range(n):
            if arr[i] not in freq:
                freq[arr[i]] = rank
                rank += 1

        # Fill answer according to original order
        for i in range(n):
            ans[i] = freq[original[i]]

        return ans