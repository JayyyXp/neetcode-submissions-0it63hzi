import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        #print(jobs)
        memo = {}
        def dfs(i):
            if (i) in memo:
                return memo[i]
            if i == len(jobs):
                return 0
            # skip job
            ret = dfs(i+1)
            j = bisect.bisect_right(jobs, (jobs[i][1],-1,-1))
            # schedule job
            ret = max(
                ret,
                jobs[i][2] + dfs(j)
            )
            memo[i] = ret
            return ret
        return dfs(0)