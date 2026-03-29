class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1  # 👈 this line is crucial
        s = 0
        ans = 0
        for i in range(len(nums)):
            s += nums[i]
            ans += prefix[s-k]
            prefix[s] += 1
        return ans