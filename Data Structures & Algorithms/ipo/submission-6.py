class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ans = [w]
        memo ={}
        def dfs(currCapital,chosenProjects):
            if len(chosenProjects) == k:
                #print(chosenProjects, currCapital)
                return currCapital
            if (currCapital, tuple(chosenProjects)) in memo:
                return memo[(currCapital, tuple(chosenProjects))]
            res = w
            for i, profit in enumerate(profits):
                if i in set(chosenProjects):
                    continue
                elif currCapital >= capital[i]:
                    
                    #skippedProjects.add(i)
                    #dfs(currCapital) 
                    #skippedProjects.remove(i)
                    res = max(
                        res,
                        dfs(currCapital+profit, chosenProjects+[i]) 
                    )
            memo[(currCapital, tuple(chosenProjects))] = res
            return res
        
        return dfs(w, [])