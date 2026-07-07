class Solution(object):
    def numberOfMatches(self, n):
        match = 0
        temp = n

        while temp > 1:
            if temp % 2 == 0:
                match += temp // 2
                temp //= 2
            else:
                match += (temp - 1) // 2
                temp = (temp - 1) // 2 + 1

        return match