class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # nums1 pointer 
        j = n - 1 # nums2 pointer
        k = m + n - 1 # placement pointer

        while k > -1:
            print(nums1)
            n1 = nums1[i] if i > -1 else -float('inf') 
            n2 = nums2[j] if j > -1 else -float('inf') 
            if n1 > n2:
                nums1[k] = n1
                k -= 1
                i -= 1
            else:
                nums1[k] = n2
                k -= 1
                j -= 1