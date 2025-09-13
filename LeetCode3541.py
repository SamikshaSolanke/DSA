class Solution(object):
    def maxFreqSum(self, s):
        track_v = {}
        track_c = {}

        for c in s:
            if c in ('a', 'e', 'i', 'o', 'u'):
                if c not in track_v:
                    track_v[c] = 1
                else:
                    track_v[c] += 1
            else:
                if c not in track_c:
                    track_c[c] = 1
                else:
                    track_c[c] += 1

        max_vowel = max(track_v.values()) if track_v else 0
        max_con = max(track_c.values()) if track_c else 0

        return max_vowel + max_con
