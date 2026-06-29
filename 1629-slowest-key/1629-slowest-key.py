class Solution(object):
    def slowestKey(self, rt, kp):
        n=len(rt)
        l=[0]*n
        l[0]=rt[0]
        for i in range(1,n):
            l[i]=rt[i]-rt[i-1]
        res=[]
        maxele=max(l)
        for i in range(n):
            if l[i]==maxele:
                res.append(i)
        ans=''
        for j in res:
            if kp[j]>ans:
                ans=kp[j]
        return ans


        