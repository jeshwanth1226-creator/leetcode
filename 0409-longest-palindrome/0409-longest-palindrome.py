class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={}
        count=0
        odd_found=False
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for i in freq.values():
            if i%2==0:
                count+=i
            else:
                count+=i-1
                odd_found=True
        if odd_found:
            count+=1
        return count
        