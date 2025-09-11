class Solution(object):
    def sortVowels(self, s):
        track = []
        vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')

        for c in s:
            if c in vowels:
                track.append(c)

        track.sort()

        s = list(s)

        for i in range(len(s)):
            if s[i] in vowels:
                c = track.pop(0)
                s[i] = c

        return "".join(s)
