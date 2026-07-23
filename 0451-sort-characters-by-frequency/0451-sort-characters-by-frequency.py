class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq={}
        l=[]
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        sort=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        for ch,i in sort:
            l.append(ch*i)
        return ''.join(j for j in l)