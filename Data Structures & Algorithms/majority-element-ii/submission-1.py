class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1
        cutoff = len(nums) / 3
        ans = []
        for num, count in counter.items():
            if count > cutoff:
                ans.append(num)            
        return ans