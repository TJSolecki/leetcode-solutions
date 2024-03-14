class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        new_min = val if len(self.stack) < 1 or val < self.getMin() else self.getMin()
        self.stack.append((val, new_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return 0


# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
