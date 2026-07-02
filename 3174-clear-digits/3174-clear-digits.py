class Solution(object):
    def clearDigits(self, s):
        stack = []

        for ch in s:
            if ch.isdigit():
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)