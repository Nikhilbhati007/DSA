class Solution(object):
    def isItPossible(self, word1, word2):
        cnt1 = {}
        cnt2 = {}

        # Build frequency map for word1
        for ch in word1:
            cnt1[ch] = cnt1.get(ch, 0) + 1

        # Build frequency map for word2
        for ch in word2:
            cnt2[ch] = cnt2.get(ch, 0) + 1

        for c1 in list(cnt1.keys()):
            for c2 in list(cnt2.keys()):

                if c1 == c2:
                    if len(cnt1) == len(cnt2):
                        return True
                    continue

                # Perform swap
                cnt1[c1] -= 1
                if cnt1[c1] == 0:
                    del cnt1[c1]

                cnt2[c2] -= 1
                if cnt2[c2] == 0:
                    del cnt2[c2]

                cnt1[c2] = cnt1.get(c2, 0) + 1
                cnt2[c1] = cnt2.get(c1, 0) + 1

                if len(cnt1) == len(cnt2):
                    return True

                # Undo swap
                cnt1[c2] -= 1
                if cnt1[c2] == 0:
                    del cnt1[c2]

                cnt2[c1] -= 1
                if cnt2[c1] == 0:
                    del cnt2[c1]

                cnt1[c1] = cnt1.get(c1, 0) + 1
                cnt2[c2] = cnt2.get(c2, 0) + 1

        return False