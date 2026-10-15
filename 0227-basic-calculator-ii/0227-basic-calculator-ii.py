class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        num=0
        op='+'

        for i in s+"+":

            if i.isdigit():
                num=num*10+int(i)

            elif i!=' ':

                if op=='+':
                    stack.append(num)

                elif op=='-':
                    stack.append(-num)

                elif op=='*':
                    stack.append(stack.pop()*num)
                
                elif op=='/':
                    stack.append(int(stack.pop()/num))   

                op=i
                num=0
        
        return sum(stack)
        