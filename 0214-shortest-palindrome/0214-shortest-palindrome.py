class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pattern=s+"#"+s[::-1]
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
        x=s[lps[-1]:][::-1]
        return x+s
         
        
        
        