class Solution(object):
    def sumZero(self, n):
        ans = []
        
        if n%2 == 1:
            ans.append(0)
            x = ((n - 1) // 2) + 1
            for i in range(1, x):
                ans.append(i)
            for j in range(1, x):
                ans.append(-j)
        else:
            x = (n // 2) + 1
            for i in range(1, x):
                ans.append(i)
            for j in range(1, x):
                ans.append(-j)
            
        return ans
