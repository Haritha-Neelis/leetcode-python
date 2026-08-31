# Two Sum
# Difficulty: Unknown
# Runtime: 1746 ms
# Memory: 19.8 MB
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
