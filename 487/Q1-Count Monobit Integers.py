from collections import defaultdict
class Solution:
    def countMonobit(self, n: int) -> int:
        count = 0
        for i in range(n+1):
            # print("Current:", i)
            if self.is_monobit(i):
                # print(i)
                count+=1
        return count


    def binary_representation(self, n):
        ans = []
        while n!=0:
            ans.append(n%2)
            n//=2 
        return ans
    
    def is_monobit(self, n):
        binary_rep = self.binary_representation(n)
        cnt = defaultdict(int)
        if n==0:
            return True
        for i in binary_rep:
            cnt[i]+=1
        if len(cnt)==1:
            return True
        return False


n = 4
solution = Solution()
ans = solution.countMonobit(n)
print(ans)

