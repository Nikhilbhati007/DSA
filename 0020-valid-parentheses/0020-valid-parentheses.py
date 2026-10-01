class Solution(object):
    def isValid(self, s):
        stk = []
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stk.append(i)
            else:
                if not stk:
                    return False
                top=stk.pop()
                if i==')' and top != '(':
                    return False
                if i== '}' and top != '{':
                    return False
                if i== ']' and top != '[':
                    return False
        return not stk