class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l, r = 0, len(arr) -k
        while l < r:
            m = (l + r) // 2
            mid = abs(arr[m] - x)
            midk = abs(arr[m+k] - x)

            if mid > midk:
                l = m+1
            else:
                r = m

        return arr[l:l+k]