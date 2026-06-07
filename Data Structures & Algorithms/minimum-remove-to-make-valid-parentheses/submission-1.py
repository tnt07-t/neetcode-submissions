class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opens,closes = 0,0
        remove = set() #indices of parentheses to be removed

        #Left to Right scan! -> find umnatched (
        for i,c in enumerate(s):
            if c == "(":
                opens += 1
            if c == ")":
                if opens == 0:
                    remove.add(i)
                else:
                    opens -= 1 #matched most recent "("
                
        #Right to left scan! find unmatched )

        for i in range(len(s) - 1, -1, -1):
            if opens == 0:
                break
            if s[i] == "(":
                remove.add(i)
                opens -= 1
            
        return "".join(c for i,c in enumerate(s) if i not in remove)