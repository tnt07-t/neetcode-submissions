class LFUCache:
    #track both frequency and recency
    # minheap -> heappop removes LFU

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        #key -> (value,freq)
        self.keyMap = {}
        #freq -> {key: None}
        self.freqMap = defaultdict(OrderedDict)
        #tells which bucket to evict from
        self.minfreq = 0
    def increment(self,key):
        #updateMRU + frequency
        val, freq = self.keyMap[key]
        del self.freqMap[freq][key] #remove from curr freq bucket
        if not self.freqMap[freq]:
            del self.freqMap[freq]
            #bucket empty, the smallest-freq element just increased frequency by 1
            if self.minfreq == freq:
                self.minfreq += 1
        self.keyMap[key] = [val,freq + 1] #update val and freq
        self.freqMap[freq+1][key] = None #add to next freq bucket

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        self.increment(key)
        return self.keyMap[key][0]

    

    def put(self, key: int, value: int) -> None:
        if key in self.keyMap: #existing key
            self.keyMap[key][0] = value
            self.increment(key)
        else:
            if self.size >= self.cap:
            #remove element with minfreq & LRU
                #or removed_key, _ = ____.popitem(last=False)
                removed_key= self.freqMap[self.minfreq].popitem(last = False)[0]
                del self.keyMap[removed_key]
                self.size -= 1
            #add new key-value
            self.keyMap[key] = [value,1]
            self.freqMap[1][key] = None
            self.minfreq = 1
            self.size += 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)