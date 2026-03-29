class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        def dfs(i, s, l):
            if i == len(customers):
                return 0

            if not grumpy[i]:
                if s:
                    return dfs(i+1,s,l-1) + customers[i] 
                else:
                    return dfs(i+1,s,l) + customers[i]
            else:
                if s:
                    if l <= 0:
                        return dfs(i+1,s,l-1)
                    else: 
                        return dfs(i+1,s,l-1) + customers[i]
                else:
                    return max(
                        dfs(i+1,s,l),
                        dfs(i+1,True,l-1) + customers[i]
                    )

        return dfs(0,False,minutes)