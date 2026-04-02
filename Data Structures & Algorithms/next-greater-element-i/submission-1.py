class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_idx = {}
        for i, n in enumerate(nums1):
            num_to_idx[n] = i
        ans = [-1] * len(nums1)
        stack = []
        for n in nums2:
            while stack and n > stack[-1]:
                val = stack.pop()
                idx = num_to_idx[val]
                ans[idx] = n

            if n in num_to_idx:
                stack.append(n)
        return ans