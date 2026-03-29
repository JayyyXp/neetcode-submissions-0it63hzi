class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ansS = set()
        ans = []
        nums.sort()
        print(nums)
        helper = []
        def dfs(i, s):
            if len(helper) == 4:
                if s == target:
                    ans.append(list(helper))
                    #ansS.add(tuple(sorted(helper)))
                return
            prev = None
            for j in range(i,len(nums)):
                if prev == nums[j]:
                    continue
                prev = nums[j]
                helper.append(nums[j])
                dfs(j+1, s+nums[j])
                helper.pop()
        dfs(0, 0)
        return ans
        return list(ans)