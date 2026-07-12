class Solution(object):
    def restoreString(self, s, indices):
        n=len(s)
        freq={}
        for i in range(n):
            freq[indices[i]]=s[i]
        indices.sort()
        out=""
        for i in indices:
            out+=freq[i]
        return out
            