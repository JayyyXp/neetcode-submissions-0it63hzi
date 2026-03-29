class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        side = sum(matchsticks)
        msMax = max(matchsticks)
        if side % 4 != 0:
            return False
        side //= 4
        if msMax > side:
            return False
        N = len(matchsticks)
        matchsticks.sort()
        used = [False] * N
        def dfs(c, curr):
            if c > 4:
                return False
            if c == 4 and all(used):
                return True
            for i, ms in enumerate(matchsticks):
                if not used[i]:
                    used[i] = True
                    if curr + ms == side:
                        if dfs(c+1, 0):
                            return True
                    elif curr + ms < side: 
                        if dfs(c, curr+ms):
                            return True
                    else:
                        used[i] = False
                        return False
                    used[i] = False
            return False 
        return dfs(0,0)