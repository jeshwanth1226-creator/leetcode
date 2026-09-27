class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen={}
        left=0
        res=0

        for right in range(len(s)):

            if s[right] in seen:

                left=max(left,seen[s[right]]+1)

            seen[s[right]]=right

            res=max(res,right-left+1)

        return res