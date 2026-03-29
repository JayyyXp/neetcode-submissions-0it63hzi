class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            haveFound = False
            print(n)
            for j, m in enumerate(nums):
                if n == m and i != j:
                    haveFound = True
            
            if not haveFound:
                return n