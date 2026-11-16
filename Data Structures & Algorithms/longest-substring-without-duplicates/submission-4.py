class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:     
        res = 0
        l = 0
        charSet = set()
        for j in range(len(s)):
            while s[j] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[j])
            res = max(res, len(charSet))
        return res