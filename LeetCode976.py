class Solution(object):
    def largestPerimeter(self, nums):
        # ans = 0
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[k] + nums[j] > nums[i]:
        #                 perimeter = nums[i] + nums[j] + nums[k]
        #                 ans = max(ans, perimeter)

        # return ans

        # nums.sort()

        # for i in xrange(len(nums) - 3, -1, -1):
        #     if nums[i] + nums[i+1] > nums[i+2]:
        #         return nums[i] + nums[i+1] + nums[i+2]

        # return 0

        nums.sort(reverse = True)
        ans = 0

        for i in range(len(nums)-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                perimeter = nums[i] + nums[i+1] + nums[i+2]
                ans = max(ans, perimeter)

        return ans
