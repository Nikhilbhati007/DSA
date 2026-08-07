class Solution(object):
    def minMoves(self, target, maxDoubles):
        move=0
        while target!=1:
            if maxDoubles == 0:
                return move + target - 1
            if target%2==0:
                target//=2
                maxDoubles-=1
            else:
                target-=1
            move+=1
        return move

        