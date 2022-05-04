class Logger:
    def __init__(self):
        self.starttime = 0
        self.messages = []

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp - self.starttime > 10:
            self.starttime += 0
            self.messages = []

        feedback = False if message in self.messages else True
        self.messages.append(message)
        return feedback

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)