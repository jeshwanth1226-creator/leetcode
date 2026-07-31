class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count=0
        a=set("aeiouAEIOU")

        for i in s[:k]:
            if i in a:
                count+=1
            
        max_count=count

        for j in range(k,len(s)):
            if s[j] in a and s[j-k] not in a:
                count+=1
            if s[j] not in a and s[j-k] in a:
                count-=1

            max_count=max(max_count,count)
        return max_count
            
