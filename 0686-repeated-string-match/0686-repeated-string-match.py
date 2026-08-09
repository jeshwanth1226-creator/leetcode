class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        pattern=b
        text=""
        c=0
        #ceil_dividion(minimum number of groups/copies required to cover at least X)
        min_copies=(len(b)+len(a)-1)//len(a)
        if len(b)>len(a):
            for i in range(min_copies):
                text+=a
                c+=1
        #bulding lps
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
        while c<=min_copies+1:
            i=0
            j=0
            while i<len(text):
                if text[i]==pattern[j]:
                    j+=1
                    i+=1    
                    if j==len(pattern):
                        return c
                else:
                    if j!=0:
                        j=lps[j-1]
                    else:
                        i+=1
            text+=a
            c+=1
        return -1
        


            