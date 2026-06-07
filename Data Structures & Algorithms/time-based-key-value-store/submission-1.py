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
        for k,t in self.store[key]:
            if t == timestamp:
                return k
            if t > timestamp:
                return save
            save = k

        return save
