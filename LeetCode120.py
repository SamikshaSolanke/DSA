class Solution(object):
    def minimumTotal(self, triangle):
        # ans = 0
        # if len(triangle) == 1:
        #     return triangle[0][0]
        # for level in triangle:
        #     ans += min(level)
        # return ans

        n = len(triangle)
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]
