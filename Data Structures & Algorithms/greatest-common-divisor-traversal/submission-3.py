class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        import math
        graph = collections.defaultdict(list)        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if math.gcd(nums[i], nums[j]) > 1:
                    graph[i].append(j)
                    graph[j].append(i)
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            ret = False
            for j in graph[i]:
                dfs(j)            
        dfs(0)
        return len(visited) == len(nums)