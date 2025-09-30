class Solution(object):
    def triangularSum(self, nums):
        l1 = []

        while len(nums) != 1:
            for i in range(len(nums) - 1):
                l1.append((nums[i] + nums[i+1]) % 10)
            nums = l1[:]
            l1 = []

        return nums[0]
