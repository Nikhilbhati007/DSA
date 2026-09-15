class Solution:
    def guessNumber(self, n):
        l = 1
        h = n

        while l <= h:
            mid = (l + h) // 2

            result = guess(mid)

            if result == 0:
                return mid

            elif result == -1:
                h = mid - 1

            else:
                l = mid + 1