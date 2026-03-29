class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        sideLen = sum(matchsticks) / 4
        #if sideLen % 4 != 0:
        #    return False
        print('sideLen', sideLen, sum(matchsticks), sideLen*4)
        #idxUsed = set()
        memo = {}

        def dfs(currSide, sideCreated, available):
            if sideCreated == 4:
                return True
            if currSide == sideLen:
                return dfs(0, sideCreated+1, available)
            if currSide > sideLen:
                return False
            if (currSide, sideCreated, tuple(available)) in memo:
                return memo[(currSide, sideCreated, tuple(available))]
            ret = False
            for i, ms in enumerate(available):
                    #idxUsed.add(i)
                if (
                    dfs(
                        currSide + matchsticks[i], 
                        sideCreated, 
                        available[:i] + available[i+1:] 
                    )
                ):
                    ret = True 
                    break
                    #idxUsed.remove(i)
            memo[(currSide, sideCreated, tuple(available))] = ret
            return ret

        return dfs(0, 0, matchsticks)