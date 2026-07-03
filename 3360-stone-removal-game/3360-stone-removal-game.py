class Solution(object):
    def canAliceWin(self, n):
        if n<10:
            return False
        flag=True
        for i in range(10,0,-1):
            if n-i>=0:
                n=n-i
            else:
                break
            if i%2==0:
                flag=True
            else:
                flag=False
        if flag:
            return True
        else:
            return False