class TimeMap:

    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: #check membership
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        save = ""
        l,r = 0, len(self.store[key]) - 1

        #binary search for k
        while l <= r:
            m = (l + r) // 2
            k,t = self.store[key][m]
            if t == timestamp:
                return k
            elif t > timestamp:
                r = m - 1
            else:
                l = m + 1
                save = k
        return save
            
