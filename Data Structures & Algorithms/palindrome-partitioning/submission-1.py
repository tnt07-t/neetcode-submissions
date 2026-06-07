class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        def isPalindrome(l,r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        #i is starting index, l 
        def backtrack(index):
            if index == len(s):
                res.append(curr.copy())
                return
            for r in range(index,len(s)):
                if isPalindrome(index, r):
                    curr.append(s[index:r+1])
                    backtrack(r+1)
                    curr.pop() #un-choose 

                
        backtrack(0)
        return res
        
