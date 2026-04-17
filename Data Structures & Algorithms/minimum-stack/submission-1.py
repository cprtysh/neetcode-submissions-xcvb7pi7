class MinStack:

    def __init__(self):
        self.stack=[]
        self.mstack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mstack:
            if self.mstack[-1]>val:
                self.mstack.append(val)
            else:
                self.mstack.append(self.mstack[-1])
        else:
            self.mstack.append(val)

    def pop(self) -> None:
        del self.stack[-1]
        del self.mstack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]
