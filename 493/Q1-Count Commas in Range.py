# 需要1-n之间的数，并且n必须要是四位数才可以有comma
# 10^5=100000, 10,000/100,000
# {4: 1, 5: 1, 6: 1}

class Solution:
    def countCommas(self, n: int) -> int:
        list_n = list(str(n))
        if len(list_n)<4:
            return 0
        res = 0
        for i in range(1000, n+1):
            res+=1
        return res
            
        