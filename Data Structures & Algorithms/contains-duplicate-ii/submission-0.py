class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        helper = collections.defaultdict(list)
        for i, ni in enumerate(nums):
            for j in helper[ni]:
                if abs(i-j) <= k:
                    return True
            helper[ni].append(i)
        return False 
