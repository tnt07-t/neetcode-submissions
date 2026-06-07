class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        #check if string s is a palindrome
        def isPalindrome(s,l,r):
            while (l < r):
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrack(index):
            if index == len(s):
                res.append(curr.copy())
                return
        
            for r in range(index,len(s)):
                #partition
                if isPalindrome(s,index,r):
                    curr.append(s[index: r+1]) 
                    backtrack(r + 1)
                    curr.pop()  #un-choose

        backtrack(0)
        return res

                #skip partition

        