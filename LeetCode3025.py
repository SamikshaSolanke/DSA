class Solution(object):
  def numberOfPairs(self, points):
      n = len(points)
      ans = 0
      points.sort(key = lambda x : (x[0], -x[1]))

      for i in range(n):
        temp = float('-inf')
        for j in range(i+1, n):
          if points[i][1] >= points[j][1] > temp:
            ans += 1
            temp = points[j][1]
            
      return ans
