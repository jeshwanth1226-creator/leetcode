class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern=s
        i=1
        j=0
        lps=[0]*len(pattern)
        while i<len(pattern):
            if pattern[i]==pattern[j]:
                j+=1
                lps[i]=j
                i+=1
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    lps[i]=0
                    i+=1
        if lps[-1]!=0 and len(pattern)%(len(pattern)-lps[-1])==0:
            return True
        return False
        