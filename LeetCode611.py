import bisect 

class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        ans = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum_val = nums[i] + nums[j]
                ind = bisect.bisect_left(nums, sum_val, j+1, len(nums))
                ans += (ind - j - 1)

        return ans
