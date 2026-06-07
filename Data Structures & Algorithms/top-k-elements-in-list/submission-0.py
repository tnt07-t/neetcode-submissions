class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ret = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            ret.append(sorted_count[i][0])  # take the number

        return ret