class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def dfs(idx,sum1, sum2):
            if sum1 == sum2:
                return True
            #if len(subset1) == 0:
            if sum2 > sum1 or idx == len(nums):  
                return False

            num1 = nums[idx]
            ret = False
            if dfs(
                idx+1, sum1-num1, 
                sum2+num1
                ):
                ret = True
            if dfs(
                idx+1, sum1, 
                sum2
                ):
                ret = True
            
            return ret

        return dfs(0, sum(nums),0)