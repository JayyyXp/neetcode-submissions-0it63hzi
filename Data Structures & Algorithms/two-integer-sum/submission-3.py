class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #for i, num in enumerate(nums):
        #    for j in range(i+1, len(nums)):
        #        if num + nums[j] == target:
        #            return [i, j]

        nums2 = {}

        for i, num in enumerate(nums):
            difference = target - nums[i]
            if difference in nums2:
                return [nums2[difference] , i]
            else:
                nums2[num] = i