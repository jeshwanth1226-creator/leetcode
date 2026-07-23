class Solution(object):
    def calPoints(self, operations):
        ops = operations
        stack = []

        for i in ops:

            if i not in ['D', 'C', '+']:
                stack.append(int(i))

            elif i == 'C':
                stack.pop()

            elif i == 'D':
                stack.append(stack[-1] * 2)

            elif i == '+':
                stack.append(stack[-1] + stack[-2])

        return sum(stack)