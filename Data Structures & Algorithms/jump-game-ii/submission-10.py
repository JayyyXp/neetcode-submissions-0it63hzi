class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 0
        jumps = 0
        while i < len(nums):
            print('new',i,nums[i])
            if i + nums[i] >= len(nums)-1:
                return jumps + 1 
            best, bestIdx = 0, 0
            p = []
            for k in range(i, i+nums[i]+1):
                p.append(nums[k])
                cand = nums[k] + k
                print(cand)
                if cand >= best:
                    best = cand
                    bestIdx = k
                
            #best = max(available)
            print(p ,best)
            i = bestIdx
            jumps += 1
        return jumps