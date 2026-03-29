class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #counter = {}
        sett = set()
        for num in nums:
            if num in sett:
                return True
                #counter[num] += 1
            else:
                sett.add(num)
        return False