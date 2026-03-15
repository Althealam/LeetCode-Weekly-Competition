# calculate the total number of commas from 1000 to n

# 1. brute force
# len(n)==4: res = 1 4//3=1
# len(n)==5: res = 1 5//3=1
# len(n)==6: res = 1 6//3=2
# len(n)==7: res = 2 7//3=2
# len(n)==8: res = 2 8//3=2
# len(n)==9: res = 2 9//3=3
# len(n)==10: res = 3
# len(n)==11: res = 3
# len(n)==12: res = 3
# 2. optimized solution
# if len(str(i))%3==0: number of commas = len(str(3))//3-1
# elif len(str(i))%3!=0: number of commas = len(str(3))//3

# 1003: 1000, 1001, 1002 ==> 3个四位数
# 1130: 1000, ..., 1130 ==> 130个四位数
# 12420: 1000, ..., 12420 ==> 11420 ==> 1000-9999共有8999个四位数，10000-12420共有2420个五位数
# 152014: 1000, ..., 152014 ==> 151014 ==> 1000-9999共有8999个四位数，10000-99999共有89999个五位数，100000-151014共有51014个五位数
# 1520153: 1000, ..., 152014 ==> 151014 ==> 1000-9999共有8999个四位数，10000-99999共有89999个五位数，100000-999999共有899999个六位数，1000000-1520153共有520153个七位数 ==> 8999*1+89999*1+899999*1+520153*2


class Solution:
    def countCommas(self, n: int) -> int:
        length_n = len(str(n))
        if length_n<4:
            return 0
        if length_n==4:
            return n-1000+1
        res = 0 
        # res+8999*1 ==> 4
        # res+89999*1 ==> 5
        # res+899999*1 ==> 6
        # res+8999999*2 ==> 7
        
        for i in range(4, length_n+1):
            cnt = int('9'+'0'*(i-1))
            if i%3==0 and i!=length_n:
                res+=cnt*(i//3-1)
            elif i%3!=0 and i!=length_n: 
                res+=cnt*(i//3)
            elif i==length_n:
                if i%3==0:
                    res+=(n-10**(i-1)+1)*(i//3-1)
                else:
                    res+=(n-10**(i-1)+1)*(i//3)
        return res
sol = Solution()
res = sol.countCommas(10010) # 1000-9999: 9000个4位数，对应9000个comma；10000-10010共有11个comma
print(res)

