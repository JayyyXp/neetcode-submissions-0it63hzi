class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ans = [w]
        chosenProjects = set()
        def dfs(currCapital):
            if len(chosenProjects) == k:
                #print(chosenProjects, currCapital)
                ans[0] = max(ans[0], currCapital)
                return 
            for i, profit in enumerate(profits):
                if i in chosenProjects:
                    continue
                elif currCapital >= capital[i]:
                    
                    #skippedProjects.add(i)
                    #dfs(currCapital) 
                    #skippedProjects.remove(i)

                    chosenProjects.add(i)
                    dfs(currCapital+profit) 
                    chosenProjects.remove(i)
            return  
        dfs(w)
        return ans[0]