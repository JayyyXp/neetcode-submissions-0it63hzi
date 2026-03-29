class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.defaultdict(int)
        for num in nums:
            c[num] += 1

        return max(c,key=lambda x: c[x])