class Solution(object):
    def destCity(self, paths):
        n=len(paths)
        src=[]
        des=[]
        for i in range(n):
            src.append(paths[i][0])
            des.append(paths[i][1])
        for i in des:
            if i not in src:
                return i
