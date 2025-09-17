from fractions import gcd

class Solution(object):
    def replaceNonCoprimes(self, nums):
        ans = []

        def isNonCoprime(num1, num2):
            return gcd(num1, num2) > 1

        def lcm(a, b):
            return (a*b) // gcd(a, b)

        for num in nums:
            ans.append(num)

            while len(ans) >= 2 and isNonCoprime(ans[-1], ans[-2]):
                num1 = ans.pop()
                num2 = ans.pop()
                ans.append(lcm(num1, num2))

        return ans
