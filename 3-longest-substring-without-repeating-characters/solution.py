# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Runtime: 179 ms
# Memory: 19.9 MB
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
