class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=1
        j=0
        lps=[0]*len(s)
        while i<len(s):
            if s[i]==s[j]:
                j+=1
                lps[i]=j
                i+=1
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    lps[i]=0
                    i+=1
        return s[:lps[-1]]
        
        