class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for i in tokens:
            if i in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                else:
                    stack.append(abs(a) // abs(b) * (-1 if a * b < 0 else 1))
            else:
                stack.append(int(i))

        return stack[-1]
        