class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            
            if nums[m] < nums[r]: #right half is sorted
                if nums[m] < target <= nums[r]:#search for bigger
                    l = m + 1
                else:
                    r = m - 1
            else: #left half is sorted
                if nums[l] <= target < nums[m]: #search for smaller
                    r = m - 1
                else:
                    l = m + 1

        return -1