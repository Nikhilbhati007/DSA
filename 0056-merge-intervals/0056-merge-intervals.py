class Solution:
    def merge(self, intervals):
        intervals.sort()
        
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            last = result[-1]
            current = intervals[i]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                result.append(current)
        return result