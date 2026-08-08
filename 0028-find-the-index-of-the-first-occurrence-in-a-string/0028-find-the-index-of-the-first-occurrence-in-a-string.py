class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=="":
            return 0
        pattern=needle
        i=1
        j=0
        lps=[0]*len(pattern)
        while i<len(pattern):
            if pattern[i]==pattern[j]:
                j+=1
                lps[i]=j
                i+=1
            elif j!=0:
                j=lps[j-1]
            else:
                lps[i]=0
                i+=1
        i=0
        j=0
        while i<len(haystack):
            if haystack[i]==pattern[j]:
                j+=1
                i+=1
                if j==len(pattern):
                    return i-j
            elif j!=0:
                j=lps[j-1]
            else:
                i+=1
        return -1
