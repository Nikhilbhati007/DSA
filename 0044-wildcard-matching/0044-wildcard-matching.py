class Solution(object):
    def isMatch(self, s, p):
        i = 0
        j = 0

        star = -1
        match = 0

        while i < len(s):

            # CHANGE 1: Check boundaries and handle '?'
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1

            # CHANGE 2: Handle '*' and store its position
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # CHANGE 3: Backtrack when a mismatch occurs
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # CHANGE 4: No match and no previous '*'
            else:
                return False

        # CHANGE 5: Skip remaining '*' characters
        while j < len(p) and p[j] == '*':
            j += 1

        # CHANGE 6: Ensure the entire pattern is matched
        return j == len(p)
