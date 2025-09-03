class Solution(object):
    def numberOfPairs(self, points):
        points.sort(key = lambda x : (x[0], -x[1]))
        ans = 0
        n = len(points)

        for i in range(n):
            y1 = points[i][1]
            limit = float('-inf')

            for j in range(i+1, n):
                y2 = points[j][1]
                if y2 <= y1 and y2 > limit:
                    ans += 1
                    limit = y2
                    if y2 == y1:
                        break

        return ans
