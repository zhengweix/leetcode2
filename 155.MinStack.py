class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        n = len(self.stack)
        self.stack.append(min(val, self.stack[-2] if n > 0 else val))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[-2]