class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        pSize = total // k
        nums.sort(reverse=True)
        available = [True] * len(nums)

        def dfs(s, t):
            if t == k:
                return True
            if s == pSize:
                return dfs(0, t + 1)
            for i, n in enumerate(nums):
                if not available[i] or s + n > pSize:
                    continue
                available[i] = False
                if dfs(s + n, t):
                    return True
                available[i] = True
                if s == 0:  # Important pruning
                    break
            return False

        return dfs(0, 0)
