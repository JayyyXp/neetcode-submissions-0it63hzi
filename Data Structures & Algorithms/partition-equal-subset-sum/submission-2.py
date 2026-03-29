class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def dfs(subset1,sum1, sum2):
            if sum1 == sum2:
                return True
            #if len(subset1) == 0:
            if sum2 > sum1:  
                return False
            
            ret = False
            for i, num1 in enumerate(subset1):
                if dfs(
                    subset1[:i] +subset1[i+1:], sum1-num1, 
                    sum2+num1
                    ):
                    ret = True
            
            return ret

        return dfs(nums, sum(nums),0)