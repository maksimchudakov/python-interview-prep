"""
Problem: Longest Common Prefix
Platform: LeetCode
Problem ID: 14
Difficulty: Easy
Link: https://leetcode.com/problems/longest-common-prefix/
"""

# Find the longest common prefix among all strings
# Start with first string as prefix
# Shrink prefix until it matches the start of each string

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pref = strs[0]
        for i in strs[1:]:
            while not i.startswith(pref):
                pref = pref[:-1]
                if not pref:
                    return ""
        return pref
