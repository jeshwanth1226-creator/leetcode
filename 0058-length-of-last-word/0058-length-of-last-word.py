class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        i=len(s)-1

        while i>=0:
            if s[i]==" ":
                
                if count>0:
                    break
            else:
                count+=1
            
            i-=1
        
        return count
        

        