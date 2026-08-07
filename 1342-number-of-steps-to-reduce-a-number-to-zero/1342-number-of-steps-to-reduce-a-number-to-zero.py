class Solution(object):
    def numberOfSteps(self, num):
        move=0
        while num!=0:
            if num%2==0:
                num=num//2
            else:
                num-=1
            move+=1
        return move