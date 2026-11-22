class Solution(object):
    def checkString(self, s):
        seen_b = False
        
        for c in s:
            if c == 'b':
                seen_b = True
            elif c == 'a' and seen_b:
                return False
        
        return True