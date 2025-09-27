class Solution(object):
    def largestTriangleArea(self, points):
        max_area = 0
        n = len(points)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    d1 = points[i][0] * (points[j][1] - points[k][1])
                    d2 = points[j][0] * (points[k][1] - points[i][1])
                    d3 = points[k][0] * (points[i][1] - points[j][1])
                    area = float(0.5 * abs(d1 + d2 + d3))
                    max_area = max(area, max_area)

        return max_area
