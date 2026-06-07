class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2 #round down

        #make A the smaller array
        if len(B) < len(A):
            A,B = B,A
        
        l,r = 0, len(A) - 1
        while True:
            #binary search on A for mid point
            mA = (l + r) // 2
            mB = half - mA - 2

            #check if correct middle part
            lA = A[mA] if mA >= 0 else float("-inf")
            rA = A[mA + 1] if (mA + 1) < len(A) else float("inf")

            lB = B[mB] if mB >= 0 else float("-inf")
            rB = B[mB + 1] if (mB + 1) < len(B) else float("inf")

            if lA <= rB and lB <= rA:
                if total % 2: #odd total
                    return min(rA,rB)#next number after left partition
                else:#even total
                    return (max(lA,lB) + min(rA,rB))/2
            elif lA > rB:
                r = mA - 1 #rA = mA causes infinite loop
            else:
                l = mA + 1
            


            