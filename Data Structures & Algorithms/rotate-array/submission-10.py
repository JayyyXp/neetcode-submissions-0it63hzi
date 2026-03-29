class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        rot = k % len(nums) if k > len(nums) else k
        rev(0, len(nums)-1)
        print(nums)
        rev(0, rot -1)
        print(nums)
        rev(rot, len(nums)-1)
        print(nums)
