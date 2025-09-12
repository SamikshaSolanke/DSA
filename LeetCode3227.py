class Solution(object):
    def doesAliceWin(self, s):
        vowels = ('a', 'e', 'i', 'o', 'u')
        cnt = 0

        for c in s:
            if c in vowels:
                cnt += 1

        return cnt > 0
