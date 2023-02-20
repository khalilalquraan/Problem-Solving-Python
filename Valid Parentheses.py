# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for braket in s:
            if braket in pair :
                stack.append(braket)
            elif len(stack) == 0 or braket != pair[stack.pop()]:
                return False
        return len(stack) == 0