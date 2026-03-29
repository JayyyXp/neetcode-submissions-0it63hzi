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
        #prev1 = nums[0]
        #curr = nums[1]
        #i = 0
        #while prev1 != curr and i != 7:
        #    print(curr, prev1)
        #    curr, prev1 = nums[curr], curr
        #    i += 1

        #count = 0
        #for num in nums:
        #    if num == curr:
        #        count += 1
        #if count != 1:
        #    return curr
        #else:
        #    return prev1