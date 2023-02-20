# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = ''
        minStr = min(strs)
        maxStr = max(strs)
        minLen = min(len(minStr), len(maxStr))
        i = 0
        while i < minLen:
            if minStr[i] == maxStr[i]:
                longestPrefix += minStr[i]
            else:
                break
            i +=1
        return longestPrefix