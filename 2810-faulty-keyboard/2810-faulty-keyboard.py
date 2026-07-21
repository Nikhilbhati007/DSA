class Solution(object):
    def finalString(self, s):
        ns = ""
        for i in s:
            if i == 'i':
                ns = ns[::-1]
            else:
                ns += i
        return ns