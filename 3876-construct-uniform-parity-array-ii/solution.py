# Construct Uniform Parity Array II
# Difficulty: Medium
# Runtime: 71 ms
# Memory: 35.2 MB
# https://leetcode.com/problems/construct-uniform-parity-array-ii/

    def uniformArray(self, nums1: List[int]) -> bool:
        min_odd = float("inf")
        min_even = float("inf")

        for x in nums1:
            if x % 2:
                min_odd = min(min_odd, x)
            else:
                min_even = min(min_even, x)

        if min_odd == float("inf"):
            return True

        if min_even == float("inf"):
class Solution:
            return True

        return min_odd < min_even

