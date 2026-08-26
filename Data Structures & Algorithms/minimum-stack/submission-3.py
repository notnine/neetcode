class MinStack:

    def __init__(self):
        self.stack = [] # keeps track of items in lifo order
        self.curr_min = [] # stack that keeps track of the min at "each level" of stack (snapshot)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.curr_min.append(min(val, self.curr_min[-1] if self.curr_min else val))
        
    def pop(self) -> None:
        self.stack.pop()
        self.curr_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr_min[-1]
