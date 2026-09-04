class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        chartonum = {
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9   
        }
        
        int1 = int2 = 0
        for c in num1:
            int1 = int1 * 10 + chartonum[c] 
        
        for c in num2:
            int2 = int2 * 10 + chartonum[c]

        res = str(int1 * int2)
        return res


