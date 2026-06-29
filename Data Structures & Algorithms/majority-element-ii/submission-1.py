class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        threshold = len(nums) // 3
        res = []

        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        for k,v in counts.items():
            if v > threshold:
                res.append(k)

        return res