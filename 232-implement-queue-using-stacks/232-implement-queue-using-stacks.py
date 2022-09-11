class MyQueue:

    def __init__(self):
        self.arr = []
        self.length = 0

    def push(self, x: int) -> None:
        self.temp_stack = []
        for i in range(self.length):
            self.temp_stack.append(self.arr.pop())
        self.arr.append(x)
        for i in range(self.length):
            self.arr.append(self.temp_stack.pop())
        self.length += 1

    def pop(self) -> int:
        if self.length > 0:
            self.length -= 1
            return self.arr.pop()
        else: return

    def peek(self) -> int:
        if self.length > 0:
            return self.arr[-1]
        else: return

    def empty(self) -> bool:
        if self.length == 0: return True
        else: return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()