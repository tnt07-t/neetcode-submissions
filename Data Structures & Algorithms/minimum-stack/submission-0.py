class MinStack:


    #array -> add to end


    def __init__(self):
        #stores values in arr
        self.arr = []
        #stores min value so far
        self.minVal = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.minVal:
            self.minVal.append(val)
        else:
            self.minVal.append(min(val, self.minVal[-1]))

    def pop(self) -> None:
        self.arr.pop()
        self.minVal.pop()
        

    def top(self) -> int:
        return self.arr[len(self.arr)-1]

    def getMin(self) -> int:
        return self.minVal[-1]