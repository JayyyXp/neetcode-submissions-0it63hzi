class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)

        r = N - 1
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1

        l = 0
        while l + 1 < N and arr[l] <= arr[l+1]:
            l += 1
        
        res = min(r, N - 1 - l)

        l, r = 0, N-1
        while l < r:

            while r < N and l + 1 < r and arr[r-1] <= arr[r] and arr[l] <= arr[r]:
                r -= 1
            
            while r < N and arr[l] > arr[r]:
                r += 1
            
            
            res = min(res, r - 1 - l)
            if arr[l] > arr[l+1]:
                break
            l += 1
        return res