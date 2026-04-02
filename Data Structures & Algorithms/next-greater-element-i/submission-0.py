class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_idx = {}
        for i, n in enumerate(nums2):
            num_to_idx[n] = i
        ans = []
        for n in nums1:
            l = len(ans)
            for i in range(num_to_idx[n], len(nums2)):
                if nums2[i] > n:
                    ans.append(nums2[i])
                    break
            if len(ans) == l:
                ans.append(-1)
        return ans