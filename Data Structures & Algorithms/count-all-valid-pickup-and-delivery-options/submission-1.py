class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1000000007
        # 1 2
        # 1 2

        # 1p 1d 2p 2d 
        # 1p 2p 1d 2d 
        # 1p 2p 2d 1d
        # 2p 1p 1d 2d
        # 2p 1p 2d 1d
        # 2p 2d 1p 1d

        def dfs(m):
            if m == 1:
                return 1
            
            prev = dfs(m-1)
            k = (2*m-1)
            ret = (k * ((k+1) // 2) * prev) % MOD
            return ret

        return dfs(n)
