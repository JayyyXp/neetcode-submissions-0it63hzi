class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        table = [0] * 10_000
        for num in nums:
            if table[num] != 0:
                return num
            else:
                table[num] = 1

        # 0,1,2,3,4
        # 1,2,3,2,2
        #slow = 0
        #fast = 0
        #while True:
        #    fast, slow = nums[nums[fast]], nums[slow]
        #    if slow == fast:
        #        return fast
        #count = 0
        #for num in nums:
        #    if num == curr:
        #        count += 1
        #if count != 1:
        #    return curr
        #else:
        #    return prev1