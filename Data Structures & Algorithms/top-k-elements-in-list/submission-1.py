import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)
        for n in nums:
            d[n] += 1

        #natural: smallest -> biggest -> reverse = True
        sorted_d = sorted(d.items(), key = lambda x: x[1], reverse = True)
        return [num for num, freq in sorted_d[:k]]
        