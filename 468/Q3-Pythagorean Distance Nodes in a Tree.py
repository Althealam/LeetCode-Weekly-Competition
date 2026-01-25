# 对树里的每一个点u，看它到三个指定点x、y、z的距离
# 如果这三个距离可以组成一个直角三角形，那么这么点就是special的
# 计算special node的数量

# 1. 建立邻接表
# 2. 分别从x、y、z上跑一次DFS，得到三条距离数组
# 3. 对每个结点u排序，计算a*a+b*b以及c*c，如果成立则计数+1
from collections import deque
class Solution:
    def specialNodes(self, n: int, edges, x: int, y: int, z: int) -> int:
        # 建立邻接表，表示u到v之间的边
        # 用于获取邻居节点
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        print(g)
        # g[x]表示节点x的邻居节点
        
        def bfs(start):
            # 初始化距离数组，-1表示未访问过
            dist = [-1]*n
            # 初始化队列，将起点加入队列
            q = deque([start])
            # 起点到起点的距离为0
            dist[start] = 0
            # 当队列不为空的时候，遍历其相邻节点，并更新距离
            while q:
                u = q.popleft()
                for v in g[u]:
                    # 如果v没有被访问过，那么可以加入到队列中
                    if dist[v]==-1:
                        # 更新距离
                        dist[v] = dist[u]+1
                        # 将v加入队列中，获取其相邻节点
                        q.append(v)
            return dist

        # 从x、y、z上跑一次BFS，得到三条距离数组
        # 分别表示每个结点到x/y/z的距离 例如distX[u]表示u到X的距离 
        distX = bfs(x)
        distY = bfs(y)
        distZ = bfs(z)
        print("distX:", distX)
        print("distY:", distY)
        print("distZ:", distZ)
        ans = 0
        for u in range(n):
            a, b, c = sorted((distX[u], distY[u], distZ[u]))
            if a*a+b*b==c*c:
                ans+=1
        return ans


n = 4
edges = [[0,1],[0,2],[0,3]]
x=1
y=2
z=3
solution = Solution()
res = solution.specialNodes(n, edges, x, y, z)
print(res)