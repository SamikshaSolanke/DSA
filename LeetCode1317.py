class Solution(object):
    def getNoZeroIntegers(self, n):
        for i in range(1, n):
            temp_str = str(i)
            j = n - i
            temp_str2 = str(j)

            if "0" not in temp_str and "0" not in temp_str2:
                ans = [i, j]
                break

        return ans
