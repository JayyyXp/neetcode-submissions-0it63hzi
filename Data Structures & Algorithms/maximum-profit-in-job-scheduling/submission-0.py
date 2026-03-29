class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        #print(jobs)
        memo = {}
        def dfs(i,t):
            if (i,t) in memo:
                return memo[(i,t)]
            if i == len(jobs):
                return 0
            # skip job
            ret = dfs(i+1, t)
            if jobs[i][0] >= t:
                # schedule job
                ret = max(
                    ret,
                    jobs[i][2] + dfs(i+1, jobs[i][1])
                )
            memo[(i,t)] = ret
            return ret
        return dfs(0,0)