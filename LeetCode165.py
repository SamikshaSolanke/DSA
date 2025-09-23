class Solution(object):
    def compareVersion(self, version1, version2):
        v1_str = version1.split('.')
        v1 = [int(s) for s in v1_str]
        v2_str = version2.split('.')
        v2 = [int(s) for s in v2_str]

        max_len = max(len(v1), len(v2))\

        for i in range(max_len):
            c1 = v1[i] if i < len(v1) else 0
            c2 = v2[i] if i < len(v2) else 0

            if c1 > c2:
                return 1
            elif c1 < c2:
                return -1

        return 0
