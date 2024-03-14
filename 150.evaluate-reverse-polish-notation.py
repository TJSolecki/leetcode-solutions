class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        num_stack = []
        for curr in tokens:
            if curr in "+-/*":
                num_2 = num_stack.pop()
                num_1 = num_stack.pop()
                op = curr
                if op == "+":
                    num_stack.append(num_1 + num_2)
                elif op == "-":
                    num_stack.append(num_1 - num_2)
                elif op == "/":
                    num_stack.append(int(float(num_1) / num_2))
                elif op == "*":
                    num_stack.append(num_1 * num_2)
            else:
                num_stack.append(int(curr))

        return num_stack[0]
