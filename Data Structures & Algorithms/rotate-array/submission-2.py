class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsH = deque(nums)
        for _ in range(k):
            numsH.appendleft(numsH.pop())

        for i in range(len(nums)):
            nums[i] = numsH[i]
