# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """The problem with this is that this goes through the whole string to split it, O(N) where as this could be solved using the fact that we just need the last word"""
        # words = s.split()
        # return len(words[-1])    

        """Another Python way to solve this is would be to do it in reverse
        1. Remove all right side spaces for edge cases..
        2. Find the next best space from right(This would be the last words start index -1)
        """
        # s = s.rstrip()
        # last_space_index = s.rfind(" ")
        # return len(s)-last_space_index -1

        """ Manual Implimentation of the above code, not used in development enviroment as this can break and development time is more prefered - Gemini"""       
        count = 0
        for i in range(len(s) - 1, -1, -1): # 
            if s[i] != " ":
                count+= 1
            elif count > 0:
                break
        return count
