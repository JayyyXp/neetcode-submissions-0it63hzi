class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 7,5 k=6
        
        #print(sum(nums)%k ,nums)
        prefix = [0]
        helper = {}
        helper = {0:-1}

        for i in range(len(nums)):
            prefix.append((prefix[-1] + nums[i])%k)
            if prefix[-1] not in helper:
                helper[prefix[-1]] = i
            elif i - helper[prefix[-1]]> 1:
                return True
            

        print(prefix, helper)
        return False
