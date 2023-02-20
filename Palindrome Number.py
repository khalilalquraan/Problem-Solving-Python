# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        rev = 0
        org = x
        while org > 0:
            rev = rev * 10 + org % 10
            org //= 10
        return rev == x