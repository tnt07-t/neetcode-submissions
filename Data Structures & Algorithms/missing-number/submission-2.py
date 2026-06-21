class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #every number XOR'ed with 0 is unchanged
        #every number XOR'ed with itself is 0!
        #-> if i XOR whole range of n in -> every number should XOR'ed 
        #itself once and become 0 -> except missing one. 
        #which XOR'ed with remaining 0 is itself
        ans = 0
        for i,n in enumerate(nums):
            ans ^= i ^ n

        ans ^= len(nums)
        return ans


