class Solution(object):
    def exclusiveTime(self, n, logs):
        ans = [0] * n
        stack = []
        prevTime = 0

        for log in logs:
            fid, typ, t = log.split(":")
            fid = int(fid)
            t = int(t)

            if typ == "start":
                if stack:
                    ans[stack[-1]] += t - prevTime
                stack.append(fid)
                prevTime = t

            else:
                ans[stack.pop()] += t - prevTime + 1
                prevTime = t + 1

        return ans