"""
Problem: Roman to Integer
Platform: LeetCode
Problem ID: 13
Difficulty: Easy
Link: https://leetcode.com/problems/roman-to-integer/
"""

# Convert Roman numeral string to integer
# Handle subtraction cases by replacing special combinations first
# Then sum up individual symbol values using a dictionary

class Solution:
    def romanToInt(self, s: str) -> int:
        transform = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        just = 0
        s = s.replace("IV","IIII").replace("IX","VIIII")
        s = s.replace("XL","XXXX").replace("XC","LXXXX")
        s = s.replace("CD","CCCC").replace("CM","DCCCC")
        for i in s:
            just += transform[i]
        return just
