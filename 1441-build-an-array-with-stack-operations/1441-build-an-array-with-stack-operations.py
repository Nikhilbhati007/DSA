class Solution(object):
    def buildArray(self, target, n):
        ans = []
        j = 0
        for i in range(1, n + 1):
            if j == len(target):
                break
            if i == target[j]:
                ans.append("Push")
                j += 1
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans