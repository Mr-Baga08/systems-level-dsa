# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if len(needle) > len(haystack):
            return -1

        lps_table = self.pi_table(needle)

        j = 0
        i = 0
        
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == len(needle):
                    return i - j
            else:
                if j != 0:
                    j = lps_table[j - 1] 
                else:
                    i += 1              
        return -1

    def pi_table(self, needle: str) -> list:
        lps = [0] * len(needle)
        momentum = 0
        ptr = 1

        while ptr<len(needle):
            if needle[momentum] == needle[ptr]:
                momentum += 1
                lps[ptr] = momentum
                ptr += 1
            else:
                if momentum != 0:
                    momentum = lps[momentum - 1]
                else:
                    lps[ptr] = 0
                    ptr += 1
        return lps

        
