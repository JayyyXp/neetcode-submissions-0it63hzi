class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        k_count = 0 
        for s in arr:
            if counter[s] == 1:
                k_count += 1
                if k_count == k:
                    return s
        return ""