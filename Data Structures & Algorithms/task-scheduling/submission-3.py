from heapq import heapify,heappop,heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) #hashmap item-freq

        maxh = [-c for c in count.values()]
        heapify(maxh)

        time = 0
        q = deque() #pairs of [-cnt, avaiTime]

        while maxh or q:
            time += 1
            if q and q[0][1] == time:
                cnt = q.popleft()[0]         
                heappush(maxh, cnt)

            if maxh:
            #execute:
                remaining = heappop(maxh) + 1
                if remaining:
                    q.append([remaining, time + n + 1])
                
        return time

