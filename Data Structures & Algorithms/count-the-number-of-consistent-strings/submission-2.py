class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        mask = 0
        for c in allowed:
            bit = 1 << (ord(c) - ord("a"))
            mask |= bit

        ans = 0 
        for word in words:
            valid = 1
            for c in word:
                if not ((mask >> (ord(c) - ord("a"))) & 1):
                    valid = 0
            ans += valid
        return ans