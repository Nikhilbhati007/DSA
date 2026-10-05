class Solution(object):
    def scoreOfParentheses(self, s):
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                val = stack.pop()

                if val == 0:
                    val = 1
                else:
                    val = 2 * val

                stack[-1] += val

        return stack[0]