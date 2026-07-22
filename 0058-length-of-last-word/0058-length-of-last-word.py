class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.split()
        l=len(s)
        return len(s[l-1])
        