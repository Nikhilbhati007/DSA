class Solution(object):
    def findRestaurant(self, list1, list2):
        n=len(list1)
        m=len(list2)
        freq={}
        for i in range(n):
            freq[list1[i]]=i
        min_idx=float('inf')
        out = []

        for j in range(m):
            if list2[j] in freq:
                idx_sum = freq[list2[j]] + j

                if idx_sum < min_idx:
                    min_idx = idx_sum
                    out = [list2[j]]

                elif idx_sum == min_idx:
                    out.append(list2[j])

        return out
            