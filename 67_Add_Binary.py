# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = self.bintodec(a) 
        y = self.bintodec(b)

        while y:    
            answer = x ^ y
            carry = (x & y) << 1
            x,y = answer, carry

        return bin(x)[2:]

    def bintodec(self, binary):
            decimal = 0
            for bit in binary:
                decimal = (decimal << 1) | int(bit)
            return decimal
