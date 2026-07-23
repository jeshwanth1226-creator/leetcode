class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freqs={}
        freqt={}
        for ch in s:
            freqs[ch]=freqs.get(ch,0)+1
        for ch in t:
            freqt[ch]=freqt.get(ch,0)+1
        if sorted(freqs.items(),key=lambda x:x[1])==sorted(freqt.items(),key=lambda x:x[1]):
            return True
        return False
        