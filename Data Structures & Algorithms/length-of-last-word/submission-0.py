class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.strip().split(" ")[-1]
        print(l)
        return len(l)