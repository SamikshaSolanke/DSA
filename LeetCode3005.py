# Soln1
# class Solution(object):
#     def maxFrequencyElements(self, nums):
#         freq = [0] * 101
#         ans = 0

#         for num in nums:
#             freq[num] += 1
        
#         max_freq = max(freq)

#         for num in nums:
#             if freq[num] == max_freq:
#                 ans += 1

#         return ans

# Soln2
class Solution(object):
    def maxFrequencyElements(self, nums):
        ans = 0
        track = {}

        for num in nums:
            if num not in track:
                track[num] = 1
            else:
                track[num] += 1

        max_freq = max(track.values())
        temp = set(nums)

        for num in temp:
            if track[num] == max_freq:
                ans += max_freq

        return ans
