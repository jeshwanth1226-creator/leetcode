class Solution:
    def calculate(self, s: str) -> int:

        stack=[]
        num=0
        res=0
        sign=1

        for i in s+'+':

            if i.isdigit():
                num=num*10+int(i)

            elif i in '+-':
                res+=sign*num
                num=0
                sign=1 if i=='+' else -1
            
            elif i=='(':
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            
            elif i==')':
                res+=sign*num
                num=0
                res*=stack.pop()
                res+=stack.pop()
        
        return res



                

