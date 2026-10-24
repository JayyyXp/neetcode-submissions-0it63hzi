class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        s = set([c for c in allowed])


        ans = 0 
        for word in words:
            if all([c in s for c in word]):
                ans += 1
        return ans