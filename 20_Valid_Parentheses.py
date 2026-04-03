# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        compliment_brackets = self.bracket_mapped()
        stack = [] 

        for char in s:
            if char in compliment_brackets:
                target_match = stack.pop() if stack else "#"
                if compliment_brackets[char] != target_match:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0


    def bracket_mapped(self) -> dict:
        compliment_brackets = {")": "(", 
                           "]": "[",
                           "}": "{"}
        
        return compliment_brackets
