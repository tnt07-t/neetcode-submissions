class CountSquares:

    def __init__(self):
        self.ptCount = defaultdict(int) #how many times a key x,y appears
        self.colYs = defaultdict(set) # x value - y values present for that x


    def add(self, point: List[int]) -> None:
        x,y = point
        self.ptCount[(x,y)] += 1
        self.colYs[x].add(y)
        

    def count(self, point: List[int]) -> int:
        #front point, for each point in colYs -> check if corresponding square points exist
        x,y = point
        total = 0

        for y2 in self.colYs[x]:
            if y2 == y:
                continue
            
            side = y2 - y
            same_col_count = self.ptCount[(x, y2)]
            for x2 in (x + side, x - side):
                total += same_col_count * self.ptCount[(x2, y)] * self.ptCount[(x2, y2)]
        return total



