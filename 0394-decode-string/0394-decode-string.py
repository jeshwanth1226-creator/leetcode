class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        num=0
        ans=""

        for i in s:

            if i.isdigit():
                num=num*10+int(i)

            elif i=="[":
                stack.append((ans,num))
                ans=""
                num=0

            elif i=="]":
                prev,k=stack.pop()
                ans=prev+ans*k
            
            else:
                ans+=i
        
        return ans