class Solution:
    def makeGood(self, s: str) -> str:

        stack=[]

        for i in s:

            if stack and (stack[-1]==chr(ord(i)+32) or stack[-1]==chr(ord(i)-32)):
                stack.pop()
            
            else:
                stack.append(i)
            
        return ''.join(stack)
        