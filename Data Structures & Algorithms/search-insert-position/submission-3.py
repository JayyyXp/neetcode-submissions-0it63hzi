class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        l, r = 0, len(nums)-1
        i = 0
        while True:
            i+=1
            #if i == 15:
            #    return
            print(l,r)
            if r-l == 1:
                if target == nums[l]:
                    return l
                return r
            if nums[r] == target:
                return r
            if nums[l] == target:
                return l

            m = (r+l) //2

            if nums[l] < target < nums[m]:
                r = m
            elif nums[m] < target < nums[r]:
                l = m
            else: 
                return m