# Count Commas in Range
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.4 MB
# https://leetcode.com/problems/count-commas-in-range/

class Solution:
    def countCommas(self, n: int) -> int:
        return 0 if n  < 1000 else n - 999 
        
