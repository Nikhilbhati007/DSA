class Solution(object):
    def oddString(self, words):
        def diff(word):
            return [ord(word[i + 1]) - ord(word[i])
                    for i in range(len(word) - 1)]

        d1 = diff(words[0])
        d2 = diff(words[1])
        d3 = diff(words[2])

        if d1 == d2:
            common = d1
        elif d1 == d3:
            return words[1]
        else:
            return words[0]

        for word in words:
            if diff(word) != common:
                return word