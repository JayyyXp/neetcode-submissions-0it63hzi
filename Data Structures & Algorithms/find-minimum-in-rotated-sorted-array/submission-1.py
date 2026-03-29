class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while True:
            print(nums[l:r+1])
            # length of the search space == 1
            if l == r:
                print('f')
                return nums[l]
            # length of the search space == 1
            if r - l == 1:
                print('s')
                return min(nums[r],nums[l])
            m = (r + l) // 2
            print(nums[m])

            # whole thing sorter
            if nums[l] < nums[r]:
                return nums[l]
            # left side sorted
            if nums[l] < nums[m]:
                if nums[l] < nums[m]:
                    l = m
                else:
                    r = m
            # right side sorted
            else:
                if nums[m] < nums[r]:
                    r = m
                else:
                    l = m
