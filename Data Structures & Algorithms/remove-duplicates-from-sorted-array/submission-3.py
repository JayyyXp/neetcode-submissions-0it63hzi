class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            print(curr, prev)
            if prev != curr:
                nums[idx] = curr
                prev = nums[i]
                idx += 1

        return idx