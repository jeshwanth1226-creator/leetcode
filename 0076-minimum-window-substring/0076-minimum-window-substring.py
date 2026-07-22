class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        freqt={}
        for i in t:
            freqt[i]=freqt.get(i,0)+1
        freqw={}
        left=0
        need=len(freqt)
        min_len=float('inf')
        formed=0
        for right in range(len(s)):
            freqw[s[right]]=freqw.get(s[right],0)+1
            
            if s[right] in freqt and freqw[s[right]]==freqt[s[right]]:
                    formed+=1
            while formed==need:
                window_len=right-left+1
                if window_len<min_len:
                    start=left
                    min_len=window_len
                left_char = s[left]
                freqw[left_char] -= 1

                if left_char in freqt and freqw[left_char] < freqt[left_char]:
                    formed -= 1

                left += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]
                
                
        




            

        