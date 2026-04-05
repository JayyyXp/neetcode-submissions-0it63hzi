class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        for char, count in c1.items():
            if c2[char] < count:
                return False
        return True