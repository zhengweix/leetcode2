class MyStack:
    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        return self.q.append(x)

    def pop(self) -> int:
        q1 = []
        for i in range(len(self.q) - 1):
            q1.append(self.q.pop(0))
        x = self.q.pop(0)
        self.q = q1
        return x

    def top(self) -> int:
        if self.q:
            return self.q[-1]
        return None

    def empty(self) -> bool:
        if self.q:
            return False
        return True