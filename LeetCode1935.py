class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        words = text.split()
        count = 0

        for word in words:
            for c in word:
                if c in brokenLetters:
                    count += 1
                    break

        return len(words) - count
