class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        self.min_track = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min:
            self.min = val
            self.min_track.append(self.min)


    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min_track[-1]:
            self.min_track.pop()
            if self.min_track:
                self.min = self.min_track[-1]
            else:
                self.min = float("inf")
    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:        
        return self.min_track[-1]

        
